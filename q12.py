##
## Si la columna _c0 es la clave en las tablas tbl0.tsv
## y tbl2.tsv, compute la suma de tbl2._c5b por cada
## valor en tbl0._c1.
## 
import pandas
import numpy as np
pandas.set_option('display.notebook_repr_html', False)
x = pandas.read_csv('tbl0.tsv',  
                    sep = '\t',         
                    thousands = None,  
                    decimal = '.')
y = pandas.read_csv('tbl2.tsv',  
                    sep = '\t',         
                    thousands = None,  
                    decimal = '.')
z = pandas.merge(x, y, on='_c0')
print((z.groupby('_c5a').sum())["_c5b"])