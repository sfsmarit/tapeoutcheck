import streamlit as st

from workflows import create_flowchart
from components.progress_bar import create_progress_bar


# Page title
page_title = "Tape-Out Checklist"
st.set_page_config(page_title=page_title, layout="wide")
st.title(page_title)


# Designer
st.text_input("Lead Designer", placeholder="Your Name")


# Part Number
st.text_input("Part Number", placeholder="DD012NQ345MD")


# TO Name
st.text("Tape-Out Name")
cols = st.columns([1, 0.2, 0.5, 0.2, 1, 4])
with cols[0]:
    st.text_input("", placeholder="DD012", label_visibility="collapsed")
with cols[1]:
    st.text("-")
with cols[2]:
    st.text_input("", "N", label_visibility="collapsed")
with cols[3]:
    st.text("-")
with cols[4]:
    st.text_input("", "OSK", label_visibility="collapsed")


# SkyFoundry URL
st.text("SkyFoundry")
cols = st.columns([2, 8])
with cols[0]:
    if st.button("Get URL"):
        pass
with cols[1]:
    pn = st.text_input("", placeholder="URL", label_visibility="collapsed")


# SAP sheet URL
st.text_input("SAP Registration Sheet", placeholder="URL")


create_flowchart()


create_progress_bar()
