import numpy as np
import Body as bd
import RK4
import Config as cfg
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def main():

    time = np.arange(cfg.ti, cfg.tf + cfg.h, cfg.h)
    Body_1 = bd.Body(pos = np.array([0.0,0.0,0.0]), vel = np.array([0.0,0.0,0.0]), mass = 100000.0)
    x1 = []
    y1 = []
    z1 = []
    Body_2 = bd.Body(pos = np.array([10.0,0.0,0.0]), vel = np.array([0.0,np.sqrt(cfg.G * 100000.0 / 10),0.0]), mass = 1.0)
    x2 = []
    y2 = []
    z2 = []
    Body_3 = bd.Body(pos = np.array([0.5, np.sqrt(3) * 0.5, 0]), vel = np.array([0.0,0.0,0.0]), mass = 0.0)
    x3 = []
    y3 = []
    z3 = []

    for i in range(len(time)):
        x1.append(Body_1.pos[0])
        y1.append(Body_1.pos[1])
        z1.append(Body_1.pos[2])
        x2.append(Body_2.pos[0])
        y2.append(Body_2.pos[1])
        z2.append(Body_2.pos[2])
        x3.append(Body_3.pos[0])
        y3.append(Body_3.pos[1])
        z3.append(Body_3.pos[2])
        RK4.step(Body_1, Body_2, Body_3, cfg.h)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    if Body_1.mass:
        ax.scatter(x1, y1, z1, color='red', label='Corpo 1')
    if Body_2.mass:
        ax.scatter(x2, y2, z2, color='blue', label='Corpo 2')
    if Body_3.mass:
        ax.scatter(x3, y3, z3, color='green', label='Corpo 3')

    # # Defina a função que será chamada a cada quadro da animação

    # # Função de animação
    # def update(i):
    #     ax.clear()
    #     ax.set_xlim3d(-1, 1)
    #     ax.set_ylim3d(-1, 1)
    #     ax.set_zlim3d(-1, 1)
    #     ax.scatter(x1[i], y1[i], z1[i])
    #     ax.scatter(x2[i], y2[i], z2[i])
    #     ax.scatter(x3[i], y3[i], z3[i])

    # # Cria a animação
    # ani = FuncAnimation(fig, update, frames=len(time), interval=20)

    plt.show()

if __name__ == '__main__':
    main()
