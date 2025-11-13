# 🤖 בוט טלגרם לניהול עסקאות לידים

בוט מתקדם לניהול עסקאות לידים באמצעות טלגרם ו-Airtable CRM

---

## 📋 תוכן עניינים

1. [תכונות](#תכונות)
2. [דרישות מקדימות](#דרישות-מקדימות)
3. [התקנה](#התקנה)
4. [הגדרת Airtable](#הגדרת-airtable)
5. [הגדרת הבוט](#הגדרת-הבוט)
6. [הפעלה](#הפעלה)
7. [שימוש](#שימוש)
8. [פקודות](#פקודות)
9. [Deployment לשרת](#deployment-לשרת)
10. [פתרון בעיות](#פתרון-בעיות)

---

## ✨ תכונות

- ✅ **יצירת עסקאות חדשות** - תייג את הבוט ב-Reply להודעה
- 👥 **ניהול לקוחות וספקים** - הוספה ומעקב
- 💰 **רישום תשלומים** - מעקב אחר תזרים מזומנים
- 📊 **חישובי רווח אוטומטיים** - מחיר ללייד, רווח כולל, הוצאות
- 📈 **סטטיסטיקות** - דוחות ונתונים בזמן אמת
- 🔄 **סנכרון עם Airtable** - כל הנתונים נשמרים ב-CRM
- 🌍 **תמיכה בעברית מלאה** - ממשק וטקסטים בעברית

---

## 📦 דרישות מקדימות

### 1. חשבון Telegram
- צור בוט חדש דרך [@BotFather](https://t.me/BotFather)
- שמור את ה-Token שתקבל

### 2. חשבון Airtable
- הירשם ל-[Airtable](https://airtable.com) (חינם)
- צור Base חדש
- קבל את ה-API Key שלך

### 3. Python 3.9+
```bash
python --version  # ודא שגרסה 3.9 או יותר
```

---

## 🚀 התקנה

### שלב 1: שכפול הפרויקט

```bash
# הורד את הקבצים לתיקייה
mkdir telegram-leads-bot
cd telegram-leads-bot

# העתק את כל הקבצים לתיקייה הזו
```

### שלב 2: התקנת תלויות

```bash
# צור סביבה וירטואלית (מומלץ)
python -m venv venv

# הפעל את הסביבה הוירטואלית
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# התקן חבילות
pip install -r requirements.txt
```

---

## 🗄️ הגדרת Airtable

### שלב 1: יצירת Base

1. היכנס ל-[Airtable](https://airtable.com)
2. לחץ על **"+ Create"** → **"Base"**
3. תן שם: `Leads CRM`

### שלב 2: יצירת טבלאות

#### טבלה 1: **Deals** (עסקאות)

לחץ על **"Add or import"** → **"Table"** → שנה שם ל-`Deals`

הוסף את השדות הבאים:

| שם השדה | סוג | הערות |
|---------|-----|-------|
| Client | Single line text | שם הלקוח |
| Supplier | Single line text | שם הספק |
| Quantity | Number | כמות לידים |
| Country | Single line text | מדינת היעד |
| Delivery Date | Date | תאריך אספקה |
| Buy Price | Currency | מחיר קנייה ליחידה |
| Sell Price | Currency | מחיר מכירה ליחידה |
| Profit | Currency | רווח (אוטומטי) |
| Price Per Lead | Currency | מחיר ממוצע ללייד |
| Deal Type | Single select | קנייה/מכירה |
| Raw Text | Long text | טקסט מקורי מהודעה |
| Telegram User | Single line text | שם משתמש בטלגרם |
| Telegram Group | Single line text | שם הקבוצה |
| Status | Single select | פעיל/הושלם/בוטל |
| Created Date | Date | תאריך יצירה |

**פורמולה לשדה Profit:**
```
({Sell Price} - {Buy Price}) * {Quantity}
```

#### טבלה 2: **Clients** (לקוחות)

לחץ **"Add table"** → שנה שם ל-`Clients`

| שם השדה | סוג | הערות |
|---------|-----|-------|
| Name | Single line text | שם |
| Type | Single select | לקוח/ספק |
| Telegram User | Single line text | מי הוסיף |
| Added Date | Date | תאריך הוספה |
| Total Deals | Number | סה"כ עסקאות |
| Total Revenue | Currency | סה"כ הכנסות |

#### טבלה 3: **Payments** (תשלומים)

לחץ **"Add table"** → שנה שם ל-`Payments`

| שם השדה | סוג | הערות |
|---------|-----|-------|
| Deal ID | Single line text | ID עסקה |
| Amount | Currency | סכום |
| Payment Date | Date | תאריך תשלום |
| Telegram User | Single line text | מי רשם |
| Type | Single select | התקבל/שולם |

### שלב 3: קבלת API Key

1. לך ל-[Airtable Account](https://airtable.com/account)
2. גלול ל-**"API"**
3. לחץ **"Generate API key"**
4. שמור את ה-Key

### שלב 4: קבלת Base ID

1. לך ל-[Airtable API Documentation](https://airtable.com/api)
2. בחר את ה-Base שיצרת
3. ה-Base ID מופיע ב-URL: `https://airtable.com/YOUR_BASE_ID/api/docs`
4. העתק את ה-`appXXXXXXXXXX` - זה ה-Base ID שלך

---

## ⚙️ הגדרת הבוט

### שלב 1: יצירת בוט בטלגרם

1. פתח שיחה עם [@BotFather](https://t.me/BotFather)
2. שלח: `/newbot`
3. תן שם לבוט (למשל: `My Leads Manager`)
4. תן username (למשל: `myleadsbot`)
5. שמור את ה-**Token** שתקבל

### שלב 2: הגדרת משתני סביבה

צור קובץ בשם `.env` בתיקיית הפרויקט:

```bash
# העתק את הקובץ לדוגמה
cp .env.example .env

# ערוך את הקובץ
nano .env  # או notepad .env בWindows
```

מלא את הערכים:

```env
TELEGRAM_BOT_TOKEN=1234567890:ABCdefGHIjklMNOpqrsTUVwxyz
AIRTABLE_API_KEY=keyXXXXXXXXXXXXXX
AIRTABLE_BASE_ID=appXXXXXXXXXXXXXX
```

**⚠️ חשוב:** אל תשתף את הקובץ `.env` עם אף אחד!

---

## 🎯 הפעלה

### הפעלה מקומית (לבדיקה)

```bash
# ודא שהסביבה הוירטואלית פעילה
source venv/bin/activate  # Linux/Mac
# או
venv\Scripts\activate  # Windows

# הרץ את הבוט
python bot.py
```

תראה:
```
2025-11-02 12:00:00 - __main__ - INFO - 🚀 Bot is starting...
```

### בדיקה ראשונית

1. פתח את הבוט בטלגרם (שלח `/start`)
2. צריך לקבל הודעת ברוכים הבאים
3. נסה פקודה: `/clients`

---

## 📱 שימוש

### 1️⃣ יצירת עסקה חדשה

**בקבוצה:**

1. מישהו כותב: `20 לידים איטליה ליום שני הקרוב`
2. תייג את הבוט ב-**Reply** להודעה: `/newdeal`
3. הבוט ישאל סוג עסקה (קנייה/מכירה)
4. שלח פרטים:

```
לקוח: ג'ון דו
ספק: ספק איטלקי
כמות: 20
מדינה: איטליה
תאריך: 2025-11-04
מחיר קנייה: 5
מחיר מכירה: 8
```

5. הבוט יחשב רווח אוטומטית: `(8-5) * 20 = $60`

### 2️⃣ הוספת לקוח

```
/newclient
```

בחר: לקוח או ספק → הזן שם

### 3️⃣ רישום תשלום

```
/payment
```

בחר עסקה מהרשימה → הזן סכום

### 4️⃣ צפייה בעסקאות

```
/deals
```

### 5️⃣ רשימת לקוחות

```
/clients
```

### 6️⃣ סטטיסטיקות

```
/stats
```

תקבל:
- סה"כ עסקאות
- סה"כ רווח
- סה"כ לידים
- ממוצעים

---

## 🎮 פקודות

| פקודה | תיאור |
|-------|-------|
| `/start` | הצג תפריט ראשי |
| `/newdeal` | עסקה חדשה (Reply להודעה) |
| `/newclient` | לקוח/ספק חדש |
| `/payment` | רישום תשלום |
| `/deals` | כל העסקאות |
| `/clients` | רשימת לקוחות |
| `/stats` | סטטיסטיקות |
| `/cancel` | ביטול פעולה נוכחית |

---

## 🌐 Deployment לשרת

### אופציה 1: Railway.app (מומלץ - חינם)

1. צור חשבון ב-[Railway.app](https://railway.app)
2. התחבר עם GitHub
3. העלה את הקבצים ל-Repository
4. ב-Railway: **"New Project"** → **"Deploy from GitHub"**
5. בחר את ה-Repository
6. הוסף משתני סביבה (Environment Variables):
   - `TELEGRAM_BOT_TOKEN`
   - `AIRTABLE_API_KEY`
   - `AIRTABLE_BASE_ID`
7. Deploy!

### אופציה 2: VPS (DigitalOcean, AWS, etc.)

```bash
# התחבר לשרת
ssh user@your-server.com

# התקן Python
sudo apt update
sudo apt install python3 python3-pip python3-venv

# העלה קבצים
scp -r telegram-leads-bot user@your-server.com:~/

# התקן תלויות
cd telegram-leads-bot
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# הגדר משתני סביבה
nano .env

# הרץ עם systemd (ריצה תמידית)
sudo nano /etc/systemd/system/telegram-bot.service
```

**תוכן הקובץ:**

```ini
[Unit]
Description=Telegram Leads Bot
After=network.target

[Service]
Type=simple
User=youruser
WorkingDirectory=/home/youruser/telegram-leads-bot
Environment="PATH=/home/youruser/telegram-leads-bot/venv/bin"
ExecStart=/home/youruser/telegram-leads-bot/venv/bin/python bot.py
Restart=always

[Install]
WantedBy=multi-user.target
```

**הפעלה:**

```bash
sudo systemctl daemon-reload
sudo systemctl enable telegram-bot
sudo systemctl start telegram-bot
sudo systemctl status telegram-bot
```

---

## 🛠️ פתרון בעיות

### הבוט לא מגיב

1. בדוק שה-Token תקין:
```bash
curl https://api.telegram.org/bot<YOUR_TOKEN>/getMe
```

2. בדוק logs:
```bash
# אם רץ עם systemd
sudo journalctl -u telegram-bot -f

# אם רץ ישירות
python bot.py  # ראה הודעות שגיאה
```

### שגיאות Airtable

**"Missing AIRTABLE_API_KEY"**
- בדוק שהקובץ `.env` קיים
- בדוק שהערכים נכונים
- בדוק שאין רווחים מיותרים

**"Table not found"**
- ודא ששמות הטבלאות: `Deals`, `Clients`, `Payments`
- שמות חייבים להיות באנגלית עם אותיות גדולות בתחילת כל מילה

### הבוט לא שומר ב-Airtable

1. בדוק Base ID:
```python
python
>>> from pyairtable import Api
>>> api = Api('YOUR_API_KEY')
>>> print(api.bases())
```

2. בדוק הרשאות:
- לך ל-Airtable → Share → ודא שיש הרשאות כתיבה

---

## 📝 הערות חשובות

1. **אבטחה:**
   - אל תשתף את ה-Token או API Key
   - השתמש ב-`.gitignore` כדי לא להעלות `.env` ל-Git

2. **גבולות:**
   - Airtable חינמי: 1,200 רשומות לבסיס
   - אם צריך יותר, שדרג ל-Pro ($20/חודש)

3. **שפה:**
   - הבוט תומך בעברית מלאה
   - ניתן להוסיף תמיכה בשפות נוספות

4. **תחזוקה:**
   - בדוק logs באופן קבוע
   - גבה את ה-Airtable Base

---

## 🆘 תמיכה

נתקלת בבעיה? 

1. בדוק את [פתרון בעיות](#פתרון-בעיות)
2. ראה את הקוד ב-`bot.py`
3. בדוק את [תיעוד Telegram Bot API](https://core.telegram.org/bots/api)
4. בדוק את [תיעוד Airtable API](https://airtable.com/api)

---

## 📄 רישיון

פרויקט זה הוא קוד פתוח - אתה רשאי לשנות ולהשתמש בו בחופשיות.

---

**בהצלחה! 🚀**

אם הכל עבד כמו שצריך, יש לך עכשיו מערכת ניהול עסקאות לידים מקצועית!
