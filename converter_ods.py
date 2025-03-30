import pandas as pd

arquivo_ods = "C:/Users/Admin/Desktop/teste-estagio/ANS_dados/operadoras_ativas/dados_operadoras_ativas.ods"  

arquivo_csv = "dados_operadoras_ativas.csv"

df = pd.read_excel(arquivo_ods, engine="odf")

df.to_csv(arquivo_csv, index=False, encoding="utf-8")

print(f"Conversão concluída! O arquivo {arquivo_csv} foi gerado com sucesso.")
