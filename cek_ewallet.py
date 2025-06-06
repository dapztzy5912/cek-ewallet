import requests
from colorama import Fore, init

init(autoreset=True)

def check_gopay(phone):
    url = "https://goid.gojekapi.com/v5/customers"
    headers = {
        "X-AppVersion": "3.30.2",
        "X-Platform": "Android",
        "X-UniqueId": "123456789",
        "X-Session-ID": "123",
        "Content-Type": "application/json; charset=UTF-8"
    }
    data = {"phone": phone}
    try:
        res = requests.post(url, json=data, headers=headers)
        if "already registered" in res.text or res.status_code == 409:
            return Fore.RED + "✅ Terdaftar"
        elif res.status_code == 200:
            return Fore.GREEN + "❌ Belum terdaftar"
        else:
            return Fore.YELLOW + "⚠️ Tidak bisa dicek"
    except:
        return Fore.YELLOW + "⚠️ Error koneksi"

def check_dana(phone):
    url = "https://api.dana.id/middleware/api/login/otp-request"
    headers = {
        "Content-Type": "application/json",
        "app-id": "com.dana.id",
    }
    json_data = {
        "mobile": phone,
        "otpType": "LOGIN",
        "source": "login"
    }
    try:
        res = requests.post(url, json=json_data, headers=headers)
        if res.status_code == 200:
            return Fore.RED + "✅ Terdaftar"
        elif res.status_code == 400:
            return Fore.GREEN + "❌ Belum terdaftar"
        else:
            return Fore.YELLOW + "⚠️ Tidak bisa dicek"
    except:
        return Fore.YELLOW + "⚠️ Error koneksi"

def banner():
    print(Fore.CYAN + """
╔═╗┌─┐┬ ┬┌─┐┌─┐┌─┐┬ ┬
║ ╦│ ││ │├─┘├─┤│  ├─┤
╚═╝└─┘└─┘┴  ┴ ┴└─┘┴ ┴
 Cek Nomor E-Wallet
""")

if __name__ == "__main__":
    banner()
    phone = input(Fore.LIGHTMAGENTA_EX + "Masukkan nomor HP (format +62): ")

    print(Fore.LIGHTYELLOW_EX + "\n🔍 Mengecek GoPay...")
    print("GoPay      ➜", check_gopay(phone))

    print(Fore.LIGHTYELLOW_EX + "\n🔍 Mengecek Dana...")
    print("Dana       ➜", check_dana(phone))

    print(Fore.LIGHTBLACK_EX + "\n⚠️  Note: Hasil bisa berubah tergantung keamanan sistem mereka.")
