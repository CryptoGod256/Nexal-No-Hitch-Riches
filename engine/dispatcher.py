import smtplib
from email.message import EmailMessage

def dispatch_alert(signal_title, signal_desc):
    ADMIN_EMAIL = "nexalhq.inc@gmail.com"
    # Placeholder for credentials - keep these secure
    SENDER_EMAIL  = "nexalhq.inc@gmail.com"
    SENDER_PASSWORD = "Pvajpshtwjqzepzy"

    msg = EmailMessage()
    msg.set_content(f"Alert: {signal_title}\n\nDetails: {signal_desc}")
    msg['Subject'] = f"NEXAL INTELLIGENCE: {signal_title}"
    msg['From'] = SENDER_EMAIL
    msg['To'] = ADMIN_EMAIL

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(SENDER_EMAIL, SENDER_PASSWORD)
            smtp.send_message(msg)
        print("Alert dispatched successfully.")
    except Exception as e:
        print(f"Dispatch failure: {e}")
