from gpiozero import LEDBarGraph
from time import sleep

graph = LEDBarGraph(6,13,19,26, pwm=True)

i=1

while(i>0):
    graph.value = 1 # (1, 1, 1, 1, 1, 1)
    sleep(1)
    graph.value = 1/2 # (1, 1, 1, 0, 0, 0)
    sleep(1)
    graph.value = -1/2 # (0, 0, 0, 1, 1, 1)
    sleep(1)
    graph.value = 1/4 # (1, 0, 0, 0, 0, 0)
    sleep(1)
    graph.value = -1 # (1, 1, 1, 1, 1, 1)
    sleep(1)
    i+=1
    print(i)