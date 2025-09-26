import streamlit as st

from task.ES_jpn import taskblocks

sp = "&nbsp;"

# Initiallize flows
if "tasks" not in st.session_state:
    st.session_state.tasks = {}
    for block in taskblocks:
        for task in block.get_task_names():
            st.session_state.tasks[task] = False

# Page title
page_title = "Tape-Out Checklist"
st.set_page_config(page_title=page_title, layout="wide")
st.title(page_title)


# Designer
designer = st.text_input("Lead Designer", placeholder="Your Name")


# Part Number
pn = st.text_input("Part Number", placeholder="DD012NQ345MD")


# TO Name
st.text("Tape-Out Name")
cols = st.columns([1, 0.2, 0.5, 0.2, 1, 4])
with cols[0]:
    tapeout_name = st.text_input("", placeholder="DD012", label_visibility="collapsed")
with cols[1]:
    st.text("-")
with cols[2]:
    tapeout_name = st.text_input("", "N", label_visibility="collapsed")
with cols[3]:
    st.text("-")
with cols[4]:
    tapeout_name = st.text_input("", "OSK", label_visibility="collapsed")


# SkyFoundry URL
st.text("SkyFoundry")
cols = st.columns([2, 8])
with cols[0]:
    if st.button("Get URL"):
        pass
with cols[1]:
    pn = st.text_input("", placeholder="URL", label_visibility="collapsed")


# SkyFoundry URL
pn = st.text_input("SAP Registration Sheet", placeholder="URL")


# Add workflows
st.markdown("---")

col_array = [4, 3, 3]

cols = st.columns(col_array)
with cols[0]:
    st.write("#### Workflows")
with cols[1]:
    st.write("#### SkyFoundry")
with cols[2]:
    st.write("#### Agile")

st.markdown("---")

for block in taskblocks:
    # Checker items
    cols = st.columns(col_array)
    with cols[0]:
        for i, task in enumerate(block.steps):
            task.create_checkbox()
            if i < len(block.steps) - 1:
                st.markdown("""
                    <div style="height:30px; border-left:3px solid #888; margin-left:7px; margin-top:-10px; margin-bottom:8px;"></div>
                """, unsafe_allow_html=True)
    with cols[1]:
        for task in block.skyfoundry:
            task.create_checkbox()
    with cols[2]:
        for task in block.agile:
            task.create_checkbox()
    
    # Gating item
    task = block.gate
    if task:
        st.markdown("---")  
        task.create_checkbox()
        st.markdown("---")


# Progress bar
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
            <progress value="{progress}" max="1" style="width: 100%; height: 20px;"></progress>
            <p>達成率{sp}{sp}{sp}{sp}{n_completed}/{n_tasks}{sp}{sp}{sp}{sp}({int(progress * 100)}%)</p>
        </div>
    </div>
""", unsafe_allow_html=True)