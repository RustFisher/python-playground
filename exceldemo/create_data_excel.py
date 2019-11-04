import os

from openpyxl import Workbook


def create_excel_demo(file_path):
    """
    创建Excel文件，并写入数据
    :param file_path: 目标文件路径
    :return none
    """
    wb = Workbook()
    ws = wb.active
    ws.title = '搜索指数概览'

    ws.append(['关键词', '整体日均值', '移动日均值', '整体同比', '整体环比', '移动同比', '移动环比'])
    ws.append(['excel', 27782, 18181, -0.11, -2, 0.21, 0.02])
    ws.append(['python', 24267, 8204, 0.27, 0.06, 0.56, 0.01])
    ws.append(['文案', 2411, 1690, 0.56, 0.33, 0.91, 0.46])
    ws.append(['okr', 1928, 880, 0.38, 0.15, 0.29, 0.09])
    ws.append(['kpi', 4212, 2784, 0.21, -0.19, 0.36, -0.22])
    wb.save(file_path)


if __name__ == '__main__':
    if not os.path.exists('out'):
        os.mkdir('out')
    create_excel_demo('out/指数.xlsx')
