from Body import Body
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from Modeling import cm_coords

def plotTrajectories(body_1: Body, body_2 : Body, body_3 : Body, show_center_of_mass : bool) -> None:
    """
    Plot the trajectories of the three bodys and center of mass
    """
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    if body_1.mass:
        ax.plot(body_1.x[::50], body_1.y[::50], body_1.z[::50], color='red', label=body_1.name)
    if body_2.mass:
        ax.plot(body_2.x[::50], body_2.y[::50], body_2.z[::50], color='blue', label=body_2.name)
    if body_3.mass:
        ax.plot(body_3.x[::50], body_3.y[::50], body_3.z[::50], color='green', label=body_3.name)
    if show_center_of_mass:
        ax.plot(cm_coords['x'], cm_coords['y'], cm_coords['z'], color='black', label='Centro de massa')
    ax.legend()
    plt.show()

def animateTrajectories(body_1: Body, body_2 : Body, body_3 : Body):
    """
    Essa função irá preparar a animação das trajetórias
    """
    print("Preparando animação")

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    body_1.x = body_1.x[::450]
    body_1.y = body_1.y[::450]
    body_1.z = body_1.z[::450]
    body_2.x = body_2.x[::450]
    body_2.y = body_2.y[::450]
    body_2.z = body_2.z[::450]
    body_3.x = body_3.x[::450]
    body_3.y = body_3.y[::450]
    body_3.z = body_3.z[::450]

    def update(frame):
        ax.cla()
        ax.plot(body_1.x[:frame], body_1.y[:frame], body_1.z[:frame], label=body_1.name)
        ax.plot(body_2.x[:frame], body_2.y[:frame], body_2.z[:frame], label=body_2.name)
        ax.plot(body_3.x[:frame], body_3.y[:frame], body_3.z[:frame], label=body_3.name)

        ax.set_xlabel('x [ua]')
        ax.set_ylabel('y [ua]')
        ax.set_zlabel('z [ua]')
        ax.legend()

        ax.set_xlim(min(body_1.x + body_2.x + body_3.x), max(body_1.x + body_2.x + body_3.x))
        ax.set_ylim(min(body_1.y + body_2.y + body_3.y), max(body_1.y + body_2.y + body_3.y))
        ax.set_zlim(min(body_1.z + body_2.z + body_3.z), max(body_1.z + body_2.z + body_3.z))

    ani = FuncAnimation(fig, update, frames=range(len(body_1.x)), interval=60, blit=False)
    ani.save('animacao.mp4', writer='ffmpeg')

    print("Animação finalizada")

def calculateDistance(body_1: Body, body_2: Body, i: int):
    return np.sqrt((body_1.x[i] - body_2.x[i])**2 +
                   (body_1.y[i] - body_2.y[i])**2 +
                   (body_1.z[i] - body_2.z[i])**2)

def minDistance(body_1: Body, body_2 : Body) -> float:
    minimo = calculateDistance(body_1, body_2)
    nterms = len(body_1.x)
    for i in range(1, nterms):
        distance = calculateDistance(body_1, body_2, i)
        if distance < minimo:
            minimo = distance
    print(f'Distância mínima entre {body_1.name} e {body_2.name}: {minimo} ua')

def maxDistance(body_1: Body, body_2 : Body) -> float:
    maximo = calculateDistance(body_1, body_2)
    nterms = len(body_1.x)
    for i in range(1, nterms):
        distance = calculateDistance(body_1, body_2, i)
        if distance > maximo:
            maximo = distance
    print(f'Distância maxima entre {body_1.name} e {body_2.name}: {maximo} ua')

def printInformations(body_1: Body, body_2 : Body, body_3 : Body) -> None:
    """
    Outputs the informations about the modeling
    """
    print("---------- Modelagem 3D do problema de três corpos ----------\n")
    print("---------- Informações do corpo 1 ----------")
    print(body_1)
    print("---------- Informações do corpo 2 ----------")
    print(body_2)
    print("---------- Informações do corpo 3 ----------")
    print(body_3)
