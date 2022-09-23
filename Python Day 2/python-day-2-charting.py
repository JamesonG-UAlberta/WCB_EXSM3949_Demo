import matplotlib.pyplot as plt

graph_x = [0,1,2,3]
graph_x2 = [10,20,30,40,50]
graph_y = [3,2,1,0]
graph_y2 = [-10,-20,-30,-40,-50]

plt.title("My Graph", loc="right")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.plot(graph_x, graph_y, marker='*', markersize = 15, linestyle = '--', color = "red", linewidth = 30, label="Data Set 1")
plt.plot(graph_x2, graph_y2, label="Data Set 2")
plt.legend()
plt.grid()
plt.show()

#The x and y axis data points are required
#All other attributes are optional

#Markers: Symbol that indicates the data point
#o: circle marker
#*: star marker
#x: x marker
#s: square marker
#D: diamond marker

#Linestyle: The style of the graph line
#-: solid line
#--: dashed line
#:: dotted line
#-.: dashed/dotted line

#Line Color: The color of the graph line
#There are 140 defined colors that can be used, otherwise you can use hexademical codes to define a color

#Line Width: Changes the thickness of the graph line



