# Relativt enkel måte å få et ikke-blokkerende delay i python,
# inspirert av millis() i arduino c. 
# Oktober. 2024

import time 

# 2 sekund intervall
intervall = 2 

prevMillis = 0 

def timer():
  # global for å være tilgjengelig utenfor funksjonen 
  global prevMillis
  currMillis = time.time()
  
  if currMillis - prevMillis >= intervall:
    
    print(f"{intervall} sekunder har gått")
    
    # Nullstiller prevmillis, timer begynner på nytt
    prevMillis = time.time()


while True:
  timer()