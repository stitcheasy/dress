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

    shoulder=data[1][0]
    chest=data[1][1]
    waist=data[1][2]
    hip=data[1][3]
    length=data[1][4]
    sleeve=data[1][5]
    BottomL=data[1][9]
    print("hip" + hip)

    lengthmark=float(length) + 2
    halfshoulder=float(shoulder) / 2
    quarterchest=float(chest) / 4
    quarterwaist=float(waist) / 4
    quarterhip=float(hip) / 4
    chestmark=halfshoulder-0.5
    waistmark=14
    hipmark=21

    st.markdown("##### :rainbow[Indian Style Simple Kurti Set - Bottom Draft]")
   
    measurementStr= 'Body Measurements : ' + ' Length ' + str(length) + ' ,Shoulder ' + str(shoulder) + ' ,Chest ' + str(chest) + ' ,Waist ' + str(waist) + ' ,Hip ' + str(hip)
    st.markdown("###### :blue[{}]".format(measurementStr))       

    # line(0,0,0,halfshoulder )
    # line(chestmark,0,chestmark, quarterchest+0.5, '--', 'magenta')
    # ax.text(chestmark+0.3, 5, 'chest line',rotation=90,color='brown', fontsize=25)
    # line(waistmark,0,waistmark, quarterwaist+0.5, '--', 'magenta')
    # ax.text(waistmark+0.3, 5, 'waist line',rotation=90,color='brown', fontsize=25)
    # line(hipmark,0,hipmark, quarterhip, '--', 'magenta')
    # ax.text(hipmark+0.3, 5, 'hip line',rotation=90,color='brown', fontsize=25)
    # line(float(length),0,float(length),quarterhip, '--', 'magenta')

    # line(4,halfshoulder,chestmark, halfshoulder, '--', 'magenta')

    # line(lengthmark,0,lengthmark,quarterhip+1.5, '-', 'blue')
    # ax.text(lengthmark-2+0.3, 5, 'required length line',rotation=90,color='brown', fontsize=25)
    # line(waistmark,quarterwaist+0.5,hipmark,quarterhip, '--', 'magenta')
    # line(waistmark,quarterwaist+0.5+1.5,hipmark,quarterhip+1.5, '-', 'blue')
    # line(hipmark,quarterhip,lengthmark,quarterhip, '--', 'magenta')

    # line(hipmark,quarterhip+1.5,lengthmark,quarterhip+1.5, '-', 'blue')
    # curve(chestmark,quarterchest+0.5,waistmark,quarterwaist+0.5, chestmark+3,quarterchest+0.5,'--', 'purple', "fit curve")
    # curve(chestmark,quarterchest+0.5+1.5,waistmark,quarterwaist+0.5+1.5, chestmark+3,quarterchest+0.5+1.5,'--','blue' ,"curve to cut")

    # curve(4,halfshoulder,chestmark,quarterchest+0.5, chestmark,halfshoulder,'--', 'black', "armhole back side")

    # line(0,halfshoulder,4,halfshoulder-0.3, '-', 'green')
    # curve(4,halfshoulder-0.3,chestmark,quarterchest+0.5, chestmark+.7,halfshoulder-1,'--', 'green',  "armhole front side")

    # line(0,halfshoulder,4,halfshoulder, '-', 'blue')
    # line(chestmark,quarterchest+0.5,chestmark,quarterchest+0.5+1.5, '-', 'blue')
    pantclothwid=(float(hip) / 4) + 5
    #line(0,0,float(length) + 2, 0 , 'dotted', 'red')
    mark1=1.5
    mark2=2
    mark3=float(BottomL)-1 + 0.5
    crotchLen=((float(hip) + 3) / 4 ) + 2.5
    print("crothlen"+ str(crotchLen))
    crotchwid=2.5
    quarterbottomwidth=((float(hip) + 3) / 4 ) + 4

    ax.text(21.5, 0.5, '...........cloth fold line..........',color='brown', fontsize=28)
    ax.text(0, 15, 'back part----.',color='blue', fontsize=38)
    # ax.text(21.5, quarterhip + 1.5 +0.5, '...........cut here..........',color='blue', fontsize=28)
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

    curve(mark1+mark2+mark3-fold,mohri,mark1+mark2+crotchLen - 0.5,quarterbottomwidth + 0.5,mark1+mark2+mark3-(fold*3),mohri+0.5,'-', 'blue',  "cut at blue line")

    line(0,quarterbottomwidth - 2.5, mark1,0 ,'--', 'blue')
    line(mark1,0, mark1+1,quarterbottomwidth - 2.5,'-', 'blue')
    line(mark1+mark2+crotchLen - 0.5 - 4,quarterbottomwidth - 2.5,mark1+1,quarterbottomwidth - 2.5)
    line(0, quarterbottomwidth -2.5,mark1+1,quarterbottomwidth - 2.5, '--', 'blue')

    #line(mark1+mark2+mark3,0, mark1+mark2+mark3,float(pantclothwid) ,'--', 'magenta')

    
    st.set_page_config(layout="wide")

    st.pyplot(fig)
    return fig

fig5=pant()
 
col1, col2 = st.columns(2)

with col1:
        multipagePdf(fig5)
with col2:
    singlepageA4(fig5)
