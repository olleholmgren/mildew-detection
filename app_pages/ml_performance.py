import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.image import imread
from src.machine_learning.evaluate_clf import load_test_evaluation


def ml_performance_metrics_body():

    version = 'v3'

    st.write('### Train, validation and test set: Labels frequencies')

    labels_distribution = plt.imread(
        f'outputs/{version}/labels_distribution.png')
    st.image(labels_distribution,
             caption='Labels distribution on train, validation and test sets')
    st.write(
        f'The dataset for this project is from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves).\n'
        f'It contains images of 2104 healthy leaves and 2104 infected leaves. '
        f'The dataset has been split into three datasets for training, '
        f'validation and test.'
    )
    st.info(
        f'* Train - healthy: 1472 images\n'
        f'* Train - powdery_mildew: 1472 images\n'
        f'* Validation - healthy: 210 images\n'
        f'* Validation - powdery_mildew: 210 images\n'
        f'* Test - healthy: 422 images\n'
        f'* Test - powdery_mildew: 422 images\n')

    st.write('---')

    st.write('### Model history')

    st.write(
        f'The graphs depict the ML model learning cycle, illustrating '
        f'accuracy and loss during training. It is clear the model follows a '
        f'typical learning curve, indicating no overfitting or underfitting.')

    col1, col2 = st.beta_columns(2)
    with col1:
        model_acc = plt.imread(f'outputs/{version}/model_training_acc.png')
        st.image(model_acc, caption='Model training accuracy')
    with col2:
        model_loss = plt.imread(f'outputs/{version}/model_training_losses.png')
        st.image(model_loss, caption='Model training losses')
    st.write('---')

    st.write('### Generalised performance on test set')
    st.dataframe(pd.DataFrame(load_test_evaluation(version),
                              index=['Loss', 'Accuracy']))
