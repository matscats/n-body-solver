from Body import Body
from Config import Config
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


class Utils:
    cm_coords = {"x": [], "y": [], "z": []}

    @staticmethod
    def calculateCenterOfMass() -> None:
        """
        Calcula o centro de massa entre os corpos do sistema
        """
        num = 0
        div = 0
        bodies = Config.bodies
        for i in range(len(bodies)):
            num += bodies[i].pos * bodies[i].mass
            div += bodies[i].mass
        center_of_mass = num / div
        Utils.cm_coords["x"].append(center_of_mass[0])
        Utils.cm_coords["y"].append(center_of_mass[1])
        Utils.cm_coords["z"].append(center_of_mass[2])

    @staticmethod
    def plotTrajectories(show_center_of_mass: bool) -> None:
        """
        Plota a trajetória de todos os corpos do sistema e o centro de massa (opcional)
        """
        fig = plt.figure()
        ax = fig.add_subplot(111, projection="3d")
        bodies = Config.bodies

        for i in range(len(bodies)):
            if bodies[i].mass:
                ax.plot(
                    bodies[i].x[::200],
                    bodies[i].y[::200],
                    bodies[i].z[::200],
                    color=bodies[i].color,
                    label=bodies[i].name,
                )

        if show_center_of_mass:
            ax.plot(
                Utils.cm_coords["x"],
                Utils.cm_coords["y"],
                Utils.cm_coords["z"],
                color="black",
                label="Centro de massa",
            )

        ax.legend()
        plt.show()

    @staticmethod
    def animateTrajectories(body_1: Body, body_2: Body, body_3: Body):
        """
        Realiza uma animação 3d das trajetórias
        """
        print("Preparando animação")

        fig = plt.figure()
        ax = fig.add_subplot(111, projection="3d")
        body_1.x = body_1.x[::450]
        body_1.y = body_1.y[::450]
        body_1.z = body_1.z[::450]
        body_2.x = body_2.x[::450]
        body_2.y = body_2.y[::450]
        body_2.z = body_2.z[::450]
        body_3.x = body_3.x[::450]
        body_3.y = body_3.y[::450]
        body_3.z = body_3.z[::450]

        @staticmethod
        def update(frame):
            ax.cla()
            ax.plot(
                body_1.x[:frame], body_1.y[:frame], body_1.z[:frame], label=body_1.name
            )
            ax.plot(
                body_2.x[:frame], body_2.y[:frame], body_2.z[:frame], label=body_2.name
            )
            ax.plot(
                body_3.x[:frame], body_3.y[:frame], body_3.z[:frame], label=body_3.name
            )

            ax.set_xlabel("x [ua]")
            ax.set_ylabel("y [ua]")
            ax.set_zlabel("z [ua]")
            ax.legend()

            ax.set_xlim(
                min(body_1.x + body_2.x + body_3.x), max(body_1.x + body_2.x + body_3.x)
            )
            ax.set_ylim(
                min(body_1.y + body_2.y + body_3.y), max(body_1.y + body_2.y + body_3.y)
            )
            ax.set_zlim(
                min(body_1.z + body_2.z + body_3.z), max(body_1.z + body_2.z + body_3.z)
            )

        ani = FuncAnimation(
            fig, update, frames=range(len(body_1.x)), interval=60, blit=False
        )
        ani.save("animacao.mp4", writer="ffmpeg")

        print("Animação finalizada")

    @staticmethod
    def calculateDistance(x0, x1, y0, y1, z0, z1):
        """
        Calcula a distância entre dois corpos quaisquer
        """
        return np.sqrt((x0 - x1) ** 2 + (y0 - y1) ** 2 + (z0 - z1) ** 2)

    @staticmethod
    def minDistance(body_1: Body, body_2: Body) -> float:
        """
        Calcula a mínima distância entre dois corpos durante o tempo da simulação
        """
        minimo = Utils.calculateDistance(body_1, body_2)
        nterms = len(body_1.x)
        for i in range(1, nterms):
            distance = Utils.calculateDistance(body_1, body_2, i)
            if distance < minimo:
                minimo = distance
        print(f"Distância mínima entre {body_1.name} e {body_2.name}: {minimo} ua")

    @staticmethod
    def maxDistance(body_1: Body, body_2: Body) -> float:
        """
        Calcula a máxima distância entre dois corpos durante o tempo da simulação
        """
        maximo = Utils.calculateDistance(body_1, body_2)
        nterms = len(body_1.x)
        for i in range(1, nterms):
            distance = Utils.calculateDistance(body_1, body_2, i)
            if distance > maximo:
                maximo = distance
        print(f"Distância maxima entre {body_1.name} e {body_2.name}: {maximo} ua")

    @staticmethod
    def printInformations() -> None:
        """
        Modo verboso do programa
        """
        bodies = Config.bodies
        print(
            f"---------- Modelagem 3D do problema de {len(bodies)} corpos ----------\n"
        )
        for i in range(len(bodies)):
            print(f"---------- Informações do corpo {i+1} ----------")
            print(bodies[i])
