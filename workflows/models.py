import streamlit as st
from dataclasses import dataclass
from typing import Callable


@dataclass
class Task:
    name: str
    link: str | None = None
    button: Callable | None = None
    icon: str = ":material/link:"

    def create_components(self):
        cols = st.columns([6, 1])

        with cols[0]:
            checked = st.checkbox(self.name, value=st.session_state.tasks[self.name], key=self.name)
            st.session_state.tasks[self.name] = checked

        with cols[1]:
            if self.link:
                st.markdown(f'<a href="{self.link}">{self.icon}</a>', unsafe_allow_html=True)
            if self.button:
                if st.button(self.icon):
                    self.button()
                

class Flow:
    headers: list[str] = []
    widths: list[int] = []

    def __init__(self,
                 gate: Task | None = None,
                 items: dict[str, list[Task]] = {}) -> None:

        self.gate: Task | None = gate
        self.items: dict[str, list[Task]] = items

        Flow.headers += [x for x in self.items.keys() if x not in Flow.headers]
        Flow.widths = [1] * len(Flow.headers)

    @property
    def tasks(self) -> list[Task]:
        tasks = [self.gate] + [task for tasks in self.items.values() for task in tasks]
        return [x for x in tasks if isinstance(x, Task)]
    
    def get_task_names(self) -> list[str]:
        return [x.name for x in self.tasks]
    
    def init_session_state(self):
        st.session_state.setdefault("tasks", {})
        for name in self.get_task_names():
            st.session_state.tasks.setdefault(name, False)
    
    def create_header(self):
        columns = st.columns(Flow.widths)
        for col, header in zip(columns, Flow.headers):
            with col:
                st.write(f"#### {header}")

    def create_components(self):
        self.init_session_state()
        
        cols = st.columns(Flow.widths)
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