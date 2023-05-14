import streamlit as st
import pandas as pd

st.title("Analysis...")

file = st.file_uploader("Upload your Excel file", type=["xlsx"])
if file is not None:
    df = pd.read_excel(file)
    st.dataframe(df.head(8))
    st.write("Total number of rows", df.shape[0])

    st.write("## Select marks column to analyse")
    cols = st.selectbox("Select columns which has marks", df.columns.tolist())

    if len(cols) <= 0:
        st.write("Choose at least one column")

    else:
        st.write("####")
        st.write(cols)

    if st.checkbox("Confirm"):
        max = st.number_input("Enter max marks", value=100)
        bins = [0, 33, 41, 51, 61, 71, 81, 91, 100]
        labels = ["Below 33", "33-40", "41-50", "51-60", "61-70", "71-80", "81-90", "91-100"]

        if max == 0:
            st.write("Max marks cannot be zero")
        else:
            df[cols] = pd.to_numeric(df[cols], errors='coerce')
            df[cols] = df.dropna()
            df[cols] = df[cols] * 100 / max
            df[cols] = df[cols].astype(int)

            df['Ranges'] = pd.cut(df[cols], bins=bins, labels=labels)

            st.write("## Analysis")
            st.dataframe(df.groupby('Ranges').count())


        

