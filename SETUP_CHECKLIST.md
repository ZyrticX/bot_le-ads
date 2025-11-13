# ✅ רשימת בדיקה להתקנה

## 📋 לפני שמתחילים

- [ ] חשבון Telegram
- [ ] חשבון Airtable (חינמי)
- [ ] Python 3.9+ מותקן (✅ יש לך 3.11.9)
- [ ] 15-20 דקות זמן

---

## 🤖 שלב 1: יצירת בוט טלגרם

- [ ] פתח [@BotFather](https://t.me/BotFather)
- [ ] שלח `/newbot`
- [ ] בחר שם לבוט (למשל: `My Leads Manager`)
- [ ] בחר username (למשל: `myleadsbot`)
- [ ] שמור את ה-**TOKEN** שתקבל

```
דוגמה: 1234567890:ABCdefGHIjklMNOpqrsTUVwxyz
```

---

## 🗄️ שלב 2: הקמת Airtable

### 2.1 יצירת Base
- [ ] היכנס ל-[airtable.com](https://airtable.com)
- [ ] לחץ **"+ Create"** → **"Base"**
- [ ] שם: `Leads CRM`

### 2.2 טבלה 1: Deals
- [ ] צור טבלה בשם `Deals`
- [ ] הוסף שדות:

| שם השדה | סוג | הערות |
|---------|-----|-------|
| Client | Single line text | שם הלקוח |
| Supplier | Single line text | שם הספק |
| Quantity | Number | כמות לידים |
| Country | Single line text | מדינה |
| Delivery Date | Date | תאריך אספקה |
| Buy Price | Currency | מחיר קנייה ליחידה |
| Sell Price | Currency | מחיר מכירה ליחידה |
| Profit | Formula | `({Sell Price} - {Buy Price}) * {Quantity}` |
| Price Per Lead | Currency | מחיר ממוצע ללייד |
| Deal Type | Single select | קנייה/מכירה |
| Raw Text | Long text | טקסט מקורי |
| Telegram User | Single line text | שם משתמש |
| Telegram Group | Single line text | קבוצה |
| Status | Single select | פעיל/הושלם/בוטל |
| Created Date | Date | תאריך יצירה |

### 2.3 טבלה 2: Clients
- [ ] צור טבלה בשם `Clients`
- [ ] הוסף שדות:

| שם השדה | סוג |
|---------|-----|
| Name | Single line text |
| Type | Single select (לקוח/ספק) |
| Telegram User | Single line text |
| Added Date | Date |
| Total Deals | Number |
| Total Revenue | Currency |

### 2.4 טבלה 3: Payments
- [ ] צור טבלה בשם `Payments`
- [ ] הוסף שדות:

| שם השדה | סוג |
|---------|-----|
| Deal ID | Single line text |
| Amount | Currency |
| Payment Date | Date |
| Telegram User | Single line text |
| Type | Single select (התקבל/שולם) |

### 2.5 קבלת API Key
- [ ] לך ל-[airtable.com/account](https://airtable.com/account)
- [ ] גלול ל-**"API"**
- [ ] לחץ **"Generate API key"**
- [ ] שמור את ה-Key

```
דוגמה: keyXXXXXXXXXXXXXX
```

### 2.6 קבלת Base ID
- [ ] לך ל-[airtable.com/api](https://airtable.com/api)
- [ ] בחר את ה-Base `Leads CRM`
- [ ] העתק את Base ID מה-URL

```
דוגמה: appXXXXXXXXXXXXXX
```

---

## 💻 שלב 3: התקנה במחשב (Windows)

### אופציה A: סקריפט אוטומטי (מומלץ)

```powershell
# הרץ את הסקריפט
.\setup_windows.ps1
```

### אופציה B: ידני

```powershell
# 1. יצירת סביבה וירטואלית
python -m venv venv

# 2. הפעלת הסביבה
venv\Scripts\Activate.ps1

# 3. התקנת חבילות
pip install --upgrade pip
pip install -r requirements.txt

# 4. יצירת קובץ .env
Copy-Item .env.example .env
notepad .env
```

---

## ⚙️ שלב 4: הגדרת משתני סביבה

- [ ] פתח את הקובץ `.env`:
```powershell
notepad .env
```

- [ ] מלא את הערכים:
```env
TELEGRAM_BOT_TOKEN=1234567890:ABCdefGHIjklMNOpqrsTUVwxyz
AIRTABLE_API_KEY=keyXXXXXXXXXXXXXX
AIRTABLE_BASE_ID=appXXXXXXXXXXXXXX
```

- [ ] שמור את הקובץ (Ctrl+S)

**⚠️ חשוב:** אל תשתף את הקובץ הזה עם אף אחד!

---

## 🚀 שלב 5: הרצת הבוט

```powershell
# הפעל סביבה וירטואלית (אם לא פעילה)
venv\Scripts\Activate.ps1

# הרץ את הבוט
python bot.py
```

### תראה:
```
2025-11-13 12:00:00 - __main__ - INFO - 🚀 Bot is starting...
```

---

## ✅ שלב 6: בדיקה

- [ ] פתח את הבוט בטלגרם
- [ ] שלח `/start`
- [ ] בדוק שהבוט מגיב
- [ ] נסה `/clients`
- [ ] נסה `/stats`

---

## 🎯 שלב 7: בדיקת עסקה ראשונה

### בצ'אט פרטי עם הבוט:

1. כתוב:
```
20 לידים איטליה
```

2. תייג את הבוט (Reply):
```
/newdeal
```

3. בחר: **מכירה**

4. שלח פרטים:
```
לקוח: בדיקה
ספק: ספק בדיקה
כמות: 20
מדינה: איטליה
תאריך: 2025-11-15
מחיר קנייה: 5
מחיר מכירה: 8
```

5. בדוק:
- [ ] הבוט אישר שנוצרה עסקה
- [ ] העסקה מופיעה ב-Airtable

---

## ❓ פתרון בעיות מהיר

### הבוט לא מגיב
```powershell
# בדוק שרץ
# צריך לראות: "Bot is starting..."

# בדוק Token
curl https://api.telegram.org/bot<YOUR_TOKEN>/getMe
```

### "Missing AIRTABLE_API_KEY"
```powershell
# בדוק .env
Get-Content .env

# ודא שאין רווחים מיותרים
```

### "Table not found"
- שמות טבלאות חייבים: `Deals`, `Clients`, `Payments` (באנגלית!)
- אותיות גדולות בתחילת מילה

---

## 📚 מסמכים נוספים

לאחר שהבוט רץ:

- [ ] קרא [EXAMPLES.md](EXAMPLES.md) - דוגמאות שימוש
- [ ] קרא [DEPLOYMENT.md](DEPLOYMENT.md) - הרצה בשרת 24/7
- [ ] קרא [TROUBLESHOOTING.md](TROUBLESHOOTING.md) - פתרון בעיות מפורט

---

## ✅ סיכום סטטוס

### מה שיש:
- ✅ Python 3.11.9
- ✅ קבצי קוד מלאים
- ✅ תיעוד מקיף

### מה שחסר:
- ❌ Token טלגרם
- ❌ Airtable Base
- ❌ קובץ .env מוגדר
- ❌ venv + חבילות מותקנות

### זמן משוער:
- 🤖 Telegram Bot: 2 דקות
- 🗄️ Airtable: 10 דקות
- 💻 התקנה: 3 דקות
- 🧪 בדיקה: 2 דקות
- **סה"כ: ~15-20 דקות**

---

**בהצלחה! 🚀**

