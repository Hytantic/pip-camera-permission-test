#!/bin/bash

# Renk tanımlamaları (Profesyonel görünüm için)
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m' # Renk yok

echo -e "${BLUE}[*] Kurulum başlatılıyor...${NC}"

# 1. Paket Güncelleme ve Python Kontrolü
echo -e "${BLUE}[*] Sistem paketleri kontrol ediliyor...${NC}"
if [ -d "/data/data/com.termux" ]; then
    # Termux ortamı
    pkg update && pkg upgrade -y
    pkg install python -y
else
    # Kali veya diğer Linux ortamları
    sudo apt update
    sudo apt install python3 python3-pip -y
fi

# 2. Python Kütüphanelerini Kur (requirements.txt üzerinden)
if [ -f "requirements.txt" ]; then
    echo -e "${BLUE}[*] Python kütüphaneleri kuruluyor...${NC}"
    pip install -r requirements.txt
else
    echo -e "${RED}[!] requirements.txt bulunamadı! Flask manuel kuruluyor...${NC}"
    pip install flask
fi

# 3. Klasör Kontrolü
if [ ! -d "captured_videos" ]; then
    mkdir captured_videos
    echo -e "${GREEN}[+] 'captured_videos' klasörü oluşturuldu.${NC}"
fi

# 4. Cloudflared Kurulumu (İnternete açmak için opsiyonel)
echo -e "${BLUE}[*] Cloudflared kontrol ediliyor...${NC}"
if ! command -v cloudflared &> /dev/null; then
    echo -e "${RED}[!] Cloudflared bulunamadı. Kurmak için GitHub sayfasındaki talimatları izleyin.${NC}"
fi

echo -e "${GREEN}[+] Kurulum başarıyla tamamlandı!${NC}"
echo -e "${BLUE}[!] Başlatmak için: ${NC}python app.py"