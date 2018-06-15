import pyodbc
import pandas as pd
import os
import csv
#import erro


s = "access_result.csv"

con = pyodbc.connect("DRIVER={Sql Server};server=localhost;database=tpc-h;user=sa;pwd=123456")
cur = con.cursor()
cur.execute("select c_custkey, c_name from customer")
for row in cur:
    #print(row.c_custkey,"***", row.c_name)
    with open(s, "a", encoding="utf-8") as arq:
        linha = csv.writer(arq, lineterminator="\n")
        linha.writerow(row)
print("Resultado Finalizado!!!")
cur.close()
con.close()

