
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def generate_email(recipient_name, your_name = None, your_position = None, your_company = None, subject = None, content = None):
    email_template = """
    Dear {recipient_name},

    {content}

    Best regards,

    {your_company}
    """
    email_content = email_template.format(
        recipient_name=recipient_name,
        your_name=your_name,
        your_position=your_position,
        your_company=your_company,
        content=content
    )
    return email_content

def sendEmail(to_whom, subject, content):
    sender_email = ""
    sender_pass = ""
    receiver_email = to_whom

    content_with_name = generate_email(
        recipient_name=to_whom,
        # your_name="Krish Mishra",  # Replace with your actual name
        # your_position="Developer/Coder",  # Replace with your actual position/title
        # your_company="SADK",  # Replace with your actual company/organization
        your_company="FoundMate",  # Replace with your actual company/organization
        subject=subject,
        content=content
    )

    try:
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = receiver_email
        msg["Subject"] = subject
        msg.attach(MIMEText(content_with_name, "plain"))

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_pass)
            server.sendmail(sender_email, receiver_email, msg.as_string())
            print("Email sent successfully")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    sendEmail("shaswatm037@gmail.com", "Resolving Email Problem", "I have tryed to resolve the prtobllem like Dear{receipent name} and then i got to know that if we will use gpt then it will not going to solve this but if we will write an email manually then we can do that automatically. This is the example email where all the field have been filled successfully")
