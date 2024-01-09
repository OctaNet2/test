# app.py

import streamlit as st

def main():
    st.title("My Streamlit Website")

    # Navbar
    st.markdown(
        """
        <style>
            .navbar {
                display: flex;
                padding: 10px;
                background-color: #f1f1f1;
            }
            .nav-item {
                margin-right: 20px;
            }
        </style>
        """
    , unsafe_allow_html=True)

    nav_options = ["Home", "Page 1", "Page 2", "About"]

    selected_nav = st.sidebar.radio("Navigation", nav_options)

    # Content based on selected navbar option
    if selected_nav == "Home":
        st.write("Welcome to the Home Page!")
    elif selected_nav == "Page 1":
        st.write("This is Page 1.")
    elif selected_nav == "Page 2":
        st.write("This is Page 2.")
    elif selected_nav == "About":
        st.write("This is the About Page.")

    # Add more components as needed

if __name__ == "__main__":
    main()
