# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt


def drawchunk(chunklist):
    if len(chunklist) == 0:
        return
    index = []
    names = []
    lengths = []
    count = len(chunklist)
    for i in range(count):
        chunk = chunklist[i]
        index.append(i)
        names.append(chunk.name)
        lengths.append(chunk.length)
    plt.bar(index, lengths, facecolor='g')
    plt.xticks(range(count), names)
    for x, y in zip(index, lengths):
        plt.text(x, y, '%d' % y, ha='center', va='bottom')
    plt.xlabel('name')
    plt.ylabel('length')
    plt.title('PNG Chunk Length')
    plt.show()
