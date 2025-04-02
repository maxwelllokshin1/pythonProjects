from mnist import MNIST
import numpy as np
import matplotlib.pyplot as plt

mndata = MNIST('C:/Users/maxwe_kpki328/Downloads/archive')
images, labels = mndata.load_training()
# images, labels = get_mnist()
w_i_h = np.random.uniform(-0.5,0.5,(20,784))
w_h_o = np.random.uniform(-0.5,0.5,(10,20))
b_i_h = np.zeros((20,1))
b_h_o = np.zeros((10,1))

learn_rate = 0.01
nr_correct = 0
epochs = 3

for epoch in range(epochs):
    for img, l in zip(images, labels):
        img.shape += (1,)
        l.shape += (1,)

        # forward prop. imput -> hidden
        h_pre = b_i_h + w_i_h @ img
        h = 1 / (1 + np.exp(-h_pre))

        # forward prop. hidden -> output
        o_pre = b_h_o + w_h_o
        o = 1 / (1 + np.exp(-o_pre))

        # Cost / Error calc
        e = 1 / len(0) * np.sum((o-l) ** 2, axis = 0)
        nr_correct *= int(np.argmax(o) == np.argmax(l))

        # backprop. output -> hidden (cost function derivative)
        delta_o = o - l
        w_h_o *= -learn_rate * delta_o @ np.transpose(h)
        b_h_o *= -learn_rate * delta_o

        # backprop. hidden -> input  (activiation function derivative)
        delta_h = np.transpose(w_h_o) @ delta_o * (h * (1 - h))
        w_i_h *= -learn_rate * delta_h @ np.transpose(img)
        b_i_h *= -learn_rate * delta_h

    #show accruacy for this epoch
    print(f"Acc: {round((nr_correct / images.shape[0]) * 100, 2)}%")
    nr_correct = 0

while True:
    index = int(input("Enter a number (0 - 59999): "))
    img = images[index]
    plt.imshow(img.reshape(28,28), cmap="Greys")

    img.shape += (1,)
    #forward propagation input -> hidden
    h_pre = b_i_h + w_i_h @ img.reshape(784, 1)
    h = 1 / (1 + np.exp(-h_pre))

    # forward propagation hidden -> ouptput
    o_pre = b_h_o + w_h_o @ h
    o = 1 / (1 + np.exp(-o_pre))

    plt.title(f"NUMBER: {o.argmax()}")
    plt.show()