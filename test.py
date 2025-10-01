import streamlit as st
from db.connection import get_engine, get_db, Base
from db.repository import add_user, get_all_users

# DB接続（SQLite）
engine = get_engine(db_type="sqlite", db_name="test.db")
Base.metadata.create_all(engine)  # テーブル作成
session = get_db(engine)

# Streamlit UI
st.title("User Management")

name = st.text_input("Name")
age = st.number_input("Age", min_value=0, step=1)

if st.button("Add User"):
    user = add_user(session, name, age)
    st.success(f"Added user: {user.name} (ID: {user.id})")

st.subheader("All Users")
users = get_all_users(session)
for user in users:
    st.write(f"ID: {user.id}, Name: {user.name}, Age: {user.age}")