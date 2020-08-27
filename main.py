from visualising.main_visualising import Visualise
from path_creation.main_path_creation import create_path
import random
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
    while True:
        if count % 30 == 1 and number_of_dots > 3:
            dots = {'original': [], 'shteins': []}
            for i in range(0, number_of_dots):
                dots['original'].append([random.randint(10, 790), random.randint(10, 790)])
            for i in range(0, number_of_dots-2):
                dots['shteins'].append([random.randint(10, 790), random.randint(10, 790)])
            lines = create_path(dots)
        number_of_dots, phase = visual_system.render(dots, lines)
        count += 1
