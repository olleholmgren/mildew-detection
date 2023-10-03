import streamlit as st


def summary_body():
    st.write('### Summary')

    st.success(
        F'This project has 2 business requirements:\n'
        F'* The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.\n\n'
        F'* The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.')
