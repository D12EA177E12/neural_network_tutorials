import autograd.numpy as np
from autograd import grad
import matplotlib.pyplot as plt

# Perform linear regression of the form y = mx + b

def predictions(weights, inputs):
	return np.dot(inputs,weights)

def cost_function(weights):
	preds = predictions(weights, inputs)
	#print "predictions", preds
	cost = (preds - targets)**2
	#print "cost", cost
	return -(0.5*1/m)*np.sum((cost))


# Build a toy dataset.
inputs = np.array([[0.52],
                   [0.88],
                   [0.52],
                   [0.74]])
targets = np.array([0.45, 0.33, -0.89, -0.11])
m = len(targets)

training_gradient_fun = grad(cost_function)

# Optimize weights using gradient descent.
weights = np.array([0.5])
print "Initial loss:", cost_function(weights)

# Set up figure.
fig = plt.figure(figsize=(12, 8), facecolor='white')
ax = fig.add_subplot(111, frameon=False)
plt.ion()
plt.show(block=False)

for i in xrange(2000):
    weights += training_gradient_fun(weights) * 0.5
    print "loss:", cost_function(weights)

    plot_inputs = np.linspace(1, 4, num=4)

    # Plot functions
    plt.cla()
    ax.plot(plot_inputs, targets, 'bo')
    ax.plot(plot_inputs, predictions(weights,inputs))
    plt.draw()
    plt.pause(1.0/60.0)

print  "Trained loss:", cost_function(weights)