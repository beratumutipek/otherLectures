import matplotlib.pyplot as plt
import numpy as np
# numpy is only for arraying
# matplotlib is for ploting the graph
x = [2.0, 4.0, 7.0, 8.0, 10.0]
y = [1.5, 4.5, 9.3, 5.4, 14.5]

k_values = []
k_eq = []

for i in range(1, 4):
    k=np.zeros([6], float)
    k[i-1] = x[i-1]-x[i]
    k[i] = 2*(x[i-1]-x[i+1])
    k[i+1] = x[i]-x[i+1]
    k[5] = 6*(((y[i-1]-y[i])/(x[i-1]-x[i]))-((y[i]-y[i+1])/(x[i]-x[i+1])))
    k_values.append([k[1], k[2], k[3]])
    k_eq.append(k[5])
eq_array= np.array(k_eq)
k_array = np.array([k_values[0], k_values[1], k_values[2]])


#Gaussian Eliminiation Method
n = len(eq_array)
Ks = np.zeros(n, float)
for k in range(n-1):
    for i in range(k+1, n):
        factor = k_array[i, k] / k_array[k, k]
        for j in range(k, n):
            k_array[i, j] = k_array[i, j] - factor * k_array[k, j]
        eq_array[i] = eq_array[i] - factor * eq_array[k]

Ks[n-1] = eq_array[n-1] / k_array[n-1, n-1]
for i in range(n-2, -1, -1):
    sum = eq_array[i]
    for j in range(i+1, n):
        sum = sum - k_array[i, j] * Ks[j]
    Ks[i] = sum / k_array[i, i]

k2, k3, k4 = Ks
k1 = 0
k5 = 0
list_K = [k1, k2, k3, k4, k5]
list_A=[]
list_B=[]

for i in range (0,4):
    A =(((y[i])/(x[i]-x[i+1]))-(1/6)*list_K[i]*(x[i]-x[i+1]))
    B =(((y[i+1])/(x[i]-x[i+1]))-(1/6)*list_K[i+1]*(x[i]-x[i+1]))
    list_A.append(A)
    list_B.append(B)

list_x=[]
list_y = []
list_arange = [2, 2.2, 2.4, 2.6, 2.8, 3.0, 3.2, 3.4, 3.6, 3.8, 4.0, 4.2, 4.4, 4.6, 4.8, 5.0, 5.2, 5.4, 5.6, 5.8, 6.0, 6.2, 6.4, 6.6, 6.8, 7.0, 7.2, 7.4, 7.6, 7.8, 8.0, 8.2, 8.4, 8.6, 8.8, 9.0, 9.2, 9.4, 9.6, 9.8, 10]
# i did this way because when we range floats with delta 0.2, it gets like this: 2.8000000000000007, 3.000000000000001, 3.4000000000000012, etc.
# this way is much more correct for the graph

l=0
for i in list_arange:
    list_x.append(i)
    y_cal = (((list_K[l]*((i-x[l+1])**3))-(list_K[l+1]*((i-x[l])**3)))/ (6*(x[l]-x[l+1]))) + list_A[l] * (i - x[l+1]) - list_B[l]* (i - x[l])
    list_y.append(y_cal)
    if i == 4.0 or i == 7.0 or i == 8.0 :
        l=l+1
        
plt.scatter(x, y, label='Data Points', color='red')
plt.plot(list_x, list_y, label='Cubic Spline', color='black')
plt.title('Cubic Spline Interpolation')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()