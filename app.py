import streamlit as st
from auth import login_user, register_user
from encryption import encrypt_message, decrypt_message
from utils import generate_key_from_password
from data_handler import save_data, load_data
import requests
from streamlit_lottie import st_lottie  # Add this import

# Load Lottie animation
def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Initialize session state
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False
    st.session_state.username = ""

# Sidebar with login form
with st.sidebar:
    st.title("🔐 Secure Data App")
    if not st.session_state.authenticated:
        st.header("Login / Register")
        choice = st.selectbox("Choose Option", ["Login", "Register"])

        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if choice == "Register":
            if st.button("Register"):
                if username and password:
                    if register_user(username, password):
                        st.success("Registered successfully. Please log in.")
                    else:
                        st.warning("Username already exists.")
                else:
                    st.error("Please enter username and password.")
        else:
            if st.button("Login"):
                if login_user(username, password):
                    st.session_state.authenticated = True
                    st.session_state.username = username
                    st.success("Logged in successfully.")  # Main page will appear below
                else:
                    st.error("Invalid credentials.")

# Main page content (only shows after login)
if st.session_state.authenticated:
    # Lottie animation
    lottie_lock = load_lottie_url("https://assets9.lottiefiles.com/packages/lf20_touohxv0.json")
    if lottie_lock:
        st_lottie(lottie_lock, height=180)

    st.title("🔐 Secure Data Encryption System")

    secret = st.text_input("Enter your secret key (password-based):", type="password")
    action = st.radio("Choose Action", ["Encrypt", "Decrypt"])

    message = st.text_area("Enter your message")

    if secret and message:
        key = generate_key_from_password(secret)
        if action == "Encrypt":
            encrypted_message = encrypt_message(message, key)
            st.text_area("Encrypted Message", encrypted_message, height=100)
            if st.button("💾 Save Encrypted Message"):
                save_data(st.session_state.username, encrypted_message)
                st.success("Encrypted message saved.")
        elif action == "Decrypt":
            try:
                decrypted_message = decrypt_message(message, key)
                st.text_area("Decrypted Message", decrypted_message, height=100)
            except Exception as e:
                st.error(f"Decryption failed: {e}")

    # Load saved encrypted message
    if st.button("📂 Load Last Saved Message"):
        saved = load_data(st.session_state.username)
        if saved:
            st.text_area("Saved Encrypted Message", saved, height=100)
        else:
            st.warning("No saved message found.")

    st.markdown("---")
    st.subheader("📁 File Encryption / Decryption")

    uploaded_file = st.file_uploader("Upload a `.txt` file", type=["txt"])
    if uploaded_file and secret:
        file_content = uploaded_file.read().decode()
        key = generate_key_from_password(secret)

        if action == "Encrypt":
            encrypted_file_text = encrypt_message(file_content, key)
            st.download_button("Download Encrypted File", encrypted_file_text, file_name="encrypted.txt")
        elif action == "Decrypt":
            try:
                decrypted_file_text = decrypt_message(file_content, key)
                st.download_button("Download Decrypted File", decrypted_file_text, file_name="decrypted.txt")
            except Exception as e:
                st.error(f"Decryption failed: {e}")

    # Logout button
    if st.button("Logout"):
        st.session_state.authenticated = False
        st.session_state.username = ""
        st.experimental_rerun()

else:
    st.sidebar.info("Please login to access the main page.")
