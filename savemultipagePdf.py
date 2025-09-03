import matplotlib.pyplot as plt
#from mpl_interactions import ioff, panhandler, zoom_factory
import streamlit as st
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages
from io import BytesIO


def multipagePdf(fig):
    # A4 size in inches (1 inch = 72 points)
    A4_WIDTH_INCH = 8.27
    A4_HEIGHT_INCH = 11.69

    # DPI - controls resolution
    DPI = 300

    # A4 size in pixels
    A4_WIDTH_PX = int(A4_WIDTH_INCH * DPI)
    A4_HEIGHT_PX = int(A4_HEIGHT_INCH * DPI)

    
    
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
        label="📥 A4 size Multipage Pdf",
        data=pdf_buffer,
        file_name="large_plot_A4_paginated.pdf",
        mime="application/pdf"
    )

#multipagePdf() 