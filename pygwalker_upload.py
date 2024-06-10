from pygwalker.api.streamlit import StreamlitRenderer
import pandas as pd
import streamlit as st
import streamlit.components.v1 as stc
import pygwalker as pyg

# Adjust the width of the Streamlit page
st.set_page_config(
    page_title="Custom Data Explorer",
    layout="wide"
)

st.title("Data Visualization Explorer")

# st.subheader("You can explore your file")
# st.write("Please, upload your CSV file here!")
with st.expander("Description:", expanded=True):
    st.markdown("In this page, you are provided with tools to be able to do Data Visualization exploration with your dataset.")
    

def load_data(data):
    try:
        df = pd.read_csv(data)
        return df
    except Exception as e:
        st.error(f"Error loading file: {e}")
        return None

with st.form("Upload Form"):
    data_file = st.file_uploader("Please, upload your CSV file", type=["csv","txt"])
    submitted = st.form_submit_button("Submit")

if submitted:
    if data_file is None:
        st.error("No file uploaded. Please upload a CSV file.")
    else:
        df = load_data(data_file)
        if df is not None:
            st.success("Your file is successfully uploaded!")
            st.dataframe(df)
            # Visualize
            pyg_html = pyg.walk(df, return_html=True)
            # Render with components
            # stc.html(pyg_html, scrolling=True, height=1000)
            pyg_app = StreamlitRenderer(df)
            # Just header for explorer
            st.write("### Let's Visualize Your Data!")
            pyg_app.explorer()
        else:
            st.error("Failed to load the file. Please check the file format and try again!")
    