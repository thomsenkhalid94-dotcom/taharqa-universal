import zipfile, time, os, sys

# --- الوان ---
R = "\033[91m"  # احمر
G = "\033[92m"  # اخضر
Y = "\033[93m"  # اصفر
C = "\033[96m"  # سماوي
M = "\033[95m"  # بنفسجي
W = "\033[97m"  # ابيض
B = "\033[94m"  # ازرق
RESET = "\033[0m"
BOLD = "\033[1m"

def banner():
    os.system('cls' if os.name=='nt' else 'clear')
    print(f"{M}{BOLD}")
    print(r"""
 ████████╗ █████╗ ██╗  ██╗ █████╗ ██████╗  ██████╗  █████╗ 
 ╚══██╔══╝██╔══██╗██║  ██║██╔══██╗██╔══██╗██╔═══██╗██╔══██╗
    ██║   ███████║███████║███████║██████╔╝██║   ██║███████║
    ██║   ██╔══██║██╔══██║██╔══██║██╔══██╗██║▄▄ ██║██╔══██║
    ██║   ██║  ██║██║  ██║██║  ██║██║  ██║╚██████╔╝██║  ██║
    ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚══▀▀═╝ ╚═╝  ╚═╝
    """)
    print(f"{C}       LEGENDARY EDITION - MADE BY TAHARQA {RESET}")
    print(f"{Y}══════════════════════════════════════════════════════{RESET}\n")

def crack(zip_file, wordlists):
    banner()
    
    if not os.path.exists(zip_file):
        print(f"{R}[!] zipfileالملف {zip_file} unfoundما لقيتو{RESET}")
        return

    print(f"{B}[*] targetالهدف:{RESET} {W}{zip_file}{RESET}")
    print(f"{B}[*] menusالقوائم:{RESET} {W}{', '.join(wordlists)}{RESET}")
    print(f"{Y}══════════════════════════════════════════════════════{RESET}\n")

    total_attempts = 0
    start_time = time.time()

    try:
        with zipfile.ZipFile(zip_file) as zf:
            for wl in wordlists:
                if not os.path.exists(wl):
                    print(f"{R}[!] menu القائمة {wl} unfound will passما موجودة - بنطها{RESET}")
                    continue
                
                print(f"{C}[+] try a list بجرب في قائمة: {wl} {RESET}")
                
                with open(wl, 'r', encoding='utf-8', errors='ignore') as f:
                    for line in f:
                        password = line.strip()
                        if not password:
                            continue
                        
                        total_attempts += 1
                        
                        # العداد الاسطوري
                        elapsed = time.time() - start_time
                        sys.stdout.write(f"\r{Y}[{total_attempts}] {W} Trying بجرب: {R}{password:<30} {C}| {elapsed:.1f}s{RESET}")
                        sys.stdout.flush()

                        try:
                            zf.extractall(pwd=password.encode())
                            print(f"\n\n{G}{BOLD}═══════════════════════════════════════════{RESET}")
                            print(f"{G}{BOLD}  [✓] found لقيتوووووووووووو!{RESET}")
                            print(f"{G}{BOLD}═══════════════════════════════════════════{RESET}")
                            print(f"{W} passwdالباسويرد هو: {G}{BOLD}{password}{RESET}")
                            print(f"{W} mount of tryعدد المحاولات: {Y}{total_attempts}{RESET}")
                            print(f"{W} timeالزمن: {C}{elapsed:.2f} ثانيةSec{RESET}")
                            print(f"{G}{BOLD}═══════════════════════════════════════════{RESET}\n")
                            return
                        except:
                            continue
            
            print(f"\n\n{R}[×] passwd un foundللأسف ما لقيت الباسويرد بعد {total_attempts} محاولة{RESET}")

    except zipfile.BadZipFile:
        print(f"{R}[!] un workable zipfileدا ما ملف zip صالح{RESET}")

if __name__ == "__main__":
    # هنا عدل اسامي الملفات لو عايز
    ZIP = input("[?] put zipfile دخل اسم ملف الـ zip: ").strip()
if not ZIP:
    ZIP = "khwajja.zip"  # غير اسم ملفك هنا
    WORDLISTS = ["rockyou-mini.txt", "خازوق.txt", "خوازيق.txt"]
    
    wordlist = input("[?] دخل اسم قائمة كلمات السر (Enter = rockyou-mini.txt): ").strip()
if not wordlist:
    wordlist = "rockyou-mini.txt"

    WORDLISTS = [wordlist]
    crack(ZIP, WORDLISTS)
