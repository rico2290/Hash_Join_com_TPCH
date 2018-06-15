import pandas as pd
#import numpy as np
import csv
import os
import errno
import time


def tranforma(id_col):
    b = ' '
    #Casoo  tamanho da numero binario for menor que 5
    if len(id_col) <= 5:
            b = 5-len(id_col)
            b ='{:0>5}'.format(id_col)
    #Caso o tamanho da numero binario for maior que 5
    if len(id_col) > 5:

            b = len(id_col) - 5
            b = id_col[b:]
    return b



with open('customer.csv') as csvfile:
    global pegaId   
    read = csv.reader(csvfile)
    inicio = time.time()
    for row in read:
        #if cont <= x:
            if row[0] == 'id': continue
            pageId = row[0]
            row[0] = pageId[12:]
            
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
                # Caso não tenha permissão para criar pasta/ arquivo 
                except OSError as exc: 
                    if exc.errno != errno.EEXIST:
                        raise
            with open(f, 'a', encoding='utf-8') as filename:
                write = csv.writer(filename, lineterminator='\n')
                #primeira_letra = csv.reader(filename)
                #write.writerow(['id', 'name', 'address', 'nationkey', 'phone', 'acctbal', 'mktsegment', 'comment' ])
                write.writerow(row) 

print("Tempo de contrução Bucket: %s segundos --" % (time.time() - inicio))


'''
x = 10
cont = 0
with open('orders.csv') as csvfile:
    global pageId 
    read = csv.reader(csvfile)
    #inicio = time.time()
    for row in read:
        if cont < x:
            del row[9]
            print(row)
            print ('-' * 150)
            cont += 1
            pageId = row[1]
            cont+=1
            pageId = ("{0:b}".format(int(pageId)))
            match = tranforma(pageId)
            #print(match)
            

            
print('\n','==========================FASE DE MATCHING==============================================','\n')
a = 0

with open('customer.csv') as csvfile:
    global pegaId   
    read = csv.reader(csvfile)
    inicio = time.time()
    for row in read:
        del row[7]
        if a <= 5:
            print(row)
            print ('-' * 150)
            if row[0] == 'id': 
                continue
            pageId = row[0]
            a+=1


with open('part.csv') as csvfile:
    global pageId 
    read = csv.reader(csvfile)
    #inicio = time.time()
    for row in read:
        if cont < x:
            print(row)
            cont += 1        


with open('part.tbl') as file:
    tabela = pd.read_table(file, sep='|', index_col=0,  lineterminator='\n')
    saida = open('part.csv','w')
    tabela.to_csv(saida,index=False)
'''