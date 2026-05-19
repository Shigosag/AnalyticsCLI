import plotext as plt

def show_bar_chart(x, y, title="Chart"):
    plt.clt()
    plt.bar(x, y)
    plt.title(title)
    plt.show()
