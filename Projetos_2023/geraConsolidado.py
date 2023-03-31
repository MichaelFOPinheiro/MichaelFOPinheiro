import pandas as pd
import tkinter as tk
from tkinter import filedialog
from openpyxl.utils import get_column_letter

# Abrindo o arquivo csv usando o diálogo do tkinter
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()
pathOut = 'C:/path'
# Lendo o arquivo csv com pandas
df = pd.read_csv(file_path, header=0, encoding='ANSI', sep=';')

# Consolidando os dados por data, produto, preco e quantidade
consolidado = df.groupby(['Data', 'Produto', 'Preco'])['Quantidade'].sum().reset_index()

# Criando um arquivo Excel com a tabela consolidada usando Pandas Styler
writer = pd.ExcelWriter(f'{pathOut}/consolidado.xlsx', engine='xlsxwriter')
consolidado.to_excel(writer, sheet_name='Consolidado', index=False)

# Formatando a tabela com Pandas Styler
workbook = writer.book
worksheet = writer.sheets['Consolidado']
header_format = workbook.add_format({
    'bold': True,
    'text_wrap': True,
    'valign': 'top',
    'fg_color': '#2F4F4F',
    'border': 1,
    'font_color': 'white'
})
for col_num, value in enumerate(consolidado.columns.values):
    worksheet.write(0, col_num, value, header_format)
for row in range(1, len(consolidado)+1):
    for col in range(len(consolidado.columns)):
        worksheet.write(row, col, consolidado.iloc[row-1,col])
data_format = workbook.add_format({'num_format': '#,##0'})
worksheet.set_column('A:A', 12)
worksheet.set_column('B:B', 20)
worksheet.set_column('C:C', 20, data_format)
worksheet.set_column('D:D', 15, data_format)

# Salvando o arquivo Excel
writer.save()
