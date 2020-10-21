import random
import path_creation.main_path_creation
import numpy as np


class Generation:
    mutation_chance = 0.1
    best_network = None

    def __init__(self, networks):
        self.networks = networks
        self.score = {}
        # self.each_score = {}

    def set_score(self, goal_value, inputs):
        print('goal_value', goal_value)
        self.score = {}
        # self.each_score = {}
        original_dots = []
        for i in range(0, len(inputs[0]), 2):
            original_dots.append([inputs[0][i], inputs[0][i + 1]])
        dots = {'original': original_dots}

        for i in range(len(self.networks)):
            predicted_dots = self.networks[i].predict(inputs)


            shteins_dots = []
            for d in range(0, len(predicted_dots[0]), 2):
                shteins_dots.append([predicted_dots[0][d], predicted_dots[0][d + 1]])

            dots['shteins'] = shteins_dots

            value = path_creation.main_path_creation.total_network_distance(dots)

            if self.score.get(value/goal_value):
                self.score[value / goal_value].append(i)
            else:
                self.score[value / goal_value] = [i]
            # self.each_score[i] = value / goal_value


    def mutate(self):
        for network in self.networks:
            old_weights = network.get_weights()
            for i in range(len(old_weights)):
                for j in range(len(old_weights[i])):
                    if type(old_weights[i][j]) is np.ndarray:
                        for k in range(len(old_weights[i][j])):
                            if random.random() < self.mutation_chance:
                                old_weights[i][j][k] *= random.choice((random.random(), -random.random()))
                    else:
                        if random.random() < self.mutation_chance:
                            old_weights[i] *= random.choice((random.random(), -random.random()))
            network.set_weights(old_weights)

    def breed(self):

        if len(self.networks) % 4 == 0:
            parent_count = len(self.networks) / 2
            parent_ratio = 2
        else:
            raise ValueError('wrong networks')

        parents = []
        count = 0
        scores = sorted(self.score)

        if self.best_network:
            if scores[-1] > 1:
                self.best_network = self.score[scores[-1]][0]
        else:
            self.best_network = self.networks[self.score[scores[-1]][0]]

        while count < parent_count:

            if self.score[scores[-1]]:
                parents.append(self.score[scores[-1]][0])
                self.score[scores[-1]].pop(0)
                count += 1
            else:
                self.score.pop(scores[-1])
                scores.pop(-1)

        params_count = self.best_network.count_params()

        children_weights = []

        for i in range(0, len(parents), 2):
            parent_1 = self.networks[parents[i]]
            parent_2 = self.networks[parents[i + 1]]

            parent_1_weights = parent_1.get_weights()
            parent_2_weights = parent_2.get_weights()
            for j in range(parent_ratio*2):
                count_1 = 0
                count_2 = 0

                weights = parent_1_weights

                for s in range(len(weights)):
                    for d in range(len(weights[s])):
                        if type(weights[s][d]) is np.ndarray:
                            for f in range(len(weights[s][d])):

                                choice = random.randint(1, 2)
                                if choice == 2:
                                    if count_2 <= params_count // 2:
                                        weights[s][d][f] = parent_2_weights[s][d][f]
                                        count_2 += 1

                        else:
                            choice = random.randint(1, 2)
                            if choice == 2:
                                if count_2 <= params_count // 2:
                                    weights[s][d] = parent_2_weights[s][d]
                                    count_2 += 1
                children_weights.append(weights)

        for i in range(len(children_weights)):
            self.networks[i].set_weights(children_weights[i])


    def get_weights(self):
        weights = []
        for network in self.networks:
            weights.append(network.get_weights())
            weights.append('New one')
        return weights


if __name__ == '__main__':
    from tensorflow import keras
    from tensorflow.keras.layers import Dense
    import numpy as np

    n = int(input('Number of networks '))

    networks = [keras.models.Sequential([
        Dense(2, activation='relu', kernel_initializer='random_normal', bias_initializer='zeros', input_shape=(6,)),
        Dense(2, activation='sigmoid', kernel_initializer='random_normal', bias_initializer='zeros')
    ]) for x in range(n)]
    for network in networks:
        network.build()
        print(network.summary())

    gen = Generation(networks)
    print('148', gen.get_weights())
    gen.mutate()
    print('150', gen.get_weights())
    print('151', gen.score)
    gen.set_score(1, [[0, 0, 0.5, 1, 1, 0]])
    print('153', gen.score)
    print('154', gen.get_weights())
    gen.breed()
    print('156', gen.get_weights())

