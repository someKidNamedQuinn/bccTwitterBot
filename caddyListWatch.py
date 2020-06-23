from botFunctions import *
import time

def main():
    try:
        newCaddyLst = startApplication()
        print(newCaddyLst)

    except:
        print("Failed to reach BCC website")
        return

    #newCaddyLst = getNewLst()

    if newCaddyLst == []:
        print("newListEmpty")
    else:
        try:
            tweet(newCaddyLst)
        except:
            print("duplicate tweet")

    time.sleep(10)


while True:
    main()
