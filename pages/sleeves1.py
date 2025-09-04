import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import io

# Streamlit setup
st.set_page_config(page_title="Plot to A4 PDF", layout="centered")
st.title("📊 Export Plot to A4 PDF")

# Sample plot function (replace with your own if needed)
#declarations
import matplotlib.pyplot as plt

from thegridM import drawgrid
from readMeasurement import getmeasurement
from drawlineM import line
from drawcurveM import curve
from savemultipagePdf import multipagePdf
from savesinglepagePdf import singlepageA4
from altitude import calculate_altitude

def sleeve():
    plt.rcParams.update({'font.size': 20})

    data=getmeasurement()
    half_sleeveround=11/2
    with plt.ioff():
        fig,ax=drawgrid(25, 12, 150)

    shoulder=data[1][0]
    chest=data[1][1]
    waist=data[1][2]
    hip=data[1][3]
    length=data[1][4]
    sleeve=data[1][5]

    armwidth=float(chest)/6  + 1
    print(armwidth)

    lengthmark=float(length) + 2
    halfshoulder=float(shoulder) / 2
    quarterchest=float(chest) / 4
    quarterwaist=float(waist) / 4
    quarterhip=float(hip) / 4
    chestmark=halfshoulder-0.5
    waistmark=14
    hipmark=21


    ax.text(5, 18, 'Indian Style Simple  Kurti - Sleeve', color='Red', fontsize=7)
    ax.text(5.5, 0.5, '...........cloth fold line..........',color='brown', fontsize=7)
    ax.text(1, 17, r'Body Measurements : ' + ' Length ' + str(length) + ' ,Shoulder ' + str(shoulder) + ' ,Chest ' + str(chest) + ' ,Waist ' + str(waist) + ' ,Sleeve ' + str(sleeve), size=8)

    alt=calculate_altitude(3,(float(chest)/4)-1)
    print(alt)

    line(0,0,float(sleeve) + 2, 0 , 'dotted', 'red')
    line(0,0,0,float(chest)/4, '-', 'red')
    line(0,0,0,float(chest)/4, '-', 'red')
    line(float(sleeve) + 0.5 ,0,float(sleeve) + 0.5,half_sleeveround, '-',"magenta")
    line(float(sleeve) + 2,0,float(sleeve) + 2,half_sleeveround + 1.5)
    line(3.5,0,3.5,alt,"-" ,"pink" )
    line(3,float(chest)/4,float(sleeve) + 2,half_sleeveround + 1.5)


   
    line(0.5,0,3.5,alt,"-","pink" )
    line(3.5, alt,3.5,quarterchest,"-","magenta" )
    line(3,9,3,10.5,"-","blue" )
    line(float(sleeve) + 0.5,half_sleeveround,3.5,alt,"-","magenta" )

    curve(2,4.5,3.5,alt,3,6, '-', 'magenta', "stitch ready")
    curve(0.5,0,2,4.5,0.5,2, '-', 'magenta', "stitch ready back side")
    curve(1,2.5,3.5,alt,4,5, '--', 'magenta', "stitch ready front")

    shift=0.5

    curve(2-shift,4.5,3.5-shift,alt,3-shift,6, '-', 'blue', "cut at blue lines")
    curve(0.5-shift,0,2-shift,4.5,0.5-shift,2, '-', 'blue', "sleeve back side")
    curve(1-shift,2.5,3.5-shift,alt,4-shift,5, '--', 'blue', "sleeve front side")

    #plt.show()
    return fig
fig2=sleeve()


col1, col2 = st.columns([3, 1])



with col1:
        st.set_page_config(layout="wide")
        st.pyplot(fig2)
with col2:
        st.subheader("Download")
        multipagePdf(fig2)
        singlepageA4(fig2)