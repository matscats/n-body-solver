from Body import Body
import matplotlib.pyplot as plt

def plotBodys(body_1: Body, body_2 : Body, body_3 : Body) -> None:
    """
    Plota as trajetórias dos três corpos
    """
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    if body_1.mass:
        ax.plot(body_1.x, body_1.y, body_1.z, color='red', label='Corpo 1')
    if body_2.mass:
        ax.plot(body_2.x, body_2.y, body_2.z, color='blue', label='Corpo 2')
    if body_3.mass:
        ax.plot(body_3.x, body_3.y, body_3.z, color='green', label='Corpo 3')
    plt.show()