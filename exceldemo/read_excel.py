from openpyxl import load_workbook


def read_xlsx_basic(file_path):
    """
    读取Excel的数据并打印出来
    """
    wb = load_workbook(file_path)
    st = wb.active
    end_row = st.max_row
    end_column = st.max_column
    print(st.title, '有', end_row, '行', end_column, '列')
    for row in range(1, end_row):
        for col in range(0, end_column):
            print(st.cell(row=row, column=col).value, end='\t')
        print()


if __name__ == '__main__':
    excel_path = 'out/指数.xlsx'
    ws1 = load_workbook(excel_path).active
    if ws1 is None:
        print('表格不存在')
    else:
        read_xlsx_basic(excel_path)
