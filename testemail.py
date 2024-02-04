#Easiest and Readable way to Email
#through Python SMTPLIB library
#This works with >>> Gmail.com <<<
import smtplib 
from email.message import EmailMessage




import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email settings
sender_email = "williamrayyan14@gmail.com"
receiver_email = "rayyanzaid0401@gmail.com"
password = "lrfe qlxb eheg oeni"  # Your email account password or app password
smtp_server = "smtp.gmail.com"
port = 587  # For starttls

# Create a multipart message
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = "Python smtplib Test"

# Mail body
mail_body = """
This is a test email sent from Python. Isn't that cool?
"""
message.attach(MIMEText(mail_body, "plain"))

try:
    # Create server object with SSL option
    server = smtplib.SMTP(smtp_server, port)
    server.starttls()  # Secure the connection
    server.login(sender_email, password)
    
    # Send the email
    server.sendmail(sender_email, receiver_email, message.as_string())
    print("Email successfully sent!")
except Exception as e:
    print(f"Error: {e}")
finally:
    server.quit()
