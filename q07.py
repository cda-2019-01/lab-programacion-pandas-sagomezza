##
## Agregue una columna  con la suma de _c0 y _c2 a la tabla tbl0.tsv 
## 
import pandas
import numpy as np
pandas.set_option('display.notebook_repr_html', False)
x = pandas.read_csv('tbl0.tsv',  
                    sep = '\t',         
                    thousands = None,  
                    decimal = '.')
x.insert(4, 'suma', x['_c0'] + x['_c2'])
print(x)