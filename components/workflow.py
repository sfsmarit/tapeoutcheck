import streamlit as st
from .task import Task
    

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