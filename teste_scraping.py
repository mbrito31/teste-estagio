import requests
import zipfile
import os

# passo 1: extrair os links dos pdfs
# passo 2: criar a pasta de destino para os arquivos
#

pdf_links = [
    "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf",
    "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_II_DUT_2021_RN_465.2021_RN628.2025_RN629.2025.pdf"
]

os.makedirs("downloads", exist_ok=True)

# Baixar os PDFs
pdf_files = []
for i, link in enumerate(pdf_links):
    pdf_path = f"downloads/anexo_{i+1}.pdf"
    response = requests.get(link)
    with open(pdf_path, "wb") as f:
        f.write(response.content)
    pdf_files.append(pdf_path)

# Compactar os PDFs em um arquivo ZIP
zip_name = "downloads/anexos.zip"
with zipfile.ZipFile(zip_name, "w") as zipf:
    for pdf in pdf_files:
        zipf.write(pdf, os.path.basename(pdf))

print(f"Arquivos compactados em {zip_name}")
