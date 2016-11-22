from simplewin import simplewin as sw

import winsound

win = sw()
def notiddie ():
    win.add_label("i know!!!")
    win.add_button ("resign." , win.quit)
    print ("im sorry")    
def mistakes ():
    win.add_label("Error! Can't fetch 2D girls!")
    win.add_button ("what the hell!!!!" , notiddie)
    win.add_button ("keep trying!!!!!!" , mistakes)
def key_down(event):
    if event.keysym == 'a':
        winsound.PlaySound("C.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
    elif event.keysym == 's':
        winsound.PlaySound("D.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
    elif event.keysym == 'd':
        winsound.PlaySound("E.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
    else:
        print("Warning! {} has been pressed!".format(event.keysym))
    
win.add_label("anime waifu")

win.add_key_handler(key_down)

win.add_button ("get em" , mistakes)

win.run()
