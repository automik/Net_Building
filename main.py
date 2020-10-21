from visualising.main_visualising import Visualise
from path_creation.main_path_creation import create_path
from genetic_algorithm.gen_alg_main import Generation
import path_creation
from tensorflow import keras
from tensorflow.keras.layers import Dense
import random
import numpy as np
# dots = {
#         'original': [[80, 0], [80, 120], [40, 160], [120, 240], [200, 160]],
#         'shteins': [[0, 40], [160, 0], [200, 240]]
#     }

if __name__ == '__main__':
    dots = {'original': [], 'shteins': []}
    lines = []
    visual_system = Visualise(lines, dots)
    number_of_dots = None
    phase = None
    count = 0

    networks = []
    generation = None


    while True:
        if count % 30 == 1 and number_of_dots > 3:
            dots = {'original': [], 'shteins': []}
            inputs = [[]]
            for i in range(0, number_of_dots):
                dot_x = random.randint(10, 790)
                dot_y = random.randint(10, 790)
                dots['original'].append([dot_x, dot_y])
                inputs[0].extend([dot_x/800, dot_y/800])

            if generation:
                if generation.best_network is None:
                    generation.set_score(random.random(), [[random.random() for x in range(2*number_of_dots)]])
                    generation.breed()
                    generation.mutate()
                else:
                    goal = generation.best_network.predict(inputs)

                    shteins_dots = []
                    for d in range(0, len(goal[0]), 2):
                        dots['shteins'].append([int(goal[0][d]*800), int(goal[0][d + 1]*800)])
                    print(dots['shteins'])
                    generation.set_score(path_creation.main_path_creation.total_network_distance(dots), inputs)
                    generation.breed()
                    generation.mutate()
            else:
                for i in range(0, number_of_dots-2):
                    dots['shteins'].append([random.randint(10, 790), random.randint(10, 790)])

            lines = create_path(dots)
        number_of_dots, phase = visual_system.render(dots, lines)
        if number_of_dots > 3 and not networks:
            for i in range(20):
                networks.append(keras.models.Sequential([
                    Dense(10, activation='relu', kernel_initializer='random_normal', bias_initializer='zeros',
                          input_shape=(number_of_dots*2,)),
                    Dense(10, activation='relu', kernel_initializer='random_normal', bias_initializer='zeros'),
                    Dense((number_of_dots-2)*2, activation='sigmoid', kernel_initializer='random_normal', bias_initializer='zeros')
                ]))
            generation = Generation(networks)
        count += 1
