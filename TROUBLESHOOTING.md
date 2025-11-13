# 🔧 פתרון בעיות (Troubleshooting)

מדריך מקיף לפתרון בעיות נפוצות

---

## 🔍 איך לאבחן בעיות

### שלב 1: זיהוי הבעיה

**שאל את עצמך:**
1. הבוט לא מגיב בכלל?
2. הבוט מגיב אבל לא שומר ב-Airtable?
3. יש הודעת שגיאה? מה היא אומרת?
4. זה עובד לפעמים אבל לא תמיד?

---

## 🚫 הבוט לא מגיב בטלגרם

### אבחון:

```bash
# בדוק שהבוט רץ:
# אם רצת עם python bot.py, אמור לראות:
# INFO - 🚀 Bot is starting...

# אם רץ כשירות:
sudo systemctl status telegram-bot

# צריך לראות:
# Active: active (running)
```

### פתרון 1: Token לא תקין

```bash
# בדוק את ה-Token:
cat .env | grep TELEGRAM_BOT_TOKEN

# בדוק בדפדפן:
# החלף YOUR_TOKEN עם ה-Token שלך:
https://api.telegram.org/botYOUR_TOKEN/getMe

# צריך לראות JSON עם פרטי הבוט
# אם שגיאה - Token לא תקין
```

