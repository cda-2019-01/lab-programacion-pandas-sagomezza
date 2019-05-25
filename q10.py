##
## Construya una tabla que contenga _c0 y una lista
## separada por ',' de los valores de la columna _c4
## de la tabla tbl1.tsv
## 
import pandas
import numpy as np
pandas.set_option('display.notebook_repr_html', False)

x = pandas.read_csv('tbl1.tsv',  
                    sep = '\t')
                    
y = pandas.DataFrame()

a = x.groupby('_c0') ['_c4'].apply(list)

y['_c0'] = a.keys()
y['lista'] = [z for z in a]
y['lista'] = [",".join(str(z) for z in sorted(elem)) for elem in y['lista']]
print(y)