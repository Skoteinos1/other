'''
This code removes spam. and keeps itself "autoupdated". It ignores SEEN emails. Doesn't work with Gmail. You need some API permissions for those

option = 1
Reads unseen emails. It removes everything which contains forbidden words.
Removes everything with same body, or from same sender. Always keeps first occurance of those.
So if Mr. Spammer send you an email his first will be kept, rest of his emails from all your acounts will be deleted. Just keep first mail as UNREAD. 
Also stores content of mails in pickle

option = 2
Prints stored mails. You can read your spam if you want without actually opening your emails. If you see important message, login to your account and mark it as READ

option = 3
If you want to block korean, russian, chinesse... language, just add their spam into 'foo' variable and it will tell you which characters occured most.
Then add those characters into 'forbidden_words'
'''

import time
import imaplib
import email
import pickle

users_dic = {
    'MAIL': ('PASSWORD', 'imap.SERVER.XX'),
    'MAIL': ('PASSWORD', 'imap.SERVER.XX'),
}
imap_ssl_port = 993

pth = '/home/skoty/Peti/Projects/P39/Email/'  # Has to be defined because of debug bug


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


forbidden_words = [
    'casino',
    'akartam tudni az árát', 'eisiau gwybod eich pris', 'makemake wau', 
    'ვ', 'ნ', 'и', 'п', 'л', 'ш', 'д', 'ь', '=?UTF-8?B?', '라', '어', '에', '원', '고', '기', '는', '다',
    'growth service, which increases',
    '.ru>',
]
#  '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',


def delete_trash_messages(usr, passwd, imap_ssl_host):
    # Get emails
    global message_list
    global from_list
    global from_list_mail
    
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
        from_str = str(email_message['From'])
        from_str2 = from_str.split('<')[1]
        print('From:', from_str)
        print('Subject:', email_message['Subject'])
        # print('Date:', email_message['Date'])
        msg_body = email_message.get_payload()
        msg_body = msg_body.replace('\n', '')
        msg_body = msg_body.replace('\r', '')
        msg_body = msg_body.strip()
        # print('Body:', msg_body)
        # print()

        if any(x in msg_body for x in forbidden_words):
            print('Body:', msg_body)
            print('-------- DELETED: Forbidden Word----------\n\n')
            mail.store(num, '+FLAGS', '\\Deleted')
        elif any(x in from_str for x in forbidden_words):
            print('Body:', msg_body)
            print('-------- DELETED: FROM Forbidden Word----------\n\n')
            mail.store(num, '+FLAGS', '\\Deleted')    
        elif msg_body in message_list:
            print('Body:', msg_body)
            print('-------- DELETED: Same message ----------\n\n')
            mail.store(num, '+FLAGS', '\\Deleted')
        elif email_message['From'] in from_list:
            print('Body:', msg_body)
            print('-------- DELETED: Same Author ----------\n\n')
            mail.store(num, '+FLAGS', '\\Deleted')
        elif from_str2 in from_list_mail:
            print('Body:', msg_body)
            print('-------- DELETED: Same Author Mail ----------\n\n')
            mail.store(num, '+FLAGS', '\\Deleted')
        else:
            message_list.append(msg_body)
            from_list.append(from_str)
            from_list_mail.append(from_str2)
        print()
        # mail.expunge()

    save_pickle('message_list', message_list)
    save_pickle('from_list', from_list)
    save_pickle('from_list_mail', from_list_mail)
    
    # Close the connection
    mail.close()
    mail.logout()


option = 1
if option == 1:
    time.sleep(5)
    # message_list = load_pickle('message_list')
    message_list = []
    from_list = []
    from_list_mail = []

    for usernm in users_dic:
        delete_trash_messages(usernm, users_dic[usernm][0], users_dic[usernm][1])

elif option == 2:
    message_list = load_pickle('message_list')
    from_list = load_pickle('from_list')
    for mssg in message_list:
        print(mssg, '\n\n')

