import numpy as np
import random
import math
np.printoptions()


def activation(x):
    """
    This function is basic activation function,
    it is made that way so it will be easy to change
    :param x: value
    :return:
    """
    return 1 / (1 + math.exp(-x))


activation = np.vectorize(activation)


class NeuralNetwork:
    def __init__(self):
        self.neural_network = None

    def build_neural_network(self, *layers):
        """
        :param layers: separate layers (number of neurons in each layer
        :return: built neural network (each layer is values of neurons, biases, weights)
        """
        if len(layers) < 2:
            raise(Exception('Neural network needs at least two layers'))

        built_neural_network = []
        for i in range(0, len(layers)):
            random.seed()
            neuron_count = layers[i]
            biases = np.array([random.uniform(-10, 10) for x in range(0, neuron_count)])
            weights = []
            if i != len(layers) - 1:
                for j in range(0, layers[i + 1]):
                    weights.append(np.array([random.uniform(-10, 10) for x in range(0, neuron_count)]))
            instant_layer = [np.array([0]*neuron_count, float), biases, np.array(weights)]
            built_neural_network.append(instant_layer)
        print(built_neural_network, '\n')
        self.neural_network = built_neural_network

    def run_neural_network(self, input_values):
        if self.neural_network is None:
            raise ValueError('You need neural network!')
        if len(input_values) != len(self.neural_network[0][0]):
            raise ValueError('Number of inputs must match with number of input neurons!')
        input_values = np.array(input_values)
        self.neural_network[0][0] = activation(input_values + self.neural_network[0][1])
        for i in range(0, len(self.neural_network) - 1):
            instant_layer = []
            for j in range(0, len(self.neural_network[i][2])):
                instant_layer.append(sum(self.neural_network[i][0]*self.neural_network[i][2][j]))
            instant_layer += self.neural_network[i+1][1]
            self.neural_network[i + 1][0] = activation(np.array(instant_layer))
        return self.neural_network[-1][0]


if __name__ == '__main__':
    neural_network = NeuralNetwork()
    neural_network.build_neural_network(1, 1, 1)
    print(neural_network.run_neural_network([1]))


