def send_email(subject, body, files=[]):
    import datetime
    import re
    import pandas as pd
    import smtplib, ssl

    from email.utils import formatdate
    from email.mime.multipart import MIMEMultipart
    from email.header import Header
    # 메일 제목과 내용을 설정하는 모듈
    from email.mime.text import MIMEText
    import os
    from email.mime.base import MIMEBase
    from email.encoders import encode_base64
    
    msg = MIMEMultipart()

    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "ironmanciti@gmail.com"  # Enter your address
    receiver_email = "trimurti@naver.com"  # Enter receiver address
    with open("password.txt", "r") as pswd:
        password = pswd.read()

    msg['From'] = sender_email 
    msg['To'] = receiver_email 
    msg['Date'] = formatdate(localtime=True)

    msg['Subject'] = Header(s=subject, charset='utf-8')
    body = MIMEText(body, _charset='utf-8')
    msg.attach(body)
    
    for f in files:
        part = MIMEBase('application', "octet-stream")
        part.set_payload(open(f,"rb").read())
        encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(f))
        msg.attach(part)
        
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())   
        server.quit()
        
    print("성공적으로 메일 발송")
