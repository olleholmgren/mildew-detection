import streamlit as st
from app_pages.multi_page import MultiPage

from app_pages.hypothesis import hypothesis_body
from app_pages.summary import summary_body
from app_pages.visualizer import visualizer_body
from app_pages.mildew_detection import mildew_detection_body
from app_pages.ml_performance import ml_performance_metrics_body

app = MultiPage(app_name='Cherry leaf mildew detection')

app.app_page('Hypothesis', hypothesis_body)
app.app_page('Summary', summary_body)
app.app_page('Visualizer', visualizer_body)
app.app_page('Mildew Detection', mildew_detection_body)
app.app_page('Machine Learning Performance', ml_performance_metrics_body)

app.run()
