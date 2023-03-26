import streamlit
import pandas as pd

streamlit.title("Hello! Rivery")
streamlit.header("This is a header sample 1")
streamlit.text("This is a text sample 1")
streamlit.text("This is a text sample 2")
streamlit.text("This is a text sample 3")
streamlit.text("This is a text sample 4")
streamlit.header("This is a header sample 2")


my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

