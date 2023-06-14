import numpy as np
import sys
from Body import Body
from Modeling import rungeKuttaStep, checkColision, calculateCenterOfMass
from Utils import plotTrajectories, printInformations, animateTrajectories
from Config import *

def main(verbose : bool):

    time = np.arange(ti, tf + h, h)                                     # Array de cada instante de tempo
    Body1 = Body(body_1_cfg)                                            # Cria o objeto corpo 1
    Body2 = Body(body_2_cfg)                                            # Cria o objeto corpo 2
    Body3 = Body(body_3_cfg)                                            # Cria o objeto corpo 3
   
    if verbose: printInformations(Body1, Body2, Body3)                  # Mostra as informações da modelagem
                                                                        # Início da modelagem
    for i in range(len(time)):
        rungeKuttaStep(Body1, Body2, Body3, h)                          # Atualiza um passo
        calculateCenterOfMass(Body1, Body2, Body3)                      # Calcula o centro de massa
        if checkColision(Body1, Body2, Body3):                          # Checa colisão
            print("Houve uma colisão: simulação encerrada")
            print(f'A colisão ocorreu em t = {time[i]} anos')
            break
    if verbose: print("---------- Modelagem finalizada ----------")
    plotTrajectories(Body1, Body2, Body3, False)                        # Plota o gráfico
    # animateTrajectories(Body1, Body2, Body3)                          # Salva a animação

if __name__ == '__main__':
    verbose = sys.argv[1]
    if verbose == 'verbose':
        main(True)
    else:
        main(False)
