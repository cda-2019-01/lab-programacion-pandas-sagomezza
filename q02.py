##
## Imprima el promedio de la _c2 por cada letra de la _c1 
## de la tabla tbl0
## 

import pandas
import numpy as np
pandas.set_option('display.notebook_repr_html', False)
x = pandas.read_csv('tbl0.tsv',  
                    sep = '\t',         
                    thousands = None,  
                    decimal = '.')
print((x.groupby('_c1').mean())["_c2"])