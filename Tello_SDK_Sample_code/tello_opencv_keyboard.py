# This is a sample program for connecting to the Tello drone, getting video, flight data and control it by keyboard.
# It uses the Opencv's waitKey() method to get pressed keys which is not optimal. if you need a better implementation of keyboard reading, you can use PyGame library


import sys
import traceback
import tellopy
import av
import cv2.cv2 as cv2  # for avoidance of pylint error
import numpy

def handler(event, sender, data, **args):   # to print flight data
    drone = sender
    if event is drone.EVENT_FLIGHT_DATA:
        print(data)

def main():
    drone = tellopy.Tello()
    
    xSPD = 0   # forward/backward
    ySPD = 0   # left/right
    zSPD = 0   # up/down
    zROT = 0   # yaw rotation
    
    try:
        drone.subscribe(drone.EVENT_FLIGHT_DATA, handler)  # to pring flight data
        timeout = 0
        drone.connect()
        drone.wait_for_connection(60.0)
        container = av.open(drone.get_video_stream())
        print("***  Connected !")
        # skip first 300 frames
        frame_skip = 300
        stopFlag = True
        while True:
            for frame in container.decode(video=0):
                if 0 < frame_skip:
                    frame_skip = frame_skip - 1
                    #print(" ******** frame skipping :{}".format(frame_skip) )
                    continue
                frame_skip = 3  #if cpu load is high, increase this number, otherwise set it to 0
                
                image = cv2.cvtColor(numpy.array(frame.to_image()), cv2.COLOR_RGB2BGR)
                cv2.imshow('Original', image)

                """the computer vision codes
                   can be placed here 
                   "image" variable contains the drone's camera data """

                key = cv2.waitKey(1)
                
                
                if key == 27 :           # escape key
                    sys.exit(0)
                elif key == 32 :         # space key
                    drone.land()

                elif key == 13 :         # enter key
                    drone.takeoff()

                elif key == 117 :        # u key
                    zSPD = 50
                    
                elif key == 106 :        # j key
                    zSPD = -50

                elif key == 119 :        # w key
                    xSPD = 50

                elif key == 115 :        # s key
                    xSPD = -50

                elif key == 100 :        # d key
                    ySPD = -50

                elif key == 97 :         # a key
                    ySPD = 50

                elif key == 101 :        # e key
                    zROT = -50

                elif key == 113 :        # q key
                    zROT = 50
                
                else :                   # no key
                    timeout +=1
                    if timeout > 3:      # if no key is pressed in a while 
                        xSPD = 0   # forward/backward
                        ySPD = 0   # left/right
                        zSPD = 0   # up/dpwn
                        zROT = 0   # yaw rotation
                        
                        
                if key == -1 :  
                    if stopFlag == True:   #to send stop only once
                        drone.forward(0)
                        drone.left(0)
                        drone.up(0)
                        drone.counter_clockwise(0)
                        stopFlag = False
                else :    # if a key is pressed, reset the timeout counter
                    stopFlag = True
                    timeout = 0        
                    if xSPD >= 0:
                        drone.forward(xSPD)
                    else :
                        drone.backward(-xSPD)
                    
                    if ySPD >= 0:
                        drone.left(ySPD)
                    else :
                        drone.right(-ySPD)
                        
                    if zSPD >= 0:
                        drone.up(zSPD)
                    else :
                        drone.down(-zSPD)
                        
                    if zROT >= 0:
                        drone.counter_clockwise(zROT)
                    else :
                        drone.clockwise(-zROT)
                     
                

    except Exception as ex:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        traceback.print_exception(exc_type, exc_value, exc_traceback)
        print(ex)
    finally:
        drone.quit()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
