import streamlit as st
from app_pages.multi_page import MultiPage

app = MultiPage(app_name='Welcome to the dashboard')

app.run()
