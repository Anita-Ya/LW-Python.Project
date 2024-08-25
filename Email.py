import smtplib

def send_email(subject, body, to_email):
    try:
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        from_email = "yanitay1215@gmail.com"
        password = "#anitay$$"
        message = f'Subject: {subject}\n\n{body}'

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(from_email, password)
            server.sendmail(from_email, to_email, message)
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {e}")

subject = input("Enter the subject: ")
body = input("Enter the email body: ")
to_email = input("Enter the recipient's email: ")
send_email(subject, body, to_email)
