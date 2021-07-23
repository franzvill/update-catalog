#!/usr/bin/env python3

import os
from datetime import date
from reports import generate_report
import emails

folder = "supplier-data/descriptions/"

def get_data(file):
    data = {}
    with open(file) as f:
        data['name'] = f.readline().strip()
        data['weight'] = f.readline().strip()

    return data

def get_paragraph():
    paragraph = ""
    files = os.listdir(folder)
    for file in files:
        if file.endswith(".txt"):
            paragraph += "<br/>"
            data = get_data(folder + file)
            paragraph += "name: {}<br/>".format(data['name'])
            paragraph += "weigth: {}<br/>".format(data['weight'])
    
    return paragraph


if __name__ == "__main__":
    paragraph = get_paragraph()
    today = date.today()
    title = "Processed Update on {} ".format(today.strftime("%b %d, %Y"))
    generate_report("/tmp/processed.pdf",title,paragraph)
    message = emails.generate_email("automation@example.com", "student-02-cb473a3de71d@example.com","Upload Completed - Online Fruit Store", "All fruits are uploaded to our website successfully. A detailed list is attached to this email.","/tmp/processed.pdf")
    emails.send_email(message)
