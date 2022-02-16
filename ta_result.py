import xlrd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
# 这是个
rulename = ['SPT', 'LPT', 'EDD', 'MWKR', 'FDD_MWKR', 'MOPNR', 'FOPNR', 'RANDOM', 'DRL20×20','DRL30×20']
scatter_class = ['.', ',', 'o', 'v', '^', '<', '>', '1', '2', '3', '4','8']

case_num = 3
algorithm_num = 10

colors = ['C0', 'C1', 'C2', 'C8', 'C4', 'C5', 'C6', 'C7', 'C3','C9']

try:
    table = xlrd.open_workbook('实验结果.xls', 'rb')
    sh = table.sheet_by_name("动态ta1.5泛化")
    case_size = []
    for i in range(case_num):
        case_size.append(sh.cell(i + 1, 0).value)
    for i in range(algorithm_num):
        obj = []
        for j in range(case_num):
            obj.append(sh.cell(j + 1, 1 + i).value)
        plt.figure(1)
        plt.plot(case_size, obj, colors[i])
        plt.scatter(case_size, obj, marker=scatter_class[i], color=colors[i])
        plt.legend(rulename)
        plt.xlabel('算例规模')
        plt.ylabel('计算结果')
        plt.savefig('./动态ta1.5泛化/算法结果.png', dpi=400)

    plt.show()

except Exception as e:
    print(e)
