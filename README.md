# Email Attachment Downloader

This script checks your email inbox for new, unread emails, extracts any attachments, and saves them to a specified directory on your local system. It is designed to work with Gmail accounts, but can be adapted for other email providers by changing the IMAP server settings.

## Features

- Connects to Gmail via IMAP using SSL (port 993).
- Checks for unread emails in your inbox.
- Downloads email attachments and saves them to a local folder.
- Handles different content types, including plain text and HTML email bodies.

## Requirements

- Python 3.x (Python 3.6 or higher recommended)
- No external dependencies required for basic functionality, as `imaplib`, `email`, `os`, and `time` are part of Python's standard library.


## Setup

1. **Clone the repository:**


2. **Install required dependencies (optional):**

If you're planning to use the optional libraries (e.g., `beautifulsoup4`, `requests`), you can install them via:


3. **Configure your email credentials:**

Open the script and replace the placeholders with your email address and password:

```python
EMAIL_ADDRESS = "your_email"  # Replace with your email address
PASSWORD = "your_password"  # Replace with your email password

**Run the application with command **
python email_attachment_downloader.py



