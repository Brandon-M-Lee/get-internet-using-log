from tool import get_current_url, check_target_url, make_session, send_email

already_mail_sent = False

while True:
    currnet_url = get_current_url()
    if check_target_url(currnet_url):
        if not already_mail_sent:
            smtp = make_session()
            send_email(smtp, 'gshsdctracker@gmail.com')
            already_mail_sent = True
    else:
        already_mail_sent = False