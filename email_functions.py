import imaplib
import email
import os

# Directory to save attachments
ATTACHMENT_DIR = "attachments"

# Ensure the attachment directory exists
if not os.path.exists(ATTACHMENT_DIR):
    os.makedirs(ATTACHMENT_DIR)

def save_attachment(part):
    """
    Save an attachment to the specified directory.
    
    Args:
    part (email.message.Message): The part of the email containing the attachment.
    
    This function decodes and saves the attachment to the specified folder.
    """
    filename = part.get_filename()  # Retrieve the attachment's filename
    if filename:
        # Decode filename if it has encoding applied
        filename = email.utils.collapse_rfc2231_value(filename)
        
        # Define the full path to save the attachment
        file_path = os.path.join(ATTACHMENT_DIR, filename)

        # Open the file in write-binary mode and save the decoded attachment
        with open(file_path, "wb") as f:
            f.write(part.get_payload(decode=True))  # Decode and save the attachment
            print(f"Attachment saved as: {file_path}")  # Log the saved attachment's path

def check_new_emails(email_address, password, imap_server, imap_port):
    """
    Connects to the IMAP server, checks for new unread emails, and processes them.
    
    Args:
    email_address (str): The email address to log in.
    password (str): The email account's password.
    imap_server (str): The IMAP server address (e.g., imap.gmail.com).
    imap_port (int): The IMAP server port (usually 993 for SSL).
    
    This function logs into the email account, searches for unseen emails, fetches their data,
    and saves any attachments found in the emails. It also handles different email content types.
    """
    try:
        # Establish a connection to the IMAP server using SSL
        mail = imaplib.IMAP4_SSL(imap_server, imap_port)
        mail.login(email_address, password)  # Login with provided email credentials
        mail.select("inbox")  # Select the inbox folder to search for emails

        # Search for unread emails (unseen)
        _, data = mail.search(None, 'UNSEEN')  # 'UNSEEN' flag indicates unread emails
        mail_ids = data[0].split()  # Split the response into individual email IDs

        # Iterate over all the unread email IDs
        for mail_id in mail_ids:
            _, data = mail.fetch(mail_id, "(RFC822)")  # Fetch the full email message
            raw_email = data[0][1]  # Extract the raw email content
            email_message = email.message_from_bytes(raw_email)  # Parse the email message

            # Print basic email details
            print("Subject:", email_message["Subject"])
            print("From:", email_message["From"])
            print("-" * 30)

            # Iterate over all parts of the email to handle different content types
            for part in email_message.walk():
                if part.get_content_type() == "text/plain":  # Check for plain text content
                    print(part.get_payload(decode=True).decode())  # Decode and print the text content
                elif part.get_content_type() == "text/html":  # Check for HTML content
                    print("HTML Email detected - cannot display directly.")
                
                # If the part is an attachment, save it to the specified directory
                if part.get_content_disposition() == "attachment":
                    save_attachment(part)

            print("=" * 50)  # Separator between emails

        # Close the mailbox and logout from the server
        mail.close()
        mail.logout()

    except Exception as e:
        print(f"An error occurred: {e}")  # Print any error that occurs during the process
