import matplotlib.pyplot as plt
import streamlit as st

from thegridM import drawgridM
from readMeasurement import getmeasurement
from drawline import line
from drawcurve import curve

from savemultipagePdf import multipagePdf
from savesinglepagePdf import singlepageA4

from altitude import calculate_altitude

def sleeve():
    smallshift=0.5
    linewid=0.8
    sizeoffont=20
    len=25
    wid=15
    #plt.rcParams.update({'legend.labelspacing':0.25, 'font.size':20})

    data=getmeasurement()
    sleeveround=data[1][6]
    half_sleeveround=float(sleeveround) /2

    with plt.ioff():
        fig,ax=drawgridM(len, wid, 150, smallshift,linewid, sizeoffont)
        


    shoulder=data[1][0]
    chest=data[1][1]
    sleeve=data[1][5]

    innermark=float(chest) / 12 
    #print(innermark+innermark)

    halfshoulder=float(shoulder) / 2
    quarterchest=float(chest) / 4
      
    
    innermark=float(chest) / 12
    #print("innermark " + str(innermark))

    sleevewidth= (float(chest) / 6) + 1.5 + 1.5 
    #print("sleeve width " + str(sleevewidth))

    st.markdown("### :rainbow[Indian Style Simple  Kurti - Sleeve Draft]")
        
    measurementStr= 'Body Measurements : Shoulder ' + str(shoulder) + ' ,Chest ' + str(chest) +  ' ,Sleeve ' + str(sleeve)
    st.markdown("##### :blue[{}]".format(measurementStr))

    ax.text(5.5, 0.5, '...........cloth fold line..........',color='brown', fontsize=25)

    alt=calculate_altitude(3,quarterchest-1)
    print("alt " +str(alt))

    line(0,0,float(sleeve) + 2, 0 , 'dotted', 'red')
    line(0,0,0,sleevewidth, '-', 'pink')

    line(innermark,0,innermark,alt,"-" ,"pink" )
    line(0,0,innermark,alt,"-","pink" )
    
    line(float(sleeve) + 2 , 0, float(sleeve) + 2, half_sleeveround + 1.5)
    line(float(sleeve) + 0.5 , 0, float(sleeve) + 0.5, half_sleeveround, "--","magenta")
    line(innermark , alt , float(sleeve) + 0.5, half_sleeveround, "--","magenta")

    line(innermark,sleevewidth+0.5,float(sleeve) + 2,half_sleeveround + 1.5)

    curve(innermark/3, sleevewidth /3,innermark, sleevewidth+0.5, innermark+0.5, 6, '-', 'green', "frontpart")
    curve(innermark/3, sleevewidth /3,innermark, sleevewidth+0.5, innermark-0.5, 6, '-', 'blue', "backpart")
    curve(innermark/3, sleevewidth /3,0,0, 0, 2, '-', 'blue', "cut at blue lines")
  
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