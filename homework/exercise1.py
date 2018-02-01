from gmail import GMail, Message

html_template = ''' <h1 style="text-align: center;"><span style="color: #ff0000;"><strong>ĐƠN XIN NGHỈ</strong></span></h1>
<p>Em ch&agrave;o anh, h&ocirc;m nay em thức dậy thấy rất đau đầu v&agrave; sốt cao. Em đi kh&aacute;m th&igrave; b&aacute;c sĩ bảo em bị {{sickness}} rồi. Nếu em m&agrave; cố đi l&agrave;m sợ l&acirc;y bệnh cho cả ph&ograve;ng&nbsp;<img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-cry.gif" alt="cry" /></p>
<p>Cho em nghỉ nh&eacute; anh.&nbsp;<img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-kiss.gif" alt="kiss" /></p>
<p>Em c&aacute;m ơn anh ạ&nbsp;<img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-embarassed.gif" alt="embarassed" /></p>'''
sickness_list = ['sot', 'cam cum', 'sida']

from random import choice
i = choice(sickness_list)

html_content = html_template.replace("{{sickness}}", i)

import datetime
current_time = datetime.datetime.now()
time = datetime.datetime(current_time.day, current_time.hour, current_time.minute)
sent_time = datetime.time(19, 46)


gmail = GMail('xuanson.c4e15@gmail.com', '10d180110')
msg = Message('hoi tham',to ='nguyenxuanson1992@gmail.com', html = html_content)
while True:
    if sent_time == time:
        gmail.send(msg)
        break
    else:
        current_time = datetime.datetime.now()
        time = datetime.time(current_time.hour,current_time.minute)
        continue
