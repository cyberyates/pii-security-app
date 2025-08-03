import hashlib
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
from pathlib import Path
import os

# -------------------------------
# File Paths (relative to project root)
# -------------------------------
DATA_FILE = Path("data/encrypted_data.csv")
HASH_LOG = Path("logs/integrity_log.txt")
PRIVATE_KEY_FILE = Path("data/private_key.pem")
PUBLIC_KEY_FILE = Path("data/public_key.pem")
SIGNATURE_FILE = Path("logs/file_signature.sig")

# -------------------------------
# 1. Generate SHA-256 Hash and Update Log
# -------------------------------
def calculate_hash(filepath):
    sha256_hash = hashlib.sha256()
    with open(filepath, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def update_integrity_log():
    hash_value = calculate_hash(DATA_FILE)
    with open(HASH_LOG, "w") as log:
        log.write(hash_value)
    print(f"[+] Hash updated and saved to {HASH_LOG}")

# -------------------------------
# 2. Integrity Verification
# -------------------------------
def verify_integrity():
    current_hash = calculate_hash(DATA_FILE)
    with open(HASH_LOG, "r") as log:
        saved_hash = log.read().strip()

    if current_hash == saved_hash:
        print("[✓] Integrity verified: File has not been altered.")
    else:
        print("[✗] Integrity check failed: File has been modified!")

# -------------------------------
# 3. Generate RSA Keys
# -------------------------------
def generate_rsa_keys():
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()

    with open(PRIVATE_KEY_FILE, "wb") as priv_file:
        priv_file.write(
            private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=serialization.NoEncryption()
            )
        )

    with open(PUBLIC_KEY_FILE, "wb") as pub_file:
        pub_file.write(
            public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            )
        )

    print(f"[+] RSA key pair generated and saved to {PRIVATE_KEY_FILE} and {PUBLIC_KEY_FILE}")
    return private_key, public_key

# -------------------------------
# 4. Digital Signing & Verification
# -------------------------------
def sign_and_verify_file(private_key, public_key):
    with open(DATA_FILE, "rb") as f:
        file_data = f.read()

    # Sign the file
    signature = private_key.sign(
        file_data,
        padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
        hashes.SHA256()
    )
    with open(SIGNATURE_FILE, "wb") as sig_file:
        sig_file.write(signature)
    print(f"[+] File signed. Signature saved to {SIGNATURE_FILE}")

    # Verify the signature
    try:
        public_key.verify(
            signature,
            file_data,
            padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
            hashes.SHA256()
        )
        print("[✓] Signature verified successfully: File integrity intact.")
    except Exception:
        print("[✗] Signature verification failed: File may be tampered with!")

# -------------------------------
# 5. Apply File Permissions
# -------------------------------
def set_permissions():
    os.chmod(DATA_FILE, 0o600)
    os.chmod(HASH_LOG, 0o600)
    print("[+] File permissions set: Owner read/write only.")

# -------------------------------
# MAIN EXECUTION
# -------------------------------
if __name__ == "__main__":
    print("\n=== INTEGRITY & CONFIDENTIALITY SUITE ===\n")

    update_integrity_log()
    verify_integrity()

    private_key, public_key = generate_rsa_keys()
    sign_and_verify_file(private_key, public_key)

    set_permissions()

    print("\n[✓] All integrity and confidentiality controls executed successfully.\n")
