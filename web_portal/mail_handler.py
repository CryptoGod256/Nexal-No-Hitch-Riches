import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, body, recipient):
    sender_email = "nexalhq.inc@gmail.com"
    app_password = "fglzsmbsyslcclmn"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, app_password)
        server.sendmail(sender_email, recipient, msg.as_string())
        server.quit()
        print(f"[!] SUCCESS: Email sent to {recipient}")
    except Exception as e:
        print(f"[!] ERROR: {e}")

def run():
    print("[!] MAIL HANDLER: Initiating sequence...")
    send_email("NEXAL INTELLIGENCE ALERT", "System engine online and operational.", "nexalhq.inc@gmail.com")
    print("[!] MAIL HANDLER: Operation complete.")

if __name__ == "__main__":
    run()

