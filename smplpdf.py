from fpdf import FPDF

# Create instance of FPDF class
pdf = FPDF()

# Add a page
pdf.add_page()

# Set font
pdf.set_font("Arial", size=12)

# Add a title
pdf.cell(200, 10, text="Sample PDF Document", ln=True, align="C")

# Add some content
pdf.ln(10)  # line break
pdf.cell(200, 10, text="This is a sample/dummy PDF file created using Python.", ln=True)
pdf.cell(200, 10, text="You can use this as a template for creating PDF documents.", ln=True)

# Add some more content
pdf.ln(10)  # line break
pdf.cell(200, 10, text="This is just a basic example. You can add images, tables, and more.", ln=True)

# Save the PDF to a file
file_path = "sample_dummy_pdf.pdf"
pdf.output(file_path)

print(f"PDF file saved as {file_path}")