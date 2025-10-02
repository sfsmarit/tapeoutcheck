import streamlit as st

from workflows import create_flowchart
from components.progress_bar import create_progress_bar


# Designer
st.text_input("Lead Designer", placeholder="Your Name")


# SkyFoundry URL
st.text("SkyFoundry")
st.text_input("", placeholder="URL", label_visibility="collapsed")


# SAP sheet URL
st.text_input("SAP Registration Sheet", placeholder="URL")


# Create flowchart
st.markdown("---")


create_flowchart()


create_progress_bar()
