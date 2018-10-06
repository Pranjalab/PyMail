import smtplib
from email.mime.multipart import MIMEMultipart, MIMEBase
from email.mime.text import MIMEText
from email import encoders
import os

LOGIN_ADDRESS = 'YOUR LOGIN ADDRESS'
_LOGIN_PASSWORD = 'PASSWORD'#TODO

class pymail:
    def __init__(self, login_address=LOGIN_ADDRESS, sent_address='',subject='',body=''):
        self.msg = MIMEMultipart()
        self.set_login_address(login_address)
        self.set_sent_address(sent_address)
        self.set_subject(subject)
        self.set_body(body)
        self.filename = ''

    def set_login_address(self, login_address):
        self.login_address = login_address

    def get_login_address(self):
        return self.login_address

    def set_sent_address(self, address):
        self.sent_address = address

    def get_sent_address(self):
        if self.sent_address:
            return self.sent_address
        else:
            print("Please first set the sent address!")

    def set_subject(self, subject):
        self.subject = subject

    def get_subject(self):
        if self.subject:
            return self.subject
        else:
            print("Please first set the subject!")

    def set_body(self, body):
        self.body = body

    def get_body(self):
        if self.body:
            return self.body
        else:
            print("Please first set the Body!")

    def attach_file(self, file_path):
        self.filename = os.path.basename(file_path)
        attachment = open(self.filename, "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % self.filename)
        self.msg.attach(part)

    def get_attach_file_name(self):
        if self.filename:
            return self.filename
        else:
            print("Please first attach the file!")

    def send_mail(self, password=_LOGIN_PASSWORD):
        if self.login_address and self.sent_address and password:
            self.msg['From'] = self.login_address
            self.msg['To'] = self.sent_address
            self.msg['Subject'] = self.subject
            self.msg.attach(MIMEText(self.body, 'plain'))

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(self.login_address, password)
            text = self.msg.as_string()
            server.sendmail(self.login_address, self.sent_address, text)
            server.quit()
        else:
            print("Please check following:\n"
                  "Login Address: {}\nTo Address: {}\nAnd check your password".format(self.login_address,self.sent_address))

