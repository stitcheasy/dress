import matplotlib.pyplot as plt
import streamlit as st
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages
from io import BytesIO


def singlepageA4(fig):
    # Save to a BytesIO buffer
    
    pdf_buffer = BytesIO()
    with PdfPages(pdf_buffer) as pdf:
        pdf.savefig(fig, bbox_inches='tight')  # Save entire figure

    pdf_buffer.seek(0)
    st.subheader("Download")
    # Download button
    st.download_button(
    label="📥 A4 size single page PDF",
    data=pdf_buffer,
    file_name="plot_a4.pdf",
    mime="application/pdf"
)
    
