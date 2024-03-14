'''
This code removes spam. and keeps itself "autoupdated". It ignores SEEN emails. Doesn't work with Gmail. You need some API permissions for those

option = 1
Reads unseen emails. It removes everything which contains forbidden words, everything with same body or from same sender. And flags them as spammers.
Once Somebody is flagged as spammer, all his messages will be deleted.
So if Mr. Spammer send you an email his first will be kept, rest of his emails from all your acounts will be deleted. Just keep first mail as UNREAD. 
Also stores content of mails in pickle

option = 2
Prints stored mails. You can read your spam if you want without actually opening your emails. If you see important message, login to your account and mark it as READ

option = 3
If you want to block korean, russian, chinesse... language, just add their spam into 'foo' variable and it will tell you which characters occured most.
Then add those characters into 'forbidden_words'
'''

import imaplib
import email
import pickle
import datetime
import re

users_dic = {
    # 'MAIL': ('PASSWORD', 'imap.SERVER.XX'),
    # 'MAIL': ('PASSWORD', 'imap.SERVER.XX'),
}
imap_ssl_port = 993

pth = '/PATH/TO/YOUR/FOLDER/'  # Has to be defined because of debug bug


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
    'casino', 'online casios', ' porn ', ' dating ', 'online slot ', 'cialis', 'captcha', ' exclusive ',
    'akartam tudni az árát', 'eisiau gwybod eich pris', 'makemake wau', 'hello. and bye.',
    'ვ', 'ნ', 'и', 'п', 'л', 'ш', 'д', 'ь', '=?UTF-8?B?', '라', '어', '에', '원', '고', '기', '는', '다',
    'growth service, which increases', 'rebuild or revamp ', 'backlink', 'marketing', ' seo ', ' loan ',
    '.ru>', '.ru/', '.ru ', '.xyz', 'si=c4=99', 
]
#  '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
forbidden_servers = [
    'mail.ru', 'yandex.ru', 'bk.ru', 'rambler.ru', 'list.ru', 'arenaigr.ru',
    'course-fitness.com', 
    '.xyz', '.fun',
]



