##
## Construya una tabla que contenga _c1 y una lista
## separada por ':' de los valores de la columna _c2
## para el archivo tbl0.tsv
## 


import pandas
import numpy as np
pandas.set_option('display.notebook_repr_html', False)
x = pandas.read_csv('tbl0.tsv',  
                    sep = '\t')

y = pandas.DataFrame()

a = x.groupby('_c1') ['_c2'].apply(list)

y['_c1'] = a.keys()
y['lista'] = [':'.join(str(z) for z in sorted(elem)) for elem in sorted(a)]
print(y)