import openpyxl, pprint

wb = openpyxl.load_workbook('example.xlsx')
sheet = wb['Лист1']
print(sheet)
print(sheet['B1'].value)

list = wb.sheetnames


