import pandas as pd
#import numpy as np
import csv
import os
import errno
import time

'''
with open('customer.tbl') as file:
    tabela = pd.read_table(file, sep='|', index_col=0,  lineterminator='\n')
    saida = open('customer1.csv','w')
    tabela.to_csv(saida,index=False)
'''
def tranforma(id_col):
    b = ' '
    if len(id_col) <= 5:

            b = 5-len(id_col)
            b ='{:0>5}'.format(id_col)

    if len(id_col) > 5:

            b = len(id_col) - 5
            b = id_col[b:]

    return b


x = 100
cont = 1
with open('customer.csv') as csvfile:
    global pegaId   
    read = csv.reader(csvfile)
    inicio = time.time()
    for row in read:
        #if cont <= x:
            if row[0] == 'id': continue
            pageId = row[0]
            
            #cont = cont +1
            pageId = ("{0:b}".format(int(pageId[12:])))
            #print(type(pageId)
            #caso o tamanho do ID for menor que o exigido
            result = tranforma(pageId)
            #inicio = time.time()
            f = 'temp/%s.csv'%result
            if not os.path.exists(os.path.dirname(f)):
                try:
                     os.makedirs(os.path.dirname(f))
                except OSError as exc: # Guard against race condition
                    if exc.errno != errno.EEXIST:
                        raise

            with open(f, 'a', encoding='utf-8') as filename:
                writer = csv.writer(filename, lineterminator='\n')
                writer.writerow(row) 

print("Tempo de contrução Bucket: %s segundos --" % (time.time() - inicio))