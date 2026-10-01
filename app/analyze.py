print("--- TAHARQA SOC ANALYSIS ---")
try:
    with open("waf.log") as f:
        lines = f.readlines()
    xss = sum(1 for l in lines if "script" in l.lower())
    print(f"XSS attempts: {xss}")
    print(f"Total lines: {len(lines)}")
    if xss > 0:
        print("[!] ALERT: XSS Attack Detected!")
except:
    print("No waf.log yet - attack the server first")
print("   ")
print(" ===================================================*by.khwajja.Sec®*=====")
