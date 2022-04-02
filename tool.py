import datetime
import os

try:
    from selenium import webdriver
except:
    os.system('pip3 install selenium')
try:
    import chromedriver_autoinstaller
except:
    os.system('pip3 install chromedriver-autoinstaller')
    import chromedriver_autoinstallers

import smtplib
from email.mime.text import MIMEText

chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]  #크롬드라이버 버전 확인

try:
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe')  
except:
    chromedriver_autoinstaller.install(True)
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe')  

driver.implicitly_wait(10)
driver.get('https://www.google.com')

def get_current_url():
    return driver.current_url

def check_target_url(url):
    if url.find('dcinside') != -1:
        idx = url.find('id=')
        if url[idx+3:idx+8] == 'hwhdg':
            return True
        else:
            return False
    else:
        return False

def make_session():
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.ehlo()
    smtp.starttls()
    smtp.login('gshskndl.kr@gmail.com', 'ttwwpjwmgairztad')
    return smtp

def send_email(smtp, email):
    today = datetime.datetime.now()
    current_url = get_current_url()
    title = '타겟 사이트에 접속한 기록 추적'
    content = f'{today.strftime("%Y-%m-%d %H:%M:%S")}에 {current_url}에 접속하였습니다.'
    msg = MIMEText(content)
    msg['Subject'] = title
    msg['To'] = email
    smtp.sendmail('gshskndl.kr@gmail.com', email, msg.as_string())