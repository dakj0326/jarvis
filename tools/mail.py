# Mail:             jarvis.mailservice@gmail.com
# Password:         jarvis1337
# Date of Birth:    1/5-2008 (Ironman 1)

import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(parent_dir)

import smtplib
import ssl
from configHandler import getValue
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465  # Use 587 for TLS
SENDER_EMAIL = "jarvis.mailservice@gmail.com"
SENDER_PASSWORD = "kxrm yxsv emkr pdjv"
RECEIVER_EMAIL = getValue("home_assistant_settings", "mail")



def sendEmail(subject: str, body: str, fileName: str, filePath: str):
    msg = MIMEMultipart()
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECEIVER_EMAIL
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    #fileName = "mail.txt"
    #script_dir = os.path.dirname(os.path.abspath(__file__))  # Get the script's directory
    #filePath = os.path.join(script_dir, "mail.txt")

    try:
        with open(filePath, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
        
        encoders.encode_base64(part)
        part.add_header("Content-Disposition", f"attachment; filename={fileName}")
        msg.attach(part)

        # Send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT, context=context) as server:
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())

        print("Email with attachment sent successfully!")
    except Exception as e:
        print(f"Error: {e}")
        

fileName = "mail.txt"
script_dir = os.path.dirname(os.path.abspath(__file__))  # Get the script's directory
filePath = os.path.join(script_dir, "mail.txt")

subject = "so fucking epic"
body = """Hello

I am jarvis, your personal assistant. You cant reply to me yet.
Here is an attatchment as well because why the fuck not

// Jarvis"""

sendEmail(subject, body, fileName, filePath)