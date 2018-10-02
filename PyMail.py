import smtplib
from email.mime.multipart import MIMEMultipart, MIMEBase
from email.mime.text import MIMEText
from email import encoders

fromaddr = "pranjalapb@gmail.com"
toaddr = "pranjalab@gmail.com"

msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Test Mail for PyMail"

body = "HI,\nI am pranjal bhaskare.\nThank you..."
msg.attach(MIMEText(body, 'plain'))

filename = "test_file.txt"
attachment = open("test_file.txt", "rb")

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

msg.attach(part)

server = smtplib.SMTP('smtp.gmail.com', 587)

server.starttls()
server.login(fromaddr, "***Hidden_Password***")

text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
