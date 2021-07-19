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


if __name__ == '__main__':
    print('rustfisher 绘制折线图事例1')
    demo1()
