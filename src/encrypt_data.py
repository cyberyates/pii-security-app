from cryptography.fernet import Fernet
import pandas as pd
import os

def encrypt_column(df, col, fernet):
    df[col] = df[col].apply(lambda val: fernet.encrypt(val.encode()).decode())
    return df

def encrypt_data(input_path='data/raw_fake_data.csv', output_path='data/encrypted_data.csv', key_path='data/encryption_key.key'):
    df = pd.read_csv(input_path)

    # Generate or load encryption key
    if not os.path.exists(key_path):
        key = Fernet.generate_key()
        with open(key_path, 'wb') as f:
            f.write(key)
    else:
        with open(key_path, 'rb') as f:
            key = f.read()

    fernet = Fernet(key)

    # Encrypt sensitive fields
    for col in ['Diagnosis', 'Patient ID']:
        df = encrypt_column(df, col, fernet)

    # Suppress the 'Phone' field
    if 'Phone' in df.columns:
        df.drop(columns=['Phone'], inplace=True)

    df.to_csv(output_path, index=False)
    print(f"[✔] Encrypted and saved (with suppression): {output_path}")

if __name__ == "__main__":
    encrypt_data()
