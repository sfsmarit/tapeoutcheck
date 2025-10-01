import streamlit as st

from contents.home import create_home, create_project


st.session_state["DEBUG"] = True


st.set_page_config(page_title="Tape-Out Checklist", page_icon=":white_check_mark:")

if st.session_state["DEBUG"] or st.session_state.get("project_selected", False):     
    create_project()
else:
    create_home()
