import os
import pandas as pd

def padronizar_arquivos(pasta):    
    colunas_padrao = ["DATA", "REG_ANS", "CD_CONTA_CONTABIL", "DESCRICAO", "VL_SALDO_INICIAL", "VL_SALDO_FINAL"]
    
    arquivos = [f for f in os.listdir(pasta) if f.endswith(".csv") and "2024" in f]
    
    for arquivo in arquivos:
        caminho_arquivo = os.path.join(pasta, arquivo)
        df = pd.read_csv(caminho_arquivo, delimiter=';', dtype=str)
        
        for coluna in colunas_padrao:
            if coluna not in df.columns:
                df[coluna] = ''  
       
        df = df[colunas_padrao]        
       
        caminho_saida = os.path.join(pasta, "padronizado_" + arquivo)
        df.to_csv(caminho_saida, sep=';', index=False, encoding='utf-8')
        print(f"Arquivo padronizado salvo: {caminho_saida}")

pasta_arquivos = r"C:\Users\Admin\Desktop\teste-estagio\ANS_dados\demonstracoes_contabeis"
padronizar_arquivos(pasta_arquivos)
