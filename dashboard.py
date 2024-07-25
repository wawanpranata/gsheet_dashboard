import streamlit as st
from streamlit_gsheets import GSheetsConnection

#--------config-------
st.set_page_config(
    page_title="Data Profiler Dashboard",
    page_icon="🐱",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ------ Judul Dashboard -----
st.title("Data Profiler")
st.markdown("---")

#-------sidebar
with st.sidebar:
    st.subheader("Promotion Data")
    st.markdown("---")

if st.sidebar.button("Start Profiling Data"):
    conn = st.connection("gsheet",type=GsheetsConnection)
    conn = conn.read(
        spreadsheet = st.secrets.gsheet_promotion["spreadsheet"],
        worksheet = st.secrets.gsheet_promotion["worksheet"]
    )