import matplotlib.pyplot as plt
import streamlit as st

from thegridM import drawgridM
from readMeasurement import getmeasurement
from drawline import line
from drawcurve import curve

from savemultipagePdf import multipagePdf
from savesinglepagePdf import singlepageA4

from altitude import calculate_altitude

def frontneck():
    smallshift=0.3
    linewid=0.8
    sizeoffont=10
    len=12
    wid=10
    
    data=getmeasurement()
    fnecksize=data[1][7]
    bnecksize=data[1][8]
    

    with plt.ioff():
        fig,ax=drawgridM(len, wid, 150, smallshift,linewid, sizeoffont)
    
    shoulder=data[1][0]
      
    st.markdown("##### :blue[Shoulder {}]".format(shoulder))
    measurementStr= 'Front Neck Size ' + str(fnecksize)
    st.markdown("##### :blue[{}]".format(measurementStr))

    ax.text(5.5, 0.5, '...........cloth fold line..........',color='brown', fontsize=25)

    return fig

def backneck():
    smallshift=0.3
    linewid=0.8
    sizeoffont=10
    len=12
    wid=10
    
    data=getmeasurement()
    fnecksize=data[1][7]
    bnecksize=data[1][8]

    with plt.ioff():
        fig,ax=drawgridM(len, wid, 150, smallshift,linewid, sizeoffont)
    
    shoulder=data[1][0]
      
        
    measurementStr= 'Back Neck Size ' + str(bnecksize)
    st.markdown("##### :blue[{}]".format(measurementStr))

    ax.text(5.5, 0.5, '...........cloth fold line..........',color='brown', fontsize=25)

    return fig



st.markdown("### :rainbow[Indian Style Simple  Kurti - Front and Back Neck Draft]")

fig3=frontneck()
fig4=backneck()

col1, col2, col3= st.columns([2,2, 1])

with col1:
        st.set_page_config(layout="wide")
        st.pyplot(fig3)
with col2:
        st.set_page_config(layout="wide")
        st.pyplot(fig4)
with col3:
        st.subheader("Download")
        multipagePdf(fig3)
        singlepageA4(fig3)