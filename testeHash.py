import pandas as pd
#import numpy as np
import csv

'''
with open('orders.tbl') as file:
    tabela = pd.read_table(file, sep='|', index_col=0, header=None, lineterminator='\n', 
                        names=['orderKey','custKey','orderStatus','totalPrice','orderDate','orderPriority',
                        'clerk','shipPriority', 'comment'])
    saida = open('order.csv','w')
    tabela.to_csv(saida,index=None) '''

'''
def transform(idCol):
     #Se nao atingir o tamanho permitido
     if len(idCol) <= 12:
        t = 12-len(idCol)
        t = '{:0>12}'.format(idCol)
        print(t)
       
     #Se passar do tamanho permitido
     if len(idCol) > 12:
        t = len(idCol)-12
        t = idCol[t:]
        print(t)
        #t = '{:0>12}'.format(idCol) 
        #print(t)
   
     
x = 20
cont = 0
with open('order.csv') as csvfile:      
    read = csv.reader(csvfile)
    for row in read:
        if cont < x:
            cont = cont+1
            print(row)
print('################################################################################')

x = 20
cont = 0
with open('customer.csv') as csvfile:   
    read = csv.reader(csvfile)
    for row in read:
        if cont < x:
            cont = cont+1
            print(row)


transform('110101')

'''
def transform(idCol):
     contador = 0
     t = ' '
     #Se nao atingir o tamanho exigido
     if len(idCol) <= 12:
        t = 12-len(idCol)
        t = '{:0>12}'.format(idCol)
        print(t)
        
       
     #Se passar do tamanho exigido
     if len(idCol) > 12:
        t = len(idCol)-12
        t = idCol[t:]
        print(t)
        #t = '{:0>12}'.format(idCol) 
       
     




#x = 200
#cont = 0
with open('customer.csv') as csvfile:
     pegaId = ' '   
     s = 0 #confirmar qtde d linhas impressas    
     read = csv.reader(csvfile)
     for row in read:
       
        if row[0] == 'id': 
            continue
        pageId = row[0]
        s = s+1
        pageId = ("{0:b}".format(int(pageId[12:])))
        print(type(pageId)