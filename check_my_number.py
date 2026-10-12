#!/usr/bin/env python3
"""
Check WhatsApp and Telegram registration for YOUR phone number.
Uses direct HTTP requests (works perfectly on Termux ARMv7).
ONLY USE ON YOUR OWN NUMBER.
"""

import requests
from bs4 import BeautifulSoup

# ============================================================
# 🔴 YOUR NUMBER (Country code + number, NO plus sign)
# ============================================================
PHONE_NUMBER = "2348080502945"   # <-- CHANGE THIS TO YOUR NUMBER

def check_whatsapp(number):
    print("\n" + "="*60)
    print("🔍 CHECKING WHATSAPP")
    print("="*60)
    url = f"https://wa.me/{number}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    try:
        response = requests.get(url, headers=headers, timeout=15, allow_redirects=True)
        if response.status_code == 200:
            if "Chat on WhatsApp" in response.text or "whatsapp" in response.text.lower():
                print(f"✅ WhatsApp: REGISTERED (+{number})")
            else:
                print(f"❌ WhatsApp: NOT REGISTERED or private")
        else:
            print(f"❌ WhatsApp: Could not verify (HTTP {response.status_code})")
    except Exception as e:
        print(f"❌ WhatsApp check failed: {e}")

def check_telegram(number):
    print("\n" + "="*60)
    print("🔍 CHECKING TELEGRAM")
    print("="*60)
    url = f"https://t.me/+{number}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    try:
        response = requests.get(url, headers=headers, timeout=15, allow_redirects=True)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            # Telegram shows the user's name if registered, or a generic join page
            title_tag = soup.find("meta", property="og:title")
            if title_tag and "Telegram" not in title_tag.get("content", ""):
                name = title_tag.get("content")
                print(f"✅ Telegram: REGISTERED (Name: {name})")
            else:
                print(f"❌ Telegram: NOT REGISTERED or hidden by privacy settings")
        else:
            print(f"❌ Telegram: Could not verify (HTTP {response.status_code})")
    except Exception as e:
        print(f"❌ Telegram check failed: {e}")

if __name__ == "__main__":
    if PHONE_NUMBER == "2348080502946":
        print("⚠️  Please edit the script and replace PHONE_NUMBER with your own number.")
        sys.exit(1)

    print(f"🔎 Checking registrations for: +{PHONE_NUMBER}")
    print("   (Only proceed if this is YOUR OWN number.)\n")

    check_whatsapp(PHONE_NUMBER)
    check_telegram(PHONE_NUMBER)

    print("\n" + "="*60)
    print("✅ Done. Review the results above.")
    print("="*60)