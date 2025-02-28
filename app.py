import streamlit as st
import preprocessor

st.sidebar.title("WhatsApp Chat Analyszerer")

uploaded_file=st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data=bytes_data.decode("utf-8")
    # st.text(data)
    df=preprocessor.preprocess(data)

    st.dataframe(df)

