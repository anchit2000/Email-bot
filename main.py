import smtplib
import pyttsx3
import speech_recognition as sr
from credentials import username,smtp,port_number,password
import pyaudio
from email_list import email_list
from email.message import EmailMessage
import sys

engine = pyttsx3.init()
listener = sr.Recognizer()

def sendEmail(smtp,port_number,username,password,destination,subject,mail_content):
    try:
        server = smtplib.SMTP(smtp,port_number)
        server.starttls()
        server.login(username,password)
        #server.sendmail('anchit2000@gmail.com','arjishrivas@gmail.com','Hey brother lets see if I am able to send you a mail using python.')
        email = EmailMessage()
        email['From'] = username
        email['To'] = destination
        email['Subject'] = subject
        email.set_content(mail_content)
        #server.sendmail(username,destination,mail_content)
        server.send_message(email)
        print("mail sent successfully to " +destination)
    except:
        print("Invalid credentials")

def talk(text):
    engine.say(text)
    engine.runAndWait()

def get_commands():
    try:
        with sr.Microphone() as source:
            talk("listening")
            print("Listening...")
            voice = listener.listen(source)
            info = listener.recognize_google(voice).lower()
        print(info)
        return(info)

    except:
        print('Please check your microphone')
        talk("Please check your microphone.")

def get_mail_content():
    print("Whom do you want to send this email to?")
    talk("Whom do you want to send this email to?")
    destination = get_commands()
    try:
        destination_addr = email_list[destination]
    except:
        print("No email address found for this contact")
        talk("No email address found for this contact")
        sys.exit()
    print("What is the subject of your mail?")
    talk("What is the subject of your mail?")
    subject = get_commands()
    print("What is the content of your mail?")
    talk("What is the content of your mail?")
    content = get_commands()
    #you can modify this content you got as input also.
    # for example if 'comma' in content : content = content.replace('comma',',')
    return destination_addr,subject,content

if __name__ == '__main__':
    destination,subject,mail_content = get_mail_content()
    #if destination == 'test':
    #    destination = 'anchit2000@gmail.com'
    sendEmail(smtp,port_number,username,password,destination,subject,mail_content)
    #print(destination)
