# 🚀 מדריך Deployment - הרצת הבוט בשרת

מדריך להעלאה והרצת הבוט בשרת באופן תמידי (24/7)

---

## 🎯 אפשרויות Deployment

1. **Railway.app** - הכי קל, חינמי, מומלץ למתחילים
2. **VPS** (DigitalOcean, AWS, Vultr) - שליטה מלאה
3. **Docker** - מתקדם
4. **Heroku** - קל אבל בתשלום

---

## אופציה 1: Railway.app (מומלץ)

### יתרונות:
- ✅ חינמי עד 500 שעות/חודש
- ✅ פריסה פשוטה מ-GitHub
- ✅ ניהול משתני סביבה קל
- ✅ לוגים בזמן אמת

### שלבים:

#### 1. העלאה ל-GitHub

```bash
# אתחול Git
cd telegram-leads-bot
git init

# הוספת קבצים
git add .
git commit -m "Initial commit"

# יצירת Repository ב-GitHub
# גש ל-github.com → New repository → telegram-leads-bot

# חיבור וה upload
git remote add origin https://github.com/YOUR_USERNAME/telegram-leads-bot.git
git branch -M main
git push -u origin main
```

#### 2. הגדרה ב-Railway

1. גש ל-[railway.app](https://railway.app)
2. לחץ **"Start a New Project"**
3. בחר **"Deploy from GitHub repo"**
4. חבר את חשבון GitHub שלך
5. בחר את הrepository `telegram-leads-bot`
6. Railway יזהה שזה Python project

#### 3. הגדרת משתני סביבה

1. בדף הפרויקט לחץ על **"Variables"**
2. הוסף:
   - `TELEGRAM_BOT_TOKEN` = [ה-Token שלך]
   - `AIRTABLE_API_KEY` = [ה-API Key שלך]
   - `AIRTABLE_BASE_ID` = [ה-Base ID שלך]

#### 4. Deploy

- Railway יעשה Deploy אוטומטית
- צפה בלוגים ב-**"Deployments"** tab
- הבוט אמור לרוץ תוך דקה

#### 5. בדיקה

1. פתח את הבוט בטלגרם
2. שלח `/start`
3. אם מגיב - הצלחת! 🎉

---

## אופציה 2: VPS (Ubuntu Server)

### דרישות:
- שרת עם Ubuntu 20.04+
- גישת SSH
- 1GB RAM מינימום

### שלב 1: התחברות לשרת

```bash
ssh user@your-server-ip
```

### שלב 2: הכנת השרת

```bash
# עדכון מערכת
sudo apt update && sudo apt upgrade -y

# התקנת Python
sudo apt install -y python3 python3-pip python3-venv git

# יצירת משתמש לבוט (אופציונלי אבל מומלץ)
sudo useradd -m -s /bin/bash botuser
sudo su - botuser
```

### שלב 3: העלאת קבצים

**אופציה A: Git Clone**

```bash
cd ~
git clone https://github.com/YOUR_USERNAME/telegram-leads-bot.git
cd telegram-leads-bot
```

**אופציה B: SCP (העתקה ישירה)**

```bash
# מהמחשב המקומי:
scp -r telegram-leads-bot user@your-server-ip:~/
```

### שלב 4: התקנה

```bash
# הרצת סקריפט ההתקנה
chmod +x install.sh
./install.sh

# או ידנית:
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### שלב 5: הגדרת משתני סביבה

```bash
# יצירת קובץ .env
cp .env.example .env
nano .env
```

מלא:
```env
TELEGRAM_BOT_TOKEN=1234567890:ABC...
AIRTABLE_API_KEY=keyXXXX...
AIRTABLE_BASE_ID=appXXXX...
```

שמור: `Ctrl+O`, `Enter`, `Ctrl+X`

### שלב 6: בדיקה ראשונית

```bash
# הפעלה ידנית לבדיקה
source venv/bin/activate
python bot.py
```

אם הכל עובד, תראה:
```
INFO - 🚀 Bot is starting...
```

לעצור: `Ctrl+C`

### שלב 7: הגדרת Systemd (ריצה תמידית)

```bash
# עריכת קובץ השירות
nano telegram-bot.service
```

החלף `YOUR_USERNAME_HERE` ב-username שלך (למשל `botuser`)

```bash
# העתקה ל-systemd
sudo cp telegram-bot.service /etc/systemd/system/

# הפעלת השירות
sudo systemctl daemon-reload
sudo systemctl enable telegram-bot
sudo systemctl start telegram-bot

# בדיקת סטטוס
sudo systemctl status telegram-bot
```

אם פעיל, תראה:
```
● telegram-bot.service - Telegram Leads Bot
   Active: active (running)
```

### שלב 8: ניהול הבוט

```bash
# הפסקת הבוט
sudo systemctl stop telegram-bot

# הפעלה מחדש
sudo systemctl restart telegram-bot

# צפייה בלוגים
sudo journalctl -u telegram-bot -f

# צפייה ב-50 שורות אחרונות
sudo journalctl -u telegram-bot -n 50
```

---

## אופציה 3: Docker

### Dockerfile

צור קובץ `Dockerfile`:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "bot.py"]
```

### docker-compose.yml

```yaml
version: '3.8'

services:
  telegram-bot:
    build: .
    container_name: leads-bot
    restart: always
    env_file:
      - .env
    volumes:
      - ./:/app
```

### הרצה

```bash
# בנייה
docker-compose build

# הפעלה
docker-compose up -d

# לוגים
docker-compose logs -f

# עצירה
docker-compose down
```

---

## 🔧 טיפים ופתרון בעיות

### בדיקת קישוריות

```bash
# בדיקת חיבור לטלגרם
curl https://api.telegram.org/bot<YOUR_TOKEN>/getMe

# בדיקת חיבור ל-Airtable
python3 -c "from pyairtable import Api; print('OK')"
```

### בעיות נפוצות

#### הבוט לא עונה

1. בדוק שהשירות רץ:
```bash
sudo systemctl status telegram-bot
```

2. ראה לוגים:
```bash
sudo journalctl -u telegram-bot -n 100
```

3. בדוק Token:
```bash
cat .env | grep TELEGRAM_BOT_TOKEN
```

#### Out of Memory

```bash
# בדוק זיכרון
free -h

# הוסף Swap (אם צריך)
sudo fallocate -l 1G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
```

#### הבוט מתנתק

- וודא ש-`Restart=always` ב-service file
- בדוק לוגים לשגיאות חוזרות

---

## 📊 Monitoring

### הגדרת התראות

**Telegram Alert Bot:**

```python
# בתוך bot.py, הוסף:
import requests

ADMIN_CHAT_ID = 'YOUR_CHAT_ID'

def send_admin_alert(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, json={
        'chat_id': ADMIN_CHAT_ID,
        'text': f"⚠️ Alert: {message}"
    })

# שימוש:
try:
    # קוד
except Exception as e:
    send_admin_alert(f"Error: {e}")
```

### Uptime Monitor

השתמש ב-[UptimeRobot](https://uptimerobot.com) (חינמי):
1. צור monitor חדש
2. בחר "Keyword"
3. URL: Telegram getUpdates endpoint
4. קבל התראות אם הבוט נופל

---

## 🔒 אבטחה

### Firewall

```bash
# אפשר רק SSH
sudo ufw allow ssh
sudo ufw enable
```

### SSL (אם משתמש בWebhook)

```bash
# התקנת Certbot
sudo apt install -y certbot

# קבלת תעודה
sudo certbot certonly --standalone -d yourdomain.com
```

### עדכוני אבטחה אוטומטיים

```bash
sudo apt install -y unattended-upgrades
sudo dpkg-reconfigure -plow unattended-upgrades
```

---

## 📈 Scale Up

### Multiple Bots

```bash
# בוט 1
cp -r telegram-leads-bot bot1
cd bot1
# שנה .env עם token אחר
# שנה service name

# בוט 2
cp -r telegram-leads-bot bot2
cd bot2
# חזור על התהליך
```

### Load Balancing

אם יש הרבה תעבורה, שקול:
- Redis לqueue
- Multiple workers
- Kubernetes

---

## ✅ Checklist Deployment

- [ ] שרת מוכן
- [ ] Python מותקן
- [ ] קבצים הועלו
- [ ] .env מוגדר נכון
- [ ] התקנה עברה בהצלחה
- [ ] בדיקה ידנית עבדה
- [ ] Systemd service מוגדר
- [ ] הבוט רץ כשירות
- [ ] בדיקת restart אחרי reboot
- [ ] לוגים נראים תקינים
- [ ] בוט עונה בטלגרם
- [ ] נתונים נשמרים ב-Airtable

---

## 🆘 תמיכה

אם תקוע:

1. בדוק לוגים:
```bash
sudo journalctl -u telegram-bot -n 100 --no-pager
```

2. בדוק משתני סביבה:
```bash
cat .env
```

3. הרץ ידנית לדיבוג:
```bash
source venv/bin/activate
python bot.py
```

4. בדוק שורות האחרונות בלוג:
```bash
tail -f /var/log/syslog | grep python
```

---

**הבוט שלך כעת רץ 24/7! 🎉**

חזור ל-[README.md](README.md) למידע נוסף.
