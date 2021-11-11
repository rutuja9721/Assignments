#Write a python program that checks presence of a file in a directory
#with time-stamp and sends an email about success if file is found at the location

import os
import time
import smtplib
from email.message import EmailMessage

fname = 'Examplefile.txt'
direct = 'D:\Python'

path = os.path.join(direct,fname)
if(os.path.exists(path)):
    ti_c = os.path.getctime(path)
    c_ti = time.ctime(ti_c)

    s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    #s.starttls() #not needed if _SSL connection
    s.login("rutujakrios@gmail.com", "Example@123")

    msg = EmailMessage()
    msg['Subject'] = "Hello from python"
    msg['From'] = "rutujakrios@gmail.com"
    msg['To'] = "rutujakrios@gmail.com"
    msg.set_content("File found! Created at " + c_ti)

    # message = "File created at " + c_ti
    # subj = "Hello from python"
    # msg = f'Subject: {subj}\n\n{message}'
    # s.sendmail("rutujakrios@gmail.com","rutujakrios@gmail.com", msg)

    s.send_message(msg)

    s.quit()

else:
    print("File not found")
