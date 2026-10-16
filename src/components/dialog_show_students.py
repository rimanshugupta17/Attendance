import streamlit as st


@st.dialog("Students Present")
def show_students_dialog(student_names, subject, timestamp):

    st.subheader(subject)

    st.caption(timestamp)

    st.divider()

    if student_names:
        st.write(f"**{len(student_names)} Students Present**")

        for name in student_names:
            st.write(f"👤 {name}")
    else:
        st.info("No students present.")