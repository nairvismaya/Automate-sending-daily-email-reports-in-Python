import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email_report():
    # Email credentials and configuration
    sender_email = "sender_mail"
    sender_password = "password"
    receiver_email = "receiver_mail"
    subject = "Daily Report"
    body = "This is your daily report."

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Create an SMTP session
        server = smtplib.SMTP('smtp.gmail.com', 587)  # Use Gmail's SMTP server
        server.starttls()  # Enable security

        # Login to the email account
        server.login(sender_email, sender_password)

        # Convert the message to a string and send it
        server.sendmail(sender_email, receiver_email, msg.as_string())

        # Close the SMTP session
        server.quit()

        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Test the email function immediately
send_email_report()
