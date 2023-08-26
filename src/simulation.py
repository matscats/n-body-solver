import numpy as np
from config import Config
from modeling import Modeling
from utils import Utils


class Simulation:
    @staticmethod
    def Run() -> None:
        """
        Executes simulation
        """
        time = np.arange(Config.ti, Config.tf + Config.h, Config.h)

        Config.setData()

        Utils.printInformations()

        for i in range(len(time)):
            Modeling.rungeKuttaStep()
            if Modeling.checkColision():
                print("Colision detected: simulation finished")
                break
            # Utils.calculateCenterOfMass()

        print("Simulation completed")

        Utils.plotTrajectories(show_center_of_mass=False)
