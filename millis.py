# Relativt enkel timer i python, inspirert av millis funksjonen i arduino c. 

import time 

intervall = 2 # 2 sekund intervall
prevmillis = 0 

while True:
  currmillis = time.time()
  if currmillis - prevmillis >= 2:
    print("To sekund har gått")
    prevmillis = time.time()
