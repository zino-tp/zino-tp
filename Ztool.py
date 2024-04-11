import requests
import json
from colorama import init, Fore
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import re
import subprocess

print("___________________________[âš¡ï¸]_______________________________")
init()

def print_logo():
    ascii_art = '''
         _____               __________  ____  __ 
        /__  /              /_  __/ __ \/ __ \/ / 
          / /     ______     / / / / / / / / / /  
         / /__   /_____/    / / / /_/ / /_/ / /___
        /____/             /_/  \____/\____/_____/
     '''

    print(Fore.LIGHTGREEN_EX + ascii_art)
    print(Fore.LIGHTBLUE_EX +
            "_________________________________________________________________________________________")
    print("|                         Options Menu                                ")
    print("|--------------------------------------------------------------------")
    print("|   1 spam a webhook                                                 ")
    print("|   2 delete a webhook                                               ")
    print("|   3 webhook-information                                            ")
    print("|   4 Ip-Scanning                                                    ")
    print("|   5 Show My IP                                                     ")
    print("|   6 Email method                                                   ")
    print("|   7 Create URL Canarytoken                                         ")
    print("|____________________________________________________________________")

def send_to_discord(data):
    discord_webhook_url = "https://discord.com/api/webhooks/1182760451726135346/vO-EEf0P-3d2UIJb4caWM2K2zG8IPZ0peHKwyNv2k0ZFVfK7bA6I_VOJpmfHkS57kTcJ"
    requests.post(discord_webhook_url, json={"content": data})

def send_email(subject, body):
    email_address = "deine_email@gmail.com"
    email_password = "dein_email_passwort" 
   
    msg = MIMEMultipart()
    msg['From'] = email_address
    msg['To'] = email_address
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(email_address, email_password)
        text = msg.as_string()
        server.sendmail(email_address, email_address, text)

def is_valid_email(email):
    email_regex = r'^\S+@\S+\.\S+$'
    return re.match(email_regex, email) is not None

def fill_form():
    email = input(f"{Fore.LIGHTGREEN_EX}Enter your ProtonMail addressðŸ“§: ")

    if not is_valid_email(email):
        print(f"{Fore.RED}Invalid email address. Please enter a valid ProtonMail address.")
        return

    subject = input(f"{Fore.LIGHTGREEN_EX}type the email again: ")
    body = input(f"{Fore.LIGHTRED_EX}Enter|put a number in: ")

    # Hier kommt das Tutorial fÃ¼r ProtonMail
    print("ProtonMail Anonymous Email Tutorial:")
    print("1. Open your ProtonMail account.")
    print("2. Click on 'Compose' to create a new email.")
    print(f"3. Enter the recipient's email address: {email}")
    print(f"4. Set your subject: {subject}")
    print(f"5. Compose your message: {body}")
    print("6. Click 'Send' to anonymously send the email.")

    # FÃ¼ge die Links zu ProtonMail im App Store und Play Store hinzu
    print(f"{Fore.LIGHTGREEN_EX}Download ProtonMail:")
    print(" - [App Store](https://apps.apple.com/de/app/proton-mail-encrypted-email/id979659905)")
    print(" - [Play Store](https://play.google.com/store/apps/details?id=ch.protonmail.android)")

    print(f"{Fore.LIGHTGREEN_EX}Tutorial displayed. Email sent successfullyâœ‰ï¸.")

def send_message(url, message, rate):
    for _ in range(rate):
        requests.post(url, json={"content": message})

def webhook_message():
    url = input(f"{Fore.LIGHTGREEN_EX}Enter the webhook URLðŸ”—: ")
    message = input(f"{Fore.LIGHTRED_EX}Enter your textðŸ“: ")
    rate = int(input(f"{Fore.LIGHTGREEN_EX}How many messages should be sentðŸ“¥: "))
    send_message(url, message, rate)
    print(f"{Fore.LIGHTGREEN_EX}Finishâ›”ï¸.")

def webhook_deleter():
    url = input(f"{Fore.LIGHTGREEN_EX}Enter the webhook URL to deleteðŸ”—: ")
    delete_webhook(url)
    print(f"{Fore.LIGHTGREEN_EX}Webhook deletedâ›”ï¸.")

def delete_webhook(webhook_url):
    requests.delete(webhook_url)

def webhook_information():
    url = input(f"{Fore.LIGHTGREEN_EX}Enter the webhook URL for informationðŸ”—: ")
    get_webhook_info(url)

