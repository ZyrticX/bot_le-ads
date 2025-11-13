# 🤖 Telegram Leads Bot

A professional Telegram bot for managing lead deals with Airtable CRM integration.

---

## ✨ Features

- ✅ **Create deals** directly from Telegram messages
- ✅ **Manage clients & suppliers** - centralized contact database
- ✅ **Record payments** - track cash flow
- ✅ **Automatic profit calculation** - price per lead, total profit
- ✅ **Real-time statistics** - instant reports
- ✅ **Airtable sync** - all data stored in cloud CRM
- ✅ **Full English support** - interface and messages

---

## 📦 Requirements

- **Python 3.9+** (Python 3.11.9 recommended)
- **Telegram Bot Token** (from @BotFather)
- **Airtable Account** (free tier works)
- **Airtable API Key** and **Base ID**

---

## 🚀 Quick Setup (15 minutes)

### Step 1: Create Telegram Bot (2 min)

1. Open [@BotFather](https://t.me/BotFather) in Telegram
2. Send: `/newbot`
3. Choose name and username
4. **Save the Token!**

### Step 2: Setup Airtable (10 min)

1. Go to [airtable.com](https://airtable.com)
2. Create new Base: `Leads CRM`
3. Create 3 tables with these exact names:

#### Table 1: **Deals**
| Field Name | Type | Notes |
|------------|------|-------|
| Client | Single line text | Client name |
| Supplier | Single line text | Supplier name |
| Quantity | Number | Number of leads |
| Country | Single line text | Target country |
| Delivery Date | Date | Delivery date |
| Buy Price | Currency | Buy price per unit |
| Sell Price | Currency | Sell price per unit |
| Profit | Formula | `({Sell Price} - {Buy Price}) * {Quantity}` |
| Price Per Lead | Currency | Average price per lead |
| Deal Type | Single select | **Buy/Sell** (English!) |
| Raw Text | Long text | Original message text |
| Telegram User | Single line text | Username |
| Telegram Group | Single line text | Group name |
| Status | Single select | **Active/Completed/Cancelled** (English!) |
| Created Date | Date | Creation date |

#### Table 2: **Clients**
| Field Name | Type | Notes |
|------------|------|-------|
| Name | Single line text | Client/Supplier name |
| Type | Single select | **Client/Supplier** (English!) |
| Telegram User | Single line text | Who added |
| Added Date | Date | Date added |
| Total Deals | Number | Total deals count |
| Total Revenue | Currency | Total revenue |

#### Table 3: **Payments**
| Field Name | Type | Notes |
|------------|------|-------|
| Deal ID | Single line text | Deal ID |
| Amount | Currency | Payment amount |
| Payment Date | Date | Payment date |
| Telegram User | Single line text | Who recorded |
| Type | Single select | **Received/Paid** (English!) |

4. Get **API Key**: Account → API → Generate API key
5. Get **Base ID**: https://airtable.com/api → Select your base → Copy `appXXXXXXXX`

**⚠️ IMPORTANT:** Single select field options MUST be in English!
- Status: Active/Completed/Cancelled
- Deal Type: Buy/Sell
- Type (Clients): Client/Supplier
- Type (Payments): Received/Paid

### Step 3: Install Bot (3 min)

#### Option A: Automatic (Windows)
```powershell
.\setup_windows.ps1
```

#### Option B: Manual
```bash
# Create virtual environment
python -m venv venv

# Activate it
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Step 4: Configure Environment

Edit `.env` file:
```env
TELEGRAM_BOT_TOKEN=your_bot_token_here
AIRTABLE_API_KEY=your_airtable_api_key_here
AIRTABLE_BASE_ID=your_airtable_base_id_here
```

### Step 5: Run!

```bash
python bot.py
```

You should see:
```
🚀 Bot is starting...
```

---

## 🎮 Usage

### Create a Deal

1. In Telegram group/chat, someone writes:
```
20 leads Italy next Monday
```

2. Reply to that message with:
```
/newdeal
```

3. Bot asks: Buy or Sell?
   - Select: **💰 Sell (I'm selling)**

4. Send deal details:
```
Client: John Doe
Supplier: Mario Italy
Quantity: 20
Country: Italy
Date: 2025-11-15
Buy Price: 5
Sell Price: 8
```

5. Bot confirms:
```
✅ Deal added successfully!
💚 Profit: $60
🔗 Added to Airtable CRM
```

### Add Client/Supplier

```
/newclient
```
- Select: **👤 Client** or **📦 Supplier**
- Enter name

### Record Payment

```
/payment
```
- Select deal from list
- Enter amount received

### View All Deals

```
/deals
```

### View Clients List

```
/clients
```

### View Statistics

```
/stats
```
Shows:
- Total deals
- Total profit
- Total leads
- Average profit per deal
- Average price per lead

---

## 📋 Commands

| Command | Description |
|---------|-------------|
| `/start` | Show main menu |
| `/newdeal` | Create new deal (Reply to message) |
| `/newclient` | Add new client/supplier |
| `/payment` | Record payment |
| `/deals` | View all deals |
| `/clients` | List all clients |
| `/stats` | Show statistics |
| `/cancel` | Cancel current operation |

---

## 🌐 Deployment (24/7)

### Option 1: Railway.app (Recommended, Free)

1. Push code to GitHub
2. Connect Railway to GitHub
3. Add environment variables
4. Deploy!

### Option 2: VPS (Ubuntu Server)

```bash
# Install Python
sudo apt update
sudo apt install python3 python3-pip python3-venv

# Upload files
git clone your-repo.git
cd telegram-leads-bot

# Install
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Configure
nano .env

# Run as service
sudo cp telegram-bot.service /etc/systemd/system/
sudo systemctl enable telegram-bot
sudo systemctl start telegram-bot
```

See `DEPLOYMENT.md` for full instructions.

---

## 🛠️ Troubleshooting

### Bot doesn't respond
- Check bot is running: `python bot.py`
- Verify Token in `.env`
- Test Token: `curl https://api.telegram.org/bot<TOKEN>/getMe`

### "Missing AIRTABLE_API_KEY" error
- Check `.env` file exists
- Verify no extra spaces in values
- Ensure environment variables are loaded

### "Table not found" error
- Table names must be: `Deals`, `Clients`, `Payments` (English!)
- Check spelling and capitalization

### Bot saves wrong Status/Type values
- **Update Airtable field options to English!**
- See `IMPORTANT_CHANGES.md` for details

---

## 📁 Project Structure

```
telegram-leads-bot/
├── bot.py                    # Main bot code
├── airtable_manager.py       # Airtable API manager
├── requirements.txt          # Python dependencies
├── .env                      # Environment variables (create this!)
├── .env.example              # Environment template
├── .gitignore                # Git ignore rules
├── README.md                 # Main README (Hebrew)
├── README_EN.md              # This file
├── IMPORTANT_CHANGES.md      # Language change notes
├── setup_windows.ps1         # Windows setup script
└── telegram-bot.service      # systemd service file (Linux)
```

---

## 💰 Cost

### Free Tier (Perfect for Starting)
- **Telegram Bot:** Free forever
- **Airtable Free:** Free up to 1,200 records
- **Railway.app:** Free up to 500 hours/month
- **Total:** $0/month

### Paid Tier (For Growth)
- **Airtable Plus:** $10/month (50,000 records)
- **VPS (DigitalOcean):** $5-20/month
- **Total:** $15-30/month

---

## 🔐 Security

- ✅ Environment variables stored in `.env` (not in Git)
- ✅ `.gitignore` configured correctly
- ✅ Airtable API encrypted (HTTPS)
- ✅ No passwords in code

**Best Practices:**
- Enable 2FA on Airtable account
- Backup Airtable weekly
- Keep Python packages updated
- Don't share `.env` file!

---

## 🤝 Contributing

This is open source (MIT License). Contributions welcome!

1. Fork the repository
2. Create feature branch
3. Make changes
4. Submit pull request

---

## 📚 Documentation

- `README.md` - Main documentation (Hebrew)
- `QUICKSTART.md` - 5-minute quick start (Hebrew)
- `AIRTABLE_SETUP.md` - Detailed Airtable setup (Hebrew)
- `DEPLOYMENT.md` - Deployment guide (Hebrew)
- `EXAMPLES.md` - 10 usage examples (Hebrew)
- `FEATURES.md` - Future features (Hebrew)
- `TROUBLESHOOTING.md` - Troubleshooting (Hebrew)
- `IMPORTANT_CHANGES.md` - Language change notes (English)

---

## ✅ Quick Test Checklist

After setup:

- [ ] Bot responds to `/start`
- [ ] Can create a new deal
- [ ] Deal appears in Airtable with "Active" status
- [ ] Can add new client
- [ ] Client appears in Airtable with correct Type
- [ ] Can record payment
- [ ] Payment appears in Airtable
- [ ] `/stats` shows correct numbers
- [ ] All messages are in English

---

## 📞 Support

**Having issues?**

1. Check `TROUBLESHOOTING.md`
2. Verify Airtable field options are in English (`IMPORTANT_CHANGES.md`)
3. Check bot logs
4. Verify `.env` configuration

---

## 📝 License

MIT License - Free to use and modify!

---

**Good luck! 🚀**

If everything works, you now have a professional leads management system running on Telegram!

---

**Project Status:** ✅ Production Ready  
**Language:** English  
**Last Updated:** November 13, 2025