def delete_trash_messages(usr, passwd, imap_ssl_host):
    # Get emails
    global message_list
    global from_list
    global from_list_mail
    global spammer_dict

    spammer_list = list(spammer_dict.keys())
    mail_and_server_list = []
    for user in users_dic:
        mail_and_server_list.append(user)
        mail_and_server_list.append(user.split('@')[1])
    
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
        from_str2 = re.search(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", from_str).group()
        from_user = from_str2.split('@')
        from_user[0] = from_user[0].replace('.', '')
        from_user[0] = from_user[0].lower()
        from_user[0] = from_user[0].split('+')[0]
        from_str2 = '@'.join(from_user)

        # mark as read
        # if any('wordpress@' + x == from_str2 for x in mail_and_server_list):
        if any(x in from_str2 for x in mail_and_server_list):            
            status, data = mail.fetch(num, '(RFC822)')
            continue

        msg_body = email_message.get_payload()
        msg_body = msg_body.replace('\n', '')
        msg_body = msg_body.replace('\r', '')
        msg_body = msg_body.strip()
        msg_body2 = msg_body.lower()
        for m_a_s in mail_and_server_list:
            msg_body2 = msg_body2.replace(m_a_s, '')

        # print('Body:', msg_body)
        # print()

        msg_deleted = False
        if any(from_str2.endswith(x) for x in forbidden_servers):
            print('From:', from_str, '\nSubject:', email_message['Subject'], )  # print('Date:', email_message['Date'])
            print('-------- DELETED: Forbidden Server----------')
            mail.store(num, '+FLAGS', '\\Deleted')
            msg_deleted = True     
        elif from_str2 in spammer_list:
            print('From:', from_str, '\nSubject:', email_message['Subject'], )  # print('Date:', email_message['Date'])
            print('-------- DELETED: Known Spammer ----------')
            mail.store(num, '+FLAGS', '\\Deleted')
            msg_deleted = True       
        elif any(x in msg_body2 for x in forbidden_words):
            print('From:', from_str, '\nSubject:', email_message['Subject'], '\nBody:', msg_body)  # print('Date:', email_message['Date'])
            print('-------- DELETED: Forbidden Word ---------')
            mail.store(num, '+FLAGS', '\\Deleted')
            msg_deleted = True
        elif any(x in from_str for x in forbidden_words):
            print('From:', from_str, '\nSubject:', email_message['Subject'], '\nBody:', msg_body)  # print('Date:', email_message['Date'])
            print('------ DELETED: FROM Forbidden Word ------')
            mail.store(num, '+FLAGS', '\\Deleted')    
            msg_deleted = True
        elif msg_body2 in message_list:
            print('From:', from_str, '\nSubject:', email_message['Subject'], '\nBody:', msg_body)  # print('Date:', email_message['Date'])
            print('-------- DELETED: Same message ----------')
            mail.store(num, '+FLAGS', '\\Deleted')
            msg_deleted = True
        elif email_message['From'] in from_list:
            print('From:', from_str, '\nSubject:', email_message['Subject'], '\nBody:', msg_body)  # print('Date:', email_message['Date'])
            print('-------- DELETED: Same Author ----------')
            mail.store(num, '+FLAGS', '\\Deleted')
            msg_deleted = True
        elif from_str2 in from_list_mail:
            print('From:', from_str, '\nSubject:', email_message['Subject'], '\nBody:', msg_body)  # print('Date:', email_message['Date'])
            print('-------- DELETED: Same Author Mail ----------')
            mail.store(num, '+FLAGS', '\\Deleted')
            msg_deleted = True
        elif msg_body.count('http') > 2 and 'WordPress' not in msg_body:
            print('From:', from_str, '\nSubject:', email_message['Subject'], '\nBody:', msg_body)  # print('Date:', email_message['Date'])
            print('-------- DELETED: 3+links ----------')
            mail.store(num, '+FLAGS', '\\Deleted')
            msg_deleted = True
        else:
            message_list.append(msg_body2)
            from_list.append(from_str)
            from_list_mail.append(from_str2)
        if msg_deleted:
            if from_str2 not in spammer_dict:
                spammer_dict[from_str2] = [datetime.datetime.date(datetime.datetime.today()), 1]
                spammer_list.append(from_str2)
            else:
                spammer_dict[from_str2][0] = datetime.datetime.date(datetime.datetime.today())
                spammer_dict[from_str2][1] += 1
        print()
        # mail.expunge()

    save_pickle('message_list', message_list)
    save_pickle('from_list', from_list)
    save_pickle('from_list_mail', from_list_mail)
    save_pickle('spammer_dict', spammer_dict)
    
    # Close the connection
    mail.close()
    mail.logout()


option = 1
if option == 1:
    # message_list = load_pickle('message_list')
    message_list = []
    from_list = []
    from_list_mail = []
    spammer_dict = load_pickle('spammer_dict')
    
    for usernm in users_dic:
        delete_trash_messages(usernm, users_dic[usernm][0], users_dic[usernm][1])

elif option == 2:
    message_list = load_pickle('message_list')
    from_list = load_pickle('from_list')
    spammer_dict = load_pickle('spammer_dict')
    word_count = {}
    print('-----------Messages-------------')
    for mssg in message_list:
        print(mssg, '\n\n')
        words = mssg.replace('.', '')
        words = words.replace('\\', '')
        words = words.replace(',', '')
        words = words.replace(':', '')
        words = words.split(' ')
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
    print('-----------Senders-------------')
    for frm in from_list:
        # print(frm, '\n')
        pass
    print('-----------Spammers-------------')
    for spammer in spammer_dict:
        print(spammer, spammer_dict[spammer])
    word_list = []
    for word in word_count:
        if word_count[word] > 3 and word not in ['', '', '', 'a', 'about', 'all', 'am', 'an', 'and', 'are', 'as', 'at', 'be', 'can', 'do', 'every', 'for', 'from', 'frоm', 'get', 'have', 'hi', 'i', 'if', 'in', 'is', 'it', 'me', 'my', 'not', 'nоt', 'of', 'on', 'or', 'our', 'so', 'that', 'the', 'they', 'this', 'thе', 'to', 'us', 'want', 'was', 'we', 'what', 'where', 'with', 'would', 'wе', 'you', 'your', 'а', 'аm', 'аnd']:    
            word_list.append([word_count[word], word])
    word_list.sort(reverse=True)
    for i in range(len(word_list)):
        print(word_list[i])
        
elif option == 3:
    # spam servers
    spammer_dict = load_pickle('spammer_dict')
    server_dict = {}
    for spammer in spammer_dict:
        spammer = spammer.split('@')[1]
        if spammer not in server_dict:
            server_dict[spammer] = 1
        else:
            server_dict[spammer] += 1
    for serv in server_dict:
        print(serv, server_dict[serv])
       

elif option == 4:
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

# Connect to the IMAP server
imap_server = imapclient.IMAPClient('imap.XXXXXX.XX:993')

# Authenticate with your email credentials
imap_server.login(user, password)

# List mailbox folders
folders = imap_server.list_folders()

print(folders)


exit()


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
