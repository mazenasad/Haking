#!/bin/bash

# تنظيف الشاشة والألوان
clear
green='\e[1;32m'
blue='\e[1;34m'
reset='\e[0m'

echo -e "${blue}جاري تشغيل مشروع Mazen-Hacking-Lab...${reset}"

# تشغيل السيرفر في الخلفية
python3 server.py &
sleep 2

# التأكد من وجود أداة Cloudflare
if [[ ! -f "cloudflared" ]]; then
    echo "تحميل محرك Cloudflare..."
    wget https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64 -O cloudflared
    chmod +x cloudflared
fi

# فتح النفق والحصول على الرابط
echo -e "${green}جاري توليد رابط Cloudflare الحقيقي...${reset}"
./cloudflared tunnel --url http://localhost:8080 > tunnel.log 2>&1 &
sleep 10

# استخراج الرابط من ملف السجل
final_link=$(grep -o 'https://[-0-9a-z.]*.trycloudflare.com' tunnel.log)

echo -e "${green}==========================================="
echo -e "           تم النجاح بالاختراق!            "
echo -e "==========================================="
echo -e "رابط التدريب العالمي الخاص بك هو:"
echo -e "${blue}$final_link${reset}"
echo -e "${green}===========================================${reset}"

# مراقبة النتائج فور وصولها
tail -f log.txt

