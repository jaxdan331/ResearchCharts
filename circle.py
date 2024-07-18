import matplotlib
from typing import List, Tuple

# matplotlib.use('Agg')  # 使用Agg后端，这个后端适用于生成图像文件但不显示它们
matplotlib.use('TkAgg')  # 选择合适的后端，如Agg, TkAgg
import matplotlib.pyplot as plt
import numpy as np
import random as rm

# plt.rcParams["font.sans-serif"] = ["SimHei"]  # 设置字体
# plt.rcParams["axes.unicode_minus"] = False  # 该语句解决图像中的“-”负号的乱码问题

# 设置默认字体为'Arial'
matplotlib.rcParams['font.family'] = 'Arial'


# matplotlib.rcParams['font.family'] = 'Times New Roman'


def plot_circle():
    # Setting labels for items in Chart
    Employee = ['Language', 'Commonsense', 'Agent', 'Safety']

    # Setting size in Chart based on
    # given values
    Salary = [40000, 50000, 70000, 54000]
    # colors
    colors = ['#FF0000', '#0000FF', '#FFFF00', '#ADFF2F']
    # explosion
    explode = (0.15, 0.05, 0.05, 0.05)
    # Pie Chart
    plt.pie(
        Salary,
        colors=colors,
        labels=Employee,
        autopct='%1.1f%%',  # 显示百分比
        pctdistance=0.7,  # 百分比离圆心的距离
        explode=explode
    )
    # draw circle
    centre_circle = plt.Circle((0, 0), 0.5, fc='white')
    fig = plt.gcf()
    # Adding Circle in Pie chart
    fig.gca().add_artist(centre_circle)
    # Adding Title of chart
    plt.title('Employee Salary Details')
    # Displaing Chart
    plt.show()


def plot_circle1():
    # 数据
    labels = ['Label1', 'Label2', 'Label3', 'Label4']
    sizes = [15, 30, 45, 10]
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']

    # explosion
    explode = (0.0, 0.0, 0.0, 0.0)

    # 绘图
    fig1, ax1 = plt.subplots()
    ax1.pie(
        sizes,
        labels=labels,
        colors=colors,
        autopct='%1.1f%%',
        pctdistance=0.45,
        startangle=90,
        explode=explode,
        wedgeprops=dict(width=0.8, edgecolor='w')
    )
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    # Draw a white circle at the center
    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)

    plt.show()


def plot_circle2():
    import numpy as np
    import matplotlib.pyplot as plt
    # plt.rcParams['font.family'] = 'SimHei'
    r1, r2 = 1.3, 0.5
    data = [[60., 32.], [37., 40.], [29., 10.]]
    plt.subplot(121)
    # 使用numpy处理数据
    vals = np.array(data)
    print(vals.sum(axis=1))
    print(vals.flatten())
    # 内层圆环
    plt.pie(
        vals.sum(axis=1),
        radius=r1 - r2,
        autopct='%1.1f%%',
        pctdistance=0.6,
        wedgeprops=dict(width=r2, edgecolor='w')
    )
    # 外层圆环
    plt.pie(
        vals.flatten(),
        radius=r1,
        autopct='%1.1f%%',
        pctdistance=0.8,
        wedgeprops=dict(width=r2, edgecolor='w')
    )
    plt.title('Bi-layered circular diagram')

    plt.subplot(122)
    # 使用Python内置方法处理数据
    # 按分组求和作为内层圆环数据源
    sums = [sum(i) for i in data]
    # 展平数据作为外层圆环数据源
    flatten = sum(data, [])
    # 内层圆环
    plt.pie(
        sums,
        radius=r1 - r2,
        autopct='%1.1f%%',
        pctdistance=0.6,
        wedgeprops=dict(width=r2, edgecolor='w')
    )
    # 外层圆环
    plt.pie(
        flatten,
        radius=r1,
        autopct='%1.1f%%',
        pctdistance=0.8,
        wedgeprops=dict(width=r2, edgecolor='w')
    )
    plt.title('Bi-layered circular diagram')
    plt.show()


def generate_hex_color():
    return '#' + ''.join(rm.choice('0123456789ABCDEF') for _ in range(6))


