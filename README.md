# TAHARQA SEC LAB | مختبر طهارقا الأمني
### Built Offline from SDN | تم بناءه في السودان

*_** _ _ _ ** *_ _
__ __   / \                                     _ \ / _ \ / \
        / _ \           __                              _)                             / _ \
        / ___ \| __             _ <             _               / ___ \
_       /_/ \_\_                _               _       \_\ \__\_\ /_/ \_\
LAB by khwajja.sec | Medani, SD

[Python](https://img.shields.io/badge/Python-3.11-blue)
[Docker](https://img.shields.io/badge/Docker-Ready-2496ED)
[Offline](https://img.shields.io/badge/Built-100%25%20Offline-success)

---
### 🇸🇩 عربي

مختبر أمن سيبراني هجومي ودفاعي، مبني **100% أوفلاين** من تلفون أندرويد في مدني  أثناء انقطاع الإنترنت والكهرباء.

**يشتغل على:** تلفون (Termux) + ويندوز + لينكس + ماك + دوكر

**الأدوات:**
- سيرفر طُعم (Honeypot) بيسجل هجمات XSS
- فاحص بورتات
- محلل SOC بيكشف الهجمات ويطلع تنبيه
- كونسول تفاعلي باللوغو

**التشغيل:**
```bash
python3 app/main.py
# أو بالدوكر
docker-compose up
### 🇺🇸 English

Offensive & defensive cybersecurity lab built *100% offline* on Android Termux from Medani, Sudan.

*Works on:* Android, Windows, Linux, Mac, Docker

*Tools:*
- Honeypot Server + WAF Logger
- Port Scanner
- SOC Analyzer (Detects 8 XSS, triggers ALERT)
- Interactive Console with Logo

*Run:*
python3 app/main.py
# or with docker
docker-compose up
---
### 🤝 المساهمة / Contributing

*عربي:*
مرحب بأي مساهمة! لو عندك فكرة لأداة جديدة أو تحسين، افتح Issue أو Pull Request. الكود لازم يكون Python صافي ويشتغل أوفلاين.

*English:*
Contributions are welcome! Open an Issue or PR. Keep it pure Python and offline-first. No external dependencies.

### 👤 Author | المطور
*khwajja.sec* | medani, Gezirah state, Sudan
> Built under blackout to prove: You don't need resources to build security tools, just willpower.
> مبني في الظلام ليثبت: لا تحتاج إمكانيات لتبني أدوات حماية، فقط إرادة.

---
### 📊 Live Result | النتيجة الحية
--- TAHARQA SOC ANALYSIS ---
XSS attempts: 8
[!] ALERT: XSS Attack Detected!
