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
selected_fruits = streamlit.multiselect("Pick some fruits: ", list(my_fruit_list.index), default=list(my_fruit_list.index))

# Check if any fruit is selected
if selected_fruits:
    # Filter the dataframe based on the selected fruits
    filtered_fruit_list = my_fruit_list.loc[selected_fruits]
    # Present the filtered table
    streamlit.dataframe(filtered_fruit_list)
else:
    # Present the entire table
    streamlit.dataframe(my_fruit_list)

# Add a callback to update the table when the user changes the selected fruits
def update_table():
    selected_fruits = multiselect_widget.current_value
    if selected_fruits:
        filtered_fruit_list = my_fruit_list.loc[selected_fruits]
        table_widget.dataframe(filtered_fruit_list)
    else:
        table_widget.dataframe(my_fruit_list)
        
        
#lesson 9 - new section        
import requests    

'''
streamlit.header("Fruityvice Fruit Advice!")
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/all")
streamlit.text(fruityvice_response)
fruit_choice = streamlit.multiselect("Pick some fruits you would like to get some more info on: ", list(my_fruit_list.index))
selected_fruit = streamlit.text('The user entered: ').write(fruit_choice)
fruityvice_response1 = requests.get("https://fruityvice.com/api/fruit/" + str(selected_fruit))
# take the json version of the response and normalize it
fruityvice_normalized = pd.json_normalize(fruityvice_response1.json())
# output it the screen as a table
streamlit.dataframe (fruityvice_normalized)
'''

streamlit.header("Fruityvice Fruit Advice!")
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/all")
streamlit.text(fruityvice_response)
fruit_choice = streamlit.multiselect("Pick some fruits you would like to get some more info on: ", list(my_fruit_list.index))
# Check if any fruit is selected
if fruit_choice:
    # Get the selected fruit
    selected_fruit = fruit_choice[0]
    streamlit.text('The user selected: ' + selected_fruit)
    # Send the API request for the selected fruit
    fruityvice_response1 = requests.get("https://fruityvice.com/api/fruit/" + selected_fruit)
    # Take the json version of the response and normalize it
    fruityvice_normalized = pd.json_normalize(fruityvice_response1.json())
    # Output it to the screen as a table
    streamlit.dataframe(fruityvice_normalized)
else:
    streamlit.text('Please select at least one fruit')
















