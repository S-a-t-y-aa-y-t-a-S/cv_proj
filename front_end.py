import streamlit as st
from PIL import Image

# Define the navbar with buttons included in the HTML
st.markdown(
    """
    <style>
    .navbar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background-color: #4CAF50;
        padding: 10px 20px;
        margin-bottom: 20px;
        border-radius: 8px;
    }
    .navbar h1 {
        margin: 0;
        color: white;
        font-size: 24px;
        font-weight: bold;
    }
    .button-container {
        display: flex;
        gap: 15px;
    }
    .navbar-button {
        padding: 10px 20px;
        background-color: white;
        border: 2px solid #4CAF50;
        color: #4CAF50;
        cursor: pointer;
        font-size: 16px;
        font-weight: bold;
        border-radius: 25px;
        transition: all 0.3s ease;
    }
    .navbar-button:hover {
        background-color: #4CAF50;
        color: white;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    </style>
    <div class="navbar">
        <h1>Image Upload and Display</h1>
        <div class="button-container">
            <button id = "login-button" class = "navbar-button">Login</button>
            <button id = "signup-button" class = "navbar-button">Sign Up</button>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# JavaScript for button interactions (this triggers Streamlit events)
st.markdown(
    """
    <script>
    const loginButton = document.getElementById('login-button');
    const signupButton = document.getElementById('signup-button');

    loginButton.onclick = function() {
        window.parent.postMessage({ type: 'login_click' }, '*');
    };

    signupButton.onclick = function() {
        window.parent.postMessage({ type: 'signup_click' }, '*');
    };
    </script>
    """,
    unsafe_allow_html=True,
)

# Placeholder to listen to the custom events triggered by the JavaScript
login_click = st.empty()
signup_click = st.empty()

# Check for clicks and update Streamlit app accordingly
if st.session_state.get('login_clicked', False):
    st.write("Login button clicked! Redirecting to login...")

if st.session_state.get('signup_clicked', False):
    st.write("Sign Up button clicked! Redirecting to sign-up...")

# Create a file uploader widget
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# If a file is uploaded
if uploaded_file is not None:
    # Open the uploaded image
    image = Image.open(uploaded_file)

    # Display the image on the page
    st.image(image, caption='Uploaded Image.', use_column_width=True)

    # Optionally, you can add more processing or display information
    st.write("Image has been successfully uploaded and displayed.")


# Listen to the messages from JavaScript and update Streamlit session state
st.markdown(
"""
    <script>
    window.addEventListener('message', (event) => {
        if (event.data.type === 'login_click') {
            window.parent.postMessage({ type: 'streamlit', key: 'login_clicked', value: true }, '*');
        } else if (event.data.type === 'signup_click') {
            window.parent.postMessage({ type: 'streamlit', key: 'signup_clicked', value: true }, '*');
        }
    });
    </script>
""",
unsafe_allow_html=True,
)

