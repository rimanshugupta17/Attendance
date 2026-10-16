import dlib
import numpy as np
import face_recognition_models
from sklearn.svm import SVC
import streamlit as st

from src.database.db import get_all_students

@st.cache_resource
def load_dlib_models():
    detector=dlib.get_frontal_face_detector()  # this is for getting coordinates of face

    sp=dlib.shape_predictor(                          # this is for getting landmarks of faces commonly 68 landmarks
        face_recognition_models.pose_predictor_model_location()
    )
    facerec=dlib.face_recognition_model_v1(
        face_recognition_models.face_recognition_model_location()  # this converts face to 128d vector embeddings 
    )

    return detector,sp,facerec

def get_face_embeddings(image_np):
    detector,sp,facerec=load_dlib_models()
    faces=detector(image_np,1) # find all faces
    encodings=[]

    for face in faces:
        shape= sp(image_np,face)# find all landmarks
        face_descriptor=facerec.compute_face_descriptor(image_np,shape,1) # gen face embedding

        encodings.append(np.array(face_descriptor))
        
    return encodings

def get_trained_model():
    X=[]
    y=[]
    student_db=get_all_students() # get all students data from supabase
    if not student_db:
        return None
    
    for student in student_db:
        embedding=student.get('face_embedding')
        if embedding:
            X.append(np.array(embedding)) # embedding stores
            y.append(student.get('student_id')) # student id stored

    if len(X)==0:
        return 0
    clf=SVC(kernel='linear',probability=True,class_weight='balanced') # create svm

    try:
        clf.fit(X,y) #train model (input embeddings -> student ids)
    except ValueError:
        pass
    return {'clf':clf,'X':X,"y":y}

def train_classifier():
    st.cache_resource.clear() # clears cache and retrains model
    model_data=get_trained_model()
    return bool(model_data)

def predict_attendance(class_image_no):
    encodings=get_face_embeddings(class_image_no)

    detected_Student={}

    model_data=get_trained_model()

    if not model_data:
        return {},[],len(encodings)
    clf=model_data['clf']
    X_train=model_data['X']    #stored embeddings
    y_train=model_data['y']     #stored student ids

    all_students=sorted(list(set(y_train))) #delete duplicates student embeddings

    for encoding in encodings:
        if len(all_students)>=2: #it should have more than 1 students to distinguish
            predicted_id=int(clf.predict([encoding])[0])
        else:
            predicted_id=int(all_students[0])

        student_embedding = X_train[y_train.index(predicted_id)]

        best_match_score = np.linalg.norm(student_embedding - encoding) # calculates euclidean distance
        resemblance_threshold=0.4

        if best_match_score<= resemblance_threshold:
            detected_Student[predicted_id]=True
    return detected_Student,all_students,len(encodings)