import os
import time
import random
import flask

pokemons = ['venusaur', 'charizard', 'blastoise', 'articuno', 'zapdos', 'moltres', 'mewtwo']
enumPoke = list(enumerate(pokemons))

actions = ['increment', 'count']
enumAct = list(enumerate(actions))

while 1:
    rPkmn = random.randint(0, 6)
    rActn = random.randint(0, 1)
    pkmn = enumPoke[rPkmn][1]
    actn = enumAct[rActn][1]
    myreq = "curl localhost:5000/" + actn + "/" + pkmn
    #print("sent " + myreq )
    os.system(myreq)
    time.sleep(2)
