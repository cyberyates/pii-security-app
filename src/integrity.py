import hashlib

def generate_hash(file_path='data/encrypted_data.csv', log_path='logs/integrity_log.txt'):
    with open(file_path, 'rb') as f:
        file_data = f.read()
    hash_val = hashlib.sha256(file_data).hexdigest()

    with open(log_path, 'w') as f:
        f.write(f"{file_path} hash:\n{hash_val}\n")
    print(f"[✔] Hash written to {log_path}")

if __name__ == "__main__":
    generate_hash()
