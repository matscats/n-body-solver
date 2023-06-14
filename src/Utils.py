from Body import Body
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
        ax.plot(body_1.x, body_1.y, body_1.z, color='red', label=body_1.name)
    if body_2.mass:
        ax.plot(body_2.x, body_2.y, body_2.z, color='blue', label=body_2.name)
    if body_3.mass:
        ax.plot(body_3.x, body_3.y, body_3.z, color='green', label=body_3.name)
    if show_center_of_mass:
        ax.plot(cm_coords['x'], cm_coords['y'], cm_coords['z'], color='black', label='Centro de massa')
    ax.legend()
    plt.show()

def animateTrajectories(body_1: Body, body_2 : Body, body_3 : Body):
    # Criação da figura e objeto de eixo 3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    body_1.x = body_1.x[::100]
    body_1.y = body_1.y[::100]
    body_1.z = body_1.z[::100]
    body_2.x = body_2.x[::100]
    body_2.y = body_2.y[::100]
    body_2.z = body_2.z[::100]
    body_3.x = body_3.x[::100]
    body_3.y = body_3.y[::100]
    body_3.z = body_3.z[::100]
    # Função de atualização para cada quadro da animação
    def update(frame):
         # Limpar o gráfico antes de cada atualização
        ax.cla()
        # Plote as trajetórias de cada corpo
        ax.plot(body_1.x[:frame], body_1.y[:frame], body_1.z[:frame], label=body_1.name)
        ax.plot(body_2.x[:frame], body_2.y[:frame], body_2.z[:frame], label=body_2.name)
        ax.plot(body_3.x[:frame], body_3.y[:frame], body_3.z[:frame], label=body_3.name)

        # Adicione rótulos e uma legenda
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.legend()

        # Defina o intervalo de exibição dos eixos
        ax.set_xlim(min(body_1.x + body_2.x + body_3.x), max(body_1.x + body_2.x + body_3.x))
        ax.set_ylim(min(body_1.y + body_2.y + body_3.y), max(body_1.y + body_2.y + body_3.y))
        ax.set_zlim(min(body_1.z + body_2.z + body_3.z), max(body_1.z + body_2.z + body_3.z))

    # Criação da animação
    ani = FuncAnimation(fig, update, frames=range(len(body_1.x)), interval=60, blit=False)
    ani.save('animacao.mp4', writer='ffmpeg')

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
