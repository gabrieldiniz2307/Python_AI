# -*- coding: utf-8 -*-
"""RedeNeural.pynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1GL30NoqGoy4FAE8KLAn2mJrXh1lI9KlU
"""

import pandas as pd
import random
from sklearn.model_selection import train_test_split
from tensorflow.keras import models, layers
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
from sklearn.metrics import accuracy_score

num_imoveis=1000

area_total = [random.uniform(50, 150) for i in range(num_imoveis)]
qtd_quartos = [random.randint(2, 5) for i in range(num_imoveis)]
qtd_banheiros = [random.randint(1, 4) for i in range(num_imoveis)]
vagas_garagem = [random.randint(0, 2) for i in range(num_imoveis)]
valor = [random.uniform(200000, 100000) for i in range(num_imoveis)]

# @title Texto de título padrão
min_length=min(len(area_total), len(qtd_quartos), len(qtd_banheiros), len(vagas_garagem), len(valor))
for l in [area_total, qtd_quartos, qtd_banheiros, vagas_garagem, valor]:
    while len(l)<min_length:
        l.pop()

titulos=['Casa Ampla com Quintal', 'Apartamento Moderno','Cobertura Duplex', 'Sobrado com Piscina']
bairros=['Centro', 'Jardim Europa','Vila Nova','Alphaville']
cidades=['São Paulo','Campinas','Belo Horizonte','Curitiba']
estados=['SP','SP','MG','PR']

titulo=[random.choice(titulos) for i in range(num_imoveis)]
bairro=[random.choice(bairros) for i in range(num_imoveis)]
cidade=[random.choice(cidades) for i in range(num_imoveis)]
estado=[random.choice(estados) for i in range(num_imoveis)]

#Colunas
caracteristicas={
    'titulo':titulo,
    'bairro':bairro,
'cidade': cidade,
    'estado': estado,
    'area_total': area_total,
    'qtd_quartos': qtd_quartos,
    'qtd_banheiros': qtd_banheiros,
    'vagas_garagem':vagas_garagem,
    'valor':valor
}

dados=pd.DataFrame(caracteristicas)

dados.to_csv('dados.csv', index=False)

dados=pd.read_csv('dados.csv')
dados.head()

#Pre processamento e normalizaçao
scarler=MinMaxScaler()
dados[['area_total','qtd_quartos','qtd_banheiros','vagas_garagem']]=scarler.fit_transform(dados[['area_total','qtd_quartos','qtd_banheiros','vagas_garagem']])
dados.iloc[:, 0] = dados['area_total']
dados.iloc[:, 1] = dados['qtd_quartos']
dados.iloc[:, 2] = dados['qtd_banheiros']
dados.iloc[:, 3] = dados['vagas_garagem']

#Codificaçao variaveis
encoder=OneHotEncoder()
dados_onehot=encoder.fit_transform(dados[['bairro','estado']])
dados=pd.concat([dados, pd.DataFrame(dados_onehot.toarray(), columns=encoder.get_feature_names_out())],axis=1)

#Valores Ausentes
dados.dropna(inplace=True)

#Treinamento e Teste
X=dados[['area_total','qtd_quartos','qtd_banheiros','vagas_garagem']+list(encoder.get_feature_names_out())]
y=dados['valor']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Rede neural
model=models.Sequential([
    layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    layers.Dense(64, activation='relu'),
    layers.Dense(1)

])
model.compile(loss='mean_squared_error', optimizer='adam', metrics=['mae'])

#Treinar modelo
model.fit(X_train, y_train, epochs=100, batch_size=32, validation_split=0.2)

#Avaliar modelo
loss, mae = model.evaluate(X_test, y_test)
print('Loss:', loss)
print('MAE:', mae)

#Fazer previsões
novo_imovel={
    'area_total': 120,
    'qtd_quartos': 3,
    'qtd_banheiros': 2,
    'vagas_garagem': 1,
    'bairro_Centro': 0,
    'bairro_Jardim Europa': 0,
    'bairro_Alphaville': 1,
    'estado_SP': 1,
    'estado_MG': 0,
    'estado_PR': 0
}

#Novo DF
novo_imovel_df=pd.DataFrame(novo_imovel, index=[0])

#Previsao
previsao=model.predict(novo_imovel_df)
print('Previsão:', previsao [0] [0])