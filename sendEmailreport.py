import smtplib
from email.mime.text import MIMEText
import os

#send resultreport to email

file = os.path.abspath(os.curdir) + '/report.html'

class SendEmail():



    def sendReportmail(self, file):

        server_host = 'smtp.163.com'
        header='ynoteios appium testing result'
        to='*@163.com'
        frome='*@163.com'

        with open(file, 'rb')as f:
            mail_body = f.read()

        msg = MIMEText(mail_body, 'html', 'utf-8')

        msg['subject'] = header

        msg['to'] = to

        msg['from'] = frome

        s = smtplib.SMTP()
        s.connect(server_host)
        s.ehlo()
        s.login('*@163.com','***')

        s.sendmail(msg['from'], msg['to'], msg.as_string())
        print 'send email sucess!'

if __name__ =='__main__':

    OO=SendEmail()
    OO.sendReportmail(file)




