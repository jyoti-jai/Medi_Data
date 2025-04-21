import pandas as pd

# Load EHR data
ehr_data = pd.read_csv("data/ehr/dummy_ehr_data.csv")
print("EHR Data:")
print(ehr_data.head())

# Load SNOMED data
snomed_data = pd.read_csv("data/snomed/dummy_snomed_data.csv")
print("SNOMED Data:")
print(snomed_data.head())