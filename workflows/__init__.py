import streamlit as st

from . import ES_JP


def create_flowchart():
    if True:
        flows = ES_JP.workflows

    flows[0].create_header()
    st.markdown("---")
    for flow in flows:
        flow.create_components()