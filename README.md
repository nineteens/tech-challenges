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

`df_expectativa_vida`
- Country: País de origem dos dados. Tipo de dado: object (string).
- Year: Ano em que os dados foram registrados. Tipo de dado: int64.
- Status: Status do país (pode ser desenvolvido ou em desenvolvimento). Tipo de dado: object (string).
- Life expectancy: Expectativa de vida média da população. Tipo de dado: float64.
- Adult Mortality: Taxa de mortalidade de adultos. Tipo de dado: float64.
- Infant deaths: Número de mortes de bebês (menores de um ano). Tipo de dado: int64.
- Alcohol: Consumo de álcool per capita. Tipo de dado: float64.
- Percentage expenditure: Porcentagem de gastos. Tipo de dado: float64.
- Hepatitis B: Cobertura de vacinação contra Hepatite B. Tipo de dado: float64.
- Measles: Número de casos de sarampo. Tipo de dado: int64.
- BMI: Índice de massa corporal médio da população. Tipo de dado: float64.
- Under-five deaths: Número de mortes de crianças menores de cinco anos. Tipo de dado: int64.
- Polio: Cobertura de vacinação contra poliomielite. Tipo de dado: float64.
- Total expenditure: Gasto total em saúde como uma porcentagem do PIB. Tipo de dado: float64.
- Diphtheria: Cobertura de vacinação contra difteria, tétano e coqueluche. Tipo de dado: float64.
- HIV/AIDS: Número de mortes por HIV/AIDS. Tipo de dado: float64.
- GDP: Produto Interno Bruto per capita. Tipo de dado: float64.
- Population: População do país. Tipo de dado: float64.
- Thinness 1-19 years: Prevalência de magreza em crianças e adolescentes de 10 a 19 anos. Tipo de dado: float64.
- Thinness 5-9 years: Prevalência de magreza em crianças de 5 a 9 anos. Tipo de dado: float64.
- Income composition of resources: Índice de Desenvolvimento Humano em termos de composição de renda. Tipo de dado: float64.
- Schooling: Número médio de anos de escolaridade. Tipo de dado: float64.

Fonte: https://www.kaggle.com/datasets/kumarajarshi/life-expectancy-who/data


----
## Próximos passos
- Perfurmaria Gráficos: Sergio e Bruna
- Datasets novos: Lucas (Dados Climáticos, Dados Economicos: Poder aquisitivo dos países consumidores)
- Estudo de correlações: Pietro e Maiara