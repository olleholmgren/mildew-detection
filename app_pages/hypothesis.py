import streamlit as st


def hypothesis_body():
    st.write('## Project hypothesis')

    st.success(
        f'* We have reason to believe that leaves infected by powdery mildew '
        f'exhibit distinct, visible markings. '
        f'Typically, powdery mildew-infected leaves display white dots '
        f'scattered across the surface, distinguishing them from healthy '
        f'leaves. \n\n'
        f'* To validate this, cherry leaves with powdery mildew will be '
        f'compared to healthy cherry leaves. \n\n'
        f'* The distinction between a healty leaf and a powdery mildew '
        f'leaf will be carried out by a trained machine learning model '
        f'with an agreed accuracy of 97% or higher. \n\n')

    st.info(
        f'* An image montage in this project illustrates that a leaf '
        f'infected by mildew '
        f'typically displays white marks scattered across its surface. '
        f'The studies involving average images, variability images, and '
        f'the differences between averages did not reveal any distinct '
        f'patterns to differentiate them, except for a slight whitening '
        f'observed in the images.'
    )
