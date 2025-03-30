import pdfplumber
import pandas as pd
import zipfile
import os

pdf_path = "downloads/anexo_1.pdf"

def extract_table_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        tables = []
        for page in pdf.pages:
            table = page.extract_table()
            if table:
                tables.append(table)
        return tables


tables = extract_table_from_pdf(pdf_path)

data = []
for table in tables:
    for row in table:
        data.append(row)

df = pd.DataFrame(data[1:], columns=data[0])

df.replace({"OD": "Descrição Completa OD", "AMB": "Descrição Completa AMB"}, inplace=True)

csv_file = "downloads/Teste_Matheus_Brito.csv"
df.to_csv(csv_file, index=False)

print(f"Dados extraídos e salvos em {csv_file}")

zip_name_csv = "downloads/Teste_Matheus_Brito.zip"
with zipfile.ZipFile(zip_name_csv, "w") as zipf:
    zipf.write(csv_file, os.path.basename(csv_file))

print(f"CSV compactado em {zip_name_csv}")
