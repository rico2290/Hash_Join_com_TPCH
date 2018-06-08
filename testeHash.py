import pandas as pd
import time
import csv
import os
import errno

#with open('customer.tbl') as file:
#tabela = pd.read_table(file, sep='|', index_col=0, header=None, lineterminator='\n', names=['id','name','address','nationkey','phone','acctbal','mktsegment','comment'])
#saida = open('result.csv','w')
#tabela.to_csv(saida,index=None)

def tranforma(id_col):
    b = ' '
    if len(id_col) <= 5:
         #c = c+1
            b = 5-len(id_col)
            b ='{:0>5}'.format(id_col)
            #print(c)
            #print((b))
    if len(id_col) > 5:
            #c = c+1
            b = len(id_col) - 5
            b = id_col[b:]
            #print(c)
            #print((b))
    return b



x = 10
cont = 1
with open('customer.csv') as csvfile:
    global pegaId   
    read = csv.reader(csvfile)
    inicio = time.time()
    for row in read:
        if cont <= x:
            if row[0] == 'id': continue
            pageId = row[0]
            
            cont = cont +1
            pageId = ("{0:b}".format(int(pageId[12:])))

            #Fase de Transformação caso o tamanho do ID for menor ou maior do que o exigido
            result = tranforma(pageId)

            #Fase de Construção
            f = 'temp/%s.csv'%result
            if not os.path.exists(os.path.dirname(f)):
                try:
                     os.makedirs(os.path.dirname(f))
                except OSError as exc: # Caso nao tgenha permissão !!!
                    if exc.errno != errno.EEXIST:
                        raise

            with open(f, 'a', encoding='utf-8') as filename:
                writer = csv.writer(filename, lineterminator='\n')
                #for col in row:
                writer.writerow(row)
    print('#########', time.time()-inicio, 'segundos #########')

'''
x = 20
cont = 1
with open('orders.txt') as csvfile:
    global pegaId
    ler = csvfile.read()
    #ler = ler.split(',')
    print(ler)


'''














#Write list ojbect to csv
'''
res = [x, y, z, ....]
csvfile = "<path to output csv or txt>"

#Assuming res is a flat list
with open(csvfile, "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    for val in res:
        writer.writerow([val])    

#Assuming res is a list of lists
with open(csvfile, "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    writer.writerows(res)
            '''
        




          
            

                
