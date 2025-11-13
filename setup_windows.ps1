# סקריפט התקנה אוטומטי לWindows
# Telegram Leads Bot Setup

Write-Host "🤖 התקנת Telegram Leads Bot" -ForegroundColor Cyan
Write-Host "================================" -ForegroundColor Cyan
Write-Host ""

# בדיקת Python
Write-Host "1️⃣ בודק Python..." -ForegroundColor Yellow
try {
    $pythonVersion = python --version 2>&1
    Write-Host "✅ נמצא: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ Python לא מותקן! התקן Python 3.9+ מ-python.org" -ForegroundColor Red
    exit 1
}

# יצירת סביבה וירטואלית
Write-Host ""
Write-Host "2️⃣ יוצר סביבה וירטואלית..." -ForegroundColor Yellow
if (Test-Path "venv") {
    Write-Host "⚠️ venv כבר קיים, מדלג" -ForegroundColor Yellow
} else {
    python -m venv venv
    Write-Host "✅ סביבה וירטואלית נוצרה" -ForegroundColor Green
}

# הפעלת סביבה וירטואלית
Write-Host ""
Write-Host "3️⃣ מפעיל סביבה וירטואלית..." -ForegroundColor Yellow
& "venv\Scripts\Activate.ps1"
Write-Host "✅ סביבה וירטואלית הופעלה" -ForegroundColor Green

# התקנת תלויות
Write-Host ""
Write-Host "4️⃣ מתקין חבילות Python..." -ForegroundColor Yellow
pip install --upgrade pip
pip install -r requirements.txt
Write-Host "✅ חבילות הותקנו בהצלחה" -ForegroundColor Green

# יצירת .env אם לא קיים
Write-Host ""
Write-Host "5️⃣ בודק קובץ .env..." -ForegroundColor Yellow
if (Test-Path ".env") {
    Write-Host "⚠️ .env כבר קיים" -ForegroundColor Yellow
} else {
    @"
# Telegram Bot Configuration
TELEGRAM_BOT_TOKEN=your_bot_token_here

# Airtable Configuration
AIRTABLE_API_KEY=your_airtable_api_key_here
AIRTABLE_BASE_ID=your_airtable_base_id_here
"@ | Out-File -FilePath ".env" -Encoding UTF8
    Write-Host "✅ קובץ .env נוצר" -ForegroundColor Green
}

Write-Host ""
Write-Host "================================" -ForegroundColor Cyan
Write-Host "✅ ההתקנה הושלמה!" -ForegroundColor Green
Write-Host ""
Write-Host "📝 הצעדים הבאים:" -ForegroundColor Yellow
Write-Host "1. ערוך את הקובץ .env והוסף את המפתחות שלך:" -ForegroundColor White
Write-Host "   notepad .env" -ForegroundColor Cyan
Write-Host ""
Write-Host "2. הרץ את הבוט:" -ForegroundColor White
Write-Host "   venv\Scripts\Activate.ps1" -ForegroundColor Cyan
Write-Host "   python bot.py" -ForegroundColor Cyan
Write-Host ""
Write-Host "📚 לתיעוד מלא: README.md" -ForegroundColor Yellow
Write-Host ""

