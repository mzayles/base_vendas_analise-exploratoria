import pandas as pd

# Aquisição de dados
df = pd.read_csv('data/base_vendas.csv')

# Visualização inicial
df.head()
df.tail()

# Informações gerais 
print("Tipo do objeto:", type(df))
print("Índices:", df.index)
print("Colunas:", df.columns)

# Acessar colunas
df['Nome Funcionario']
print("Tipo da coluna 'Nome Funcionario':", type(df['Nome Funcionario']))

# Padronização dos nomes das colunas
colunas = [
    'matricula_funcionario', 'nome_funcionario', 'cargo', 'codigo_loja',
    'nome_loja', 'codigo_produto', 'descricao_produto', 'categoria',
    'preco_custo', 'valor_unitario', 'quantidade', 'comissao',
    'dt_venda', 'dt_entrega'
]
df.columns = colunas

# Primeiras 5 linhas
df.head()

# Informação do DataFrame
qtd_linhas = df.shape[0]
qtd_colunas = df.shape[1]
print(f"Número de linhas: {qtd_linhas}, Número de colunas: {qtd_colunas}")

# Informações específicas
df.info()

# Estatísticas descritivas para variáveis numéricas
df.describe().round(1)

# Estatísticas para variáveis categóricas 
df.describe(include=object)

# Estatísticas específicas de colunas
df.quantidade.describe().round(2)
df[['quantidade', 'matricula_funcionario']].describe().round(1)

# Verificação de valores faltantes
percentual_nulos = df.isnull().sum() / qtd_linhas * 100
print("Percentual de dados faltantes por coluna:\n", percentual_nulos)

# Verificação de duplicatas
print("Registros duplicados (linha completa):", df.duplicated().sum())
print("Duplicações em 'quantidade' e 'matricula_funcionario':",
      df[['quantidade', 'matricula_funcionario']].duplicated().sum())

# Frequência de vendas por quantidade
df.quantidade.value_counts()

# Visualizar informações atualizadas
df.info()

# Exibir coluna 'valor_unitario'
df.valor_unitario