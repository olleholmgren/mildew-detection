import streamlit as st
from app_pages.multi_page import MultiPage

from app_pages.hypothesis import hypothesis_body
from app_pages.summary import summary_body

app = MultiPage(app_name='Cherry leaf mildew detection')

app.app_page('Hypothesis', hypothesis_body)
app.app_page('Summary', summary_body)

app.run()
