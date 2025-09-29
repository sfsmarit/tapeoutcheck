import streamlit as st

from contents.home import create_home, create_project


st.set_page_config(page_title="Tape-Out Checklist", page_icon=":white_check_mark:")

if st.session_state.get("project_selected", False):
    create_project()
else:
    create_home()
