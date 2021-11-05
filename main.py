from LightShow import LightShow
import sys
import argparse

def main(mode):
    myLightShow = LightShow()
    try:
        if(mode == ""):
            mode = "basic"
        myLightShow.run(mode)
    except KeyboardInterrupt:
        myLightShow.turn_off()        
        sys.exit()

if __name__== "__main__" :
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', dest='mode', type=str, help='mode of light show you want to do')
    args = parser.parse_args()
    main(args.mode)

