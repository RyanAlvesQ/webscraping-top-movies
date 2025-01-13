import pandas as pd

# extrai os dados da tabela a partir do link da web

tabelas = pd.read_html("https://pt.wikipedia.org/wiki/Lista_de_filmes_de_maior_bilheteria")

tabela = tabelas[0]
#print(tabela)

tabela_filtrada = tabela[["Diretor(a)", "Bilheteria (US$)"]]

tabela_filtrada["Bilheteria (US$)"] = (
    tabela_filtrada["Bilheteria (US$)"]
    .str.replace(".","", regex=False)
    .str.replace(" ", "")
    .astype("int64"))
#tabela_filtrada.info()
print (tabela_filtrada)

# agrupamento por somando o valor de bilheteria
print(tabela_filtrada.groupby("Diretor(a)").sum())
