# Date: February 10, 2025
# Author: Prince Kyeremeh


import streamlit as st
import pandas as pd
import docx2txt
import pdfplumber

page_icon = "file_upload_icon.png"
st.set_page_config(page_title="File Upload", page_icon=page_icon, layout="centered")

st.title("File Upload App")


def upload_image():
    """
    Allows users to upload one or more image files. If a file is uploaded, it displays the
    file name and renders the image in a Streamlit image widget. Supported image formats
    are PNG, JPG, and JPEG.

    Parameters
    ----------

    None

    Returns
    -------

    None
    """
    image_file = st.file_uploader(
        "Upload Images", type=["png", "jpg", "jpeg"], accept_multiple_files=True
    )
    if image_file is not None:
        for image in image_file:
            st.image(
                image,
                caption=image.name.split(".")[0].capitalize(),
                use_container_width=True,
            )


def upload_dataset():
    """
    Allows users to upload a CSV dataset file. If a file is uploaded, it displays the file name
    and renders the data in a Streamlit dataframe. Only single file uploads are supported.
    """

    dataset_file = st.file_uploader(
        "Upload Dataset",
        type=["csv"],
        accept_multiple_files=False,
    )
    if dataset_file is not None:
        # st.write(type(dataset_file))
        # st.write(dataset_file)
        st.write("**File Name:** ", dataset_file.name)
        # for file in dataset_file:
        # st.write(dataset_file.name.split(".")[0])
        data = pd.read_csv(dataset_file)
        st.dataframe(data)


def upload_document_files():
    """
    Allows users to upload one or more document files (PDF, DOCX, TXT). If a file is uploaded, it
    displays the file name and provides buttons to toggle visibility of file details and view file content.
    File details include name, type, and size. File content is extracted using pdfplumber, docx2txt, or
    plain text read. If an error occurs while extracting file content, an error message is displayed.
    """

    # Initialize session state for tracking file details, visibility, and content
    if "file_details" not in st.session_state:
        st.session_state.file_details = {}
    if "show_details" not in st.session_state:
        st.session_state.show_details = {}
    if "file_content" not in st.session_state:
        st.session_state.file_content = {}

    # Allow multiple file uploads
    uploaded_files = st.file_uploader(
        "Upload Document Files",
        type=["pdf", "docx", "txt"],
        accept_multiple_files=True,
    )

    if uploaded_files:
        for uploaded_file in uploaded_files:
            file_name = uploaded_file.name

        # Extract file details and store them in  session state
        if file_name not in st.session_state.file_details:
            st.session_state.file_details[file_name] = {
                "FileName": file_name,
                "FileType": uploaded_file.type,
                "FileSize": f"{uploaded_file.size / 1024:.2f} KB",  # Format size in KB
            }

        # Initialize visibility state for this file if not already present
        if file_name not in st.session_state.show_details:
            st.session_state.show_details[file_name] = False

        # Button to toggle visibility of file details
        if st.button(f"Toggle Details: {file_name}", key=f"toggle_{file_name}"):
            st.session_state.show_details[
                file_name
            ] = not st.session_state.show_details[file_name]

        # Display file details if visible
        if st.session_state.show_details[file_name]:
            st.write(f"### File Details for {file_name}")
            for key, value in st.session_state.file_details[file_name].items():
                st.write(f"**{key}:** {value}")
        else:
            st.write(
                f"File details for {file_name} are hidden. Click the button to show them."
            )

        # Button to view file content
        if st.button(f"View Content for {file_name}", key=f"view_{file_name}"):
            # Extract and store file content in session state
            if file_name not in st.session_state.file_content:
                try:
                    if uploaded_file.type == "text/plain":
                        # For .txt files
                        st.session_state.file_content[file_name] = (
                            uploaded_file.read().decode("utf-8")
                        )
                    elif uploaded_file.type == "application/pdf":
                        # For .pdf files

                        with pdfplumber.open(uploaded_file) as pdf:
                            text = ""
                            for page in pdf.pages:
                                text += page.extract_text()

                            # Extract
                            st.session_state.file_content[file_name] = text
                    elif (
                        uploaded_file.type
                        == "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                    ):
                        # For .docx files
                        st.session_state.file_content[file_name] = docx2txt.process(
                            uploaded_file
                        )
                    else:
                        st.error(f"Unsupported file type: {file_name.type} ")
                        st.session_state.file_content[file_name] = None

                except Exception as e:
                    st.error(f"Error reading file {file_name}: {e}")
                    st.session_state.file_content[file_name] = None

            # Display file content if available
            if st.session_state.file_content[file_name]:
                st.write(f"### Content of {file_name}")
                st.text_area(
                    f"Content of {file_name}",
                    value=st.session_state.file_content[file_name],
                    height=400,
                )


def main():
    """
    Main entry point for the Streamlit app. Shows a sidebar with options to upload either
    an image, a dataset, or document files. Depending on the selection, it calls the
    corresponding function to handle the upload.

    :return: None
    """
    menu = ["Home", "Dataset", "Document Files"]
    st.sidebar.markdown("## File Upload Options")
    choice = st.sidebar.selectbox("**Menu**", menu)

    match choice:
        case "Home":
            st.subheader("Home")
            upload_image()

        case "Dataset":
            st.subheader("Dataset")
            upload_dataset()

        case "Document Files":
            st.subheader("Document Files")
            upload_document_files()


if __name__ == "__main__":
    main()
