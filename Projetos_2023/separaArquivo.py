import pandas as pd
import tkinter as tk
from tkinter import filedialog

# Abrindo janela para seleção do arquivo csv
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()

# Lendo o arquivo csv com pandas usando a codificação "ANSI" e delimitador ';'
df = pd.read_csv(file_path, encoding='ANSI', sep=';')
nomeArquivo = file_path.split('/')[-1].split('.')[-2]

# Definindo o número máximo de linhas por parte
max_rows_per_part = 500000
pathOut = 'C:path'
# Dividindo o dataframe em partes com um número máximo de linhas
num_parts = len(df) // max_rows_per_part + 1
for i in range(num_parts):
    start = i * max_rows_per_part
    end = min(start + max_rows_per_part, len(df))
    df_part = df.iloc[start:end]
    df_part.to_csv(f'{pathOut}/{nomeArquivo}_{i}.csv', index=False, encoding='ANSI', sep=';')

