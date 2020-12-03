Simple convnet architecture for MNIST handwritten digit classification

Architecture:
convolution layer 2D - 32 3x3 filters, relu
max pooling layer 2D - 2x2
convolution layer 2D - 64 3x3 filters, relu
max pooling layer 2D - 2x2
convolution layer 2D - 64 3x3 filters, relu
flatten layer
dense layer - 64, relu
dense layer - 10, softmax

Even this simplistic implementation yields more than 99% accuracy on the test MNIST dataset.