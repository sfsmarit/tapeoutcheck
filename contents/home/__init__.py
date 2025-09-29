import streamlit as st

from utils.enums import MaskType, FilterType


def create_home():
    st.header("Tape-Out Checklist")

    # Create project
    st.subheader("Create new project")

    cols = st.columns([1,1,1,1])
    with cols[0]:
        st.session_state["mask_type"] = st.radio("Mask Type", [str(x) for x in MaskType])
    with cols[1]:
        st.session_state["filter_type"] = st.radio("Filter Type", [str(x) for x in FilterType])

    if st.button("Create project"):
        st.session_state["project_selected"] = True
        st.rerun()

    st.markdown("---")

    # Find project
    st.subheader("Find projects")
    items = [
        {"name": "DD010", "category": "回路"},
        {"name": "DD021", "category": "EMC"},
        {"name": "DD022", "category": "筐体"},
    ]

    # Search Window
    query = st.text_input("", placeholder="Keywords")
    if query:
        results = [item for item in items if query.lower() in item["name"].lower()]
    else:
        results = items

    # Display search results
    for item in results:
        name = item["name"]
        cols = st.columns([1, 3, 3, 3])
        with cols[0]:
            if st.button(":material/move_item:", key=name):
                open_project(name)
        with cols[1]:
            st.text(name)


def create_project():
    if st.session_state["mask_type"] == str(MaskType.ES):
        st.navigation([
            st.Page(page="contents/ES/top.py", title="Top", icon=":material/home:"),
            st.Page(page="contents/ES/design_check.py", title="Design Check", icon=":material/edit_document:"),
            st.Page(page="contents/ES/layout_check.py", title="Layout Check", icon=":material/border_color:"),
        ]).run()


def open_project(name: str):
    pass