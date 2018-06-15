import pandas as pd
#import numpy as np
import csv
import os
import errno
import time
from decimal import Decimal


def tranforma(id_col):
    #print(id_col)
    b = ' '
    #Caso o  tamanho do numero binario for menor que 5
    if len(id_col) <= 8:
            b = 8-len(id_col)
            b ='{:0>8}'.format(id_col)
            #print(b, 'menor')
    #Caso o tamanho do numero binario for maior que 5
    if len(id_col) > 8:
            b = len(id_col) - 8
            b = id_col[b:]
            #print(b, 'maior')
            
    return b


x = 100
cont = 0
with open('orders.csv') as csvfile:
    global pegaId   
    read = csv.reader(csvfile)
    #Start
    inicio = time.time()
    for row in read:
        if cont <= x:
            if row[1] == 'id': continue
            pageId = row[1]
            #row[0] = pageId[13:]
            
            cont = cont +1
            pageId = ("{0:b}".format(int(pageId)))

            # Fase de construção Hash
            result = tranforma(pageId)

            f = 'temp/%s.csv'%result
            #a =f[5:9]
            if not os.path.exists(os.path.dirname(f)):
                try:
                     os.makedirs(os.path.dirname(f))
                # Caso não tenha permissão para criar pasta/ arquivo 
                except OSError as exc: 
                    if exc.errno != errno.EEXIST:
                        raise
            with open(f, 'a', encoding='utf-8') as filename:
                write = csv.writer(filename, lineterminator='\n')
                #write.writ("{0:b}".format(int(pageId[12:])))erow(['id', 'name', 'address', 'nationkey', 'phone', 'acctbal', 'mktsegment', 'comment' ])
                write.writerow(row) 
    print((pageId))

print('Tempo de contrução Bucket: %s segundos --' % (time.time() - inicio))



'''

# ============================= Fase de Matching ===================================
'''
start = time.time()
def match(tabela1, atributo1):
   
    x = 10 
    cont = 0 
    achou = ' '
    line = ' '
    with open(tabela1) as csvfile:
        #print('estou entrando')
        read = csv.reader(csvfile)
        for row in read:            
            if row[0] == atributo1:
                #print('achou no orders')
                #print( row[0], '=', atributo1)
                achou = row[0]
                #print("achou:", achou)
                line = row
                break
                
        atributo1 = ("{0:b}".format(int(achou)))
        atributo1 = tranforma(atributo1)
                
                #atributo1 = atributo1.split('/')[0].split('.')[0]
                
        try:
            bucket = 'temp/{}.csv'.format(atributo1)
            print(bucket)
        except:
            print("Bucket nao encontrado")
            return

        #print(atributo1)
        with open(bucket, 'r', encoding='utf-8') as arq:
            #print('entrou pra pegar')
            ler = csv.reader(arq)
            for linha in ler:
                print(linha[1],'*** casou ***', line[0])
                #input()
                if linha[1] == line[0]:
                    print(linha,'\n', line)
                    break
ttt = Decimal(repr(time.time()-start))
print('Tempo de Join:',' ',"{0:.15f}".format(round(ttt,2)))
#float("{:.8f}".format(float(ttt))
#print('Fase de Junção : %s segundos --', (%(time.time() - start)))
       
            



f = 'customer.csv'
a = '39136'
match(f, a)





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