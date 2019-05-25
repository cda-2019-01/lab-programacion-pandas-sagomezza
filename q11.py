##
## Construya una tabla que contenga _c0 y una lista
## separada por ',' de los valores de la columna _c5a
## y _c5b (unidos por ':') de la tabla tbl2.tsv
## 

import pandas
import numpy as np
pandas.set_option('display.notebook_repr_html', False)

x = pandas.read_csv('tbl2.tsv',  
                    sep = '\t')

x['_c5'] = x['_c5a'] + ":" + x['_c5b'].astype('str')

a = x.groupby('_c0')['_c5'].apply(list)

y = pandas.DataFrame()
y['_c0'] = a.keys()
y['lista'] = [z for z in a]
y['lista'] = [",".join(str(z) for z in sorted(c)) for c in y['lista']]
print(y)