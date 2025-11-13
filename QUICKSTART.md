# ⚡ התחלה מהירה - 5 דקות

מדריך מקוצר להרצת הבוט במהירות

---

## ✅ צ'קליסט מהיר

### לפני שמתחילים - תכין:
- [ ] חשבון Telegram
- [ ] חשבון Airtable (חינמי)
- [ ] Python 3.9+ מותקן
- [ ] 10 דקות זמן פנוי

---

## 🚀 3 שלבים פשוטים

### שלב 1: הגדרת Telegram Bot (2 דקות)

1. פתח [@BotFather](https://t.me/BotFather) בטלגרם
2. שלח: `/newbot`
3. תן שם: `My Leads Bot`
4. תן username: `myleadsbot123`
5. **שמור את ה-Token!** נראה כך:
   ```
   1234567890:ABCdefGHIjklMNOpqrsTUVwxyz
   ```

---

### שלב 2: הגדרת Airtable (4 דקות)

1. היכנס ל-[airtable.com](https://airtable.com)
2. **Create** → **Base** → שם: `Leads CRM`
3. צור 3 טבלאות:

**טבלה 1: Deals**
```
שדות: Client, Supplier, Quantity, Country, Delivery Date, 
       Buy Price, Sell Price, Profit (formula), Price Per Lead, 
       Deal Type, Raw Text, Telegram User, Telegram Group, Status, Created Date
```

**טבלה 2: Clients**
```
שדות: Name, Type, Telegram User, Added Date, Total Deals, Total Revenue
```

**טבלה 3: Payments**
```
שדות: Deal ID, Amount, Payment Date, Telegram User, Type
```

*מדריך מפורט: [AIRTABLE_SETUP.md](AIRTABLE_SETUP.md)*

4. **קבל API Key:**
   - Account → API → Generate API key
   - שמור!

5. **קבל Base ID:**
   - [airtable.com/api](https://airtable.com/api)
   - בחר Base
   - URL: `airtable.com/YOUR_BASE_ID/api`
   - העתק את `appXXXXXXXX`

---

### שלב 3: הרצת הבוט (2 דקות)

#### Windows:

```cmd
cd telegram-leads-bot

python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

copy .env.example .env
notepad .env
```

מלא את הערכים ב-.env:
```env
TELEGRAM_BOT_TOKEN=1234567890:ABC...
AIRTABLE_API_KEY=keyXXXX...
AIRTABLE_BASE_ID=appXXXX...
```

```cmd
python bot.py
```

#### Linux/Mac:

```bash
cd telegram-leads-bot

./install.sh

cp .env.example .env
nano .env
# מלא ערכים, שמור (Ctrl+O, Enter, Ctrl+X)

python bot.py
```

---

## 🎯 בדיקה ראשונה

1. פתח את הבוט בטלגרם
2. שלח: `/start`
3. אמור לראות:

```
👋 שלום!

🤖 ברוך הבא לבוט ניהול עסקאות לידים

📋 פקודות זמינות:
/newdeal - יצירת עסקה חדשה
...
```

4. נסה: `/clients`

אם הבוט עונה - **הצלחת!** 🎉

---

## 📱 שימוש ראשון

### צור עסקה:

1. בקבוצת טלגרם (או בצ'אט פרטי עם הבוט):
   ```
   20 לידים איטליה ליום שני
   ```

2. תייג את הבוט ב-Reply:
   ```
   @YourBot /newdeal
   ```

3. בחר: **מכירה**

4. שלח:
   ```
   לקוח: ג'ון
   ספק: מריו
   כמות: 20
   מדינה: איטליה
   תאריך: 2025-11-04
   מחיר קנייה: 5
   מחיר מכירה: 8
   ```

5. הבוט יודיע:
   ```
   ✅ עסקה נוספה בהצלחה!
   💚 רווח: $60
   ```

6. בדוק ב-Airtable - העסקה שם! ✨

---

## 🔥 פקודות חיוניות

| פקודה | מה עושה |
|-------|---------|
| `/newdeal` | עסקה חדשה (Reply להודעה) |
| `/newclient` | לקוח/ספק חדש |
| `/payment` | רישום תשלום |
| `/stats` | סטטיסטיקות |

---

## ❓ בעיות?

### הבוט לא מגיב
```bash
# בדוק שרץ:
# צריך לראות: "Bot is starting..."
```

### "Missing AIRTABLE_API_KEY"
```bash
# בדוק .env:
cat .env

# ודא שאין רווחים מיותרים
```

### "Table not found"
- שמות טבלאות חייבים: `Deals`, `Clients`, `Payments` (באנגלית!)

---

## 📚 למידע מפורט

- **[README.md](README.md)** - מדריך מלא
- **[AIRTABLE_SETUP.md](AIRTABLE_SETUP.md)** - הקמת Airtable צעד אחר צעד
- **[EXAMPLES.md](EXAMPLES.md)** - דוגמאות שימוש
- **[DEPLOYMENT.md](DEPLOYMENT.md)** - הרצה בשרת 24/7

---

## 🚀 Next Steps

1. ✅ הבוט רץ? מעולה!
2. 📖 קרא [EXAMPLES.md](EXAMPLES.md) לתרחישי שימוש
3. 🌐 רוצה 24/7? ראה [DEPLOYMENT.md](DEPLOYMENT.md)
4. 🎨 התאם אישית את Airtable
5. 📊 הוסף Automations ב-Airtable

---

**זהו! תהנה מהבוט! 🎉**

שאלות? בדוק את הקבצים האחרים או הרץ מחדש את המדריך.
