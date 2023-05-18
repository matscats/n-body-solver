import numpy as np
from Body import Body
from Modeling import RungeKuttaStep, CheckColision
from Utils import plotBodys
from Config import *

def main():

    time = np.arange(ti, tf + h, h)                         # Array de cada instante de tempo
    Body1 = Body(pos_1, vel_1, mass_1, size_1)              # Cria o objeto corpo 1
    Body2 = Body(pos_2, vel_2, mass_2, size_2)              # Cria o objeto corpo 2
    Body3 = Body(pos_3, vel_3, mass_3, size_3)              # Cria o objeto corpo 3

    for i in range(len(time)):
        RungeKuttaStep(Body1, Body2, Body3, h)              # Atualiza um passo
        if CheckColision(Body1, Body2, Body3):              # Checa colisão
            print("Houve uma colisão: simulação encerrada")
            break
        
    plotBodys(Body1, Body2, Body3)                          # Plota o gráfico

if __name__ == '__main__':
    main()
