#import pandas as pd
#import numpy as np
import csv

#with open('customer.tbl') as file:
#tabela = pd.read_table(file, sep='|', index_col=0, header=None, lineterminator='\n', names=['id','name','address','nationkey','phone','acctbal','mktsegment','comment'])
#saida = open('result.csv','w')
#tabela.to_csv(saida,index=None)
x = 20
cont = 0
with open('result.csv') as csvfile:
    global pegaId       
    read = csv.reader(csvfile)
    for row in read:
        if cont <= x:
            if row[0] == 'id': continue
            pageId = row[0]
            
            cont = cont +1
            pageId = ("{0:b}".format(int(pageId[12:])))
            #print(type(pageId)
            #caso o tamanho do ID for menor que o exigido
            if len(pageId) <= 5:
                a = 5-len(pageId)
                a ='{:0>5}'.format(pageId)
                print(a)
                