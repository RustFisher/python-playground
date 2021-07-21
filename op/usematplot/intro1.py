import math

import matplotlib.pyplot as plt


def demo1():
    x_list = []
    y_list = []
    for i in range(0, 100):
        x_list.append(i)
        y_list.append(math.sin(i * 0.1))
    ax = plt.gca()
    ax.set_title('rustfisher.com mapplotlib example')
    ax.set_xlabel('x')
    ax.set_ylabel('y = sin(x)')
    ax.grid()
    plt.plot(x_list, y_list)
    plt.show()
    # plt.savefig('out.png')


def demo_subplot():
    x_list = []
    y_list = []
    y2_list = []
    for i in range(0, 365):
        x_list.append(i)
        y_list.append(math.sin(i * 0.1))
        y2_list.append(math.cos(i * 0.1))
    fig, (ax1, ax2) = plt.subplots(2)
    ax1.set_title('rustfisher.com 1')
    ax2.set_title('rustfisher.com 2')
    ax1.set_xlabel('x')
    ax1.set_ylabel('y = sin(x)')
    ax2.set_xlabel('x')
    ax2.set_ylabel('y = cos(x)')
    ax1.plot(x_list, y_list)
    ax2.plot(x_list, y2_list)
    fig.tight_layout()
    plt.show()


def demo3():
    x_list = []
    y_list = []
    y2_list = []
    for i in range(0, 365):
        x_list.append(i)
        y_list.append(math.sin(i * 0.1))
        y2_list.append(math.cos(i * 0.1))
    fig, (ax1, ax2) = plt.subplots(2)
    ax1.set_title('rustfisher.com 1')
    ax1.set_xlabel('x')
    ax1.set_ylabel('y = sin(x)')
    ax2.set_title('rustfisher.com 2')
    ax2.set_xlabel('x')
    ax2.set_ylabel('y = cos(x)')

    ax1.set_xlim(left=50, right=200.6)
    ax1.set_ylim(top=1, bottom=0.3)

    ax2.set_xlim(xmin=1, xmax=156.6)
    ax2.set_ylim(ymin=-0.3, ymax=0.3)

    ax1.plot(x_list, y_list)
    ax2.plot(x_list, y2_list)

    ax1.set_xticks([50, 60, 70, 150])
    ax1.set_yticks([0.1, 0.2, 0.3, 0.7, 0.9])
    ax1.grid()  # 显示格子

    ax2.set_xticks([1, 60, 70, 150], minor=True)
    ax2.set_yticks([-0.1, 0, 0.1, 0.3], minor=True)
    ax2.grid()

    plt.setp(ax1.xaxis.get_majorticklabels(), rotation=-45)
    plt.setp(ax2.xaxis.get_majorticklabels(), rotation=-60)

    fig.tight_layout()
    plt.show()


def demo_spine():
    x_list = []
    y_list = []
    for i in range(0, 365):
        x_list.append(i)
        y_list.append(math.sin(i * 0.1))

    fig, (ax1, ax2, ax3) = plt.subplots(3)
    ax_list = [ax1, ax2, ax3]
    for i in range(0, 3):
        cur_ax = ax_list[i]
        cur_ax.set_title('rustfisher.com ' + str(i))
        cur_ax.plot(x_list, y_list)
        cur_ax.set_xlabel('x')
        cur_ax.set_ylabel('y = sin(x)')

    fig.tight_layout()
    plt.show()


if __name__ == '__main__':
    print('rustfisher 图表讲解')
    demo_spine()
