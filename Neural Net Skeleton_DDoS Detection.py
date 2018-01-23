import numpy as np
import matplotlib.pyplot as plt 
import talkey
#import pyshark

#Data set prediction Model
#[CPU Usage, average packetsize, total number of TCP connections, prediction(1 =Legit, 0 = Attack)]

data = [[0,0,0,1],
        [0,0,1,1 ],
        [0,1,0,1],
        [1,0,1,0],
        [2,1,2,0],
        [1,1,0,0],
        [2,2,1,0],
        [1,1,1,0]]

#targetV = [1,1,2]

#sigmoid function 
def sigmoid(x):
    return 1/(1+np.exp(-x))
#plt.axis([0,3,0,3])
#plt.grid()

#for i in range(len(data)):
 #   point = data[i]
 #   plt.plot([point[0], point[1]])
  #  plt.grid()
#training 

w1 = np.random.randn()
w2 = np.random.randn()
w3 = np.random.randn()
b = np.random.randn()    
eta = 0.10

costs = []
for i in range(50000):
    ri = np.random.randint(len(data))
    point = data[ri]
    target = point[3]
        
    #feed forward
    z = w1 * point[0] +w2 * point[1] +w3 * point[3] +b
    pred = sigmoid(z)
        
    cost =(pred - target)**2
        
    #derivative of cost function with respect to prediction
    dcost_dpred = 2*(pred -target)
     
    #der_ sigmoid
    dpred_dz = sigmoid(z)*(1-sigmoid(z))
        
    dz_dw1 = point[0]
    dz_dw2 = point[1]
    dz_dw3 = point[2]
    dz_db  = 1
        
        
    dcost_dw1 = dcost_dpred * dpred_dz * dz_dw1
    dcost_dw2 = dcost_dpred * dpred_dz * dz_dw2
    dcost_dw3 = dcost_dpred * dpred_dz * dz_dw3
    dcost_db = dcost_dpred * dpred_dz * dz_db
      
    w1 -= eta * dcost_dw1
    w2 -= eta * dcost_dw2
    w3 -= eta * dcost_dw3
    b -= eta * dcost_db
    
    if i % 100 == 0:
        cost_sum =0
        for j in range(len(data)):
            point = data[ri]
            
            z = point[0] * w1 + point[1] * w2 + point[2] * w3 +b
            pred = sigmoid(z)
            
            target = point[3]
            cost_sum += np.square(pred - target)
        costs.append(cost_sum/len(data))
        
sp = talkey.Talkey()


def client(t, m, p):
    z = t * w1 + m *w2 +p * w3 +b
    pred = sigmoid(z)
    if pred < .5:
        sp.say("It's an Attacker. Go hide. Proceeding counter measure.")
        
    else:
        sp.say("It's Legit user")

plt.plot(costs)
plt.grid()


    
    
    