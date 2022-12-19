import numpy as np

f = np.array(
    [
        [0, 0],
        [0, 1],
        [1, 0],
        [1, 1]
    ]
)

labels = np.array([0, 1, 1, 1])

w = [1, 0.5]
theta = 0.5
learning_rate = 0.1
epoch = 5

for j in range(0, epoch):
    print("epoch", j)
    for i in range(0, f.shape[0]):
        actual = labels[i]
        instance = f[i]

        x0 = instance[0]
        x1 = instance[1]

        net = w[0] * x0 + w[1] * x1 - theta

        if net > 0:
            y = 1
        else:
            y = 0

        delta = actual - y

        if (delta != 0):
            w[0] = w[0] + learning_rate * delta * x0
            w[1] = w[1] + learning_rate * delta * x1
            theta = theta + (-1) * delta * learning_rate

        print("Calculated Value:", y, "actual value", delta)

    print(".............")