#declarations
import matplotlib.pyplot as plt
from mpl_interactions import ioff, panhandler, zoom_factory
import streamlit as st

from thegridM import drawgridM
from readMeasurement import getmeasurement
from drawline import line
from drawcurve import curve
from savemultipagePdf import multipagePdf
from savesinglepagePdf import singlepageA4

def pant():
    smallshift=0.5
    linewid=0.8
    sizeoffont=15
    len=50
    wid=18

    #plt.rcParams.update({'font.size': 35})

    data=getmeasurement()

    with plt.ioff():
        fig,ax=drawgridM(len, wid, 150, smallshift,linewid, sizeoffont)

    waist=data[1][2]
    hip=data[1][3]
    BottomL=data[1][9]
    #print("hip" + hip)
    

    st.markdown("##### :rainbow[Indian Style Simple Kurti Set - Bottom Draft]")
   
    measurementStr= 'Body Measurements : ' + ' Bottom Length ' + str(BottomL) + ' , Waist ' + str(waist) + ' , Hip ' + str(hip)
    st.markdown("###### :blue[{}]".format(measurementStr))       

    pantclothwid=(float(hip) / 4) + 5
    
    mark1=1.5
    mark2=2
    mark3=float(BottomL)-1 + 0.5
    crotchLen=((float(hip) + 3) / 4 ) + 2.5
    print("crothlen"+ str(crotchLen))
    #crotchwid=2.5
    quarterbottomwidth=((float(hip) + 3) / 4 ) + 4

    ax.text(21.5, 0.5, '...........cloth fold line..........',color='brown', fontsize=28)
    ax.text(0, 15, 'back part----.',color='blue', fontsize=38)
    
    line(0,0,float(BottomL) + 7, 0, '--', 'brown')
    line(0,0, 0,float(pantclothwid) ,'--', 'cyan')
    line(mark1,0, mark1,float(pantclothwid) ,'--', 'pink')
    line(mark1+mark2,0, mark1+mark2,float(pantclothwid) ,'--', 'pink')
    line(0,quarterbottomwidth,mark1+mark2+crotchLen - 0.5,quarterbottomwidth,'--', 'pink')
    line(0,quarterbottomwidth - 2.5,mark1+mark2+crotchLen - 0.5,quarterbottomwidth - 2.5,'--', 'cyan')
    line(mark1+mark2+crotchLen - 0.5,quarterbottomwidth - 2.5,mark1+mark2+crotchLen - 0.5,quarterbottomwidth + 0.5,'--', 'cyan')

    curve(mark1+mark2+crotchLen - 0.5,quarterbottomwidth + 0.5,mark1+mark2+crotchLen - 0.5 - 4,quarterbottomwidth - 2.5,mark1+mark2+crotchLen - 0.5,quarterbottomwidth - 2.5,'-', 'blue',  "front part")

    mohri=10.0 + 0.5
    fold=4
    line(mark1+mark2+mark3,0, mark1+mark2+mark3,mohri ,'--', 'pink')
    line(mark1+mark2+mark3+fold,0, mark1+mark2+mark3+fold,mohri ,'-', 'blue')
    line(mark1+mark2+mark3-fold,mohri, mark1+mark2+mark3+fold,mohri ,'-', 'blue')

    curve(mark1+mark2+mark3-fold,mohri,mark1+mark2+crotchLen - 0.5,quarterbottomwidth + 0.5,mark1+mark2+mark3-(fold*4),mohri+2.5,'-', 'pink',  "cut choice")
    line(mark1+mark2+mark3-fold,mohri,mark1+mark2+crotchLen - 0.5,quarterbottomwidth + 0.5 ,'-', 'blue')
    line(0,quarterbottomwidth - 2.5, mark1,0 ,'--', 'blue')
    line(mark1,0, mark1+1,quarterbottomwidth - 2.5,'-', 'blue')
    line(mark1+mark2+crotchLen - 0.5 - 4,quarterbottomwidth - 2.5,mark1+1,quarterbottomwidth - 2.5)
    line(0, quarterbottomwidth -2.5,mark1+1,quarterbottomwidth - 2.5, '--', 'blue')

        
    st.set_page_config(layout="wide")

    st.pyplot(fig)
    return fig

fig5=pant()
 
col1, col2 = st.columns(2)

with col1:
        multipagePdf(fig5)
with col2:
    singlepageA4(fig5)
