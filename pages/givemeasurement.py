# home.py
import csv
import streamlit as st

#st.title("The Tailor Master")
#st.write("This is the main content of your home page.")
st.markdown("### :rainbow[Indian Style Simple Kurti Set - Bottom Draft]")
st.markdown("##### :grey[Specify Measurements in inches]")
col1, col2 = st.columns([1,1] , border=True)

with col1:

    # https://www.ethnicrajasthan.com/pages/kurti-size-chart

        
    shoulder = st.slider('Shoulder',12.0,18.0, (12+18)/2,step=0.5)
    chest = st.slider('Chest',37.0,52.0,(37+52)/2, step=0.5)
    waist = st.slider('Waist',33.0,48.0,(33+48)/2, step=0.5)
    hip = st.slider('Hip',40.0,54.0,(40+54)/2, step=0.5)
    length = st.slider('Length',23.0,49.0,(23+49)/2, step=0.5)
    


with col2:
        sleeve = st.slider('Sleeve length',6.0,19.0,(6+19)/2, step=0.5)
        sleeveround = st.slider('Sleeve Round',6.0,19.0,(6+19)/2, step=0.5)
        frontneck = st.slider('Front Neck Size',4.0,10.0,(0+10)/2, step=0.5)
        backneck = st.slider('Back Neck Size',3.0,10.0,(0+10)/2, step=0.5)
        bottomlen = st.slider('Bottom length',20.0,44.0,(20+44)/2, step=0.5)



measurements_in_inches = [shoulder,chest,waist,hip,length,sleeve, sleeveround,frontneck, backneck, bottomlen]


def my_function():
    st.write("Values saved in measurement.csv ")
    with open('measurement.csv','w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["shoulder","chest","waist","hip","length","sleeve", "sleeveround","frontneck", "backneck", "bottomlength" ])
                writer.writerow(measurements_in_inches)

if st.button("Done"):
    my_function()

            

