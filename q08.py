##
## Agregue el año como una columna a la tabla tbl0.tsv 
## 

import pandas
import numpy as np
pandas.set_option('display.notebook_repr_html', False)
x = pandas.read_csv('tbl0.tsv',  
                    sep = '\t')
x['ano'] = [i.split('-')[0] for i in x['_c3']]
print(x)