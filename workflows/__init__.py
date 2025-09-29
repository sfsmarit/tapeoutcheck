import streamlit as st

from . import SAW_ES_JP

def create_flowchart():
    # Select flow
    if True:
        flows = SAW_ES_JP.flows

    # Initiallize session_state
    if "tasks" not in st.session_state:
        st.session_state.tasks = {}
        for block in flows:
            for task in block.get_task_names():
                st.session_state.tasks[task] = False

    # Create flowchart
    st.markdown("---")

    col_array = [4, 3, 3]

    cols = st.columns(col_array)
    with cols[0]:
        st.write("#### Workflows")
    with cols[1]:
        st.write("#### SkyFoundry")
    with cols[2]:
        st.write("#### Agile")

    st.markdown("---")

    for block in flows:
        # Checker items
        cols = st.columns(col_array)
        with cols[0]:
            for i, task in enumerate(block.workflows):
                task.create()
                if i < len(block.workflows) - 1:
                    st.markdown("""
                        <div style="height:30px; border-left:3px solid #888; margin-left:7px; margin-top:-10px; margin-bottom:8px;"></div>
                    """, unsafe_allow_html=True)
        with cols[1]:
            for task in block.skyfoundry:
                task.create()
        with cols[2]:
            for task in block.agile:
                task.create()
        
        # Gating item
        task = block.gate
        if task:
            st.markdown("---")  
            task.create()
            st.markdown("---")