import streamlit as st

from state import state
state.init()

from contents.home.header import create_header
from contents.home.tapeout_finder import create_tapeout_finder
from contents.home.pages import create_pages


page_title = "SAW Tape-Out Checklist"
st.set_page_config(page_title=page_title, layout="wide")
st.title(page_title)

st.markdown("---")
create_header()
st.markdown("---")

if not state.tapeout.has_valid_name():
    create_tapeout_finder()
else:
    create_pages()    
