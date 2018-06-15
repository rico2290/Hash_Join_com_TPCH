import pandas as pd
import csv
import os
import errno
import time

def adjust(id_col):
    '''
    Função para deixar a saída em bits do tamanho adequado.
    '''
    b = ' '
    
    #Caso o  tamanho da numero binario for menor que 8
    if len(id_col) <= 12:
            b = 12-len(id_col)
            b ='{:0>12}'.format(id_col)
    #Caso o tamanho da numero binario for maior que 8
    if len(id_col) > 12:

            b = len(id_col) - 12
            b = id_col[b:]
    return b

#

def create_buckets(table_name='orders.csv'):
    '''
    Função que pega uma tabela .csv e cria seus respectivos buckets.
    '''

    with open(table_name) as csvfile:
        print("Start to build buckets...")
        read = csv.reader(csvfile)
        
        inicio = time.time()

        for row in read:
            #if cont <= x:
            if row[0] == 'id':
                continue
            
            #print(row, row[0], type(row[0]) )
            join_attribute = row[0]
                        
            join_attribute_binary = "{0:b}".format(int(join_attribute))
            #print(join_attribute_binary, join_attribute, type(join_attribute_binary))
            #input("Enter...")

            #Caso o tamanho do atributo de junção for menor que o exigido:
            bucket_name = adjust(join_attribute_binary)
            
            #inicio = time.time()
            
            #O endereço dos buckets com seus respectivos nomes:
            #Pegando o nome da tabela sem o '.csv'.
            bucket_subpath = table_name.split('.')[0]
            bucket_path = 'temp/{}/{}.csv'.format(bucket_subpath, bucket_name)
            
            #Se não existe o endereço desse bucket:
            if not os.path.exists( os.path.dirname(bucket_path) ):
                try:
                    os.makedirs(os.path.dirname(bucket_path))
                
                # Caso não tenha permissão para criar pasta/ arquivo 
                except OSError as exc: 
                    if exc.errno != errno.EEXIST:
                        raise
            #
            
            with open(bucket_path, 'a', encoding='utf-8') as filename:
                write = csv.writer(filename, lineterminator='\n')
                #writer.seek(0)
                #primeira_letra = csv.reader(filename)
                #if not primeira_letra:
                #write.writerow(['id', 'name', 'address', 'nationkey', 'phone', 'acctbal', 'mktsegment', 'comment' ])
                #else:
                write.writerow(row) 
        #
    
    print("End of Create Buckets: %s sec --" % (time.time() - inicio))

#

def transform_tbl(table_name=None, path=None):
    '''
    Função para transformar um .tbl para .csv.
    '''

    #Caminho do .tbl:
    path = 'TPCH/tpch-dbgen/' + table_name

    #Pegando o nome da table:
    table_name = table_name.split('.')[0]

    #Abrindo o arquivo .tbl:
    with open(path) as file:
        table = pd.read_table(file, sep='|', lineterminator='\n')
        result = open(table_name + '.csv','w')
        table.to_csv(result, index=False)

#

def exist_buckets(table_name=None):
    '''
    Função que checa se os Buckets já estão construídos.
    '''
    #Pegando o nome da tabela sem o '.csv'.
    bucket_subpath = table_name.split('.')[0]
    bucket_path = os.path.dirname('temp/{}/'.format(bucket_subpath))

    return os.path.exists(bucket_path)

#

def match(table_smaller=None, table_bigger=None, attribute=None):
    
    inicio = time.time()

    #Abrindo o arquivo que contêm as tuplas: 
    with open(table_smaller) as csvfile:
        #count, maximum = 0,20
        print('Open smaller table: {}'.format(table_smaller))
        
        #Lendo todo o arquivo csv:
        read = csv.reader(csvfile)

        #Para cada linha:
        for row in read:
            #Limitador de operação:
            #if count == maximum:
            #    break
            
            #count=count+1
            
            #Pegando o atributo de junção:
            join_attribute = row[0]  
                       
            #Verificação de teste:
            if join_attribute == attribute:
                
                join_attribute_binary = ("{0:b}".format(int(join_attribute)))
                join_attribute_binary = adjust(join_attribute_binary)

                print("Attribute: ", join_attribute, " = Bucket { ", join_attribute_binary, " }")

                try:
                    bucket_subpath = table_bigger.split('.')[0]
                    bucket_path = 'temp/{}/{}.csv'.format(bucket_subpath, join_attribute_binary)
                    #print(bucket_path)

                    with open(bucket_path, 'r', encoding='utf-8') as bucket:
                        print('Entrando no Bucket: {}'.format(bucket_path))
                        
                        #Fazendo a leitura do CSV do Bucket:
                        bucket = csv.reader(bucket)
                        
                        #Percorrer cada linha do Bucket, procurando pelo atributo de junção:
                        row_count = 0
                        for bucket_row in bucket:
                            #Pegando o atributo de junção do Bucket:
                            join_attribute_bucket = bucket_row[0]
                            
                            if join_attribute == join_attribute_bucket:
                                print(row_count, ' : ', row, " |", bucket_row)
                                print()
                                
                            row_count = row_count + 1
                    #
                
                except Exception:
                    print(Exception)

                    print("Caminho com Bucket não encontrado.")
                    return
                

    print("End of Match: %s sec --" % (time.time() - inicio))

#

def hash_join(table_smaller='customer.csv', table_bigger='orders.csv', join_attribute='39136'):
    '''
    Função de implementação do Hash Join.
    '''
    
    #Verificando qual a maior tabela. E a menor também:
    #table_bigger, table_smaller = table_info()

    #Se os buckets da tabela maior não estão construídos, construí-los:
    if not exist_buckets(table_name=table_bigger):
        create_buckets(table_name=table_bigger)

    #Fazendo o match dos valores:
    match(table_smaller=table_smaller, table_bigger=table_bigger, attribute=join_attribute)

#

#Fazendo um Hash Join com Customer e Orders. O atributo de junção é o ID 39136:
hash_join(join_attribute='39136')

#exist_buckets(table_name="orders.csv")

#transform_tbl('customer.tbl')
#get_bucketName('temp/00000.csv')
#create_buckets()
