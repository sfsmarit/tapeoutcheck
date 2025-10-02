import streamlit as st

from state import state
from utils.enums import MaskType, FETech

from db.connection import get_session
from db.models import TapeoutData
from db.repository import Respository


def create_header():
    is_valid_tapeout = state.tapeout.has_valid_name()

    if not is_valid_tapeout:
        st.subheader("Create New Tape-Out")

    # TO Name
    st.text("Tape-Out Name")
    tapeout_name = ""

    cols = st.columns([1, 0.2, 0.5, 0.2, 1, 4])

    with cols[0]:
        value = state.tapeout.name[:5] if is_valid_tapeout else ""
        tapeout_name += st.text_input("", value, disabled=is_valid_tapeout, placeholder="DF123", label_visibility="collapsed")
    with cols[1]:
        st.text("-")
        tapeout_name += "-"
    with cols[2]:
        value = state.tapeout.name[6] if is_valid_tapeout else "N"
        tapeout_name +=  st.text_input("", value, disabled=is_valid_tapeout, label_visibility="collapsed")
    with cols[3]:
        st.text("-")
        tapeout_name += "-"
    with cols[4]:
        value = state.tapeout.name[8:] if is_valid_tapeout else "OSK"
        tapeout_name +=  st.text_input("", value, disabled=is_valid_tapeout, label_visibility="collapsed")

    cols = st.columns([1,1,1,1])

    # Mask Type
    with cols[0]:
        idx = 0 if state.tapeout.mask_type is None else list(MaskType).index(state.tapeout.mask_type)
        x = st.radio("Mask Type", [x.name for x in MaskType], index=idx, disabled=is_valid_tapeout)
        state.tapeout.mask_type = MaskType[x]
    with cols[1]:
        idx = 0 if state.tapeout.fe_tech is None else list(FETech).index(state.tapeout.fe_tech)
        x = st.radio("Filter Type", [x.name for x in FETech], index=idx, disabled=is_valid_tapeout)
        state.tapeout.fe_tech = FETech[x]

    # Create TO button
    if not is_valid_tapeout and st.button("Create TO"):
        state.tapeout.name = tapeout_name
        
        if not state.tapeout.has_valid_name():
            st.error(f"Invalid Tape-Out name '{state.tapeout.name}'")
        else:
            tapeout_repo = Respository(get_session(), TapeoutData)
            state.tapeout = tapeout_repo.add(
                name=state.tapeout.name,
                mask_type=state.tapeout.mask_type,
                fe_tech=state.tapeout.fe_tech,
            )
            st.rerun()
