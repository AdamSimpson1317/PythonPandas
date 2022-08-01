#Should Break (Version Control/Panda)

from direct.showbase.ShowBase import ShowBase

class MyApp(ShowBase):

    def __int__(self):
        ShowBase.__init__(self)

app = MyApp()
app.run()
