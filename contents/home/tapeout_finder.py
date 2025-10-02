import streamlit as st

from state import state

from db.connection import get_session
from db.models import TapeoutData
from db.repository import Respository


def create_tapeout_finder():
    st.subheader("Find projects")

    tapeout_repo = Respository(get_session(), TapeoutData)
    tapeouts: list[TapeoutData] = tapeout_repo.get_all()

    # Search Window
    query = st.text_input("", placeholder="Keywords")
    if query:
        filtered = [tapeout for tapeout in tapeouts if query.lower() in tapeout.name.lower()]
    else:
        filtered = tapeouts

    # Display search results
    widths = [1, 3, 3, 3, 3, 3, 3]
    cols = st.columns(widths)
    with cols[1]:
       st.markdown("Part Number")
    with cols[2]:
       st.markdown("Mask Type")
    with cols[3]:
       st.markdown("FE Tech")

    for i, tapeout in enumerate(filtered):
        cols = st.columns(widths)
        with cols[0]:
            if st.button(":material/move_item:", key=i):
                load_tapeout(tapeout.name)
        with cols[1]:
            st.text(tapeout.name)
        with cols[2]:
            st.text(tapeout.mask_type.name)
        with cols[3]:
            st.text(tapeout.fe_tech.name)


def load_tapeout(name):
    tapeout_repo = Respository(get_session(), TapeoutData)
    state.tapeout = tapeout_repo.get_by_fields(name=name) # type: ignore
    st.rerun()