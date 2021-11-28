from music21 import *
from harmonizer import *
import pprint

#training with Bach's chorales to harmonize Chinese folks
def demo_train():
    bachBundle = corpus.search('bach', 'composer')
    bach_4parts=[e.parse() for e in bachBundle if e.metadata.numberOfParts>=4] #Let the highest notes be the note in the melody, and let others form a chord
    h=Harmonizer()
    h.train(bach_4parts)
    return h

def demo_harmonize(h,songs=None):
    if songs is None:
        songs=corpus.search('china','locale')
    while True:
        str_id=input("input song id (0-%d) (input -1 to exit):" %(len(songs)-1))
        song_id=int(str_id)
        if song_id==-1:
            return songs
       
        s=songs[song_id].parse()
        try:
            ns=h.harmonize(s)
            if ns is None:
                print("can't harmonize this song. please select other songs.")
                continue
            #s.show()
            ns.show()
            s.show('midi')
            ns.show('midi')
        except:
            raise
            print("something wrong with harmonizing this song. please select other songs.")

def prepare():
    h=demo_train()
    chinese_folk=corpus.search('china','locale')
    pprint.pprint([(i,e.metadata.title) for i,e in enumerate(chinese_folk)])
    return h,chinese_folk

def run(h,scores):
    demo_harmonize(h,scores)
