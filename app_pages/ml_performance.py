import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.image import imread
from src.machine_learning.evaluate_clf import load_test_evaluation


def ml_performance_metrics_body():

    version = 'v3'

    st.write('### Train, validation and test set: Labels frequencies')

    labels_distribution = plt.imread(
        f'output/{version}/labels_distribution.png')
    st.image(labels_distribution,
             caption='Labels distribution on train, validation and test sets')
    st.write('---')

    st.write('### Model history')
    col1, col2 = st.beta_columns(2)
    with col1:
        model_acc = plt.imread(f'output/{version}/model_training_acc.png')
        st.image(model_acc, caption='Model training accuracy')
    with col2:
        model_loss = plt.imread(f'output/{version}/model_training_losses.png')
        st.image(model_loss, caption='Model training losses')
    st.write('---')

    st.write('### Generalised performance on test set')
    # st.dataframe(pd.DataFrame(load_test_evaluation(version),
    # index=['Loss', 'Accuracy'])
