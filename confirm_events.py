"""
Draft script for sending a confirmation email to students when they sign up for BINFSOC events. Emails and passwords have been redacted for security purposes. 
"""

from csv import reader 
import smtplib

# def recieve_inputs(): 
#     email = input("EMAIL: ")
#     password = input("PASSWORD: ")
#     subject = input("SUBJECT: ")
#     text = input("TEXT: ")
#     csv_file = input("FILE: ")
    
#     info = (email, password, subject, text, csv_file)
    
#     return info 

# def email_people(info_tuple, to):
#     messenger = info_tuple[0]
#     subject = info_tuple[2]
#     text = info_tuple[3]
    
#     message = f'From: {messenger}\nTo: {to}\nSubject: {subject}\n\n{text}'

# def open_file(csv_file, text): 
#     with open(csv_file, 'r') as read_obj: 
#         csv_reader = reader(read_obj)
        
#         for row in csv_reader: 
#             addressed_message = f"Hi, {row[1]}" + text 
            

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




