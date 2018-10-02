
import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("pranjalapb@gmail.com", "***Hidden_Password***")

msg = "Test Successful!!!"
server.sendmail("pranjalapb@gmail.com", "pranjalab@gmail.com", msg)
server.quit()