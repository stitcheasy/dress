import streamlit as st
import fitz  # PyMuPDF
import tempfile
from PIL import Image

# Set Streamlit page config
st.set_page_config(page_title="PDF Grid Viewer", layout="wide")

#st.title(" PDF Page Grid Viewer 📄")
st.markdown("### :rainbow[ PDF Pages 📄 Grid Viewer ]")

uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

# Select number of columns for the grid
#columns_per_row = st.slider("Number of columns in grid", min_value=1, max_value=7, value=7)
columns_per_row = 7

if uploaded_file:
    # Save the uploaded file to a temp file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.read())
        pdf_path = tmp_file.name

    # Load PDF using PyMuPDF
    doc = fitz.open(pdf_path)
    total_pages = len(doc)
    if total_pages == 1:
        columns_per_row = 1
        st.success(f"Loaded PDF with {total_pages} page")
    else:
        st.success(f"Loaded PDF with {total_pages} pages")

    # Convert pages to images
    images = []
    for page_num in range(total_pages):
        page = doc.load_page(page_num)
        pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))  # Scale factor 2 for better resolution
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        images.append(img)

    # Display images in grid
    rows = (len(images) + columns_per_row - 1) // columns_per_row
    for row in range(rows):
        cols = st.columns(columns_per_row)
        for col_index in range(columns_per_row):
            img_index = row * columns_per_row + col_index
            if img_index < len(images):
                with cols[col_index]:
                    st.image(images[img_index], caption=f"Page {img_index + 1}", use_container_width=True)
