import numpy as np
import matplotlib.pyplot as plt



class NeuralNetwork():
    def __init__(self):
        np.random.seed(1)
        self.synaptic_weights = 2 * np.random.random((3,1)) - 1
        self.allOut = []

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self,x):
        return x * (1-x)



    def train(self, tInputs, tOutputs, tIterations):
        
        for i in range(tIterations):
            output = self.think(tInputs)
            self.allOut.append(output)
            error = tOutputs - output
            adjustments = np.dot(tInputs.T, error * self.sigmoid_derivative(output))
            self.synaptic_weights += adjustments

    def think(self, inputs):
        inputs = inputs.astype(float)
        output = self.sigmoid(np.dot(inputs, self.synaptic_weights))

        return output
nn = NeuralNetwork()

print('Random synaptic weights:')
print(nn.synaptic_weights)

tInputs = np.array([[0,0,1],[1,1,1],[1,0,1],[0,1,1]])

tOutputs = np.array([[0,1,1,0]]).T

nn.train(tInputs, tOutputs, 20000)

print('Synaptic weights after')
print(nn.synaptic_weights)

A = str(input('Input 1: '))
B = str(input('Input 2: '))
C = str(input('Input 3: '))

print('New situation: input data: ', A, B, C)
print('Output:')

print(nn.think(np.array([A, B, C])))

x = []
y = []

for i in range(10000):
    x.append(i)

for i in range(10000):
    y.append(nn.allOut[i][0])

plt.plot(x,y)
plt.show()