import streamlit as st
from typing import Callable

from state import state
from utils import generate_sha256_hash

from db.connection import get_session
from db.models import TaskData
from db.repository import Respository


class Task:
    def __init__(self,
                 name: str,
                 link: str = "",
                 button: Callable | None = None,
                 icon: str = "") -> None:

        self.id: str = generate_sha256_hash(name)
        self.name: str = name
        self.link: str = link
        self.button: Callable | None = button
        self.icon: str = icon

        if link and not icon :
            self.icon = ":material/link:"
            
        self.check_db()
            
    def check_db(self):
        repo = Respository(get_session(), TaskData)
        
        data = repo.get_by_fields( # type: ignore
            tapeout=state.tapeout.name,
            task_id=self.id
        )
        
        if data is not None:
            self.data: TaskData = data
        else:
            self.data: TaskData = repo.add(
                tapeout=state.tapeout.name,
                task_id=self.id,
                name=self.name,
            )

    def create_components(self):
        cols = st.columns([6, 1])

        with cols[0]:
            checked = st.checkbox(self.name, value=self.data.status, key=self.name)
            if checked != self.data.status:
                repo = Respository(get_session(), TaskData)
                id = repo.get_id_by_fields(tapeout=state.tapeout.name, task_id=self.id)
                if id is not None:
                    self.data = repo.update(id, status=checked) # type: ignore
                
        with cols[1]:
            if self.link:
                st.markdown(f'<a href="{self.link}">{self.icon}</a>', unsafe_allow_html=True)
            if self.button:
                if st.button(self.icon):
                    self.button()
                