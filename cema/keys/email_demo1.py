# 邮箱
import smtplib
# 邮件文本内容
from email.mime.text import MIMEText
# 邮箱头部
from email.header import Header
# 发送附件
from email.mime.multipart import MIMEMultipart
# 创建邮箱服务器，SMTP_SSL(邮箱链接地址，端口号)
con = smtplib.SMTP_SSL('smtp.qq.com', '465')
# 登录
con.login('1214114828@qq.com', 'xfbmhcptjzydijch')
# 发送者账号
sender = '1214114828@qq.com'
# 接收者账号，列表形式，可以传多个
recevier = ['1214114828@qq.com']
# 邮件内容，_text正文内容，_subtype 文件类型，plain文本，txt\html\base64
message = MIMEText(_text='正文内容', _subtype='plain', _charset='utf-8')
# 设置头部
message['Subject'] = Header('这是标题')
# 发件人
message['From'] = Header('李商隐<1214114828@qq.com>')
# 接收人
message['To'] = Header('李商隐<1214114828@qq.com>')
# 发送邮件，.sendmail发送者、接受者、内容
try:
    con.sendmail(sender, recevier, message.as_string())
    print('发送邮件成功')
except Exception as e:
    print('无法发送邮件%e' % e)
