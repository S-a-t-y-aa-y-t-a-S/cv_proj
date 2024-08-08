import streamlit as st
from PIL import Image

# set the title of the app
st.title("Image upload and display")

# # Create a simple navigation bar with a title, login, and signup buttons
# st.markdown(
#     """
#     <style>
#     .navbar {
#         display: flex;
#         justify-content: space-between;
#         align-items: center;
#         background-color: #4CAF50; # lime green
#         padding: 10px;
#     }
#     .navbar h1 {
#         margin: 0;
#     }
#     </style>
#     <div class="navbar">
#         <h1>Image Upload and Display</h1>
#         <div>
#             <button onclick>
#     </div>

# """
# )


# # Create sections for login and signup
# st.markdown("<h2 id = 'login'>Login</h2>", unsafe_allow_html=True)
# if st.button("Login"):
#     st.write("Redirecting to login....")

# st.markdown("<h2 id = 'sign-up'>Sign Up</h2>", unsafe_allow_html=True)
# if st.button("Sign-up"):
#     st.write("Redirecting to sign-up....")



# create a file uploader widget
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# if a file is uploaded
if uploaded_file is not None:
    # Open the uploaded image
    image = Image.open(uploaded_file)

    # Display the image on the page
    st.image(image, caption="Uploaded Image.", use_column_width=True)

    # Optionally, you can add more processing or display information
    st.write("Image has been successfully uploaded and displayed.")