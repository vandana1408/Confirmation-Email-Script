"""
CONFIRMATION EMAIL SCRIPT

Sending an email to a list of people from a csv file to confirm that they can attend an event. (ADD DOCSTRINGS SOON)
"""
from csv import reader 
import smtplib


def receive_inputs(): 
    
    email = input("Email: ")
    password = input("Password: ")
    subject = input("Subject: ")
    main_text = input("Main Text: ")
    mailing_list = input("Mailing List: ")
    
    return (email, password, subject, main_text, mailing_list)

def send_email(info, to, first_name): 
    text = f"Hi, {first_name}\n" + info[3]
    
    message = f'From: {info[0]}\nTo: {to}\nSubject: {info[2]}\n\n{text}'
    
    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.ehlo()
        #server.starttls()
        server.login(info[0], info[1])
        server.sendmail(info[0], to, message)
        server.close()
        print('successfully sent the mail')
    except:
        print("email didn't send vibes")
        pass

if __name__ == "__main__": 
    
    all_inputs = receive_inputs()
    
    with open(all_inputs[-1], 'r') as read_obj: 
        
        csv_reader = reader(read_obj)
        
        for row in csv_reader: 
            send_email(all_inputs, row[3], row[1])