import smtplib

host="smtp.gmail.com"
port=587
username="sassy150922@gmail.com"
password="06091999@"

email_conn=smtplib.SMTP(host,port)
email_conn.ehlo()
email_conn.starttls()
email_conn.login(username,password)
email_conn.sendmail(username,username,"hii how are you dear")
