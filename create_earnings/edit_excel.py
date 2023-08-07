import openpyxl
import configparser
import datetime

def open_excel() : 
    #設定ファイルからエクセルのパスを取得
    inifile = configparser.SafeConfigParser()
    inifile.read('config/config.ini', encoding='utf-8')
    excel_path = inifile.get('DEFAULT', 'ExcelPath')
    
    #現年の販売リストシートを開く
    wb = openpyxl.load_workbook(excel_path)
    current_year = datetime.date.today().year
    ws = wb['販売リスト %s' %current_year]
    
    for row in ws.iter_rows():
        for cell in row:
            print(cell.value)
    maxRow = ws.max_row
    print(maxRow)
    #ws.cell(row=2, column=1).value = 1
    #wb.save(excelPath)