elif option == 3:
    # Creates list of characters in string and sorts them by occurance
    foo = '''
Заказать   парсинг пользователей. 
 
Наш сервис предлагает эффективные решения для парсинга пользователей, подписчиков и аудитории с любого сайта. Спарсить участников, пользователей и подписчиков аккаунтов стало проще и быстрее с нашими инструментами.  Парсинг аудитории с сайта позволяет получить ценную информацию о своих конкурентах, анализировать поведение пользователей и определять целевую аудиторию. Наш сервис позволяет заказать парсинг аккаунтов и спарсить участников различных платформ и социальных сетей. Мы предлагаем надежные и эффективные методы для сбора данных и анализа аудитории. Не упускайте возможности улучшить свой бизнес и оптимизировать маркетинговые стратегии с помощью парсинга аудитории. Парсинг аудитории: лучшие инструменты и методы Парсинг аккаунтов и подписчиков Парсинг аккаунтов и подписчиков позволяет узнать, кто входит в аудиторию конкретного аккаунта в социальных сетях. Это особенно полезно для продвижения товара или услуги через Instagram или Telegram. С помощью специальных инструментов вы можете быстро спарсить участников, подписчиков и пользователей популярных аккаунтов и использовать эту информацию для целевой рекламы. Парсинг аудитории с сайта Парсинг аудитории с сайта - это отличный способ узнать больше о своих клиентах и посетителях. С помощью парсинга можно собрать данные о пользователях, их предпочтениях и поведении на вашем сайте. Зная свою аудиторию, вы сможете оптимизировать содержимое и рекламу на сайте и привлекать больше потенциальных клиентов. Если вы хотите заказать парсинг аудитории, то вам потребуются лучшие инструменты и методы. На данный момент на рынке существует множество программ и сервисов, которые специализируются на сборе и анализе данных о пользователе. Выберите тот, который лучше всего подходит для вашей задачи и начинайте получать полезные сведения о своей аудитории. Парсинг аудитории поможет вам сделать правильные стратегические шаги и увеличить эффективность вашего бизнеса. Парсинг аккаунтов и подписчиков Кроме парсинга аудитории с сайта, также можно провести парсинг аккаунтов и спарсить информацию о их подписчиках. Это полезная функция для тех, кто хочет изучить своих конкурентов или просто узнать о своей целевой аудитории на более глубоком уровне. С помощью инструментов и методов парсинга аккаунтов и подписчиков, вы сможете получить детальные данные о пользователях, их интересах, поведении и взаимодействии с другими аккаунтами. Эта информация поможет вам лучше понять свою аудиторию и принять более эффективные решения в развитии вашего бизнеса. Парсинг аккаунтов и подписчиков также поможет вам найти новых участников для вашего проекта или сообщества. Вы сможете собрать данные о пользователях, которые активно взаимодействуют с аккаунтами, похожими на ваш, и предложить им свои продукты или услуги. Это отличный способ увеличить свою целевую аудиторию и привлечь новых клиентов. Парсинг аккаунтов Для парсинга аккаунтов и получения данных о них и их подписчиках, вы можете воспользоваться специализированными сервисами и программами. Одним из таких сервисов является Парсинг сайтов. С его помощью вы сможете удобно и быстро собрать информацию о аккаунтах и их подписчиках на разных платформах. Парсинг подписчиков Спарсить подписчиков можно не только с аккаунтов в социальных сетях, но и с других платформ, таких как блоги, форумы и интернет-магазины. Парсинг подписчиков позволит вам получить данные о пользователях, которые проявляют интерес к определенным аккаунтам или тематикам, и использовать их для разработки маркетинговых стратегий и привлечения новых клиентов. Сбор данных о пользователях и участниках Парсинг аккаунтов Один из основных видов парсинга аудитории - это парсинг аккаунтов. С его помощью можно получить информацию о пользователях, их именах, дате регистрации, количестве подписчиков и других данных. Парсинг аккаунтов особенно полезен для анализа конкурентов, определения целевой аудитории и разработки маркетинговых стратегий. Парсинг подписчиков и участников Еще один важный аспект парсинга аудитории - это парсинг подписчиков и участников. С помощью этого инструмента можно получить информацию о пользователях, которые подписаны на определенный аккаунт или участвуют в определенном событии или сообществе. Эта информация может быть использована для анализа целевой аудитории, разработки рекламных кампаний и улучшения работы существующих сообществ. Таким образом, парсинг аудитории и сбор данных о пользователях и участниках помогает получить ценную информацию для развития бизнеса, оценки конкурентов и разработки маркетинговых стратегий. Вы можете заказать парсинг аудитории с сайта у опытных специалистов, чтобы получить максимальную пользу от собранных данных о подписчиках и участниках.
    '''

    char_dic = {}
    for i in range(len(foo)):
        if foo[i] in char_dic:
            char_dic[foo[i]] += 1
        else:
            char_dic[foo[i]] = 1
    
    my_lst = []
    for k in char_dic:
        my_lst.append([char_dic[k], k])
    my_lst.sort()
    print(my_lst)

    



