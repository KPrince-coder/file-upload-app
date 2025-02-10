# File Upload App

Welcome to the **File Upload App**! This Streamlit-based app allows users to upload various types of files, including images, CSV datasets, and document files such as PDFs, DOCX, and TXT. It provides features to view and display file details and content, along with an option to toggle visibility of file details.

## Features

- **Image Upload**: Upload images (PNG, JPG, JPEG) and display them.
- **CSV Dataset Upload**: Upload CSV files and view the contents in a table format.
- **Document File Upload**: Upload PDF, DOCX, and TXT files, view their details, and extract the content.

### File Types Supported

- **Images**: PNG, JPG, JPEG
- **Dataset**: CSV
- **Documents**: PDF, DOCX, TXT

## How to Use

1. **Run the App**:
   To run the app, follow these steps:

   - Clone this repository to your local machine.
   - Install the necessary dependencies using **`uv`**:

     ```bash
     uv install
     ```

   - Run the app with the following command:

     ```bash
     uv run app.py
     ```

   - Open your browser and go to `http://localhost:8501` to view the app.

2. **Upload Files**:
   - **Images**: Select "Home" from the sidebar to upload one or more image files. The app will display the images with their file names.
   - **CSV Dataset**: Select "Dataset" from the sidebar to upload a CSV file. The data will be displayed as a table.
   - **Document Files**: Select "Document Files" from the sidebar to upload one or more PDF, DOCX, or TXT files. You can view the file details and extract the content. Supported formats include:
     - **PDF**: Text is extracted using `pdfplumber`.
     - **DOCX**: Text is extracted using `docx2txt`.
     - **TXT**: Plain text is extracted directly.

3. **View File Details**:
   - After uploading a document file, you can toggle the visibility of file details (e.g., file name, type, size).
   - You can also extract and view the content of the file with the click of a button.

4. **Error Handling**:
   - If an unsupported file type is uploaded or an error occurs while extracting file content, the app will display an error message.

## Requirements

- **Streamlit**: For the web interface.
- **Pandas**: For handling and displaying the CSV dataset.
- **pdfplumber**: For extracting text from PDF files.
- **docx2txt**: For extracting text from DOCX files.

To install the dependencies using **`uv`**, run:

```bash
uv install
