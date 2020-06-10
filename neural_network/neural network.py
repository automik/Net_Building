import numpy as np
import random
import math
np.printoptions()


def activation(x):
    return 1 / (1 + math.exp(-x))


activation = np.vectorize(activation)


class NeuralNetwork:
    def __init__(self):
        self.neural_network = None


    def build_neural_network(self, *layers):
        if len(layers) < 2:
            raise(Exception('Neural network need at least two layers'))

        built_neural_network = []
        for i in range(0, len(layers)):
            random.seed()
            neuron_count = layers[i]
            biases = np.array([(random.randint(-100, 100)/10) for x in range(0, neuron_count)])
            weights = []
            if i != len(layers) - 1:
                for j in range(0, layers[i + 1]):
                    weights.append(np.array([(random.randint(-100, 100)/10) for x in range(0, neuron_count)]))
            print([np.array([0]*neuron_count, float), biases, np.array(weights)])
            instant_layer = np.array([np.array([0]*neuron_count, float), biases, np.array(weights)])
            print(instant_layer)
            built_neural_network.append(instant_layer)
        print(built_neural_network, '\n')
        built_neural_network = np.array(built_neural_network)
        print(built_neural_network, '\n')
        self.neural_network = built_neural_network

    def run_neural_network(self, input_values):
        if self.neural_network is not None:
            input_values = np.array(input_values)
            self.neural_network[0][0] = activation(input_values + self.neural_network[0][1])
            for i in range(0, len(self.neural_network) - 1):
                instant_layer = []
                for j in range(0, len(self.neural_network[i][2])):
                    instant_layer.append(self.neural_network[i][0][j]*self.neural_network[i][2][j]
                                         + self.neural_network[i+1][1][j])
                self.neural_network[i + 1][0] = activation(np.array(instant_layer))
            return self.neural_network[-1][0]


if __name__ == '__main__':
    neural_network = NeuralNetwork()
    neural_network.run_neural_network([1])
    neural_network.build_neural_network(3, 3, 3)
    print(neural_network.run_neural_network([1]))


