# main_app.py
import streamlit as st

# Define your pages
home_page = st.Page("./pages/home.py", title="Home", icon=":material/home:")
qameez_page = st.Page("./pages/qameez.py", title="Indian Style Qameez", icon=":material/draw:")

# Create the navigation menu
selected_page = st.navigation([home_page, qameez_page])

# Run the selected page
selected_page.run()

