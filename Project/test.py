import numpy as np
import Visulasation as vis

highscore_file = np.array([[161, 'Dev 1'],[184, 'Dev 2'], [200 , 'Cas'], [311, 'Vin'],[100, 'Max']])
vis.highscore(highscore_file)
highscore_file = highscore_file[highscore_file[:,0].argsort()][::-1]
print(highscore_file.shape)
vis.highscore(highscore_file)
