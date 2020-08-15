import numpy as np
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
import pandas as pd
x=np.array([[1,3.5,'y'],[2,4.0,'n'],[4,5.8,'y'],[2,5.8,'n']])
print(x)
ct = ColumnTransformer(
    [('one_hot_encoder', OneHotEncoder(categories='auto',sparse=False), [1,2])],   # The column numbers to be transformed (here is [0] but can be [0, 1, 3])
    remainder='passthrough'                                         # Leave the rest of the columns untouched
)

x = ct.fit_transform(x)
print(x)