'''
CODE WHICH I TESTED

# print(a[0][1].decode("utf-8"))

import time
from itertools import chain
import email
import imaplib
import base64
import os
import re




# if need to restrict mail search.
criteria = {}
uid_max = 0

def search_string(uid_max, criteria):
    c = list(map(lambda t: (t[0], '"'+str(t[1])+'"'), criteria.items())) + [('UID', '%d:*' % (uid_max+1))]
    return '(%s)' % ' '.join(chain(*c))
    # Produce search string in IMAP format:
    #   e.g. (FROM "me@gmail.com" SUBJECT "abcde" BODY "123456789" UID 9999:*)
#Get any attachemt related to the new mail

#Getting the uid_max, only new email are process

#login to the imap
mail = imaplib.IMAP4_SSL(imap_ssl_host)
mail.login(username, password)
#select the folder
mail.select('Inbox')

result, data = mail.uid('SEARCH', None, search_string(uid_max, criteria))
uids = [int(s) for s in data[0].split()]
if uids:
    uid_max = max(uids)
    # Initialize `uid_max`. Any UID less than or equal to `uid_max` will be ignored subsequently.
#Logout before running the while loop
print(uid_max)
mail.logout()


while 1:
    mail = imaplib.IMAP4_SSL(imap_ssl_host)
    mail.login(username, password)
    mail.select('inbox')
    result, data = mail.uid('search', None, search_string(uid_max, criteria))
    uids = [int(s) for s in data[0].split()]

    for uid in uids:
        # Have to check again because Gmail sometimes does not obey UID criterion.
        if uid > uid_max:
            result, data = mail.uid('fetch', str(uid), '(RFC822)')
            for response_part in data:
                if isinstance(response_part, tuple):
                    #message_from_string can also be use here
                    print(email.message_from_bytes(response_part[1])) #processing the email here for whatever
            uid_max = uid
    break
mail.logout()
time.sleep(1)






from aspose.email import SaveOptions, MboxrdStorageReader

# Read the storage file
reader = MboxrdStorageReader("ExampleMbox.mbox", False)

# Read first message
eml = reader.read_next_message()

# Read all messages in a loop
while (eml is not None):
    # Manipulate message - show contents
    print("Subject: " + eml.subject)
    
    # Save this message in EML or MSG format
    eml.save(eml.subject + "_out.eml", SaveOptions.default_eml)
    eml.save(eml.subject + "_out.msg", SaveOptions.default_msg_unicode)

    # Get the next message
    eml = reader.read_next_message()

# Close the streams
reader.dispose()

exit()
import imapclient
import datetime


# Connect to the IMAP server
imap_server = imapclient.IMAPClient('imap.XXXXXX.XX:993')

# Authenticate with your email credentials
imap_server.login(user, password)

# List mailbox folders
folders = imap_server.list_folders()

print(folders)



exit()
# Importing libraries
import imaplib, email
 

 
# Function to get email content part i.e its body part
def get_body(msg):
    if msg.is_multipart():
        return get_body(msg.get_payload(0))
    else:
        return msg.get_payload(None, True)
 
# Function to search for a key value pair 
def search(key, value, con): 
    result, data = con.search(None, key, '"{}"'.format(value))
    return data
 
# Function to get the list of emails under this label
def get_emails(result_bytes):
    msgs = [] # all the email data are pushed inside an array
    for num in result_bytes[0].split():
        typ, data = con.fetch(num, '(RFC822)')
        msgs.append(data)
 
    return msgs
 
# this is done to make SSL connection with GMAIL
con = imaplib.IMAP4_SSL(imap_url) 

# logging the user in
con.login(user, password) 

exit() 
# calling function to check for email under this label
con.select('Inbox') 
 
 # fetching emails from this user "tu**h*****1@gmail.com"
msgs = get_emails(search('FROM', 'no-reply@accounts.google.com', con))
 
# Uncomment this to see what actually comes as data 
print(msgs) 
 
exit()
# Finding the required content from our msgs
# User can make custom changes in this part to
# fetch the required content he / she needs
 
# printing them by the order they are displayed in your gmail 
for msg in msgs[::-1]: 
    for sent in msg:
        if type(sent) is tuple: 
 
            # encoding set as utf-8
            content = str(sent[1], 'utf-8') 
            data = str(content)
 
            # Handling errors related to unicodenecode
            try: 
                indexstart = data.find("ltr")
                data2 = data[indexstart + 5: len(data)]
                indexend = data2.find("</div>")
 
                # printing the required content which we need
                # to extract from our email i.e our body
                print(data2[0: indexend])
 
            except UnicodeEncodeError as e:
                pass




'''

