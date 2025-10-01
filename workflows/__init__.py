import streamlit as st

from . import SAW_ES_JP


def create_flowchart():
    if True:
        flows = SAW_ES_JP.flows

    flows[0].create_header()
    st.markdown("---")
    for flow in flows:
        flow.create_components()