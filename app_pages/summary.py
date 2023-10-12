import streamlit as st


def summary_body():
    st.write('### Summary')

    st.success(
        f'This project has 2 business requirements:\n'
        f'* The client is interested in conducting a study to visually '
        f'differentiate a healthy cherry leaf '
        f'from one with powdery mildew.\n\n'
        f'* The client is interested in predicting if a cherry leaf is '
        f'healthy or contains powdery mildew.')
