import imaplib
import email
import pickle

imap_ssl_host = 'imap.XXXXXXXXXXXX.com'
imap_ssl_port = 993

pth = '/home/XXXXXXXXXX/'  # Has to be defined because of debug bug
def save_pickle(file, data1):
    if '.pkl' not in file:
        file += '.pkl'
    pkl_file = open(pth + file, 'wb')
    pickle.dump(data1, pkl_file)
    pkl_file.close()

def load_pickle(fl_nm):
    if '.pkl' not in fl_nm:
        fl_nm += '.pkl'
    try:
        pkl_file = open(pth + fl_nm, 'rb')
        data1 = pickle.load(pkl_file)
        pkl_file.close()
    except:
        print('Missing pickle table:', fl_nm)
        # pkl_file = open(file, 'wb')
        data1 = ''
    return data1


def delete_trash_messages(usr, passwd):
    # Get emails
    global message_list
    
    # Set up the IMAP connection
    mail = imaplib.IMAP4_SSL(imap_ssl_host)
    mail.login(usr, passwd)
    mail.select('Inbox')

    # Search for all email messages in the inbox
    # status, data = mail.search(None, 'ALL')
    status, data = mail.search(None, 'UNSEEN')

    for num in data[0].split():
        # status, data = mail.fetch(num, '(RFC822)')
        status, data = mail.fetch(num, '(BODY.PEEK[])')
        email_message = email.message_from_bytes(data[0][1])
        print('From:', email_message['From'])
        print('Subject:', email_message['Subject'])
        # print('Date:', email_message['Date'])
        msg_body = email_message.get_payload()
        msg_body = msg_body.replace('\n', '')
        msg_body = msg_body.replace('\r', '')
        msg_body = msg_body.strip()
        # print('Body:', msg_body)
        # print()

        if 'makemake wau' in msg_body:
            print('Body:', msg_body)
            print('-------- MESSAGE DELETED ----------\n\n')
            mail.store(num, '+FLAGS', '\\Deleted')
        elif msg_body in message_list:
            print('Body:', msg_body)
            print('-------- MESSAGE DELETED ----------\n\n')
            mail.store(num, '+FLAGS', '\\Deleted')
        print()
        # mail.expunge()
        message_list.append(msg_body)

    save_pickle('message_list', message_list)
    
    # Close the connection
    mail.close()
    mail.logout()


option = 3
if option == 1:
    # Goes through your email list and removes duplicate messages. DO NOT RUN TWICE, IT WILL DELETE ALL NEW EMAILS
    message_list = load_pickle('message_list')
    users_dic = {
        'EMAIL': 'PASSWORD',
    }

    for usernm in users_dic:
        delete_trash_messages(usernm, users_dic[usernm])

elif option == 2:
    # For Test, it reads messages from saved dictionary
    mail_dict = load_pickle('mail_dict')
    message_list = []
    for num in mail_dict:
        # print(num, mail_dict[num][1], mail_dict[num][0][0][0], '\n', mail_dict[num][0][0][1].decode("utf-8"), '\n\n\n')
        print(num, mail_dict[num][1], mail_dict[num][0][0][0], '\n')
        email_message = email.message_from_bytes(mail_dict[num][0][0][1])
        print('From:', email_message['From'])
        print('Subject:', email_message['Subject'])
        print('Date:', email_message['Date'])
        msg_body = email_message.get_payload()
        msg_body = msg_body.replace('\n', '')
        msg_body = msg_body.replace('\r', '')
        msg_body = msg_body.strip()
        print('Body:', msg_body)
        print('\n\n\n')
    
        message_list.append(msg_body)
        

    print(message_list)
elif option == 3:
    # For Test, prints emails from list
    message_list = load_pickle('message_list')
    for mssg in message_list:
        print(mssg, '\n\n')



# print(a[0][1].decode("utf-8"))




