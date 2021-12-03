import os
from LightShow import LightShow
import sys
import argparse

def main(mode, lightmode):
    myLightShow = LightShow()
    try:
        myLightShow.run(mode, lightmode)
    except KeyboardInterrupt:
        myLightShow.turn_off()        
        sys.exit()        


if __name__== "__main__" :
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', dest='mode', type=str, help='mode of light show you want to do')
    parser.add_argument('--lightmode', dest='lightmode', type=str, help='mode of light mode you want to do')
    args = parser.parse_args()
    main(args.mode,args.lightmode)

