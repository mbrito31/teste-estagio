import pandas as pd

caminho_arquivo = "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/4T2023.csv"

df = pd.read_csv(caminho_arquivo, delimiter=";", encoding="utf-8", header=0)

# Tive a necessidade de converter as datas que estavam no formato "01-jan-24" para "YYYY-MM-DD" de alguns arquivos
def converter_data(data):
    try:
        return pd.to_datetime(data, format="%d-%b-%y").strftime("%Y-%m-%d")
    except:
        return data  

# aqui vou aplicar a conversão na coluna data
df["DATA"] = df["DATA"].apply(converter_data)
caminho_saida = "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/4T2023_corrigido.csv"
df.to_csv(caminho_saida, index=False, sep=";")

print(f"Arquivo corrigido salvo em: {caminho_saida}")
