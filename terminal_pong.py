import os
import threading
(width, height) = os.get_terminal_size()
b=""
cx=10
cy=10

died=0
px=1
i=0
j=0
sx=1
sy=1

def run():
    global died
    global b
    global cx
    global cy
    global px
    global i
    global j
    global sx
    global sy
    timer = threading.Timer(0.1,run )
    if died==0:
         if cx>=0 and cx<=width:
             if cy<height:
                 cx+=sx
                 cy+=sy
             elif cx==px:
                 sy*=-1
                 cy+=sy
                 cx+=sx
             else:
                 died=1
         else:
             sx*=-1
             cx+=sx
             cy+=sy
         for y in range(1, height):
             if cy==y:
                 for x in range(0, width):
                     if cx==x:
                         b+='o'
                     else:
                         b+='.'
                         i+=1
             else:
                 for x in range(0, width):
                     b+='.'
                     i+=1
                 j+=1
             print(b)
             b=""
         pl=""
         for x in range(0, width):
             if cx==x:
                 pl+='='
             else:
                 pl+='.'
         print(pl)
         timer.start()
    else:
        print("you lost")

run()