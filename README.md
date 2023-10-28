# tech-challenges
# Projeto Vinho
## Documentação dos DataFrames

### Descrição Geral
Este documento fornece uma visão geral e descrições detalhadas dos conjuntos de dados utilizados em nosso projeto, cobrindo vendas, exportações, importações, processamento de produtos e produção desde o ano de 1970 até 2021.

### DataFrames de Comércio
`df_comercio`
- ID: Identificador único para cada registro.
- categoria: Categoria do produto.
- subcategoria: Subcategoria do produto.
- 1970 a 2021: Total de vendas de cada categoria e subcategoria para cada ano.

### DataFrames de Exportação
`df_exportacao_total`

Este dataframe consolida todas as informações de exportação, abrangendo diferentes categorias e subcategorias de produtos desde o ano de 1970 até 2021. O país de origem para todas as exportações é o Brasil.

Estrutura do dataframe:
- id: Identificador único para cada registro.
- pais: País de destino da exportação.
- ano: Ano da transação.
- valor: Valor exportado no ano específico.
- categoria: Categoria do produto exportado.
- subcategoria: Subcategoria do produto exportado.

Exemplos de uso:
Para filtrar as exportações de uma categoria específica em um ano específico:
```
df_exportacao_total[(df_exportacao_total['categoria'] == 'Bebida') & (df_exportacao_total['ano'] == '2020')]
```
Para filtrar todas as exportações para um país específico:
```
df_exportacao_total[df_exportacao_total['País'] == 'Estados Unidos']
```
Para filtrar todas as exportações de uma subcategoria específica:
```
df_exportacao_total[df_exportacao_total['subcategoria'] == 'Espumante']
```

`df_exp_espumantes`
- id: Identificador único.
- pais: País de destino da exportação.
- 1970 a 2021: Valor exportado de espumante para cada ano.

`df_exp_suco`
- id: Identificador único.
- pais: País de destino da exportação.
- 1970 a 2021: Valor exportado de suco para cada ano.

`df_exp_uva`
- id: Identificador único.
- pais: País de destino da exportação.
- 1970 a 2021: Valor exportado de uva para cada ano.

`df_exp_vinho`
- id: Identificador único.
- pais: País de destino da exportação.
- 1970 a 2021: Valor exportado de vinho para cada ano.

### DataFrames de Importação
`df_imp_espumantes`
- id: Identificador único.
- pais: País de origem da importação.
- 1970 a 2021: Valor importado de espumante para cada ano.

`df_imp_uvas`
- id: Identificador único.
- pais: País de origem da importação.
- 1970 a 2021: Valor importado de espumante para cada ano.

`df_imp_vinhos`
- id: Identificador único.
- pais: País de origem da importação.
- 1970 a 2021: Valor importado de espumante para cada ano.

`df_imp_suco`
- id: Identificador único.
- pais: País de origem da importação.
- 1970 a 2021: Valor importado de espumante para cada ano.

### DataFrames de Processamento
`df_proc_americanas`
- id: Identificador único.
- control: Tipo de controle.
- cultivar: Tipo de cultivo.
- 1970 a 2021: Quantidade de matéria-prima processada para cada ano.

`df_proc_mesa`
- id: Identificador único.
- control: Tipo de controle.
- cultivar: Tipo de cultivo.
- 1970 a 2021: Quantidade de matéria-prima processada para cada ano.

`df_proc_viniferas`
- id: Identificador único.
- control: Tipo de controle.
- cultivar: Tipo de cultivo.
- 1970 a 2021: Quantidade de matéria-prima processada para cada ano.

### DataFrame de Produção
`df_producao`
- id: Identificador único.
- produto: Tipo de produto produzido.
- 1970 a 2021: Quantidade produzida de cada produto para cada ano.

### DataFrames Genéricos
`df_temperaturas`
- Country: País.
- Year: Ano.
- AvgTemperature: Temperatura média registrada.

Fonte: https://www.kaggle.com/datasets/subhamjain/temperature-of-all-countries-19952020/data


----
## Próximos passos
- Perfurmaria Gráficos: Sergio e Bruna
- Datasets novos: Lucas (Dados Climáticos, Dados Economicos: Poder aquisitivo dos países consumidores)
- Estudo de correlações: Pietro e Maiara