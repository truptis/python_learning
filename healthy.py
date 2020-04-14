from pygame import mixer
from datetime import datetime
from time import time

def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break

def log_now(msg):
    with open("mylogs.txt","a") as f:
        f.write(f"{msg} {datetime.now()}")


if __name__ == '__main__':
   # musiconloop("water.mp3","stop")
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    watersec = 30*60
    exsecs = 20*60
    eyessecs = 40*60
    print (init_water)

    while True:
        if time() - init_water > watersec:
            print("water drinking time enter 'drank' to stop alerting" )
            musiconloop("water.mp3","drank")
            init_water = time()
            log_now("drank water at time")

        if time() - init_water > eyessecs:
            print("Eyeexcercise time enter 'eyeexcer' to stop alerting" )
            musiconloop("water.mp3","eyeexcer")
            init_eyes = time()
            log_now("done eyeexcercise at time")

        if time() - init_water > exsecs:
            print("physical excercise time enter 'done' to stop alerting" )
            musiconloop("water.mp3","done")
            init_excercise = time()
            log_now("drank water at time")
