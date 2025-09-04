import matplotlib.pyplot as plt
from mpl_interactions import ioff, panhandler, zoom_factory
import streamlit as st
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages
from io import BytesIO
import io


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


# A4 size in inches (1 inch = 72 points)
A4_WIDTH_INCH = 8.27
A4_HEIGHT_INCH = 11.69

# DPI - controls resolution
DPI = 300

# A4 size in pixels
A4_WIDTH_PX = int(A4_WIDTH_INCH * DPI)
A4_HEIGHT_PX = int(A4_HEIGHT_INCH * DPI)

st.title("Print Large Plot as PDF in A4 Pages")
st.write("This app splits a large plot into multiple A4-sized pages and generates a paginated PDF.")

# Save to a BytesIO buffer
buf = BytesIO()
fig.savefig(buf, format="png", dpi=DPI)
buf.seek(0)
plt.close(fig)

# Load image with matplotlib
img = plt.imread(buf)

# Image dimensions
img_height, img_width, _ = img.shape

# Number of pages needed
cols = int(np.ceil(img_width / A4_WIDTH_PX))
rows = int(np.ceil(img_height / A4_HEIGHT_PX))

st.write(f"Image dimensions: {img_width} x {img_height} px")
st.write(f"Pages needed: {cols} columns × {rows} rows = {cols*rows} pages")

# Generate PDF
pdf_buffer = BytesIO()
with PdfPages(pdf_buffer) as pdf:
    page_num = 1
    for row in range(rows):
        for col in range(cols):
            # Calculate cropping box
            left = col * A4_WIDTH_PX
            right = min((col + 1) * A4_WIDTH_PX, img_width)
            top = row * A4_HEIGHT_PX
            bottom = min((row + 1) * A4_HEIGHT_PX, img_height)

            # Slice the image
            cropped = img[top:bottom, left:right, :]

            # Create a figure for this slice
            fig, ax = plt.subplots(figsize=(A4_WIDTH_INCH, A4_HEIGHT_INCH))
            ax.imshow(cropped)
            ax.axis("off")
            ax.set_title(f"Page {page_num} (Row {row+1}, Col {col+1})", fontsize=10)
            pdf.savefig(fig)
            plt.close(fig)
            page_num += 1

pdf_buffer.seek(0)

# Download button
st.download_button(
    label="📥 Download PDF",
    data=pdf_buffer,
    file_name="large_plot_A4_paginated.pdf",
    mime="application/pdf"
)

# Save plot to PDF (A4)
pdf_buffer1 = io.BytesIO()
with PdfPages(pdf_buffer1) as pdf:
    pdf.savefig(fig, bbox_inches='tight')  # Save entire figure
pdf_buffer.seek(0)

# Download button
st.download_button(
    label="📥 Download Full Plot as A4 PDF",
    data=pdf_buffer1,
    file_name="plot_a4.pdf",
    mime="application/pdf"
)


