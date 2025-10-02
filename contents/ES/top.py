import streamlit as st

from components.progress_bar import create_progress_bar

from workflows import ES_JP


# Designer
st.text_input("Lead Designer", placeholder="Your Name")


# SkyFoundry URL
st.text("SkyFoundry")
st.text_input("", placeholder="URL", label_visibility="collapsed")


# SAP sheet URL
st.text_input("SAP Registration Sheet", placeholder="URL")


# Create flowchart
st.markdown("---")


if True:
    flows = ES_JP.workflows

flows[0].create_header()
st.markdown("---")

statuses = []
for flow in flows:
    flow.create_components()
    statuses += [task.data.status for task in flow.tasks]

create_progress_bar(statuses)    