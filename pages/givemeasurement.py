# home.py
import csv
import streamlit as st

#st.title("The Tailor Master")
#st.write("This is the main content of your home page.")

kurta_measure = st.container()
bottom_measure= st.container()
with kurta_measure:
   

# https://www.ethnicrajasthan.com/pages/kurti-size-chart

    st.subheader("Specify Measurement in inches")
    shoulder = st.slider('Shoulder',14.0,18.0, 16.0,step=0.5)
    chest = st.slider('Chest',37.0,52.0,(37+52)/2, step=0.5)
    waist = st.slider('Waist',33.0,48.0,(33+48)/2, step=0.5)
    hip = st.slider('Hip',40.0,54.0,(40+54)/2, step=0.5)
    length = st.slider('Length',23.0,49.0,(23+49)/2, step=0.5)
    sleeve = st.slider('Sleeve length',6.0,19.0,(6+19)/2, step=0.5)


measurements_in_inches = [shoulder,chest,waist,hip,length,sleeve ]


def my_function():
    st.write("Check 'Indian Style Qameez' for the pattern draft with these measurements ")
    with open('measurement.csv','w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["shoulder","chest","waist","hip","length","sleeve" ])
                writer.writerow(measurements_in_inches)

if st.button("Done"):
    my_function()

            

