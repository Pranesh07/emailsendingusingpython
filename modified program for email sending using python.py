import smtplib,webbrowser
def get_mail():
    servicesAvailable=['hotmail','gmail','yahoo','outlook']
    while True:
        mail_id=input("Enter your Email-Id: ")
        if '@' in mail_id and '.com' in mail_id:
            symbol_pos = mail_id.find('@')
            dotcom_pos = mail_id.find(".com")
            sp = mail_id[symbol_pos+1:dotcom_pos]
            if sp in servicesAvailable:
                return mail_id,sp
                break
            else:
                print("we dont't provide for "+sp)
                print("we provide services only for :hotmail/yahoo/gmail/outlook")
                continue
        else:
            print("Invalid E-mail retype  again")
            continue
def set_smtp_domain(serviceProvider):
    if serviceProvider=='gmail':
        return 'smtp.gmail.com'
    elif serviceProvider=='outlook' or serviceProvider=='hotmail':
        return 'smtp.mail.yahoo.com'
    elif serviceProvider=='yahoo':
        return 'smtp.mail.yahoo.com'
print('Welcome you can send an E-mail through this program')
print('Please enter your E-mail and password:')
e_mail,serviceProvider = get_mail()
password = input('password: ')
while True:
    try:
        smtpDomain=set_smtp_domain(serviceProvider)
        connection=smtplib.SMTP(smtpDomain,587)
        connection.ehlo()
        connection.starttls()
        connection.login(e_mail,password)
    except:
        if serviceProvider=='gmail':
            print("Login unsuccessfull there are two possible reason:")
            print("1.)you typed wrong username or password ")
            print("2.)you are using gmail their is an option to allow access to lesssecure apps ")
            print("Do you want to us to open webpage")
            answer=input("yes or no ?")
            if answer =="yes":
                webbrowser.open("https://myaccount.google.com/lesssecureapps")
            else:
                print("we wont open for you :you type your own")
                print("please retype your email and password")
                e_mail,serviceProvider= get_mail()
                password=input("Password:")
                continue
        else:
            print("Login unseccuessfull wronf id or password")
            print("please retype your email and password")
            e_mail,serviceProvider= get_mail()
            password=input("Password:")
            continue
    else:
        print("login successfull")
        break
print("please type receiver's e-mail address")
receiverAddress,receiverSP=get_mail()
print("Now please type subject and message ")
Subject = input("subject : ")
Message = input("Message : ")
connection.sendmail(e_mail , receiverAddress,("Subject: "+str(Subject)+"\n\n" +str(Message)))
print("E-mail send successfully")
connection.quit()

