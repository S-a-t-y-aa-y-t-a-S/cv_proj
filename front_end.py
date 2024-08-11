import streamlit as st
from PIL import Image
import time

# Function to navigate to the detect page
def go_to_detect():
    st.session_state.page = "detect"

# Function to navigate to the upload page
def go_to_upload():
    st.session_state.page = "upload"

# Initialize session state if not already done
if "page" not in st.session_state:
    st.session_state.page = "upload"

if "uploaded_file" not in st.session_state:
    st.session_state.uploaded_file = None

# Check the current page
if st.session_state.page == "upload":
    # Create a container for the navbar
    with st.container():
        # Define the layout: 4 columns where the first takes more space for the heading
        col1, col2 = st.columns([4, 1])

        with col1:
            # Center the heading vertically
            st.markdown("<h1 style='color: white; margin: 0;'>Image Upload and Display</h1>", unsafe_allow_html=True)

        with col2:
            # Button for detecting damage
            if st.button("Detect Damage"):
                if st.session_state.uploaded_file is not None:
                    go_to_detect()
                else:
                    # Create a placeholder for the warning message
                    warning_placeholder = st.empty()
                    warning_placeholder.write("Please upload an image file first!!")
                    time.sleep(3)  # Wait for 3 seconds
                    warning_placeholder.empty()  # Clear the placeholder

    # Create a file uploader widget
    st.session_state.uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    # If a file is uploaded
    if st.session_state.uploaded_file is not None:
        # Open the uploaded image
        image = Image.open(st.session_state.uploaded_file)

        # Optionally, you can add more processing or display information
        st.write("Image has been successfully uploaded and displayed.")

        # Display the image on the page
        st.image(image, caption="Uploaded Image.", use_column_width=True)
    

elif st.session_state.page == "detect":
    with st.container():
        # Define the layout: 4 columns where the first takes more space for the heading
        col1, col2 = st.columns([4, 1])

        with col1:
            # Center the heading vertically
            st.markdown("<h1>Damage Detection Page</h1>", unsafe_allow_html=True)
        with col2:
            # Button for going back to the upload page
            if st.button("Go Back to the Upload"):
                go_to_upload()
            
    if st.session_state.uploaded_file is not None:
        image = Image.open(st.session_state.uploaded_file)
        # Display the image on the page
        st.image(image, caption="Uploaded Image.", use_column_width=True)
