import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from config.config import resume_path
import os

# Your email credentials
def send_email(sender, sender_pass, receiver , e_subject , e_body):
    sender_email = sender
    receiver_email = receiver
    password = sender_pass 

    # Create the email content
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = e_subject

    # Email body
    body = e_body
    message.attach(MIMEText(body, "plain"))

    # Attach PDF file
    pdf_file = resume_path # Replace with the path to your resume PDF file
    with open(pdf_file, "rb") as f:
        attach = MIMEApplication(f.read(),_subtype="pdf")
        attach.add_header('Content-Disposition','attachment',filename=str(os.path.basename(pdf_file)))
        message.attach(attach)

    # Send the email
    try:
        # Set up the SMTP server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()  # Start TLS for security
        # Log in to your Gmail account
        server.login(sender_email, password)
        # Send the email
        text = message.as_string()
        server.sendmail(sender_email, receiver_email, text)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        server.quit()