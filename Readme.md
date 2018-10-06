# Pran_Pymail:
This project helps you to send mails using Python script with attachment.(Tested for G-mail Account)
# Inspiration:
Whenever I train a Deep Learning modal it takes more than 3-4 hours and I don't get to know when the training is Completed. So I  decided to make a project which can notify me of training competition by E-Mailing me with the results files.  
# Dependency:
> 1. smtplib: pip install smtplib
# How does it work:
Using the login_address and password PyMail login in your email address and sends the mail to given sent_address. I know that typing password in visible form is very risky so I decided to use two methods for it which you can read in 'How to Use:' section.
Following are the PyMail sections:
>1. login_address: E-mail address from you want to login  
[PyMail.pymail(login_address='YOUR_LOGIN_ADDRESS') or PyMail.pymail.set_login_address('YOUR_LOGIN_ADDRESS')]
>2. sent_address: E-mail address where you want to send mail  
[PyMail.pymail(sent_address='SENT_ADDRESS') or PyMail.pymail.set_sent_address('SENT_ADDRESS')] 
>3. Subject(Optional): Subject of your mail  
[PyMail.pymail(subject='YOUR_MAIL_SUBJECT') or PyMail.pymail.set_subject('YOUR_MAIL_SUBJECT')] 
>4. Body(Optional): Content of your mail  
[PyMail.pymail(body='YOUR_MAIL_BODY') or PyMail.pymail.set_body('YOUR_MAIL_BODY')] 
>5. File Attachment(Optional): Attach you file, You can attach multiple files separately  
[PyMail.pymail.attach_file('FILE_PATH')] 
>6. send Mail: send mail  
[PyMail.pymail.send_mail() if password is encrypted inside the file (method 1) or PyMail.pymail.send_mail('YOUR LOGIN PASSWORD') (method 2).
# How to use it:
As mentioned in 'How does it work' section password security is an important domain, so I decided to perform to methods. In the first method (I prefer), we can encrypt the login email address and password using Pran_Pyencrypt's Pyencrypter.py file. It will convert the PyMail.py file to PyMail.<system_variables>.pyd file which is kind of python .dll files which is not readable.
In the second method, we can directly use PyMail.py file and set our login password while sending the mail by PyMail.send_mail('PASSWORD') but the password will be visible.
## Method 1:
> 1. Open PyMail.py and store your login address and password in LOGIN_ADDRESS and _LOGIN_PASSWORD respectively and close the file.
> 2. Open terminal in Pran_PyMail directory and type:
        
        python Pyencrypter.py -f "PyMail.py"
>3. Hit enter, It will create a PyMail.<system_variables>.pyd file  

Now, this file contains everything you can use it anywhere by importing it in other python files.  
Don't Share .pyd file with anyone alto its encrypted be it's not impossible to decrypt it.
	Import PyMail
## Method 2:
Directly import the PyMail.py file and use it, While sending the mail you can enter your password in PyMail.send_mail('PASSWORD')
## Errors:
1. smtplib.SMTPAuthenticationError: (534,....): This error is because your login email address is not allowing to login to the less secure apps to avoid this error you can go to this link and select Turn On
https://www.google.com/settings/security/lesssecureapps 
    