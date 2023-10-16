import streamlit as st


def summary_body():
    st.write('## Summary')

    st.info(
        f'Powdery mildew, caused by Podosphaera clandestina, affects '
        f'cherry trees, leading to white powdery spots on leaves and stems, '
        f'especially on lower leaves.\n '
        f'It thrives in high humidity and moderate '
        f'temperatures, causing significant damage to plants and reducing '
        f'harvests.')

    st.success(
        f'This project has 2 business requirements:\n'
        f'* The client is interested in conducting a study to visually '
        f'differentiate a healthy cherry leaf '
        f'from one with powdery mildew.\n\n'
        f'* The client is interested in predicting if a cherry leaf is '
        f'healthy or contains powdery mildew.')
