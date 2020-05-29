import smtplib
connection =smtplib.SMTP('smtp.gmail.com',587) 
connection.ehlo()
connection.starttls()
connection.login('sender user id','password')
connection.sendmail('sender email address','receiver email address','your message like subject:------')
connection.quit()


#  if you get any error due  to google security go to "https://myaccount.google.com/lesssecureapp"
#  them click on "Allow less secure apps:"ON""
