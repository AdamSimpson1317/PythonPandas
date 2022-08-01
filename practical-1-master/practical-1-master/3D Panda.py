import argparse

from math import pi, sin, cos

from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor

class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        mySound = self.loader.loadSfx("models/audio/sfx/bear_polar.wav")
        mySound.setVolume(0.5)
        mySound.setBalance(-0.5)
        status = mySound.status()
        if mySound.status() == mySound.PLAYING:
            mySound.stop()

        # Load the environment model.
        self.scene = self.loader.loadModel("models/environment")
        # Reparent the model to render.
        self.scene.reparentTo(self.render)
        # Apply scale and position transforms on the model.
        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setPos(-8, 42, 0)

        parser = argparse.ArgumentParser(description="Parses Command")
        parser.add_argument("--spin", type=int, help="Spin camera?")
        parser.add_argument("--spawn", type=int, help="Spawn Panda?")
        args = parser.parse_args()

        # Add the spinCameraTask procedure to the task manager.
        if args.spin == 1:
            self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")

        # Load and transform the panda actor.
        if args.spawn == 1:
            self.pandaActor = Actor("models/panda-model",
                                    {"walk": "models/panda-walk4"})
            self.pandaActor.setScale(0.005, 0.005, 0.005)
            self.pandaActor.reparentTo(self.render)
            # Loop its animation.
            self.pandaActor.loop("walk")

            if mySound.status() == mySound.READY:
                mySound.play()

        # Define a procedure to move the camera.
    def spinCameraTask(self, task):
        angleDegrees = task.time * 6.0
        angleRadians = angleDegrees * (pi / 180.0)
        self.camera.setPos(20 * sin(angleRadians), -20.0 * cos(angleRadians), 3)
        self.camera.setHpr(angleDegrees, 0, 0)
        return Task.cont


app = MyApp()
app.run()
