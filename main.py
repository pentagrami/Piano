import winsound as w
from simplewin import simplewin as sw
import time

class piano ():
    def __init__ (self):
        self.notes = ["C","Cs","D","Ds","E","F","Fs","G","Gs","A","As","B","C2"]
    def play (self, i):
        #When called plays note with corresponding index.
        name = self.notes[i] +".wav"
        w.PlaySound(name, w.SND_FILENAME | w.SND_ASYNC)
class recorder ():
    def __init__ (self):
        self.tracks = []
        self.keys = ["a","w","s","e","d","f","r","g","t","h","y","j","k"]
        self.win = None
    def record (self, key, tempo):
        #Fixed. Appends into current track.
        self.tracks[len(self.tracks)-1][0].append(tempo)
        self.tracks[len(self.tracks)-1][1].append(key)
    def records (self):
        #Opens a window with all recorded tracks.
        #Calls replay automatically fsr. !!! Need to fix.
        self.win = sw()
        self.win.add_label("Current Records:")
        for i in range (0, len (self.tracks)):
            self.win.add_button("Track " + str(i+1), self.replay(i))
        self.win.run()    
    def replay (self, n):
        #Currently supposed to print tempo and note index.
        #Must be changed to play recorded song when called instead.
        print(self.tracks[n][0])
        print(self.tracks[n][1])
    def quitrecord(self):
        self.win.quit()
    def recording (self):
        #Initiates recording of a new track.
        self.tracks.append([[],[]])
    def start (self):
        #Confirmate recording.
        self.win = sw()
        self.win.add_label("Recording now...")
        self.recording()
        self.win.run()

class app:
    def __init__(self):
        self.win = None
    def togglerec (self):
        #Opens/closes recording on same button.
        if self.tog == False:
            self.tog = True
            self.rdr.start()
            self.last = time.time()
        else:
            self.tog = False
            self.rdr.quitrecord()
            self.last = 0
    def run(self):
        self.tog = False
        self.last = 0
        self.win = sw()
        self.rdr = recorder()
        self.win.add_label("My Piano")
        self.win.add_button("Recorder", self.togglerec)
        #When this button is pressed and records is called replay is executed too. Why?
        self.win.add_button("Tracks", self.rdr.records)
        self.win.add_button("Quit", self.quit_program)
        self.win.add_key_handler(self.key_down)
        self.win.run()
    def key_down(self, event):
        keys = ["a","w","s","e","d","f","r","g","t","h","y","j","k"]
        key = event.keysym
        p = piano ()
        #Plays pressed key.
        if key in keys:
            p.play(keys.index(key))
            #If recording is on, appends key and time interval into current track.
            if self.tog == True:
                #Time not working. Can't calculate tempo properly.
                self.last = time.time() - self.last
                self.rdr.record(keys.index(key),(time.time() - self.last))            
    def quit_program(self):
        print("Goodbye!")
        self.win.quit()

app = app()
app.run()
