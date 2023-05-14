import streamlit as st
import pandas as pd
from utils import utils

st.title("Easy Excel!")

file = st.file_uploader("Upload your Excel file", type=["xlsx"])
if file is not None:
    df = pd.read_excel(file)
    st.dataframe(df.head(8))

    st.write("## Select columns")
    cols = st.multiselect("Select columns", df.columns.tolist())

    if len(cols) <= 0:
        st.write("Choose at least one column")
    else:
        st.write("####")
        st.write(cols)

    if st.checkbox("Confirm"):
        st.write("You have selected", len(cols), "columns")
        final = df.loc[:, cols]

        st.write("## Sort by")
        sort_by = st.selectbox("Select column to sort by", cols)
        final = final.sort_values(by=sort_by)
        st.dataframe(final.head(8))

        final.to_excel("easy.xlsx", index=False)

        with open('easy.xlsx', 'rb') as excel_file:
            if st.download_button(label = 'Download', data = excel_file, file_name = 'easy.xlsx', mime = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'):
                st.success("Downloaded")
        