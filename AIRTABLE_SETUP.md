# 📊 מדריך הקמת Airtable CRM - צעד אחר צעד

מדריך מפורט ומאויר להקמת מסד הנתונים ב-Airtable

---

## 🎯 מטרה

ליצור מסד נתונים מאורגן שישמש כ-CRM (מערכת ניהול קשרי לקוחות) לעסקאות הלידים שלך.

---

## 📋 תוכן עניינים

1. [הרשמה ויצירת Base](#שלב-1-הרשמה-ויצירת-base)
2. [יצירת טבלת Deals](#שלב-2-טבלת-deals-עסקאות)
3. [יצירת טבלת Clients](#שלב-3-טבלת-clients-לקוחות)
4. [יצירת טבלת Payments](#שלב-4-טבלת-payments-תשלומים)
5. [קבלת API Key](#שלב-5-קבלת-api-key)
6. [קבלת Base ID](#שלב-6-קבלת-base-id)
7. [בדיקה](#שלב-7-בדיקה)

---

## שלב 1: הרשמה ויצירת Base

### 1.1 הרשמה ל-Airtable

1. גש ל-[https://airtable.com](https://airtable.com)
2. לחץ על **"Sign up for free"**
3. השתמש ב-Google/Apple או מייל + סיסמה
4. אשר את המייל

### 1.2 יצירת Base חדש

1. לחיצה על **"Create a base"** או **"+"** למעלה
2. בחר **"Start from scratch"**
3. תן שם: **`Leads CRM`**
4. בחר צבע/אייקון (אופציונלי)

---

## שלב 2: טבלת Deals (עסקאות)

### 2.1 שינוי שם הטבלה הראשונה

1. הטבלה הראשונה נוצרת אוטומטית בשם "Table 1"
2. לחץ על חץ ליד "Table 1" → **"Rename table"**
3. שנה ל-**`Deals`**

### 2.2 הוספת שדות

**הסר את השדות הקיימים:**
- לחץ על חץ ליד "Name", "Notes", "Attachments" → **"Delete field"**

**עכשיו נוסיף את השדות החדשים:**

#### שדה 1: Client (לקוח)
1. לחץ **"+"** בצד ימין של השדות
2. בחר **"Single line text"**
3. שם השדה: `Client`
4. לחץ **"Create field"**

#### שדה 2: Supplier (ספק)
- סוג: **Single line text**
- שם: `Supplier`

#### שדה 3: Quantity (כמות)
- סוג: **Number**
- שם: `Quantity`
- Format: Integer (מספר שלם)

#### שדה 4: Country (מדינה)
- סוג: **Single line text**
- שם: `Country`

#### שדה 5: Delivery Date (תאריך אספקה)
- סוג: **Date**
- שם: `Delivery Date`
- Date format: בחר פורמט מועדף (למשל DD/MM/YYYY)
- Include time: אופציונלי

#### שדה 6: Buy Price (מחיר קנייה)
- סוג: **Currency**
- שם: `Buy Price`
- Precision: 2 decimal places
- Currency: USD ($)

#### שדה 7: Sell Price (מחיר מכירה)
- סוג: **Currency**
- שם: `Sell Price`
- Precision: 2 decimal places
- Currency: USD ($)

#### שדה 8: Profit (רווח) - מחושב
- סוג: **Formula**
- שם: `Profit`
- Formula:
```
({Sell Price} - {Buy Price}) * {Quantity}
```
- Formatting: Currency (USD)

#### שדה 9: Price Per Lead (מחיר ללייד)
- סוג: **Formula**
- שם: `Price Per Lead`
- Formula:
```
IF({Quantity} > 0, {Sell Price}, 0)
```
- Formatting: Currency (USD)

#### שדה 10: Deal Type (סוג עסקה)
- סוג: **Single select**
- שם: `Deal Type`
- Options:
  - `קנייה` (צבע: כחול)
  - `מכירה` (צבע: ירוק)

#### שדה 11: Raw Text (טקסט מקורי)
- סוג: **Long text**
- שם: `Raw Text`
- Enable rich text: לא

#### שדה 12: Telegram User
- סוג: **Single line text**
- שם: `Telegram User`

#### שדה 13: Telegram Group
- סוג: **Single line text**
- שם: `Telegram Group`

#### שדה 14: Status (סטטוס)
- סוג: **Single select**
- שם: `Status`
- Options:
  - `פעיל` (צבע: ירוק)
  - `הושלם` (צבע: כחול)
  - `בוטל` (צבע: אדום)

#### שדה 15: Created Date (תאריך יצירה)
- סוג: **Created time**
- שם: `Created Date`
- Date format: בחר פורמט מועדף
- Include time: כן

### 2.3 תצוגת הטבלה

הטבלה אמורה להיראות כך:

| Client | Supplier | Quantity | Country | Delivery Date | Buy Price | Sell Price | Profit | Price Per Lead | Deal Type | Raw Text | Telegram User | Telegram Group | Status | Created Date |
|--------|----------|----------|---------|---------------|-----------|------------|--------|----------------|-----------|----------|---------------|----------------|--------|--------------|
| (ריק)  | (ריק)    | (ריק)    | (ריק)   | (ריק)         | (ריק)     | (ריק)      | (מחושב)| (מחושב)        | (בחירה)   | (ריק)    | (ריק)         | (ריק)          | (בחירה)| (אוטומטי)    |

---

## שלב 3: טבלת Clients (לקוחות)

### 3.1 יצירת טבלה חדשה

1. לחץ על **"+"** ליד "Deals" (למטה משמאל)
2. בחר **"Create empty table"**
3. שנה שם ל-**`Clients`**

### 3.2 הוספת שדות

#### שדה 1: Name (שם)
- סוג: **Single line text**
- שם: `Name`

#### שדה 2: Type (סוג)
- סוג: **Single select**
- שם: `Type`
- Options:
  - `לקוח` (צבע: כחול)
  - `ספק` (צבע: סגול)

#### שדה 3: Telegram User
- סוג: **Single line text**
- שם: `Telegram User`

#### שדה 4: Added Date
- סוג: **Created time**
- שם: `Added Date`

#### שדה 5: Total Deals (סה"כ עסקאות)
- סוג: **Number**
- שם: `Total Deals`
- Format: Integer
- (**הערה:** זה ימולא ידנית או דרך automation)

#### שדה 6: Total Revenue (סה"כ הכנסות)
- סוג: **Currency**
- שם: `Total Revenue`
- Currency: USD

---

## שלב 4: טבלת Payments (תשלומים)

### 4.1 יצירת טבלה חדשה

1. לחץ **"+"** ליד "Clients"
2. בחר **"Create empty table"**
3. שנה שם ל-**`Payments`**

### 4.2 הוספת שדות

#### שדה 1: Deal ID
- סוג: **Single line text**
- שם: `Deal ID`

#### שדה 2: Amount (סכום)
- סוג: **Currency**
- שם: `Amount`
- Currency: USD

#### שדה 3: Payment Date
- סוג: **Date**
- שם: `Payment Date`
- Include time: כן

#### שדה 4: Telegram User
- סוג: **Single line text**
- שם: `Telegram User`

#### שדה 5: Type (סוג תשלום)
- סוג: **Single select**
- שם: `Type`
- Options:
  - `התקבל` (צבע: ירוק)
  - `שולם` (צבע: אדום)

---

## שלב 5: קבלת API Key

### 5.1 גישה להגדרות החשבון

1. לחץ על האייקון שלך בפינה השמאלית עליונה
2. בחר **"Account"**
3. גלול למטה עד **"API"** section

### 5.2 יצירת API Key

1. לחץ על **"Generate API key"**
2. Key יופיע - **שמור אותו במקום בטוח!**
3. הוא נראה כך: `keyXXXXXXXXXXXXXX`

**⚠️ אזהרה:**
- ה-API Key הוא כמו סיסמה!
- אל תשתף אותו
- אם חושף - צור חדש

---

## שלב 6: קבלת Base ID

### 6.1 דרך ה-API Documentation

1. גש ל-[https://airtable.com/api](https://airtable.com/api)
2. בחר את ה-Base שיצרת (`Leads CRM`)
3. בדף שנפתח, ב-URL תראה:
```
https://airtable.com/YOUR_BASE_ID/api/docs
```
4. ה-Base ID הוא החלק `appXXXXXXXXXXXXXX`
5. העתק אותו

### 6.2 דרך חלופית - מה-URL

1. פתח את ה-Base
2. ראה את ה-URL:
```
https://airtable.com/appXXXXXXXXXXXXXX/tblYYYYYYYYYYYYYY
```
3. החלק `appXXXXXXXXXXXXXX` הוא ה-Base ID

---

## שלב 7: בדיקה

### 7.1 בדיקה ידנית

1. הוסף רשומה ידנית לטבלת Deals:
   - Client: `בדיקה`
   - Quantity: `10`
   - Buy Price: `5`
   - Sell Price: `10`
   
2. שדה Profit צריך להראות אוטומטית: `50`

### 7.2 בדיקה עם Python

צור קובץ `test_airtable.py`:

```python
from pyairtable import Api

API_KEY = 'keyXXXXXXXXXXXXXX'  # החלף
BASE_ID = 'appXXXXXXXXXXXXXX'  # החלף

api = Api(API_KEY)
base = api.base(BASE_ID)

# בדיקת חיבור
try:
    deals_table = base.table('Deals')
    records = deals_table.all()
    print(f"✅ חיבור הצליח! נמצאו {len(records)} רשומות")
except Exception as e:
    print(f"❌ שגיאה: {e}")
```

הרץ:
```bash
python test_airtable.py
```

---

## 🎨 טיפים להתאמה אישית

### תצוגות (Views)

צור תצוגות שונות לצרכים שונים:

**תצוגה 1: עסקאות פעילות**
1. ליד "All Deals" לחץ **"+"**
2. שם: `פעיל`
3. הוסף Filter: `Status = פעיל`
4. Sort: `Created Date` (descending)

**תצוגה 2: עסקאות השבוע**
- Filter: `Created Date is within the last week`

**תצוגה 3: לפי לקוח**
- Group by: `Client`

### צבעים ותיוג

- לחץ על רשומה → צבע ברקע
- הוסף תיוגים בשדות Select
- התאם צבעים לסטטוסים

### Automations

הגדר אוטומציות:
1. לחץ על **"Automations"** למעלה
2. דוגמה: שלח מייל כשעסקה חדשה נוצרת
3. דוגמה: עדכן סטטוס אחרי 7 ימים

---

## 🔐 הגדרות אבטחה

### שיתוף ה-Base

1. לחץ **"Share"** בפינה הימנית עליונה
2. הוסף משתמשים במידת הצורך
3. קבע הרשאות:
   - **Editor**: קריאה + כתיבה
   - **Commenter**: רק הערות
   - **Read only**: רק קריאה

**⚠️ לבוט צריך הרשאות Editor!**

### גיבוי

1. לחץ על `...` ליד שם ה-Base
2. **"Duplicate base"**
3. עשה גיבוי אחת לשבוע

---

## 📊 מבנה מומלץ

```
Leads CRM (Base)
│
├── Deals (טבלה)
│   ├── 15 שדות
│   └── Views: All, Active, This Week, By Client
│
├── Clients (טבלה)
│   ├── 6 שדות
│   └── Views: All, Customers, Suppliers
│
└── Payments (טבלה)
    ├── 5 שדות
    └── Views: All, Received, Paid
```

---

## ✅ Checklist סיום

- [ ] Base נוצר בשם `Leads CRM`
- [ ] טבלת Deals עם כל 15 השדות
- [ ] טבלת Clients עם כל 6 השדות
- [ ] טבלת Payments עם כל 5 השדות
- [ ] Formula ב-Profit עובדת
- [ ] API Key נשמר במקום בטוח
- [ ] Base ID נשמר
- [ ] בדיקה עם Python הצליחה
- [ ] הרשאות מוגדרות נכון

---

## 🆘 בעיות נפוצות

### "Could not find table Deals"
- **פתרון:** ודא ששם הטבלה הוא `Deals` בדיוק (אותיות גדולות)

### "Invalid API key"
- **פתרון:** העתק את ה-Key שוב, ללא רווחים

### "Permission denied"
- **פתרון:** ב-Share → ודא שיש הרשאות Editor

### Formula לא עובדת
- **פתרון:** ודא שמות שדות נכונים בתוך `{}` בדיוק כמו בטבלה

---

**סיימת! 🎉**

המסד נתונים מוכן לשימוש עם הבוט!

חזור ל-[README.md](README.md) להמשך ההקמה.
