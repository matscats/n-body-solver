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
        distances = []
        time = np.arange(Config.ti, Config.tf + Config.h, Config.h)

        Config.setData()

        Utils.printInformations()

        for i in range(len(time)):
            Modeling.rungeKuttaStep()
            # if Modeling.checkColision():
            #     print("Houve uma colisão: simulação encerrada")
            #     print(f"A colisão ocorreu em t = {time[i]} anos")
            #     break
            Utils.calculateCenterOfMass()
            distances.append(Utils.calculateDistance(Config.bodies[1].x[i],Config.bodies[0].x[i],
                                                     Config.bodies[1].y[i],Config.bodies[1].y[i],
                                                     Config.bodies[1].z[i],Config.bodies[2].z[i]))
        distances = np.array(distances)
        np.save('distancias.npy', distances)
        np.save('x_1.npy',Config.bodies[0].x); np.save('y_1.npy',Config.bodies[0].y); np.save('z_1.npy',Config.bodies[0].z)
        np.save('x_2.npy',Config.bodies[1].x); np.save('y_2.npy',Config.bodies[1].y); np.save('z_2.npy',Config.bodies[1].z)

        print("Simulação concluída com sucesso")

        Utils.plotTrajectories(False)
