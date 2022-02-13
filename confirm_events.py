"""
Draft script for sending a confirmation email to students when they sign up for BINFSOC events. Emails and passwords have been redacted for security purposes. 
"""

from csv import reader 
import smtplib

with open('emails.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    # Iterate over each row in the csv using reader object
    for row in csv_reader:
        # row variable is a list that represents a row in csv
        FROM = "REDACTED"
        TO = row[3]
        SUBJECT = "Confirmation Email for Event"
        words = "You amazing person" if row[-1] == 'Cereal' else "You unbelievable psycopath"
        TEXT = f""" 
        Hi, {row[1]} 

        Just confirming that you enjoy putting {row[-1]} first, {words}

        Kind Regards 
        m e 
        """
        
        message = f'From: {FROM}\nTo: {TO}\nSubject: {SUBJECT}\n\n{TEXT}'

        try:
            server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
            server.ehlo()
            #server.starttls()
            server.login("REDACTED", "REDACTED")
            server.sendmail(FROM, TO, message)
            server.close()
            print('successfully sent the mail')
        except:
            print("email didn't send vibes")
            pass
        
"""
What can be added: 
    - put some stuff in functions this looks really gross 
    - try make it more abstract, i.e. if the file is converted into a csv, the email column isn't always column 3 
    - Let their be user input for subject, from and text (also do entries for the csv file where emails are read from)
"""




