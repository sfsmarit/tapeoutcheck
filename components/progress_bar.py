import streamlit as st

sp = "&nbsp;"

def create_progress_bar():
    n_completed = sum(v for v in st.session_state.tasks.values())
    n_tasks = len(st.session_state.tasks)
    progress =  n_completed / n_tasks 

    st.markdown(f"""
        <style>
        .footer-bar {{
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: #333333;
            padding: 10px;
            text-align: center;
            z-index: 100;
        }}
        .progress-container {{
            width: 80%;
            margin: auto;
        }}
        </style>
        <div class="footer-bar">
            <div class="progress-container">
                <progress value="{progress}" max="1" style="width: 80%; height: 20px;"></progress>
                <p>達成率{sp}{sp}{sp}{sp}{n_completed}/{n_tasks}{sp}{sp}{sp}{sp}({int(progress * 100)}%)</p>
            </div>
        </div>
    """, unsafe_allow_html=True)