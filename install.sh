#!/bin/bash
# סקריפט התקנה מהיר

echo "🚀 מתחיל התקנה..."

# בדיקת Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 לא מותקן. מתקין..."
    sudo apt update
    sudo apt install -y python3 python3-pip python3-venv
fi

echo "✅ Python מותקן"

# יצירת סביבה וירטואלית
echo "📦 יוצר סביבה וירטואלית..."
python3 -m venv venv

# הפעלת הסביבה
source venv/bin/activate

# התקנת תלויות
echo "📥 מתקין חבילות..."
pip install --upgrade pip
pip install -r requirements.txt

echo ""
echo "✅ ההתקנה הושלמה!"
echo ""
echo "📝 הוראות:"
echo "1. צור קובץ .env מהקובץ .env.example"
echo "2. מלא את הערכים (TOKEN, API_KEY, BASE_ID)"
echo "3. הרץ: python bot.py"
echo ""
echo "או הרץ:"
echo "  cp .env.example .env"
echo "  nano .env"
echo "  python bot.py"
echo ""
