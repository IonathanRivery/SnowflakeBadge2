import streamlit
import pandas as pd

streamlit.title("Hello! Rivery")
streamlit.header("This is a header sample 1")
streamlit.text("This is a text sample 1")
streamlit.text("This is a text sample 2")
streamlit.text("This is a text sample 3")
streamlit.text("This is a text sample 4")
streamlit.header("This is a header sample 2")

streamlit.header("My Fruit List")
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# setting an index by the column "Fruit" - indexes will be taken from this column instead of default number indexes
my_fruit_list = my_fruit_list.set_index("Fruit")

# Creating a selection for the user with streamlit.multiselect()
streamlit.multiselect("Pick some fruits: ", list(my_fruit_list.index))

# Filter the dataframe based on the selected fruits
filtered_fruit_list = my_fruit_list.loc[list(my_fruit_list)]

# Present the table
streamlit.dataframe(filtered_fruit_list)