**תיקון:**
1. חזור ל-[@BotFather](https://t.me/BotFather)
2. שלח `/mybots` → בחר בוט → `API Token`
3. העתק Token חדש
4. עדכן ב-`.env`

### פתרון 2: הבוט לא רץ

```bash
# Windows:
venv\Scripts\activate
python bot.py

# Linux/Mac:
source venv/bin/activate
python bot.py

# אם יש שגיאה - קרא את הודעת השגיאה!
```

### פתרון 3: קשר רשת

```bash
# בדוק אינטרנט:
ping 8.8.8.8

# בדוק גישה לטלגרם:
curl https://api.telegram.org
```

---

## 💾 הבוט מגיב אבל לא שומר ב-Airtable

### אבחון:

הבוט עונה בטלגרם אבל כשבודקים ב-Airtable - שום דבר.

### פתרון 1: API Key/Base ID לא נכונים

```python
# צור קובץ test.py:
from pyairtable import Api
import os

API_KEY = os.getenv('AIRTABLE_API_KEY')
BASE_ID = os.getenv('AIRTABLE_BASE_ID')

print(f"API Key: {API_KEY[:10]}...")
print(f"Base ID: {BASE_ID}")

try:
    api = Api(API_KEY)
    base = api.base(BASE_ID)
    deals = base.table('Deals')
    records = deals.all()
    print(f"✅ הצליח! נמצאו {len(records)} רשומות")
except Exception as e:
    print(f"❌ שגיאה: {e}")
```

```bash
python test.py
```

**אם יש שגיאה:**
- בדוק API Key ב-[airtable.com/account](https://airtable.com/account)
- בדוק Base ID ב-[airtable.com/api](https://airtable.com/api)

### פתרון 2: שמות טבלאות לא נכונים

הטבלאות **חייבות** להיקרא:
- `Deals` (לא "deals", לא "עסקאות")
- `Clients` (לא "clients", לא "לקוחות")
- `Payments` (לא "payments", לא "תשלומים")

**תיקון:**
1. פתח Airtable
2. לחיצה על שם טבלה → Rename
3. שנה ל-`Deals` בדיוק

### פתרון 3: שדות חסרים

```python
# בדוק אילו שדות יש:
from pyairtable import Api
import os

api = Api(os.getenv('AIRTABLE_API_KEY'))
base = api.base(os.getenv('AIRTABLE_BASE_ID'))
deals = base.table('Deals')

# נסה ליצור רשומה:
try:
    record = deals.create({
        'Client': 'Test',
        'Quantity': 10
    })
    print("✅ עובד!")
    deals.delete(record['id'])
except Exception as e:
    print(f"❌ שגיאה: {e}")
```

---

## 📝 שגיאות נפוצות והפתרונות

### שגיאה: `ModuleNotFoundError: No module named 'telegram'`

**סיבה:** החבילות לא מותקנות

**פתרון:**
```bash
pip install -r requirements.txt
```

### שגיאה: `Missing AIRTABLE_API_KEY`

**סיבה:** קובץ `.env` לא קיים או ריק

**פתרון:**
```bash
# בדוק שהקובץ קיים:
ls -la .env

# אם לא קיים:
cp .env.example .env
nano .env
# מלא את הערכים
```

### שגיאה: `Conflict: terminated by other getUpdates`

**סיבה:** הבוט רץ בשני מקומות בו-זמנית

**פתרון:**
```bash
# עצור את כל המופעים:
pkill -f "python bot.py"

# או:
sudo systemctl stop telegram-bot

# חכה 10 שניות
# הפעל מחדש במקום אחד בלבד
```

### שגיאה: `pyairtable.api.types.MissingValueError`

**סיבה:** שדה חובה ריק ב-Airtable

**פתרון:**
- בדוק ב-Airtable שאין שדות שסומנו כ-"Required"
- או: מלא את כל השדות בבוט

### שגיאה: `401 Unauthorized`

**סיבה:** API Key לא תקף

**פתרון:**
1. גש ל-[airtable.com/account](https://airtable.com/account)
2. Revoke API key
3. צור חדש
4. עדכן ב-`.env`

---

## ⚠️ בעיות ביצועים

### הבוט איטי

**סיבות אפשריות:**
1. חיבור אינטרנט איטי
2. Airtable API מגביל (Rate limiting)
3. הרבה רשומות ב-Airtable

**פתרון:**
```python
# הוסף cache ב-airtable_manager.py:
from functools import lru_cache
from datetime import datetime, timedelta

class AirtableManager:
    def __init__(self):
        # ...
        self._cache = {}
        self._cache_time = {}
    
    def get_all_deals(self):
        # בדוק cache
        if 'deals' in self._cache:
            if datetime.now() - self._cache_time['deals'] < timedelta(minutes=5):
                return self._cache['deals']
        
        # שלוף מ-Airtable
        deals = self.deals_table.all()
        self._cache['deals'] = deals
        self._cache_time['deals'] = datetime.now()
        return deals
```

### הבוט מפסיק לעבוד

**סיבות:**
1. Out of memory
2. Crash בגלל exception
3. Connection timeout

**פתרון:**

הוסף error handling טוב יותר:

```python
# בbot.py:
import traceback

async def error_handler(update, context):
    """Log errors"""
    logger.error(f"Exception: {context.error}")
    logger.error(traceback.format_exc())
    
    # שלח לעצמך התראה:
    if update and update.effective_user:
        await context.bot.send_message(
            chat_id=YOUR_ADMIN_CHAT_ID,
            text=f"⚠️ Error: {context.error}"
        )

# ב-main():
application.add_error_handler(error_handler)
```

---

## 🔐 בעיות אבטחה

### מישהו מנסה לפרוץ לבוט

**סימנים:**
- פקודות מוזרות בלוגים
- ניסיונות SQL injection
- Spam של פקודות

**הגנה:**

```python
# הוסף whitelist של משתמשים:
ALLOWED_USERS = [123456789, 987654321]  # Telegram User IDs

async def start(self, update, context):
    user_id = update.effective_user.id
    if user_id not in ALLOWED_USERS:
        await update.message.reply_text("אין לך הרשאה להשתמש בבוט.")
        logger.warning(f"Unauthorized access attempt by {user_id}")
        return
    
    # המשך רגיל...
```

**מציאת User ID שלך:**
```python
# שלח /start לבוט ותראה בלוג:
print(f"User ID: {update.effective_user.id}")
```

---

## 📊 בעיות עם Airtable Views

### View לא מציג נתונים נכונים

**פתרון:**
1. בדוק Filters - אולי יש filter שמסתיר רשומות
2. בדוק Sort - אולי ממוין הפוך
3. נסה "Clear all filters"

### Formula לא עובדת

**בעיות נפוצות:**

❌ שגוי:
```
{Sell Price} - {Buy Price} * {Quantity}
```

✅ נכון:
```
({Sell Price} - {Buy Price}) * {Quantity}
```

**טיפ:** השתמש בסוגריים!

---

## 🌐 בעיות Deployment

### Railway.app - Build fails

**שגיאה:** `No Python version specified`

**פתרון:**
צור `runtime.txt`:
```
python-3.11.0
```

### VPS - Service לא מתחיל

```bash
# ראה מה השגיאה:
sudo journalctl -u telegram-bot -n 50

# שגיאות נפוצות:
# 1. Path לא נכון - בדוק paths ב-service file
# 2. משתני סביבה - ודא ש-.env במקום הנכון
# 3. הרשאות - chmod 644 .env
```

### Docker - Container מת מיד

```bash
# ראה logs:
docker logs telegram-bot

# Debug:
docker run -it telegram-bot /bin/bash
python bot.py
```

---

## 🛠️ כלי עזר לדיבוג

### 1. לוגים מפורטים

```python
# ב-bot.py, שנה:
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG  # במקום INFO
)
```

### 2. בדיקת חיבורים

```bash
# צור test_connections.py:
import os
from pyairtable import Api
import requests

print("🔍 בודק חיבורים...\n")

# 1. Telegram
token = os.getenv('TELEGRAM_BOT_TOKEN')
try:
    r = requests.get(f'https://api.telegram.org/bot{token}/getMe')
    if r.status_code == 200:
        print("✅ Telegram: OK")
        print(f"   Bot: @{r.json()['result']['username']}")
    else:
        print(f"❌ Telegram: Failed ({r.status_code})")
except Exception as e:
    print(f"❌ Telegram: {e}")

# 2. Airtable
print()
try:
    api = Api(os.getenv('AIRTABLE_API_KEY'))
    base = api.base(os.getenv('AIRTABLE_BASE_ID'))
    deals = base.table('Deals')
    records = deals.all(max_records=1)
    print("✅ Airtable: OK")
    print(f"   Base: {os.getenv('AIRTABLE_BASE_ID')}")
except Exception as e:
    print(f"❌ Airtable: {e}")
```

```bash
python test_connections.py
```

---

## 📞 קבלת עזרה

### לוג מפורט לשיתוף

```bash
# רוץ עם debug ושמור ללוג:
python bot.py 2>&1 | tee bot.log

# או אם רץ כשירות:
sudo journalctl -u telegram-bot -n 200 > bot.log
```

### מידע שימושי לשיתוף:

```bash
# גרסאות:
python --version
pip list | grep telegram
pip list | grep airtable

# מערכת:
uname -a  # Linux
ver  # Windows

# קבצים:
ls -la

# קובץ .env (בלי ערכים רגישים!):
cat .env | sed 's/=.*/=***/'
```

---

## ✅ Checklist דיבוג

כשיש בעיה, עבור על זה:

- [ ] הבוט רץ? (`python bot.py` או `systemctl status`)
- [ ] Token תקין? (בדוק עם `getMe`)
- [ ] API Key תקין? (בדוק עם `test.py`)
- [ ] שמות טבלאות נכונים? (`Deals`, `Clients`, `Payments`)
- [ ] קובץ `.env` קיים ומלא?
- [ ] חיבור אינטרנט תקין?
- [ ] Logs נקיים משגיאות?
- [ ] נסיתי להפעיל מחדש?
- [ ] עדכנתי חבילות? (`pip install -U -r requirements.txt`)

---

**רוב הבעיות נפתרות עם restart פשוט! 🔄**

אם לא - בדוק את הלוגים ותראה מה השגיאה.
