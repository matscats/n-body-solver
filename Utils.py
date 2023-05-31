from Body import Body
import matplotlib.pyplot as plt
import numpy as np
from Modeling import cm_coords

def plotTrajectories(body_1: Body, body_2 : Body, body_3 : Body, show_center_of_mass : bool) -> None:
    """
    Plot the trajectories of the three bodys and center of mass
    """
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    if body_1.mass:
        ax.plot(body_1.x, body_1.y, body_1.z, color='red', label=body_1.name)
    if body_2.mass:
        ax.plot(body_2.x, body_2.y, body_2.z, color='blue', label=body_2.name)
    if body_3.mass:
        ax.plot(body_3.x, body_3.y, body_3.z, color='green', label=body_3.name)
    if show_center_of_mass:
        ax.plot(cm_coords['x'], cm_coords['y'], cm_coords['z'], color='black', label='Centro de massa')
    ax.legend()
    plt.show()

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
