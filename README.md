# Confidentiality and Integrity Demo App (Healthcare PII)

This Python-based project demonstrates foundational data protection concepts — confidentiality and integrity — by processing a synthetic healthcare dataset that contains personally identifiable information (PII).

## 🔐 Key Security Features

* **Anonymization** using Faker
* **AES Encryption** (Fernet) for selected PII fields
* **Field Suppression** to minimize data exposure
* **Integrity Check** using SHA-256 hashing

---

## 📁 Project Structure

```
pii-security-app/
├── data/
│   ├── raw_fake_data.csv
│   ├── encrypted_data.csv
│   └── encryption_key.key
├── logs/
│   └── integrity_log.txt
├── src/
│   ├── generate_data.py
│   ├── encrypt_data.py
│   └── integrity.py
├── main.py
├── requirements.txt
├── README.md
├── run_instructions.txt
└── venv/ (not included in repo)
```

---

## 🚀 Getting Started

### Prerequisites

* Python 3.8+
* pip
* Git

---

### Setup Instructions

1. **Clone the repository**

   ```bash
   git clone https://github.com/cyber-yates/pii-security-app.git
   cd pii-security-app
   ```

2. **Create and activate a virtual environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**

   ```bash
   python3 main.py
   ```

---

## 🗃️ Output Files

* `data/raw_fake_data.csv` – Anonymized dataset
* `data/encrypted_data.csv` – Encrypted dataset (with `Phone` suppressed)
* `data/encryption_key.key` – AES key for decryption
* `logs/integrity_log.txt` – SHA-256 hash to validate data integrity

---

## 📚 Author

**Ryan Yates**
GitHub: [@cyber-yates](https://github.com/cyber-yates)
Course: Healthcare Information Systems Security

---

## 📄 License

This project is for educational purposes only.
# pii-security-app
# pii-security-app
