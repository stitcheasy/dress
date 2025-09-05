import matplotlib.pyplot as plt
import streamlit as st

from thegridM import drawgridM
from readMeasurement import getmeasurement
from drawline import line
from drawcurve import curve

from savemultipagePdf1 import multipagePdf1
# from savesinglepagePdf import singlepageA4

from altitude import calculate_altitude



smallshift=0.3
linewid=0.8
sizeoffont=10
len=12
wid=10

data=getmeasurement()
chest=data[1][1]
fnecksize=data[1][7]
bnecksize=data[1][8]
shoulder=data[1][0]
neckwid=float(chest) / 12


def frontneck():
    
    with plt.ioff():
        fig,ax=drawgridM(len, wid, 150, smallshift,linewid, sizeoffont)
        
    
    

    ax.text(0.5, 0.2, '.....cloth fold line..........',color='brown', fontsize=25)
    line(0,0,0, float(shoulder) / 2, '--', 'pink')
    line(0,0,float(fnecksize) + 2, 0, '--', 'brown')

    #Box
    line(0.5,0,0.5, neckwid, '--', 'cyan')
    line(float(fnecksize) + 0.5, 0, float(fnecksize) + 0.5, neckwid,'--', 'cyan')
    line(0.5,neckwid, float(fnecksize) + 0.5, neckwid,'--', 'cyan')

    #inner mark
    curve(float(fnecksize)  + 0.5 , 0, 2, neckwid, float(fnecksize) +0.5,neckwid,'--', 'black', "neck inner cut")
    line(2, neckwid, 0, neckwid,'--', 'black')

    #outer mark
    NstripWidth=1
    curve(float(fnecksize)  + 0.5 + NstripWidth , 0, 2 , neckwid + NstripWidth, float(fnecksize) +0.5+ NstripWidth,neckwid+ NstripWidth,'--', 'blue', "neck outer cut")
    line(2, neckwid+ NstripWidth, 0, neckwid+ NstripWidth,'--', 'blue')

    return fig

def backneck():
        
    with plt.ioff():
        fig,ax=drawgridM(len, wid, 150, smallshift,linewid, sizeoffont)

    ax.text(0.5, 0.2, '..cloth fold line..........',color='brown', fontsize=25)
    line(0,0,0, float(shoulder) / 2, '--', 'pink')
    line(0,0,float(fnecksize) + 2, 0, '--', 'brown')

    #Box
    line(0.5,0,0.5, neckwid, '--', 'cyan')
    line(float(bnecksize) + 0.5, 0, float(bnecksize) + 0.5, neckwid,'--', 'cyan')
    line(0.5,neckwid, float(bnecksize) + 0.5, neckwid,'--', 'cyan')

    #inner mark
    curve(float(bnecksize)  + 0.5 , 0, 2, neckwid, float(bnecksize) +0.5,neckwid,'--', 'black', "neck inner cut")
    line(2, neckwid, 0, neckwid,'--', 'black')

    #outer mark
    NstripWidth=1
    curve(float(bnecksize)  + 0.5 + NstripWidth , 0, 2 , neckwid + NstripWidth, float(bnecksize) +0.5+ NstripWidth,neckwid+ NstripWidth,'--', 'blue', "neck outer cut")
    line(2, neckwid+ NstripWidth, 0, neckwid+ NstripWidth,'--', 'blue')

    return fig



st.markdown("### :rainbow[Indian Style Simple  Kurti - Front and Back Neck Draft]")
st.markdown("##### :blue[Shoulder {}]".format(shoulder))
measurementStr= 'Front Neck Size ' + str(fnecksize)
st.markdown("##### :blue[{}]".format(measurementStr))
measurementStr2= 'Back Neck Size ' + str(bnecksize)
st.markdown("##### :blue[{}]".format(measurementStr2))

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
        st.subheader("Download Pdfs")
        multipagePdf1(fig3, fname="FrontN.pdf", L="DownloadFrontN", K="FNeck")
        # singlepageA4(fig3)
        # st.subheader("Download Back")
        multipagePdf1(fig4, fname="BackN.pdf", L="DownloadBackN", K="BNeck")
