#!/usr/bin/env python3

from email.message import EmailMessage
import smtplib
import os

def generate_email(sender, recipient, subject, body, attachment):
    message = EmailMessage()
    message['From'] = sender
    message['To'] = recipient
    message['Subject'] = subject
    message.set_content(body)

    with open(attachment, "rb") as f:
        message.add_attachment(f.read(), maintype="application", subtype="pdf", filename=os.path.basename(attachment))

    return message


def send_email(message):
    mail_server = smtplib.SMTP('localhost')
    mail_server.send_message(message)