def bi_layered_circular_diagrams(values: List[Tuple], labels_1: List, labels_2: List):
    """
    双层环形图
    :param values: 按组划分的数值，全部展开后为外层环的数值，按组求和后为内层环的数值
    :param labels_1: 内层环的标签
    :param labels_2: 外层环的标签
    :return:
    """
    # # 数据值和标签
    # V = 1 / 13
    # values = [(2 * V, 2 * V, 2 * V, 3 * V), (V, V), (V, V)]
    # print(values)
    #
    # # 标签
    # labels_1 = ['Chatting', 'Emotional', 'Feedback']
    # labels_2 = ['Consistency', 'Coherence', 'Expressive', 'Safety', 'Empathy', 'Helpful', 'Favourite', 'Character']

    # 设置数据值
    values_1 = [sum(v) for v in values]
    # values_2 = [*values[0], *values[1], *values[2]]
    values_2 = [i for v in values for i in v]
    print(values_1)
    print(values_2)
    # values_1 = [48.0, 31.0, 21.0]
    # values_2 = [12.5, 10.0, 12.5, None, 18.0, 13.0, None]

    # 设置扇区颜色
    colors_1 = ['#99CCFF', '#FF99CC', '#CCFF00']
    # RGBA 颜色，最后两位表示透明度
    colors_2 = ['#99CCFF60', '#99CCFF60', '#99CCFF60', '#99CCFF95', '#FF99CC70', '#FF99CC40', '#CCFF0085', '#CCFF0060']

    # 设置阴影颜色
    explode_1 = (0, 0, 0)
    explode_2 = (0, 0, 0, 0, 0, 0, 0, 0)

    r1, r2 = 1.0, 1.35

    # 绘制双层圆环图
    # # 内层圆环
    # plt.subplot(221)
    # plt.pie(
    #     values_1,
    #     labels=labels_1,
    #     colors=colors_1,
    #     radius=r1,
    #     explode=explode_1,
    #     # autopct='%1.1f%%',  # 在扇形中显示百分比
    #     # pctdistance=0.2,  # 百分比标签距圆心距离
    #     labeldistance=0.2,  # 标签距圆心距离
    #     startangle=90,
    #     wedgeprops=dict(width=1.0, edgecolor='w')
    # )
    # # 外层圆环
    # plt.subplot(222)
    # plt.pie(
    #     values_2,
    #     labels=labels_2,
    #     colors=colors_2,
    #     radius=r2,
    #     explode=explode_2,
    #     # autopct='%1.1f%%',  # 在扇形中显示百分比
    #     # pctdistance=0.2,
    #     startangle=90,
    #     wedgeprops=dict(width=1.0, edgecolor='w')
    # )
    #
    # plt.subplot(223)
    # 绘制双层饼图的时候得先绘制大图，在绘制小图
    # 外层圆环
    # plt.setp(plt.gca(), aspect='equal')
    plt.pie(
        values_2,
        labels=labels_2,
        colors=colors_2,
        radius=r2,
        explode=explode_2,
        autopct='%1.1f%%',  # 在扇形中显示百分比
        pctdistance=0.87,
        startangle=60,
        wedgeprops=dict(width=1.0, edgecolor='w'),
    )
    # 内层饼图
    plt.pie(
        values_1,
        labels=labels_1,
        colors=colors_1,
        radius=r1,
        explode=explode_1,
        # autopct='%1.1f%%',  # 在扇形中显示百分比
        # pctdistance=1.0,  # 百分比标签距圆心距离
        labeldistance=0.25,  # 标签距圆心距离
        startangle=60,
        textprops={'fontname': 'Arial', 'fontsize': 12},
        wedgeprops=dict(width=1.0, edgecolor='w')
    )
    # plt.title('Human Evaluation Paradigm')

    # 显示图形
    plt.show()


def plot_circle3():
    # 定义数据
    sizes = [215, 130, 245, 210]
    labels = ['A', 'B', 'C', 'D']

    # 创建饼图
    plt.figure(figsize=(5, 5))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', pctdistance=0.85)

    # 获取饼图的扇形角度和半径
    angles = plt.gca().patches[0].theta1
    radii = 0.5 / np.cos(np.deg2rad(angles))

    # 在扇形内部居中显示文本
    for angle, size, label in zip(angles, radii, labels):
        ha = 'center' if angle > 90 else 'left'
        va = 'center' if angle > 180 else 'bottom'
        plt.text(angle, size, label, size=12, ha=ha, va=va, fontweight='bold', color='white')

    # 显示图形
    plt.show()


if __name__ == '__main__':
    # plot_circle()
    # plot_circle1()
    # plot_circle2()
    # 设置最小分度值
    V = 1 / 13
    bi_layered_circular_paradigm(
        values=[(2 * V, 2 * V, 2 * V, 3 * V), (V, V), (V, V)],
        labels_1=['Chatting', 'Emotional', 'Feedback'],
        labels_2=['Consistency', 'Coherence', 'Expressive', 'Safety', 'Empathy', 'Helpful', 'Favourite', 'Character']
    )

    # plot_circle3()
