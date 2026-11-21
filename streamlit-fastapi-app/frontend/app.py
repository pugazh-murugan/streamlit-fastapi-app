import os

import requests
import streamlit as st

BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")
API = f"{BACKEND_URL}/api/items"

st.set_page_config(page_title="Sample App", page_icon="📦", layout="centered")
st.title("📦 Streamlit + FastAPI Sample")


def api_ok() -> bool:
    try:
        return requests.get(f"{BACKEND_URL}/health", timeout=3).ok
    except requests.RequestException:
        return False


if not api_ok():
    st.error(f"Backend not reachable at {BACKEND_URL}")
    st.stop()

st.success("Backend connected")

# --- Add item ---
with st.form("add_item", clear_on_submit=True):
    name = st.text_input("Name")
    description = st.text_area("Description")
    if st.form_submit_button("Add item"):
        if name.strip():
            r = requests.post(API + "/", json={"name": name, "description": description}, timeout=5)
            st.toast("Item added" if r.ok else f"Error: {r.text}")
            st.rerun()
        else:
            st.warning("Name is required")

# --- List items ---
st.subheader("Items")
items = requests.get(API + "/", timeout=5).json()

if not items:
    st.info("No items yet.")
for item in items:
    col1, col2 = st.columns([5, 1])
    col1.markdown(f"**{item['name']}**  \n{item['description']}")
    if col2.button("Delete", key=f"del_{item['id']}"):
        requests.delete(f"{API}/{item['id']}", timeout=5)
        st.rerun()
