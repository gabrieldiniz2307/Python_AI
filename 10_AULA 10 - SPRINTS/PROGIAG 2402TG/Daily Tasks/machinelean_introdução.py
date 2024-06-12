# -*- coding: utf-8 -*-
"""machinelean-introdução.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18ffxtfvYGUOnkHHu6osUWJGJljDTvVSB
"""

import pandas as pd
import numpy as np
from sklearn.svm import LinearSVC

"""Identificar porco ou cachorro
* Caracteristicas
- Pelo (pelo curso ou longo)
- Latir (Faz "au-au"?)
- Rabo (Tem rabo curto ou longo?)
** Sempre comprar com 'algo'

0 - Tem pelo curto
1 - Tem pelo longo

----

0 - Não faz "au au"
1 - Faz "au au"

----

0 - Rabo Curto
1 - Rabo longo
"""

porco1=[0,1,0] #pelo curto, não au-au, rabo curto
porco2=[0,1,1]
porco3=[1,1,0]

cachorro1=[0,1,1] #pelo curto, não au-au, rabo longo
cachorro2=[1,0,1]
cachorro3=[1,1,1]

treino_x=[porco1,porco2,porco3,cachorro1,cachorro2,cachorro3]
treino_y=[1,1,1,0,0,0] # 0 - cachorro, 1- porco

modelo=LinearSVC()

modelo.fit (treino_x,treino_y)

animal_misterioso=[1,1,1]
modelo.predict([animal_misterioso])