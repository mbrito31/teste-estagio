-- Importação de arquivos CSV para a tabela demonstracoes_contabeis
LOAD DATA LOCAL INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/nome' 
INTO TABLE demonstracoes_contabeis
FIELDS TERMINATED BY ';'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES
(@DATA, @REG_ANS, @CD_CONTA_CONTABIL, @DESCRICAO, @VL_SALDO_INICIAL, @VL_SALDO_FINAL)
SET 
    DATA = @DATA,
    REG_ANS = @REG_ANS,
    CD_CONTA_CONTABIL = @CD_CONTA_CONTABIL,
    DESCRICAO = @DESCRICAO,
    VL_SALDO_INICIAL = REPLACE(@VL_SALDO_INICIAL, ',', '.'),
    VL_SALDO_FINAL = REPLACE(@VL_SALDO_FINAL, ',', '.'),
    patrimonio = NULL,
    passivo = NULL,
    ativo = NULL;

-- Query para encontrar as 10 operadoras com maiores despesas no último trimestre
SELECT
    REG_ANS,
    SUM(VL_SALDO_FINAL) AS total_despesas
FROM demonstracoes_contabeis
WHERE DESCRICAO LIKE '%SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE%'
    AND YEAR(DATA) = (SELECT MAX(YEAR(DATA)) FROM demonstracoes_contabeis)
    AND QUARTER(DATA) = (SELECT MAX(QUARTER(DATA)) 
                         FROM demonstracoes_contabeis 
                         WHERE YEAR(DATA) = (SELECT MAX(YEAR(DATA)) FROM demonstracoes_contabeis))
GROUP BY REG_ANS
ORDER BY total_despesas DESC
LIMIT 10;

-- Query para encontrar as 10 operadoras com maiores despesas no último ano
SELECT
    REG_ANS,
    SUM(VL_SALDO_FINAL) AS total_despesas
FROM demonstracoes_contabeis
WHERE DESCRICAO LIKE '%SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE%'
    AND YEAR(DATA) = (SELECT MAX(YEAR(DATA)) FROM demonstracoes_contabeis)
GROUP BY REG_ANS
ORDER BY total_despesas DESC
LIMIT 10;
