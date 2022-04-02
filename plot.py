import numpy as np 
from matplotlib import pyplot as plt 



res = []
fp = open('re1', 'r')
try:
    lines = fp.readlines()#读取出全部数据，按行存储
finally:
    fp.close()
point = lines[0]
x = point[point.find("(")+1:point.find(",")]
y = point[point.find(",")+1:point.find(")")]
#print(x,y)
for line in lines[1:]:
    line_list = line.split()
    #print(line_list)
    nx=[]
    ny=[]
    for index in range(1,len(line_list)):
        point = line_list[index]
        x = float(point[point.find("(")+1:point.find(",")])
        y = float(point[point.find(",")+1:point.find(")")])
        nx.append(x)
        ny.append(y)
    print(nx,ny)
    plt.plot(nx, ny, linewidth=6)

plt.show()
plt.savefig("fig")

      

        
