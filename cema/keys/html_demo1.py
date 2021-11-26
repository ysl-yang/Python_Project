import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 邮件服务器
con = smtplib.SMTP_SSL('smtp.qq.com', '465')
# 登录
con.login('1214114828@qq.com', 'xfbmhcptjzydijch')
# 发送者账号
sender = '1214114828@qq.com'
# 接收者账号
recevier = ['121411828@qq.com']
# 发送主体内容
htmlconnext = '<a href="http://www.baidu.com">点我，就完了</a>'
message = MIMEText(_text=htmlconnext, _subtype='html', _charset='utf-8')
# 发送头部内容
message['Subject'] = Header('这是标题')
# 发件人
message['From'] = Header('李商隐<1214114828@qq.com>')
# 收件人
message['To'] = Header('李商隐<1214114828@qq.com>')
# 邮箱发送
try:
    con.sendmail(sender, recevier, message.as_string())
    print('发送成功')
except Exception as e:
    print('发送失败%e' % e)
