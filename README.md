Secure Data Encryption System Using Streamlit
This application allows users to securely encrypt and decrypt their messages and files using a password-based encryption system. It is built using Python, Streamlit, and a Lottie animation for a user-friendly interface. The application supports user authentication, encryption, and decryption functionalities.

Features
User Authentication: Users can register and log in with a username and password.

Encrypt and Decrypt Text: Encrypt or decrypt messages using a secret key (password-based encryption).

Save and Load Data: Save encrypted messages and load them back from the app's storage.

File Encryption/Decryption: Upload .txt files for encryption or decryption, and download the processed files.

Animations: Lottie animations provide an interactive user experience.

Requirements
To run this application, you will need the following dependencies:

Python 3.x

Streamlit

streamlit-lottie (for Lottie animations)

Requests (for loading Lottie animations from URLs)

Install dependencies:
You can install the required libraries using pip:

bash
Copy
Edit
pip install streamlit
pip install streamlit-lottie
pip install requests
Usage
Run the application: After setting up the environment and installing dependencies, you can run the Streamlit app with the following command:

bash
Copy
Edit
streamlit run app.py
Authentication:

The app will display a sidebar with options to either Login or Register.

Register a new user with a unique username and password, then log in using the same credentials.

Encrypt/Decrypt Message:

After logging in, enter a secret key (password) to generate an encryption key.

Select whether you want to Encrypt or Decrypt a message.

Input your message and the app will process it accordingly.

You can also save your encrypted message for later use.

File Encryption/Decryption:

Upload a .txt file to either encrypt or decrypt the file.

After processing, you can download the resulting file.

Logout:

You can log out anytime, which will reset the session.

Code Structure
auth.py: Contains functions for user authentication (login and register).

data_handler.py: Handles saving and loading encrypted data.

encryption.py: Functions for encrypting and decrypting text or files.

utils.py: Helper functions for generating keys from passwords.

app.py: Main application logic that integrates everything and provides the user interface.

Lottie Animation
The app uses Lottie animations to enhance the user experience. The animations are loaded dynamically from a URL using the streamlit-lottie package.

Contribution
Feel free to fork this repository and contribute. If you find any issues or have suggestions for improvements, please create an issue or submit a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.

