from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

# Generate RSA private and public keys
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key()

# Save private key
with open("../data/private_key.pem", "wb") as priv_file:
    priv_file.write(
        private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        )
    )

# Save public key
with open("../data/public_key.pem", "wb") as pub_file:
    pub_file.write(
        public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
    )

# Signing the encrypted file
with open("../data/encrypted_data.csv", "rb") as f:
    file_data = f.read()

signature = private_key.sign(
    file_data,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

with open("../logs/file_signature.sig", "wb") as sig_file:
    sig_file.write(signature)

print("File signed. Signature saved in 'logs/file_signature.sig'.")

# Verifying the signature
try:
    public_key.verify(
        signature,
        file_data,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print("Signature verified successfully: File integrity intact.")
except Exception:
    print("Signature verification failed: File may be tampered with.")

print("RSA key pair generated and saved in 'data/' folder.")


