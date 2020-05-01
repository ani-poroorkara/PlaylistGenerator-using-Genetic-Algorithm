# Mixed Tape Using Genetic Algorithm 
Create a mixed tape using Genetic Algorithms with Python DEAP library. 

## Genetic Algorithms
1. Create a random initial *population*
2. Create a sequence of new populations using the individuals in the previous generation to create the next population.
   To create the new population, perform the following:
   - Score each member of the current population by computing its *fitness value.
   - Select *parents* based on their fitness value.
   - Produce *children* from the parents using crossover.
   - *Mutation* to maintain diversity within the population. 
3. Replace the current population with the children to form the next generation.
4. Stop when best generation is created or the stopping criteria is met. 

## Dependencies

```python 3
import os
from essentia.standard import *
import pickle
import pandas as pd
import numpy as np
from scipy.stats import entropy
from math import log, e
from deap import base, creator, tools, algorithms
import random
from pydub import AudioSegment
```

#### DEAP Library
[DEAP](https://github.com/DEAP/deap) is used to create and run the Genetic Algorithm.

#### Essentia Library
[Essentia](https://github.com/MTG/essentia) for audio analysis and audio-based music information retrieval.

#### Pydub Library
[Pydub](https://github.com/jiaaro/pydub) to combine the songs in playlist to make a record.

## Run the model

1. Collect all the music file into a folder.
2. Change the code according to the structure of your folder.
3. Run the *[preprocess.py](https://github.com/ani-poroorkara/PlaylistGenerator-using-Genetic-Algorithm/blob/master/preprocess.py)*.
4. Run the *[playlist_GA.py](https://github.com/ani-poroorkara/PlaylistGenerator-using-Genetic-Algorithm/blob/master/playlist_GA.py)*.


## License
This project is liscensed under [Apache License 2.0](https://github.com/ani-poroorkara/PlaylistGenerator-using-Genetic-Algorithm/blob/master/LICENSE)

##### I recommend using Google Colab or Jupyter notebooks to run the file cell by cell
##### Connect with me on [LinkedIn](https://www.linkedin.com/in/anirudh-poroorkara-34900017b/)
