import matplotlib
matplotlib.use("TkAgg")

from matplotlib import pyplot
#1. Prepare data
text = ["Androis", "Ios", "Web"]
values = [300, 400, 300]
color = ["red", 'orange', 'green']
explode = [0.1,0.2,0.1]

#2. pyplot
pyplot.pie(values, labels = text, colors = color, explode= explode)
pyplot.axis('equal') # cho n tron

#3. Show
pyplot.show()
