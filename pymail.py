# -*- coding: utf-8 -*-
"""
Well come to PyMail
===================
PyMail is a Python module which helps us to sand mails easily through the python script.
It required a Google email account from which we can sand mail to other email address and its
password.
we can store our mail and password in the following variables:
LOGIN_ADDRESS = 'EMAIL@gmail.com'
_LOGIN_PASSWORD = 'PASSWORD'
"""
import smtplib
from email.mime.multipart import MIMEMultipart, MIMEBase
from email.mime.text import MIMEText
from email import encoders
import os


LOGIN_ADDRESS = ''
_LOGIN_PASSWORD = ''


class PyMail:
    """
    This PyMail class contain this __init__ methods:
    - __init__(self, login_address=LOGIN_ADDRESS, send_address='', subject='', body=''):

    we can initialize the mail by creating the object of PyMail class and giving the following
    variables or we can also initialize the variables from set_ methods:
    > sand_address : The email address where we want to sand the mail.
    eg. send_address='SEND_ADDRESS@gmail.com'
    > subject : Subject of mail
    > body : Body of mail
    """
    def __init__(self, login_address=LOGIN_ADDRESS, send_address='', subject='', body=''):
        self.msg = MIMEMultipart()
        self.set_login_address(login_address)
        self.set_mail_address(send_address)
        self.set_subject(subject)
        self.set_body(body)
        self.filename = ''

    def set_login_address(self, login_address):
        """
        Change or set new login address.
        :param login_address: Email address from which mail will be sand
        """
        self.login_address = login_address

    def get_login_address(self):
        """
        get login address.
        :return: login address
        """
        return self.login_address

    def set_mail_address(self, address):
        """
        Change or set new send address.
        :param address: sand address
        """
        self.sent_address = address

    def get_mail_address(self):
        """
        get send address.
        :return: send address
        """
        if not self.sent_address:
            raise Exception('Please set the mail address!\n'
                            'Use set_mail_address("MAIL_ADDRESS") to set mail address.')

        return self.sent_address

    def set_subject(self, subject):
        """
        set or change subject of the mail
        :param subject: subject of the mail
        """
        self.subject = subject

    def get_subject(self):
        """
        get subject of the mail
        :return: subject of the mail
        """
        if not self.subject:
            raise Exception('Please set the subject!\n'
                            'Use set_subject("SUBJECT FOR THE MAIL") to set subject.')
        return self.subject

    def set_body(self, body):
        """
        set or change body of the mail
        :param body: body of the mail
        """
        self.body = body

    def get_body(self):
        """
        get body of the mail
        :return: body of the mail
        """
        if not self.body:
            raise Exception('Please set the body!\n'
                            'Use set_body("BODY FOR THE MAIL") to set body.')
        return self.body

    def attach_file(self, file_path):
        """
        change or set attached file path to mail.
        :param file_path: full path of attach file.
        """
        self.filename = os.path.basename(file_path)
        attachment = open(self.filename, "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % self.filename)
        self.msg.attach(part)

    def get_attach_file_name(self):
        """
        get attached file name
        :return: file name
        """
        if self.filename:
            raise Exception('Please attach the file!\n'
                            'Use attach_file("FILE_PATH") to attach file in mail.')
        return self.filename

    def send_mail(self, password=_LOGIN_PASSWORD):
        """
        Sand mail when the mail is compiled. we can also initialize the password if the password is
        not stored in the _LOGIN_PASSWORD variable.
        :param password: Login password
        """
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
                  "Login Address: {}\nTo Address: {}\n"
                  "And check your password".format(self.login_address, self.sent_address))
