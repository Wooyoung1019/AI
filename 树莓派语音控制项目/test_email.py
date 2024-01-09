import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

email = MIMEMultipart() # 创建邮件主题对象
email['From'] = '846425789@qq.com'
email['To'] = '2723281723@qq.com'
email['Subject'] =Header('email_test', 'utf-8')
content = '''hello world！！！'''
email.attach(MIMEText(content, 'plain', 'utf-8'))

smtp_obj = smtplib.SMTP_SSL('smtp.qq.com', 465) # 创建SMTP_SSL对象（连接邮件服务器）
smtp_obj.login('846425789@qq.com', 'lutoqkqipscxbchg')
smtp_obj.sendmail(
    '846425789@qq.com',
    '2723281723@qq.com',
    email.as_string()
)