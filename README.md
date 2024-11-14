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
