
# Web Scraping de Dados de Bilheteria

Este projeto realiza a extração de dados diretamente da [Wikipedia](https://pt.wikipedia.org/wiki/Lista_de_filmes_de_maior_bilheteria) utilizando a biblioteca **Pandas**. Após a extração, os dados são tratados e analisados para fornecer insights sobre as bilheterias de filmes, agrupados por diretor(a).

## Funcionalidades

- **Extração de Dados**: Coleta dados diretamente de uma página da Wikipedia.
- **Filtragem**: Seleciona as colunas de interesse, como o(a) diretor(a) e a bilheteria dos filmes.
- **Tratamento de Dados**: 
  - Remove caracteres indesejados como pontos e espaços dos valores de bilheteria.
  - Converte os valores para o tipo numérico (`int64`).
- **Agrupamento e Análise**:
  - Soma os valores de bilheteria agrupados por diretor(a).
  - Exibe o resultado em formato tabular para análise.

## Tecnologias Utilizadas

- **Python**: Linguagem principal do projeto.
- **Pandas**: Biblioteca para manipulação e análise de dados.
- **HTML**: Fonte dos dados extraídos.

## Como Utilizar

1. Clone o repositório:
   ```bash
   git clone https://github.com/RyanAlvesQ/webscraping-top-movies.git
   ```
2. Instale as dependências em um ambiente virtual:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
3. Execute o script:
   ```bash
   python3 webscraping.py
   ```

## Resultados

O script exibe:
- A tabela filtrada com os diretores e a bilheteria correspondente.
- A soma da bilheteria total agrupada por diretor(a).

## Exemplo de Saída

Tabela inicial filtrada:

```
          Diretor(a)  Bilheteria (US$)
0      James Cameron     2847246203
1     Anthony Russo     2797800564
2      James Cameron     2187463944
...
```

Bilheteria total por diretor(a):

```
               Bilheteria (US$)
Diretor(a)                     
Anthony Russo        4200000000
James Cameron        5034710147
...
```

## Melhorias Futuras

- Adicionar visualizações gráficas com **Matplotlib** ou **Seaborn**.
- Exportar os resultados para um arquivo CSV.
- Ampliar o scraping para outras páginas de dados de filmes.

---

**Autor:** [Ryan Alves](https://github.com/RyanAlvesQ)
