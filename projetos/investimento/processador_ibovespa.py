import pandas as pd

class ProcessadorIbovespa:
    def __init__(self, caminho_arquivo):
        self.df = pd.read_csv(caminho_arquivo, sep=",")
        self.preprocessar()

    def converter_volume(self, valor):
        if isinstance(valor, float): 
            return valor
        if 'M' in valor:
            return float(valor.replace('M', '').replace(',', '.')) * 1e6
        elif 'K' in valor:
            return float(valor.replace('K', '').replace(',', '.')) * 1e3
        else:
            return float(valor.replace(',', '.'))

    def descrever_features(self):
        descricoes = {
            'Data': 'Data da observação.',
            'Último': 'Valor de fechamento do índice no dia.',
            'Abertura': 'Valor de abertura do índice no dia.',
            'Máxima': 'Valor máximo atingido pelo índice no dia.',
            'Mínima': 'Valor mínimo atingido pelo índice no dia.',
            'Vol.': 'Volume de negociações no dia.',
            'Variacao_Diaria_Pontos': 'Diferença entre os valores de fechamento e abertura.',
            'Amplitude_Diaria': 'Diferença entre os valores máximo e mínimo no dia.',
            'Volume_Normalizado': 'Volume de negociações normalizado entre 0 e 1.',
            'Dia_Semana': 'Dia da semana correspondente à data (0 = Segunda, 1 = Terça, etc.).',
            'Dia_0': 'Indicador para segunda-feira (1 se for segunda-feira, 0 caso contrário).',
            'Dia_1': 'Indicador para terça-feira (1 se for terça-feira, 0 caso contrário).',
            'lag_1': 'Valor de fechamento do índice com um dia de atraso.',
            'lag_2': 'Valor de fechamento do índice com dois dias de atraso.',
            'diff_1': 'Diferença no valor de fechamento em relação ao dia anterior.',
            'diff_2': 'Diferença no valor de fechamento em relação a dois dias atrás.',
            'Volatilidade_5d': 'Volatilidade histórica do índice calculada em uma janela de 5 dias.',
            'Media_Movel_5d': 'Média móvel de 5 dias do valor de fechamento.',
            'Media_Movel_20d': 'Média móvel de 20 dias do valor de fechamento.'
        }
        for coluna, descricao in descricoes.items():
            print(f"\033[1m{coluna}\033[0m:\t{descricao}")
    
    def preprocessar(self):
        self.df['Data'] = pd.to_datetime(self.df['Data'], format='%d.%m.%Y')
        self.df.sort_values('Data', inplace=True)

        self.df['Vol.'] = self.df['Vol.'].apply(self.converter_volume)

        self.df['Variacao_Diaria_Pontos'] = self.df['Último'] - self.df['Abertura']
        self.df['Amplitude_Diaria'] = self.df['Máxima'] - self.df['Mínima']
        self.df['Volume_Normalizado'] = (self.df['Vol.'] - self.df['Vol.'].min()) / (self.df['Vol.'].max() - self.df['Vol.'].min())

    def adicionar_features(self, features):
        if 'dias_semana' in features:
            self.df['Dia_Semana'] = self.df['Data'].dt.dayofweek
            dias_semana = pd.get_dummies(self.df['Dia_Semana'], prefix='Dia')
            self.df = pd.concat([self.df, dias_semana], axis=1)

        if 'lags' in features:
            for lag in range(1, 4):
                self.df[f'lag_{lag}'] = self.df['Último'].shift(lag)

        if 'diffs' in features:
            for diff in range(1, 4):
                self.df[f'diff_{diff}'] = self.df['Último'].diff(periods=diff)

        if 'volatilidade' in features:
            self.df['Volatilidade_5d'] = self.df['Último'].pct_change().rolling(window=5).std() * (252 ** 0.5)  # Anualizada

        if 'medias_moveis' in features:
            self.df['Media_Movel_5d'] = self.df['Último'].rolling(window=5).mean()
            self.df['Media_Movel_20d'] = self.df['Último'].rolling(window=20).mean()

    def get_dataframe(self, features=None):
        if features:
            self.adicionar_features(features)
        return self.df
