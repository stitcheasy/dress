#declarations
import matplotlib.pyplot as plt
import streamlit as st

from thegrid import drawgrid
from readMeasurement import getmeasurement
from drawline import line
from drawcurve import curve
from savemultipagePdf import multipagePdf
from savesinglepagePdf import singlepageA4

def sleeve():
    plt.rcParams.update({'font.size': 40})

    data=getmeasurement()

    with plt.ioff():
        fig,ax=drawgrid(25, 12, 150)

    shoulder=data[1][0]
    chest=data[1][1]
    waist=data[1][2]
    hip=data[1][3]
    length=data[1][4]
    sleeve=data[1][5]
   

    lengthmark=float(length) + 2
    halfshoulder=float(shoulder) / 2
    quarterchest=float(chest) / 4
    quarterwaist=float(waist) / 4
    quarterhip=float(hip) / 4
    chestmark=halfshoulder-0.5
    waistmark=14
    hipmark=21


    ax.text(5, 18, 'Indian Style Simple  Kurti - Sleeve', color='Red', fontsize=35)
    ax.text(5.5, 0.5, '...........cloth fold line..........',color='brown', fontsize=28)
    ax.text(1, 17, r'Body Measurements : ' + ' Length ' + str(length) + ' ,Shoulder ' + str(shoulder) + ' ,Chest ' + str(chest) + ' ,Waist ' + str(waist) + ' ,Sleeve ' + str(sleeve), size=28)


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