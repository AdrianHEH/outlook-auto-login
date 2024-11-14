import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


# Function to read credentials from a text file
def read_credentials(file):
    credentials = []
    with open(file, "r") as f:
        for line in f:
            email, password = line.strip().split(":")  # Split email:password
            credentials.append((email, password))
    return credentials

# Function to create a Chrome guest profile and log into Outlook
def create_chrome_guest():
    chrome_options = Options()
    chrome_options.add_argument("--guest")  # Guest mode
    chrome_options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"  # Path to chrome.exe
    
    # Use webdriver-manager to automatically install and fetch the correct chromedriver
    driver_path = ChromeDriverManager().install()  # Downloads and installs the compatible driver
    service = Service(driver_path)  # Create a service with the installed driver
    
    # Create a new driver with the specified options
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

# Function to log into Outlook
def login(driver, email, password):
    try:
        print("Accessing the login page...")
        driver.get("https://go.microsoft.com/fwlink/p/?LinkID=2125442&clcid=0x409&culture=en-us&country=us")
        sleep(3)  # Wait for the page to load
        
        # Find fields and log in
        print("Entering email...")
        driver.find_element("xpath", '//*[@id="i0116"]').send_keys(email)  # Email field
        driver.find_element("xpath", '//*[@id="idSIButton9"]').click()  # Click 'Next'
        sleep(2)
        
        print("Entering password...")
        driver.find_element("xpath", '//*[@id="i0118"]').send_keys(password)  # Password field
        driver.find_element("xpath", '//*[@id="idSIButton9"]').click()  # Click 'Sign In'
        sleep(5)  # Wait for the login to complete
    except Exception as e:
        print(f"An error occurred during login: {e}")

# Main function
def main():
    # Get the path of the current script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))  # Directory of the script
    CREDENTIALS_PATH = os.path.join(script_dir, "credentials.txt")  # Path to credentials file in the same directory

    print(f"Looking for credentials file at: {CREDENTIALS_PATH}")
    
    # Read credentials from the file
    credentials = read_credentials(CREDENTIALS_PATH)
    
    drivers = []  # List to store the instances of the open drivers
    
    for i, (email, password) in enumerate(credentials, start=1):
        print(f"Logging into profile {i} with email {email}...")
        
        # Create a Chrome guest profile and log in
        driver = create_chrome_guest()
        drivers.append(driver)  # Add this instance to the list to keep the reference
        sleep(30)

        try:
            login(driver, email, password)
        except Exception as e:
            print(f"An error occurred for profile {i}: {e}")
        
        # Keep the window open for the first login
        if i == 1:
            print("First login completed, window kept open.")

        else:
            print(f"Profile {i} login completed in a new window.")
        
    # Keep all windows open after the logins
    print("All profiles are open. Press Ctrl+C to close.")
    sleep(100000)  # Keep the script running so the windows remain open

if __name__ == "__main__":
    main()
