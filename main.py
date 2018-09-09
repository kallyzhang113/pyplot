# coding:utf8
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
from dateutil import rrule
import load_data
import random
def compare_key2num(elem):
    return int(elem[0])

def compare_value(elem):
    return int(elem[1])

def generate_graph(graph_type, keys, values, title, xlabel=None, ylabel=None,labels=None,xlim=None, ylim=None, marker=None, tag=False, accumulate=False):
    bar_width = 0.45
    n = len(values)
    for i in range(n):
        if graph_type == 'bar':
            accumulate_height = values[0]
            if i == 0:
                plt.bar(range(len(keys[i])), values[i], label=labels[i], align='center', alpha=0.8, width=bar_width)
                if tag:
                    for x, y in enumerate(values[i]):
                        plt.text(x, y + 5, '%s' % y, ha='center')
            else:
                if accumulate == False:
                    plt.bar(np.arange(len(keys[i])) + i*bar_width, values[i], label=labels[i], align='center', alpha=0.8, width=bar_width)
                else:
                    plt.bar(np.arange(len(keys[i])), values[i], label=labels[i], align='center', alpha=0.8, width=bar_width, bottom=accumulate_height)
                    for ah in range(len(accumulate_height)):
                        accumulate_height[ah] += values[i][ah]
                if tag:
                    for x, y in enumerate(values[i]):
                        plt.text(x+i*bar_width, y + 5, '%s' % y, ha='center')

        elif graph_type == 'plot':
            linestyles = ['-.','-','--',':']
            plt.plot(keys[i], values[i], marker=marker, label=labels[i],linestyle=linestyles[random.randint(-1,3)])
            if tag:
                for x, y in enumerate(values[i]):
                    plt.text(x, y + 5, '%s' % y, ha='center')

        elif graph_type == 'pie':
            patches, l_text, p_text = plt.pie(values, labels=keys, autopct='%3.1f%%', shadow=False, startangle=90, pctdistance=0.6)
            for t in l_text:
                t.set_size = (10)
            for t in p_text:
                t.set_size = (10)
            plt.axis('equal')
            break

    plt.title(title)

    if graph_type == 'bar':
        # xticks
        if accumulate == False:
            plt.xticks(np.arange(len(keys[0])) + 0.5 * (n-1) * bar_width, keys[0])
        else:
            plt.xticks(np.arange(len(keys[0])), keys[0])

    if graph_type == 'bar' or graph_type == 'plot':
        if xlabel != None:
            plt.xlabel(xlabel)
        if ylabel != None:
            plt.ylabel(ylabel)
        if xlim != None:
            plt.xlim(xlim)
        if ylim != None:
            plt.ylim(ylim)

    plt.legend()
    plt.show()
