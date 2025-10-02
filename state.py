import streamlit as st

from db.models import TapeoutData, TaskData


class StateWrapper:
    @classmethod
    def init(cls):
        st.session_state.setdefault("tapeout", TapeoutData())
        st.session_state.setdefault("task", TaskData())

    @property
    def tapeout(self) -> TapeoutData:
        return st.session_state["tapeout"]
    
    @tapeout.setter
    def tapeout(self, x: TapeoutData):
        st.session_state["tapeout"] = x
        
    @property
    def task_data(self) -> TaskData:
        return st.session_state["task_data"]
    
    @task_data.setter
    def task_data(self, x: TaskData):
        st.session_state["task_data"] = x
        
    
        
        
state = StateWrapper()