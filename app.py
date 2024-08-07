import streamlit as st

# Set the title of the app
st.title('My First Streamlit App')

# Add a text input
user_input = st.text_input("Enter some text:")

# Display the entered text
st.write(f'You entered: {user_input}')

# Add a slider
slider_value = st.slider('Select a value:', 0, 100, 50)

# Display the slider value
st.write(f'Slider value: {slider_value}')

# Add a button and display a message when clicked
if st.button('Click me'):
    st.write('Button clicked!')
