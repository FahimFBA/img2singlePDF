import os
import img2pdf

# Replace the directory path with the folder containing JPEG images to be converted
directory_path = "C:\\Users\\fahim\\Desktop\\img2singlePDF"

# List all files in the directory and filter only JPEG images (ending with ".jpg")
image_files = [i for i in os.listdir(directory_path) if i.endswith(".jpg")]

# Convert the list of JPEG images to a single PDF file
pdf_data = img2pdf.convert(image_files)

# Write the PDF content to a file (make sure you have write permissions for the specified file)
with open("output.pdf", "wb") as file:
    file.write(pdf_data)
