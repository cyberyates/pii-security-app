from faker import Faker
import pandas as pd

def generate_fake_healthcare_data(file_path='data/raw_fake_data.csv', num_records=50):
    fake = Faker()
    data = []

    diagnosis_list = [
        'Type 2 Diabetes',
        'Hypertension',
        'Acute Bronchitis',
        'Asthma',
        'Chronic Kidney Disease',
        'Migraine',
        'COVID-19',
        'Allergic Rhinitis',
        'Urinary Tract Infection',
        'Iron Deficiency Anemia',
        'Depression',
        'Generalized Anxiety Disorder',
        'Hypothyroidism',
        'Gastroesophageal Reflux Disease',
        'Osteoarthritis',
        'Hyperlipidemia',
        'Acute Sinusitis',
        'ADHD',
        'Insomnia',
        'Upper Respiratory Infection'
    ]

    for _ in range(num_records):
        data.append({
            'First Name': fake.first_name(),
            'Last Name': fake.last_name(),
            'Email': fake.email(),
            'Phone': fake.phone_number(),
            'Diagnosis': fake.random_element(diagnosis_list),
            'Patient ID': fake.uuid4()
        })

    df = pd.DataFrame(data)
    df.to_csv(file_path, index=False)
    print(f"[✔] Data saved to {file_path}")

if __name__ == "__main__":
    generate_fake_healthcare_data()
