
import streamlit as st
from supabase import create_client, Client

# Supabase接続情報
url = "https://celxjiaztmqihjapdncj.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImNlbHhqaWF6dG1xaWhqYXBkbmNqIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTkxMDQ2OTUsImV4cCI6MjA3NDY4MDY5NX0.jX0oNbCMTzaBVBSp_kwz9CnFtX694FvSHDI2BBsDYNw"  # ダッシュボードから取得

supabase: Client = create_client(url, key)

# 入力フォーム
st.title("TOチェックリスト")
user = st.text_input("名前")
item = st.text_input("項目")
status = st.selectbox("ステータス", ["未完了", "完了"])

if st.button("保存"):
    data = {
        "user": user,
        "item": item,
        "status": status
    }
    res = supabase.table("test").insert(data).execute()
    print(res)

# データ表示
