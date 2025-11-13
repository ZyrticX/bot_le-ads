# 📊 Airtable CRM Setup Guide - Step by Step

Detailed illustrated guide for setting up your Airtable database

---

## 🎯 Goal

Create an organized database to serve as a CRM (Customer Relationship Management system) for your leads deals.

---

## 📋 Table of Contents

1. [Sign Up and Create Base](#step-1-sign-up-and-create-base)
2. [Create Deals Table](#step-2-deals-table)
3. [Create Clients Table](#step-3-clients-table)
4. [Create Payments Table](#step-4-payments-table)
5. [Get API Key](#step-5-get-api-key)
6. [Get Base ID](#step-6-get-base-id)
7. [Testing](#step-7-testing)

---

## Step 1: Sign Up and Create Base

### 1.1 Sign Up to Airtable

1. Go to [https://airtable.com](https://airtable.com)
2. Click **"Sign up for free"**
3. Use Google/Apple or Email + Password
4. Verify your email

### 1.2 Create New Base

1. Click **"Create a base"** or **"+"** at the top
2. Choose **"Start from scratch"**
3. Name it: **`Leads CRM`**
4. Choose color/icon (optional)

---

## Step 2: Deals Table

### 2.1 Rename the First Table

1. The first table is automatically created as "Table 1"
2. Click the arrow next to "Table 1" → **"Rename table"**
3. Change to **`Deals`**

### 2.2 Add Fields

**Remove existing fields:**
- Click the arrow next to "Name", "Notes", "Attachments" → **"Delete field"**

**Now add the new fields:**

#### Field 1: Client
1. Click **"+"** on the right side of the fields
2. Choose **"Single line text"**
3. Field name: `Client`
4. Click **"Create field"**

#### Field 2: Supplier
- Type: **Single line text**
- Name: `Supplier`

#### Field 3: Quantity
- Type: **Number**
- Name: `Quantity`
- Format: Integer (whole number)

#### Field 4: Country
- Type: **Single line text**
- Name: `Country`

#### Field 5: Delivery Date
- Type: **Date**
- Name: `Delivery Date`
- Date format: Choose preferred format (e.g., MM/DD/YYYY)
- Include time: Optional

#### Field 6: Buy Price
- Type: **Currency**
- Name: `Buy Price`
- Precision: 2 decimal places
- Currency: USD ($)

#### Field 7: Sell Price
- Type: **Currency**
- Name: `Sell Price`
- Precision: 2 decimal places
- Currency: USD ($)

#### Field 8: Profit (Calculated)
- Type: **Formula**
- Name: `Profit`
- Formula:
```
({Sell Price} - {Buy Price}) * {Quantity}
```
- Formatting: Currency (USD)

**How to add a formula:**
1. Add new field → Choose "Formula"
2. Name: `Profit`
3. In the formula box, type: `({Sell Price} - {Buy Price}) * {Quantity}`
4. Click "Save"
5. Click the field again → "Customize field type" → Set formatting to "Currency"

#### Field 9: Price Per Lead
- Type: **Currency**
- Name: `Price Per Lead`
- Precision: 2 decimal places
- Currency: USD ($)

#### Field 10: Deal Type
- Type: **Single select**
- Name: `Deal Type`
- Options:
  - `Buy`
  - `Sell`

**⚠️ IMPORTANT:** Options must be in English!

**How to add options:**
1. Add field → "Single select"
2. Name: `Deal Type`
3. Under "Options" click "+ Add option"
4. Add: `Buy`
5. Click "+ Add option" again
6. Add: `Sell`
7. Choose colors for each option (optional)
8. Click "Create field"

#### Field 11: Raw Text
- Type: **Long text**
- Name: `Raw Text`
- Enable rich text: Optional

#### Field 12: Telegram User
- Type: **Single line text**
- Name: `Telegram User`

#### Field 13: Telegram Group
- Type: **Single line text**
- Name: `Telegram Group`

#### Field 14: Status
- Type: **Single select**
- Name: `Status`
- Options:
  - `Active`
  - `Completed`
  - `Cancelled`

**⚠️ IMPORTANT:** Options must be in English!

#### Field 15: Created Date
- Type: **Date**
- Name: `Created Date`
- Date format: Choose preferred format
- Include time: Yes (recommended)

---

### 2.3 Verification

Your Deals table should now have these 15 fields:

1. ✅ Client (Single line text)
2. ✅ Supplier (Single line text)
3. ✅ Quantity (Number)
4. ✅ Country (Single line text)
5. ✅ Delivery Date (Date)
6. ✅ Buy Price (Currency)
7. ✅ Sell Price (Currency)
8. ✅ Profit (Formula)
9. ✅ Price Per Lead (Currency)
10. ✅ Deal Type (Single select: Buy, Sell)
11. ✅ Raw Text (Long text)
12. ✅ Telegram User (Single line text)
13. ✅ Telegram Group (Single line text)
14. ✅ Status (Single select: Active, Completed, Cancelled)
15. ✅ Created Date (Date)

---

## Step 3: Clients Table

### 3.1 Create New Table

1. Click **"+ Add or import"** at the bottom left
2. Choose **"Table"**
3. Name it: **`Clients`**

### 3.2 Add Fields

**Remove default fields:**
- Delete "Name", "Notes", "Attachments" if they exist

**Add new fields:**

#### Field 1: Name
- Type: **Single line text**
- Name: `Name`

#### Field 2: Type
- Type: **Single select**
- Name: `Type`
- Options:
  - `Client`
  - `Supplier`

**⚠️ IMPORTANT:** Options must be in English!

#### Field 3: Telegram User
- Type: **Single line text**
- Name: `Telegram User`

#### Field 4: Added Date
- Type: **Date**
- Name: `Added Date`
- Include time: Yes

#### Field 5: Total Deals
- Type: **Number**
- Name: `Total Deals`
- Format: Integer
- Default value: 0

#### Field 6: Total Revenue
- Type: **Currency**
- Name: `Total Revenue`
- Currency: USD ($)
- Default value: 0

---

### 3.3 Verification

Your Clients table should have these 6 fields:

1. ✅ Name (Single line text)
2. ✅ Type (Single select: Client, Supplier)
3. ✅ Telegram User (Single line text)
4. ✅ Added Date (Date)
5. ✅ Total Deals (Number)
6. ✅ Total Revenue (Currency)

---

## Step 4: Payments Table

### 4.1 Create New Table

1. Click **"+ Add or import"** again
2. Choose **"Table"**
3. Name it: **`Payments`**

### 4.2 Add Fields

#### Field 1: Deal ID
- Type: **Single line text**
- Name: `Deal ID`

#### Field 2: Amount
- Type: **Currency**
- Name: `Amount`
- Currency: USD ($)

#### Field 3: Payment Date
- Type: **Date**
- Name: `Payment Date`
- Include time: Yes

#### Field 4: Telegram User
- Type: **Single line text**
- Name: `Telegram User`

#### Field 5: Type
- Type: **Single select**
- Name: `Type`
- Options:
  - `Received`
  - `Paid`

**⚠️ IMPORTANT:** Options must be in English!

---

### 4.3 Verification

Your Payments table should have these 5 fields:

1. ✅ Deal ID (Single line text)
2. ✅ Amount (Currency)
3. ✅ Payment Date (Date)
4. ✅ Telegram User (Single line text)
5. ✅ Type (Single select: Received, Paid)

---

## Step 5: Get API Key

### 5.1 Access API Settings

1. Click your profile picture at the top right
2. Select **"Account"**
3. Scroll to **"API"** section

### 5.2 Generate API Key

1. Click **"Generate API key"**
2. Copy the key (it looks like: `keyXXXXXXXXXXXXXX`)
3. **Save it securely!** You'll need it for the `.env` file

**⚠️ Security Note:**
- This key gives full access to your Airtable data
- Don't share it with anyone
- Don't commit it to Git
- Store it only in your `.env` file

---

## Step 6: Get Base ID

### 6.1 Access API Documentation

1. Go to [https://airtable.com/api](https://airtable.com/api)
2. You'll see a list of your Bases

### 6.2 Select Your Base

1. Find and click **"Leads CRM"**
2. The page will show documentation for your Base

### 6.3 Copy Base ID

The Base ID appears in multiple places:

**Option 1: From URL**
- Look at the browser URL
- It will be: `https://airtable.com/YOUR_BASE_ID/api/docs#...`
- Your Base ID is the part that starts with `app` (e.g., `appXXXXXXXXXXXXXX`)

**Option 2: From Documentation**
- In the "Authentication" section
- You'll see: "The ID of this base is `appXXXXXXXXXXXXXX`"

**Copy the Base ID** - you'll need it for the `.env` file

---

## Step 7: Testing

### 7.1 Add Test Record

Let's verify everything works:

1. Go to your **Deals** table
2. Click **"+ Add record"** or click in the empty row
3. Fill in test data:

```
Client: Test Client
Supplier: Test Supplier
Quantity: 10
Country: USA
Delivery Date: Tomorrow's date
Buy Price: 5
Sell Price: 8
Price Per Lead: 8
Deal Type: Sell
Status: Active
Created Date: Today's date
```

4. Check that:
   - ✅ The **Profit** field automatically calculates: `(8 - 5) * 10 = $30`
   - ✅ All fields accept data correctly
   - ✅ Single select dropdowns show English options

### 7.2 Test Other Tables

**Test Clients table:**
1. Add a test client
2. Verify the **Type** dropdown shows "Client" and "Supplier" (English)

**Test Payments table:**
1. Add a test payment
2. Verify the **Type** dropdown shows "Received" and "Paid" (English)

---

## 📝 Final Checklist

Before connecting to the bot:

### Tables
- [ ] Deals table exists with 15 fields
- [ ] Clients table exists with 6 fields
- [ ] Payments table exists with 5 fields

### Field Names (Exact spelling required!)
- [ ] All field names match exactly as specified
- [ ] Field names are in English
- [ ] No extra spaces in field names

### Single Select Options (CRITICAL!)
- [ ] Deal Type: Buy, Sell (English)
- [ ] Status: Active, Completed, Cancelled (English)
- [ ] Clients Type: Client, Supplier (English)
- [ ] Payments Type: Received, Paid (English)

### Credentials
- [ ] API Key copied and saved
- [ ] Base ID copied and saved
- [ ] Both ready to add to `.env` file

---

## 🎨 Optional Enhancements

### Views

Create custom views for better organization:

**Deals Table Views:**
1. **Active Deals**
   - Filter: Status = "Active"
   - Sort: Created Date (newest first)

2. **By Country**
   - Group by: Country
   - Sort: Delivery Date

3. **Profit Analysis**
   - Sort: Profit (highest first)
   - Hide: Raw Text, Telegram Group

**To create a view:**
1. Click "Grid view" dropdown at the top
2. Select "+ Create new view"
3. Choose "Grid" (or Calendar/Kanban)
4. Name it and configure filters/sorting

### Colors and Formatting

Make it visual:

**Status Field Colors:**
- Active → Green
- Completed → Blue
- Cancelled → Red

**Deal Type Colors:**
- Buy → Orange
- Sell → Green

**To change colors:**
1. Click on the field header
2. Click "Customize field type"
3. Click on each option's color circle
4. Choose desired color

### Automations (Advanced)

Set up automatic actions:

**Example 1: Email notification when deal is created**
1. Click "Automations" at the top
2. "Create automation"
3. Trigger: "When record created" in Deals
4. Action: "Send email"
5. Configure email details

**Example 2: Update status after 30 days**
1. Trigger: "When record matches conditions"
2. Condition: Created Date is 30 days ago AND Status = "Active"
3. Action: "Update record" → Set Status to "Completed"

---

## 🔍 Common Issues

### Issue: "Field not found" error in bot

**Solution:**
- Check field names are exactly as specified
- Field names are case-sensitive
- Example: "Client" ≠ "client" ≠ "CLIENT"

### Issue: Bot saves wrong Status values

**Solution:**
- Single select options must be in English
- Check: Status = "Active" (not "פעיל")
- Update options as described in "IMPORTANT_CHANGES.md"

### Issue: Profit formula doesn't calculate

**Solution:**
1. Click on Profit field
2. "Customize field type"
3. Verify formula: `({Sell Price} - {Buy Price}) * {Quantity}`
4. Ensure field references match exactly (with curly braces)
5. Set formatting to "Currency"

### Issue: Can't find API Key

**Solution:**
- Go to: Account (top right) → API section
- If no key exists, generate new one
- If you lost it, delete old and create new

### Issue: Wrong Base ID

**Solution:**
- Go to: https://airtable.com/api
- Select your base
- Base ID starts with "app" (e.g., appXXXXXXXXXXXXXX)
- Copy from URL or documentation page

---

## 📊 Understanding the Data Flow

```
Telegram Message
      ↓
   Bot parses
      ↓
Creates record in Deals table
      ↓
Updates Clients table stats
      ↓
Records payment in Payments table
      ↓
   All synced in real-time
```

---

## 🔗 Next Steps

After completing this setup:

1. **Update `.env` file:**
   ```env
   AIRTABLE_API_KEY=keyXXXXXXXXXXXXXX
   AIRTABLE_BASE_ID=appXXXXXXXXXXXXXX
   ```

2. **Run the bot:**
   ```bash
   python bot.py
   ```

3. **Create your first deal:**
   - Send `/newdeal` in Telegram
   - Watch it appear in Airtable!

4. **Explore Airtable features:**
   - Create custom views
   - Set up automations
   - Build reports

---

## 📚 Additional Resources

- [Airtable Support](https://support.airtable.com)
- [Formula Field Reference](https://support.airtable.com/hc/en-us/articles/203255215-Formula-field-reference)
- [Airtable API Documentation](https://airtable.com/api)
- [Airtable Community](https://community.airtable.com)

---

## ✅ Summary

You now have:
- ✅ Airtable account
- ✅ Leads CRM Base with 3 tables
- ✅ All fields properly configured in English
- ✅ API Key and Base ID ready
- ✅ Ready to connect to the Telegram bot!

**Total time:** ~10-15 minutes  
**Difficulty:** Easy  
**Result:** Professional CRM system for leads management!

---

**Need help?** See `TROUBLESHOOTING.md` or `IMPORTANT_CHANGES.md`

**Ready to use the bot?** See `README_EN.md` for next steps!

---

Last Updated: November 13, 2025

