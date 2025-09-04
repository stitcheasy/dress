import matplotlib.pyplot as plt
# Importing required library
from mpl_interactions import ioff, panhandler, zoom_factory
import streamlit as st
import numpy as np

from thegridM import drawgrid
from readMeasurement import getmeasurement
from drawline import line
from drawcurve import curve

plt.rcParams.update({'font.size': 35})

data=getmeasurement()

with plt.ioff():
    fig,ax=drawgrid(50, 18, 150)

shoulder=data[1][0]
chest=data[1][1]
waist=data[1][2]
hip=data[1][3]
length=data[1][4]
sleeve=data[1][5]
#print(length)

lengthmark=float(length) + 2
halfshoulder=float(shoulder) / 2
quarterchest=float(chest) / 4
quarterwaist=float(waist) / 4
quarterhip=float(hip) / 4

print(quarterhip)

chestmark=halfshoulder-0.5
waistmark=14
hipmark=21

line(0,0,0,halfshoulder )
line(chestmark,0,chestmark, quarterchest+0.5, '--', 'magenta')
ax.text(chestmark+0.3, 5, 'chest line',rotation=90,color='brown', fontsize=25)
line(waistmark,0,waistmark, quarterwaist+0.5, '--', 'magenta')
ax.text(waistmark+0.3, 5, 'waist line',rotation=90,color='brown', fontsize=25)
line(hipmark,0,hipmark, quarterhip, '--', 'magenta')
ax.text(hipmark+0.3, 5, 'hip line',rotation=90,color='brown', fontsize=25)
line(float(length),0,float(length),quarterhip, '--', 'magenta')

line(4,halfshoulder,chestmark, halfshoulder, '--', 'magenta')

line(lengthmark,0,lengthmark,quarterhip+1.5, '-', 'blue')
ax.text(lengthmark-2+0.3, 5, 'required length line',rotation=90,color='brown', fontsize=25)
line(waistmark,quarterwaist+0.5,hipmark,quarterhip, '--', 'magenta')
line(waistmark,quarterwaist+0.5+1.5,hipmark,quarterhip+1.5, '-', 'blue')
line(hipmark,quarterhip,lengthmark,quarterhip, '--', 'magenta')

line(hipmark,quarterhip+1.5,lengthmark,quarterhip+1.5, '-', 'blue')
curve(chestmark,quarterchest+0.5,waistmark,quarterwaist+0.5, chestmark+3,quarterchest+0.5,'--', 'purple', "fit curve")
curve(chestmark,quarterchest+0.5+1.5,waistmark,quarterwaist+0.5+1.5, chestmark+3,quarterchest+0.5+1.5,'--','blue' ,"curve to cut")

curve(4,halfshoulder,chestmark,quarterchest+0.5, chestmark,halfshoulder,'--', 'black', "armhole back side")

line(0,halfshoulder,4,halfshoulder-0.3, '-', 'green')
curve(4,halfshoulder-0.3,chestmark,quarterchest+0.5, chestmark+.7,halfshoulder-1,'--', 'green',  "armhole front side")

line(0,halfshoulder,4,halfshoulder, '-', 'blue')
line(chestmark,quarterchest+0.5,chestmark,quarterchest+0.5+1.5, '-', 'blue')

line(0,0,float(length) + 2, 0 , 'dotted', 'red')

ax.text(21, 18, 'Indian Style Simple  Kurti', color='Red', fontsize=35)
ax.text(21.5, 0.5, '...........cloth fold line..........',color='brown', fontsize=28)
ax.text(21.5, quarterhip + 1.5 +0.5, '...........cut here..........',color='blue', fontsize=28)
ax.text(15, 17, r'Body Measurements : ' + ' Length ' + str(length) + ' ,Shoulder ' + str(shoulder) + ' ,Chest ' + str(chest) + ' ,Waist ' + str(waist) + ' ,Hip ' + str(hip), size=28)


#curve()

#plt.show()
st.set_page_config(layout="wide")
#st.write(fig)

disconnect_zoom = zoom_factory(ax)
# Enable scrolling and panning with the help of MPL
# Interactions library function like panhandler.
pan_handler = panhandler(fig)

st.pyplot(fig)
