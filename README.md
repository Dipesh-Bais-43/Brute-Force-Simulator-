# 🛡️ Brute-Force Attack & Defender Simulator

Yeh ek educational tool hai jo dikhata hai ki **Brute-Force attacks** kaise kaam karte hain aur unhe rokne ke liye **Rate Limiting** aur **Account Lockout** jaise security features kitne zaroori hain.

## 📋 Table of Contents

* [Features](https://www.google.com/search?q=%23-features)
* [Installation](https://www.google.com/search?q=%23-installation)
* [How to Use](https://www.google.com/search?q=%23-how-to-use)
* [Security Concepts Covered](https://www.google.com/search?q=%23-security-concepts-covered)
* [Screenshots](https://www.google.com/search?q=%23-screenshots)

---

## ✨ Features

* **Attacker Script:** `itertools` ka use karke passwords ke sabhi possible combinations try karta hai.
* **Defender System:** - **Rate Limiting:** Har attempt ke beech mein delay (0.1s - 0.5s) daalta hai.
* **Account Lockout:** 5 galat attempts ke baad system ko 5-10 seconds ke liye freeze kar deta hai.


* **Modern GUI:** `CustomTkinter` library ka use karke ek dark-themed dashboard.
* **Live Logs:** Console/Textbox mein live dikhta hai ki kaunsa combination try ho raha hai.

---

## ⚙️ Installation

1. **Repository Clone Karein:**
```bash
git clone https://github.com/aapka-username/Brute-Force-Simulator.git
cd Brute-Force-Simulator

```


2. **Python install karein** (Python 3.8 ya upar).
3. **Required Libraries Install Karein:**
```bash
pip install customtkinter

```



---

## 🚀 How to Use

1. `main.py` file ko run karein:
```bash
python main.py

```


2. Ek "Target Password" set karein (e.g., `abc1`).
3. "Start Attack" button par click karein.
4. Dekhiye kaise **Defender** attacker ko block karta hai jab woh limit cross karta hai.

---

## 🛡️ Security Concepts Covered

Is project ke zariye aap niche diye gaye concepts seekh sakte hain:

1. **Brute-Force Complexity:** Password jitna lamba hoga, cracking mein utna zyada time lagega.
2. **Defensive Programming:** Galat input ko handle karna aur system ko protect karna.
3. **Multi-threading:** GUI ko freeze hone se rokne ke liye background threads ka use.

---

## 📸 Screenshots

*(Yahan apne running software ka screenshot ya GIF dalein)*
`![App Demo](screenshot.png)`

---

## 📜 License

Yeh project **MIT License** ke under hai. Aap isse seekhne ke liye freely use kar sakte hain.

---
