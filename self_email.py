import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr




def send_email(sender, receiver, password, content):
    # ### 1.邮件内容配置 ###
    
    # ### 2.发送邮件 ###
    server = smtplib.SMTP_SSL("smtp.qq.com", 465)
    server.login(sender, password)
    server.sendmail(sender, receiver, content)
    server.quit()


def notify_runover(text):
    """
    邮件提醒脚本运行完成
    """
    sender_name = 'Achuan-2'
    sender = "achuan-2@foxmail.com"
    receiver = "achuan-2@outlook.com"
    password = "klhknkiyfwfqbjdd"
    # 邮件文本
    # print(text)
    msg = MIMEText(text, 'html', 'utf-8')
    msg['From'] = formataddr([sender_name, sender])
    msg['Subject'] = "脚本运行完成"
    content = msg.as_string()

    send_email(sender, receiver, password, content)


def main():
    notify_runover(__file__)


if __name__ == "__main__":
    main()

