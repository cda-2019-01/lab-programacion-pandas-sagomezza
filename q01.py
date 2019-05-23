##
## Imprima la cantidad de registros por cada letra 
## de la columna _c1 de la tabla tbl0
## 
import pandas
import numpy as np
pandas.set_option('display.notebook_repr_html', False)
x = pandas.read_csv('tbl0.tsv',  
                    sep = '\t',         
                    thousands = None,  
                    decimal = '.') 
y = x.groupby('_c1').count()['_c0']
print(y)