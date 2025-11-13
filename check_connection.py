#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Check server connectivity to Telegram API
"""

import os
import socket
import requests
from dotenv import load_dotenv

# Load .env
load_dotenv()

print("=" * 60)
print("🌐 Testing Server Connectivity to Telegram")
print("=" * 60)
print()

# Test 1: DNS Resolution
print("1️⃣ Testing DNS Resolution...")
try:
    ip = socket.gethostbyname("api.telegram.org")
    print(f"✅ DNS OK: api.telegram.org → {ip}")
except Exception as e:
    print(f"❌ DNS Failed: {e}")
    print("   Try: sudo systemctl restart systemd-resolved")
print()

# Test 2: Internet Connection
print("2️⃣ Testing Internet Connection...")
try:
    response = requests.get("https://www.google.com", timeout=5)
    print(f"✅ Internet OK: status {response.status_code}")
except Exception as e:
    print(f"❌ Internet Failed: {e}")
print()

# Test 3: Telegram API Reachability
print("3️⃣ Testing Telegram API...")
try:
    response = requests.get("https://api.telegram.org", timeout=10)
    print(f"✅ Telegram API Reachable: status {response.status_code}")
except Exception as e:
    print(f"❌ Telegram API Failed: {e}")
    print("   This might be a firewall or network issue")
print()

# Test 4: Bot Token Validation
print("4️⃣ Testing Bot Token...")
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
if TOKEN:
    try:
        response = requests.get(
            f"https://api.telegram.org/bot{TOKEN}/getMe",
            timeout=15
        )
        if response.status_code == 200:
            bot_info = response.json()
            if bot_info.get('ok'):
                print(f"✅ Bot Token Valid!")
                print(f"   Bot Name: {bot_info['result']['first_name']}")
                print(f"   Username: @{bot_info['result']['username']}")
            else:
                print(f"❌ Invalid Token: {bot_info}")
        else:
            print(f"❌ HTTP Error: {response.status_code}")
    except requests.exceptions.Timeout:
        print("❌ Timeout: Cannot reach Telegram API")
        print("   Possible causes:")
        print("   • Firewall blocking")
        print("   • Network restrictions")
        print("   • Need proxy/VPN")
    except Exception as e:
        print(f"❌ Error: {e}")
else:
    print("❌ TELEGRAM_BOT_TOKEN not found in .env")

print()
print("=" * 60)
print("💡 Common Solutions:")
print("=" * 60)
print()
print("If Telegram is blocked in your region:")
print("1. Use a VPN")
print("2. Use a proxy server")
print("3. Use webhook mode with a proxy")
print()
print("Check firewall:")
print("  sudo ufw status")
print("  sudo ufw allow 443/tcp")
print("  sudo ufw allow 80/tcp")
print()
print("Check if running behind a proxy:")
print("  echo $http_proxy")
print("  echo $https_proxy")
print("=" * 60)

