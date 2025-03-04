# Mail:             jarvis.mailservice@gmail.com
# Password:         jarvis1337
# Date of Birth:    1/5-2008 (Ironman 1)

import smtplib
import ssl
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465  # Use 587 for TLS
SENDER_EMAIL = "jarvis.mailservice@gmail.com"
SENDER_PASSWORD = "jarvis1337"
RECEIVER_EMAIL = "davidi.kjellberg@gmail.com"

subject = "Jarvis Test"
body = """Hello, 

This is a test

- Jarvis"""

msg = MIMEMultipart()
msg["From"] = SENDER_EMAIL
msg["To"] = RECEIVER_EMAIL
msg["Subject"] = subject
msg.attach(MIMEText(body, "plain"))

fileName = "test.txt"
filePath = os.path.join(os.getcwd(), "test.txt")

print(f"Looking for file at: {filePath}")

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