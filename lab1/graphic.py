import matplotlib.pyplot as pyplot


def graphics(frame):
    type_graph = ['line', 'hist', 'box', 'kde', 'density', 'bar', 'scatter', 'hexbin', 'area', 'pie']
    print('Select number of graphics:')
    n = int(input())
    print("Select from this columns:\n" + "\n".join(frame.columns) + "\n")
    print("Select from this kinds of graphic:\n" + "\n".join(type_graph) + "\n")

    for i in range(n):
        print('Select graphic in that format: column_x:column_y:graphic_kind')
        str = input().split(":")
        frame.plot(x=str[0], y=str[1], kind=str[2])

    pyplot.xticks(rotation=90)
    pyplot.show()
