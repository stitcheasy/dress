
import streamlit as st

# Define your pages
home_page = st.Page("./pages/home.py", title="Home", icon=":material/home:")
measurement_page = st.Page("./pages/givemeasurement.py", title="Measurements", icon=":material/measuring_tape:")
qameez_page = st.Page("./pages/qameez.py", title="Kurti-Front&Back", icon=":material/draw:")
sleeves_page = st.Page("./pages/sleeves.py", title="Sleeves", icon=":material/edit:")
neck_page = st.Page("./pages/neck.py", title="Neck Design", icon=":material/edit:")
bottom_page = st.Page("./pages/bottom.py", title="Bottom Design",  icon=":material/draw:")
pdfview_page = st.Page("./pages/pdfGridViewer.py", title="Pdf Viewer", icon=":material/photo_prints:")

# Create the navigation menu
selected_page = st.navigation([home_page,measurement_page,qameez_page,sleeves_page, neck_page,bottom_page,pdfview_page])

# Run the selected page
selected_page.run()

