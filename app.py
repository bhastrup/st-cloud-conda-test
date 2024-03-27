import sys
import streamlit as st


with st.echo():
    st.write(f"sys.version: {sys.version}")
    st.write(f"sys.executable: {sys.executable}")

st.write("Should have been something like '/home/adminuser/.conda/bin/python' ")

