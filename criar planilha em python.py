import openpyxl
from openpyxl.styles import Font

wb = openpyxl.Workbook()

sheet = wb.active
sheet.title = "dados de exemplo "
cabecalhos = ["nome","idade","email"]
sheet.append(cabecalhos)

dados = [
    ["lucas kalell", 26, "kalell306@gmail.com" ],
    ["ane caroline", 3, "anecaroline@hotmail.com"],
    ["carolinehainocz",23,"carol@gmail.com"],
]

for linha in dados:
    sheet.append(linha)
    for cell in sheet["1:1"]:
        cell.font = Font(bold=True)
wb.save("dados_exemplo.xlsx")

print("planilha criada com sucesso")