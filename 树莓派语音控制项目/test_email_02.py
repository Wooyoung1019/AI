import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from urllib.parse import quote

email = MIMEMultipart() # 创建邮件主题对象
email['From'] = '846425789@qq.com'
email['To'] = '2723281723@qq.com'
email['Subject'] =Header('email_test_01', 'utf-8')
content =  '''
    <p>hello world !!!</p>
    <p>frist email_python </p>
    <br>
    <p>无恙</p>
'''
email.attach(MIMEText(content, 'html', 'utf-8'))
with open(f'audio/test.docx', 'rb') as file:
    attachment = MIMEText(file.read(), 'base64', 'utf-8')
    attachment['content-type'] = 'application/octet-stream'
    filename = quote('test.docx')
    attachment['content-disposition'] = f'attchment;filename="{filename}"'

smtp_obj = smtplib.SMTP_SSL('smtp.qq.com', 465) # 创建SMTP_SSL对象（连接邮件服务器）
smtp_obj.login('846425789@qq.com', 'lutoqkqipscxbchg')
smtp_obj.sendmail(
    '846425789@qq.com',
    '2723281723@qq.com',
    email.as_string()
)