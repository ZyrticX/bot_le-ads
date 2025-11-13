#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test script to verify .env configuration
"""

import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

print("=" * 60)
print("🔍 Testing .env Configuration")
print("=" * 60)
print()

# Check if .env file exists
if os.path.exists('.env'):
    print("✅ .env file found")
else:
    print("❌ .env file NOT found!")
    print("   Create it with: cp .env.example .env")
    exit(1)

print()

# Check each environment variable
variables = {
    'TELEGRAM_BOT_TOKEN': 'Telegram Bot Token',
    'AIRTABLE_API_KEY': 'Airtable API Key',
    'AIRTABLE_BASE_ID': 'Airtable Base ID'
}

all_good = True

for var_name, description in variables.items():
    value = os.getenv(var_name)
    
    if value:
        # Check if it's a placeholder
        if 'your_' in value or 'here' in value:
            print(f"⚠️  {var_name}: Found but contains placeholder")
            print(f"   Current value: {value}")
            print(f"   Please replace with real {description}")
            all_good = False
        else:
            # Mask the value for security
            masked = value[:10] + "..." + value[-5:] if len(value) > 15 else value[:5] + "..."
            print(f"✅ {var_name}: {masked}")
    else:
        print(f"❌ {var_name}: NOT SET!")
        print(f"   Add this to your .env file")
        all_good = False
    
    print()

print("=" * 60)

if all_good:
    print("✅ All environment variables are configured!")
    print("   You can now run: python bot.py")
else:
    print("❌ Some variables are missing or need to be updated")
    print()
    print("📝 Edit your .env file:")
    print("   nano .env      # Linux")
    print("   notepad .env   # Windows")
    print()
    print("Make sure it looks like this:")
    print()
    print("TELEGRAM_BOT_TOKEN=1234567890:ABCdefGHIjklMNOpqrsTUVwxyz")
    print("AIRTABLE_API_KEY=keyXXXXXXXXXXXXXX")
    print("AIRTABLE_BASE_ID=appXXXXXXXXXXXXXX")

print("=" * 60)

