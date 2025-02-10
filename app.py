import streamlit as st

page_icon = "file_upload_icon.png"
st.set_page_config(page_title="File Upload", page_icon=page_icon, layout="centered")

st.title("File Upload App")


def main():
    menu = ["Home", "Dataset", "Document Files", "Images", "Others"]
    st.sidebar.markdown("## File Upload")
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home")
        image_file = st.file_uploader(
            "Upload Images", type=["png", "jpg", "jpeg"], accept_multiple_files=True
        )
        if image_file is not None:
            for image in image_file:
                st.image(image)

    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        st.write(uploaded_file)


if __name__ == "__main__":
    main()
