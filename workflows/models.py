from dataclasses import dataclass
from typing import Callable
import streamlit as st


@dataclass
class Task:
    name: str
    link: str | Callable | None = None
    button: dict[str, Callable] | None = None

    def create(self):
        cols = st.columns([6, 1])

        with cols[0]:
            checked = st.checkbox(self.name, value=st.session_state.tasks[self.name], key=self.name)
            st.session_state.tasks[self.name] = checked

        with cols[1]:
            if self.link:
                st.markdown(f'<a href="{self.link}">:material/link:</a>', unsafe_allow_html=True)
            if self.button:
                for label, func in self.button.items():
                    if st.button(label=label):
                        func()
                

@dataclass
class Flow:
    gate: Task | None
    workflows: list[Task]
    skyfoundry: list[Task]
    agile: list[Task]
    
    def get_task_names(self) -> list[str]:
        tasks = [self.gate] + self.workflows + self.skyfoundry + self.agile
        return [task.name for task in tasks if task is not None]
        
