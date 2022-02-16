import xlrd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

rulename = ['SPT', 'LPT', 'EDD', 'MWKR', 'FDD_MWKR', 'MOPNR', 'FOPNR', 'RANDOM', 'DRL', 'GA']
scatter_class = ['.', ',', 'o', 'v', '^', '<', '>', '1', '2', '3', '4', '8']

case_num = 7
algorithm_num = 10
worse_rule = [0, 1, 2, 6, 7]
worse_rulename = ['MWKR', 'FDD_MWKR', 'MOPNR', 'DRL', 'GA']

try:
    table = xlrd.open_workbook('实验结果.xls', 'rb')
    sh = table.sheet_by_name("JSSP_Tardiness")
    case_size = []
    for i in range(case_num):
        case_size.append(sh.cell(3 * (i + 1), 0).value)
    for i in range(algorithm_num):
        obj = []
        obj_time = []
        for j in range(case_num):
            obj.append(sh.cell(3 * (j + 1) - 1, 2 + i).value)
            obj_time.append(sh.cell(3 * (j + 1) + 1, 2 + i).value)
        plt.figure(1)
        plt.plot(case_size, obj)
        plt.scatter(case_size, obj, marker=scatter_class[i])
        plt.legend(rulename)
        plt.xlabel('算例规模')
        plt.ylabel('算法结果Tardiness')
        plt.savefig('算法结果Tardiness.png', dpi=400)
        plt.figure(2)
        plt.plot(case_size, obj_time)
        plt.scatter(case_size, obj_time, marker=scatter_class[i])
        plt.legend(rulename)
        plt.xlabel('算例规模')
        plt.ylabel('算法平均用时/s')
        plt.savefig('算法平均用时.png', dpi=400)
        if i not in worse_rule:
            plt.figure(3)
            plt.plot(case_size, obj,color=plt.rcParams['axes.prop_cycle'].by_key()['color'][i])
            plt.scatter(case_size, obj, marker=scatter_class[i],color=plt.rcParams['axes.prop_cycle'].by_key()['color'][i])
            plt.legend(worse_rulename)
            plt.xlabel('算例规模')
            plt.ylabel('算法结果Tardiness')
            plt.savefig('算法结果Tardiness_局部放大.png', dpi=400)

        if i == 9:
            continue
        else:
            plt.figure(4)
            plt.plot(case_size, obj_time)
            plt.scatter(case_size, obj_time, marker=scatter_class[i])
            plt.legend(rulename[0:-1])
            plt.xlabel('算例规模')
            plt.ylabel('算法平均用时/s')
            plt.savefig('算法平均用时_局部放大.png', dpi=400)

    plt.show()

except Exception as e:
    print(e)
