from src.generate_data import generate_fake_healthcare_data
from src.encrypt_data import encrypt_data
from src.integrity import generate_hash

if __name__ == "__main__":
    print("▶ Running PII Security App...\n")
    generate_fake_healthcare_data()
    encrypt_data()
    generate_hash()
    print("\n✅ All steps completed successfully.")
