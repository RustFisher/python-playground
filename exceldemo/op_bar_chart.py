from openpyxl import load_workbook
from openpyxl.chart import Reference, BarChart


def create_bar_chart(file_path):
    """
    插入柱形图
    :param file_path: Excel 文件路径
    :return: None
    """
    wb = load_workbook(file_path)
    st = wb.active

    data1 = Reference(st, min_col=2, min_row=1, max_row=7, max_col=3)
    cats1 = Reference(st, min_col=1, min_row=2, max_row=7)

    chart1 = BarChart()
    chart1.type = "col"
    chart1.style = 10
    chart1.title = "对比"
    chart1.y_axis.title = '数值'
    chart1.x_axis.title = st.cell(column=1, row=1).value

    chart1.add_data(data1, titles_from_data=True)
    chart1.set_categories(cats1)
    chart1.shape = 4
    st.add_chart(chart1, 'A8')
    wb.save(file_path)


if __name__ == '__main__':
    excel_path = 'out/指数.xlsx'
    create_bar_chart(excel_path)
