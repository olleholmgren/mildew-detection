import streamlit as st


def hypothesis_body():
    st.write('### Project hypothesis')

    st.success(
        f"* We have reason to believe that leaves affected by powdery mildew 
        exhibit distinct, visible markings, "
        f"typically, powdery mildew-infected leaves display white dots 
        scattered across the surface, distinguishing them from healthy 
        leaves. \n\n"
        f"* An image montage illustrates that a leaf affected by mildew 
        typically displays white marks scattered across its surface. "
        f"The studies involving average images, variability images, and 
        the differences between averages did not reveal any distinct "
        f"patterns to differentiate them, except for a slight whitening 
        observed in the images."
    )
