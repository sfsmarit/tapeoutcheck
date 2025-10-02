import streamlit as st

from utils.enums import MaskType


def create_pages():
    if st.session_state.tapeout.mask_type == MaskType.ES:
        # Create sidebar
        st.navigation([
            st.Page(page="contents/ES/top.py", title="Top", icon=":material/home:"),
            st.Page(page="contents/ES/design_check.py", title="Design Check", icon=":material/edit_document:"),
            st.Page(page="contents/ES/layout_check.py", title="Layout Check", icon=":material/border_color:"),
        ]).run()

    if st.session_state.tapeout.mask_type == MaskType.MP:
        pass
    