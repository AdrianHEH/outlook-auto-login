# Outlook Auto Login

This Python script automates the login process to multiple Outlook accounts using Selenium. It reads email and password pairs from a text file, opens a new Chrome browser session in guest mode for each account, and logs in automatically. This setup allows multiple sessions to stay open simultaneously, each with its own isolated profile.

## Features
- **Automated Multi-Account Login**: Logs into multiple Outlook accounts in sequence.
- **Guest Mode**: Uses Chrome's guest profile mode for each session, keeping them isolated.
- **Credential Management**: Reads login credentials from a text file.
- **Selenium Integration**: Uses Selenium WebDriver with `webdriver-manager` for easy ChromeDriver setup and management.

## Requirements
- **Python** (version 3.6+)
- **Selenium**: Web automation tool
- **webdriver-manager**: Automatically handles ChromeDriver installation

## Setup and Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/outlook-auto-login.git
   cd outlook-auto-login
   
2. **Install the required packages: Install Selenium and `webdriver-manager` using the `requirements.txt` file:y**
   ```bash
   
   pip install -r requirements.txt
   
3. **repare your credentials: Create a file named `credentials.txt` in the project directory. List your Outlook accounts in this file, using the format `email:password` for each account on a new line:**:
   ```bash
   
   user1@example.com:password1
   user2@example.com:password2
   
4. **Update the Credentials Path: update the path in the script:**
   Open `outlook_auto_login.py`
   Modify the `CREDENTIALS_PATH` variable on line 52 to the location of your credentials.txt file:**:
   
   ```bash
   chrome_options.binary_location = r"path\to\your\chrome.exe"
   
5. **Running the Script:**
   
 ```bash
   python outlook_auto_login.py



