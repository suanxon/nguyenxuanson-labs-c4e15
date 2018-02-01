from gmail import GMail, Message
from random import choice
import datetime
"c4e.201708@gmail.com"
Mailbox = "nguyenxuanson1992@gmail.com"

html_template = '''<p style="text-align: center;"><strong>Xin nghỉ ốm</strong></p>
<p style="text-align: left;">&nbsp;</p>
<p>Em ch&agrave;o anh,</p>
<p>H&ocirc;m nay em thức dậy thấy rất đau đầu, sốt cao.</p>
<p>Em đi kh&aacute;m, b&aacute;c sĩ chẩn đo&aacute;n bị <em><strong>{{sickness}}</strong></em>.</p>
<p>Cho em nghỉ.</p>
<p>&nbsp;</p>
'''

sickness_list = ['viêm phổi', 'cảm cúm', 'dị ứng']
sickness = choice(sickness_list)

html_content = html_template.replace('{{sickness}}', sickness)

gmail = GMail('dktu.cfailiat@gmail.com', 'Tahy22495')

msg = Message('Xin nghi om', to = Mailbox, html = html_content)

now = datetime.datetime.now()
check_time = datetime.time(now.hour, now.minute)
my_time = datetime.time(19, 38)

# while True:
#        import datetime
#        if datetime.datetime() > my_time:
#             gmail.send(msg)
#             print("Gmail sent successfully!")
#             break
while True:
    if check_time == my_time:
        gmail.send(msg)
        print("Gmail sent successfully!")
        break
    else:
        now = datetime.datetime.now()
        check_time = datetime.time(now.hour, now.minute)
        continue
