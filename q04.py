##
## Imprima los valores unicos de la columna _c4 de 
## de la tabla tbl1 en mayusculas
## 
import pandas
import numpy as np
pandas.set_option('display.notebook_repr_html', False)
y = pandas.read_csv('tbl1.tsv',  
                    sep = '\t',         
                    thousands = None,  
                    decimal = '.') 
leters = list(sorted(set(y['_c4'])))
print([(leter.upper()) for leter in leters])

