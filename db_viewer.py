import streamlit as st
import sqlite3
import pandas as pd
import os

st.title("SQLite DB ビューワー")

# .dbファイルのパスを指定（例: checklist.db）
db_path = st.text_input("SQLiteファイルのパスを入力", "test.db")

if os.path.exists(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # テーブル一覧を取得
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = [row[0] for row in cursor.fetchall()]

    if tables:
        selected_table = st.selectbox("表示するテーブルを選択", tables)

        # テーブル内容を取得して表示
        df = pd.read_sql_query(f"SELECT * FROM {selected_table}", conn)
        st.subheader(f"テーブル: {selected_table}")
        st.dataframe(df)
    else:
        st.warning("テーブルが存在しません。")
    
    conn.close()
else:
    st.error("指定された .db ファイルが存在しません。")