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
            if checked:
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
                

class WorkFlow:
    headers: list[str] = []
    widths: list[int] = []

    def __init__(self,
                 gate: Task | None = None,
                 items: dict[str, list[Task]] = {}) -> None:

        self.gate: Task | None = gate
        self.items: dict[str, list[Task]] = items

        WorkFlow.headers += [x for x in self.items.keys() if x not in WorkFlow.headers]
        WorkFlow.widths = [1] * len(WorkFlow.headers)

    @property
    def tasks(self) -> list[Task]:
        tasks = [self.gate] + [task for tasks in self.items.values() for task in tasks]
        return [x for x in tasks if isinstance(x, Task)]
    
    def get_task_names(self) -> list[str]:
        return [x.name for x in self.tasks]
    
    def create_header(self):
        columns = st.columns(WorkFlow.widths)
        for col, header in zip(columns, WorkFlow.headers):
            with col:
                st.write(f"#### {header}")

    def create_components(self):
        cols = st.columns(WorkFlow.widths)
        for icol, (col, tasks) in enumerate(zip(cols, self.items.values())):
            with col:
                for i, task in enumerate(tasks):
                    task.create_components()
                    if icol == 0 and i < len(tasks) - 1:
                        # タテ線
                        st.markdown("""
                            <div style="height:30px; border-left:3px solid #888; margin-left:7px; margin-top:-10px; margin-bottom:8px;"></div>
                        """, unsafe_allow_html=True)

        # Gate
        task = self.gate
        if task:
            st.markdown("---")  
            task.create_components()
            st.markdown("---")