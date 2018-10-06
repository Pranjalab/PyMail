import PyMail

mail = PyMail.pymail(login_address='YOUR_LOGIN_ADDRESS', sent_address='SEND_ADDRESS')
mail.set_subject('Test 1!')
mail.set_body("Hello... \nI am Pranjal Bhaskare creater for PyMail.\nTest Complete.\nThank You :-)")
mail.attach_file('Readme.md')
mail.send_mail('PASSWORD')