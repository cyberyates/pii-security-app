import hashlib

def calculate_hash(filepath):
    sha256_hash = hashlib.sha256()
    with open(filepath, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

file_path = "../data/encrypted_data.csv"
current_hash = calculate_hash(file_path)

with open("../logs/integrity_log.txt", "r") as log_file:
    original_hash = log_file.read().strip()

if current_hash == original_hash:
    print("Integrity verified: File has not been altered.")
else:
    print("Integrity check failed: File has been modified!")
