import time
from email_functions import check_new_emails

# Email account credentials
EMAIL_ADDRESS = "your_email"  # Replace with your email address
PASSWORD = "your_password"  # Replace with your email password

# IMAP server settings for Gmail
IMAP_SERVER = "imap.gmail.com"
IMAP_PORT = 993  # Use 993 for SSL

if __name__ == "__main__":
    # Loop to check for new emails at regular intervals (every 60 seconds)
    while True:
        check_new_emails(EMAIL_ADDRESS, PASSWORD, IMAP_SERVER, IMAP_PORT)
        time.sleep(60)  # Wait for 60 seconds before checking again
