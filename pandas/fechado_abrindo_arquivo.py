import os as os
import pandas as pd
import pygetwindow as gw
import time as time

rota = rota = "C:/Users/joth1/Documents/arquivo_excel.xlsx"
# fecha todos os arquivos
excel_window = gw.getWindowsWithTitle("Excel")
for excel in excel_window:
    excel.close()

# contabiliza 2 minutos e abre o arquivo 
time.sleep(120)
# abre o arquivo
os.startfile(rota)
print('Fim da execução com sucesso')

