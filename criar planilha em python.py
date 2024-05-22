import openpyxl
from openpyxl.styles import Font

wb = openpyxl.Workbook()

sheet = wb.active
sheet.title = "dados de exemplo "
cabecalhos = ["nome","idade","email","cidade","estado","pais"]
sheet.append(cabecalhos)

dados = [
    ["lucas f", 26, "kalell306@gmail.com","londrina", "parana","brasil"],
    ["lucas bruno", 26, "kalew909@gmail.com","ponta grossa", "parana","brasil"],
    ["lucas o.g", 26, "klew300@gmail.com","londrina", "parana","brasil"],
    ["ane peixe", 10, "anecars@hotmail.com","ponta grossa", "parana","brasil"],
    ["carolin wrosh",23,"tramontina@gmail.com","londrina", "parana","brasil"],
]

for linha in dados:
    sheet.append(linha)
    for cell in sheet["1:1"]:
        cell.font = Font(bold=True)
wb.save("dados_exemplo.xlsx")

print("planilha criada com sucesso")