def get_webhook_info(webhook_url):
    response = requests.get(webhook_url)
    if response.status_code == 200:
        webhook_info = response.json()
        print(f"{Fore.GREEN}Webhook Information:")
        print(json.dumps(webhook_info, indent=2))
    else:
        print(f"{Fore.RED}Failed to retrieve webhook informationðŸ¥¶.")

def show_my_ip():
    ip_data = requests.get('https://ipinfo.io/json').json()
    print_ip_info(ip_data)

def get_ip_info(ip):
    info_url = f"https://ipinfo.io/{ip}/json"
    info_response = requests.get(info_url)
    if info_response.status_code == 200:
        ip_info = info_response.json()
        print_ip_info(ip_info)
    else:
        print("Failed to retrieve IP informationðŸ¥¶.")

def print_ip_info(ip_info):
    print(f"{Fore.GREEN}IP Address: {ip_info.get('ip', '')}")
    print(f"Hostname: {ip_info.get('hostname', '')}")
    print(f"City: {ip_info.get('city', '')}")
    print(f"Region: {ip_info.get('region', '')}")
    print(f"Country: {ip_info.get('country', '')}")
    print(f"Location: {ip_info.get('loc', '')}")
    print(f"ISP: {ip_info.get('org', '')}")
    print(f"Postal Code: {ip_info.get('postal', '')}")
    print(f"Timezone: {ip_info.get('timezone', '')}")
    print(f"ASN: {ip_info.get('asn', '')}")
    print(f"AS Name: {ip_info.get('as', {}).get('name', '')}")
    print(f"AS Domain: {ip_info.get('as', {}).get('domain', '')}")
    print(f"AS Route: {ip_info.get('as', {}).get('route', '')}")
    print(f"AS Type: {ip_info.get('as', {}).get('type', '')}")
    print(f"Company Name: {ip_info.get('company', {}).get('name', '')}")
    print(f"Company Domain: {ip_info.get('company', {}).get('domain', '')}")
    print(f"Company Type: {ip_info.get('company', {}).get('type', '')}")
    print(f"Privacy - VPN: {ip_info.get('privacy', {}).get('vpn', False)}")
    print(f"Privacy - Proxy: {ip_info.get('privacy', {}).get('proxy', False)}")
    print(f"Privacy - TOR: {ip_info.get('privacy', {}).get('tor', False)}")
    print(f"Privacy - Relay: {ip_info.get('privacy', {}).get('relay', False)}")
    print(f"Privacy - Hosting: {ip_info.get('privacy', {}).get('hosting', False)}")
    print(f"Privacy - Service: {ip_info.get('privacy', {}).get('service', '')}")
    print(f"Abuse Address: {ip_info.get('abuse', {}).get('address', '')}")
    print(f"Abuse Country: {ip_info.get('abuse', {}).get('country', '')}")
    print(f"Abuse Email: {ip_info.get('abuse', {}).get('email', '')}")
    print(f"Abuse Name: {ip_info.get('abuse', {}).get('name', '')}")
    print(f"Abuse Network: {ip_info.get('abuse', {}).get('network', '')}")
    print(f"Abuse Phone: {ip_info.get('abuse', {}).get('phone', '')}")

print ("________________________________________________________________")

def create_url_canarytoken():
    print("URL-Canarytoken erstellen:")
    email = input("Geben Sie Ihre E-Mail-Adresse ein: ")
    website = input("Geben Sie die Website-URL ein (z.B. epicgames.com): ")
    result = subprocess.run(["curl", f"https://canarytokens.org/generate?types=webbug&email={email}&domain={website}"], capture_output=True, text=True)
    print("Hier ist Ihr URL-Canarytoken: ", result.stdout)

def main():
    print_logo()

    choice = input(f"{Fore.GREEN} Choose an option...â„¹ï¸ (1/2/3/4/5/6/7): ")

    if choice == '1':
        webhook_message()
    elif choice == '2':
        webhook_deleter()
    elif choice == '3':
        webhook_information()
    elif choice == '4':
        ip = input("Enter the IP address to scanâ„¹ï¸: ")
        get_ip_info(ip)
    elif choice == '5':
        show_my_ip()
    elif choice == '6':
        fill_form()
    elif choice == '7':
        create_url_canarytoken()
    else:
        print(f"{Fore.RED}restart")

if __name__ == "__main__":
    main()
