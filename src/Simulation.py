from Body import Body
import json
import os
import numpy as np
from Config import Config
from Modeling import Modeling
from Utils import Utils

class Simulation:
    
    def __init__(self):
        pass
  
    def Run(self) -> None:
        """
        Executa a simulação
        """
        cfg = Config()
        time = np.arange(cfg.ti, cfg.tf + cfg.h, cfg.h)

        cfg.setSimulation()

        Utils.printInformations(cfg.bodies)

        for i in range(len(time)):
            Modeling.rungeKuttaStep(cfg)
            if Modeling.checkColision(cfg.bodies):
              print("Houve uma colisão: simulação encerrada")
              print(f'A colisão ocorreu em t = {time[i]} anos')
              break

        print("Simulação concluída com sucesso")
        
        Utils.plotTrajectories(cfg.bodies, False)
      
        
        