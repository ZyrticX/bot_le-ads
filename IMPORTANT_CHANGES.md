# ⚠️ IMPORTANT CHANGES - English Version

## What Changed?

All bot messages, interface text, and code comments have been **converted from Hebrew to English**.

---

## 🚨 CRITICAL: Airtable Field Values Must Also Be in English!

Since the bot now uses English text, you **MUST** update your Airtable field values to match.

### Required Changes in Airtable:

#### 1. **Deals Table** - Status Field
Update the "Status" **Single Select** field options:

**Old (Hebrew):**
- פעיל
- הושלם
- בוטל

**New (English):**
- Active
- Completed
- Cancelled

#### 2. **Deals Table** - Deal Type Field
Update the "Deal Type" **Single Select** field options:

**Old (Hebrew):**
- קנייה
- מכירה

**New (English):**
- Buy
- Sell

#### 3. **Clients Table** - Type Field
Update the "Type" **Single Select** field options:

**Old (Hebrew):**
- לקוח
- ספק

**New (English):**
- Client
- Supplier

#### 4. **Payments Table** - Type Field
Update the "Type" **Single Select** field options:

**Old (Hebrew):**
- התקבל
- שולם

**New (English):**
- Received
- Paid

---

## 📝 How to Update Airtable Field Options

For each field mentioned above:

1. Open your Airtable Base
2. Click on the field header (e.g., "Status")
3. Click "Customize field type"
4. Under "Options", **delete the old Hebrew options**
5. Add the new English options
6. Click "Save"

**Example for Status field:**

```
Before:
✓ פעיל
✓ הושלם
✓ בוטל

After:
✓ Active
✓ Completed
✓ Cancelled
```

---

## 🔄 Bot Behavior Changes

### Command Messages (Now in English)

**`/start` command:**
```
👋 Hello FirstName!

🤖 Welcome to Leads Management Bot

📋 **Available Commands:**

/newdeal - Create new deal (Reply to a message)
/newclient - Add new client/supplier
/payment - Record payment
/deals - View all deals
/clients - List clients
/stats - Statistics
```

**`/newdeal` - Deal Type Selection:**
```
🛒 Buy (I'm buying)
💰 Sell (I'm selling)
```

**Deal Details Format:**
```
Client: Client name
Supplier: Supplier name (if relevant)
Quantity: 20
Country: Italy
Date: 2025-11-04
Buy Price: 100
Sell Price: 150
```

**`/newclient` - Type Selection:**
```
👤 Client
📦 Supplier
```

**All success/error messages are now in English**

---

## 🧪 Testing After Changes

After updating Airtable field options, test the bot:

### Test 1: Create a new deal
```
1. Send a message in Telegram: "20 leads Italy"
2. Reply with /newdeal
3. Select "Sell"
4. Send deal details in English format
5. Check Airtable - Status should show "Active"
```

### Test 2: Add a new client
```
1. Send /newclient
2. Select "Client"
3. Enter client name
4. Check Airtable - Type should show "Client"
```

### Test 3: View statistics
```
1. Send /stats
2. All labels should be in English
```

---

## 📊 Data Migration (If You Have Existing Data)

If you already have data in Airtable with Hebrew values:

### Option 1: Manual Update (Small dataset)
1. Open Airtable
2. For each record, change field values manually to English

### Option 2: Formula/Automation (Larger dataset)
Create a formula field to convert:

```javascript
// For Status field
SWITCH(
  {Status},
  "פעיל", "Active",
  "הושלם", "Completed",
  "בוטל", "Cancelled",
  {Status}
)
```

Then copy the formula results and paste as values.

### Option 3: Fresh Start
- Export existing data
- Delete all records
- Update field options to English
- Re-import data with English values

---

## 🔍 What Stays the Same

### Table Names (Keep in English)
- ✅ Deals
- ✅ Clients
- ✅ Payments

### Field Names (Keep in English)
- ✅ Client, Supplier, Quantity, Country, etc.
- These are already in English, no changes needed!

### Commands
- ✅ `/start`, `/newdeal`, `/newclient`, `/payment`, `/deals`, `/clients`, `/stats`
- Commands remain the same

---

## ❓ Common Questions

**Q: Will my existing deals still work?**
A: Only if you update the Status/Type values to English in Airtable

**Q: Can I keep Hebrew data?**
A: No, the bot expects English values now (Active, Client, etc.)

**Q: Do I need to recreate my Airtable Base?**
A: No, just update the field options as described above

**Q: What if I forget to update Airtable?**
A: The bot will still work, but you might see unexpected values in some fields

---

## ✅ Summary Checklist

Before using the bot:

- [ ] Updated "Status" field options in Deals table (Active/Completed/Cancelled)
- [ ] Updated "Deal Type" field options in Deals table (Buy/Sell)
- [ ] Updated "Type" field options in Clients table (Client/Supplier)
- [ ] Updated "Type" field options in Payments table (Received/Paid)
- [ ] Tested creating a new deal
- [ ] Tested adding a new client
- [ ] Verified data shows correctly in English

---

## 📚 Related Files

- `bot.py` - Main bot code (now in English)
- `airtable_manager.py` - Airtable manager (now in English)
- `AIRTABLE_SETUP.md` - Airtable setup instructions (still in Hebrew)
- `README.md` - Main documentation (still in Hebrew)

---

**Need Help?**

If you encounter issues after the language change:
1. Double-check Airtable field options match English values
2. Restart the bot: `python bot.py`
3. Check logs for error messages
4. See `TROUBLESHOOTING.md` for common issues

---

**Last Updated:** November 13, 2025
**Change Type:** Language conversion (Hebrew → English)
**Impact:** High - Requires Airtable field updates

