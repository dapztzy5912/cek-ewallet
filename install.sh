#!/bin/bash
echo "🔧 Menginstal dependensi..."
pkg update -y
pkg install python -y
pip install requests colorama

echo "✅ Instalasi selesai!"
echo "📌 Jalankan dengan: python cek_ewallet.py"
