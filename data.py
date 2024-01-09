# app.py

import streamlit as st

def main():
    st.title("My Streamlit Website")
    st.write("Welcome to my website!")

    # Add more content
    st.header("Some Content Section")
    st.write("This is some text.")
    
    # Example of a button
    if st.button("Click me!"):
        st.success("Button clicked!")

    # Example of a selectbox
    option = st.selectbox("Choose an option", ["Option 1", "Option 2", "Option 3"])
    st.write("You selected:", option)

    # Add more components as needed

if __name__ == "__main__":
    main()
