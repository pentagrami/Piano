import winsound as w
from simplewin import simplewin as sw

class piano ():
    def __init__ (self):
        self.notes = ["C.wav","Cs.wav","D.wav","Ds.wav","E.wav","F.wav","Fs.wav","G.wav","Gs.wav","A.wav","As.wav","B.wav","C2.wav"]
    def play (self, i):
        name = self.notes[i]
        w.PlaySound(name, w.SND_FILENAME | w.SND_ASYNC)

class app:
    def __init__(self):
        # the special keyword “None” indicates no object
        self.win = None
        
    def stroke (self, key, keys):
        
                return i

    def run(self):
        self.win = sw()
        self.win.add_label("My Piano")
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
