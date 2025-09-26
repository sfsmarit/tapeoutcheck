from dataclasses import dataclass
from typing import Callable
import streamlit as st

@dataclass
class Task:
    name: str
    link: str | Callable | None = None
    button: Callable | None = None

    def create_checkbox(self):
        checked = st.checkbox(self.name, value=st.session_state.tasks[self.name], key=self.name)
        st.session_state.tasks[self.name] = checked
        
        if self.link:
            st.button(":link:")
            

@dataclass
class Taskblock:
    gate: Task | None
    
    # Required tasks to complete gating item
    steps: list[Task]
    skyfoundry: list[Task]
    agile: list[Task]
    
    def get_task_names(self) -> list[str]:
        tasks = [self.gate] + self.steps + self.skyfoundry + self.agile
        return [task.name for task in tasks if task is not None]
        
