import winsound as w
from simplewin import simplewin as sw
import time

class piano ():
    def __init__ (self):
        self.notes = ["C","Cs","D","Ds","E","F","Fs","G","Gs","A","As","B","C2"]
    def play (self, i):
        name = self.notes[i] +".wav"
        w.PlaySound(name, w.SND_FILENAME | w.SND_ASYNC)
class track ():
    def __init__ (self):
        self.keys = []
        self.tempo = []
class recorder ():
    def __init__ (self):
        self.tracks = []
        self.keys = ["a","w","s","e","d","f","r","g","t","h","y","j","k"]
        self.win = None
    def record (self, event):
        #Error seems to be around here. Missing event when called, apparently.
        self.tracks.append(track())
        self.win = sw()
        start = time.gmtime()
        key = event.keysym
        p = piano ()
        if key in self.keys:
            for i in range(0,len(keys)):
                if key == self.keys[i]:
                    current = time.gmtime() - start
                    self.tracks[i].tempo.append(current)
                    self.tracks[i].keys.append(keys[i])
                    p.play(i)
                elif key == "z":
                    return None
        
    def play (self, n):
        #Don't worry about checking this, I'll fix it when I can run it.
        tem = time.clock()
        p = piano ()
        while tem <= self.tracks[n].tempo[len(self.tracks[n].tempo)-1]:
            ctem = tem
            if ctem in self.tracks[n].tempo:
                for i in range (0, len(self.tracks[n].tempo)):
                    if ctem == self.tracks[n].tempo[i]:
                        for j in range (0, len(keys)):
                            if self.tracks[n].keys[i] == self.keys[j]:
                                p.play[j]          
    def quitrecord(self):
        self.win.quit()
    def start (self):
        self.win = sw()
        self.win.add_label("Recorder")
        self.win.add_key_handler(self.record)
        #Called here.
        self.win.add_button("Record", self.record)
        for i in range (0,len(self.tracks)):
            self.win.add_button("Play Track " + str(i), self.play(i))
        self.win.add_button("Quit", self.quitrecord)
        self.win.run()

class app:
    def __init__(self):
        self.win = None

    def run(self):
        self.win = sw()
        self.rdr = recorder()
        self.win.add_label("My Piano")
        self.win.add_button("Recorder", self.rdr.start)
        self.win.add_button("Quit", self.quit_program)
        self.win.add_key_handler(self.key_down)
        self.win.run()

    def key_down(self, event):
        keys = ["a","w","s","e","d","f","r","g","t","h","y","j","k"]
        key = event.keysym
        p = piano ()
        if key in keys:
            for i in range(0,len(keys)):
                if key == keys[i]:
                    p.play(i)
            
    def quit_program(self):
        print("Goodbye!")
        self.win.quit()

app = app()
app.run()
