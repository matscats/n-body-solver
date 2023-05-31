import numpy as np
from Body import Body
from Modeling import rungeKuttaStep, CheckColision, calculateCenterOfMass
from Utils import plotTrajectories
from Config import *

def main():

    time = np.arange(ti, tf + h, h)                             # Array de cada instante de tempo
    Body1 = Body(body_1_cfg)                                    # Cria o objeto corpo 1
    Body2 = Body(body_2_cfg)                                    # Cria o objeto corpo 2
    Body3 = Body(body_3_cfg)                                    # Cria o objeto corpo 3
    for i in range(len(time)):
        rungeKuttaStep(Body1, Body2, Body3, h)                  # Atualiza um passo
        calculateCenterOfMass(Body1, Body2, Body3)              # Calcula o centro de massa
        if CheckColision(Body1, Body2, Body3):                  # Checa colisão
            print("Houve uma colisão: simulação encerrada")
            print(f'A colisão ocorreu em t = {time[i]} anos')
            break
        
    plotTrajectories(Body1, Body2, Body3, True)                  # Plota o gráfico

if __name__ == '__main__':
    main()
