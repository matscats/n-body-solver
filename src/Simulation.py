import numpy as np
from Config import Config
from Modeling import Modeling
from Utils import Utils


class Simulation:
    @staticmethod
    def Run() -> None:
        """
        Executa a simulação
        """
        time = np.arange(Config.ti, Config.tf + Config.h, Config.h)

        Config.setData()

        Utils.printInformations()

        for i in range(len(time)):
            Modeling.rungeKuttaStep()
            if Modeling.checkColision():
                print("Houve uma colisão: simulação encerrada")
                print(f"A colisão ocorreu em t = {time[i]} anos")
                break

        print("Simulação concluída com sucesso")

        Utils.plotTrajectories(False)
