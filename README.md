# ballad-harmonizer

Language: Python

Environment: Jupiter notebook

Generate chord accompaniments for traditional Chinese ballads based on the Hidden Markov Model.

## Install


Install [Music21](https://web.mit.edu/music21/doc/): for MacOS users, run the following in cmd
```
conda install -c conda-forge music21 
```

Install [Musescore](https://musescore.org/en/download ) to show the score

## Usage

Run the following to see the list of all avaliable Chinese Ballads:
```
from music21 import *

chinese_folk = corpus.search('china','locale')
[(i,e.metadata.title) for i,e in enumerate(chinese_folk)] 
```

Run the following to harmonize 
```
h = demo_train()
demo_harmonize(h)
```

The demo training set is Bach's chorales. These as well as Chinese ballads come from the corpus of music21. 
