from body import Body
from config import Config
import numpy as np
import matplotlib.pyplot as plt


class Utils:
    cm_coords = {"x": [], "y": [], "z": []}

    @staticmethod
    def calculateCenterOfMass() -> None:
        """
        Calculates system's center of mass
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
        Plots trajectories and show center of mass (optional)
        """
        fig = plt.figure()
        ax = fig.add_subplot(111, projection="3d")
        bodies = Config.bodies

        for i in range(len(bodies)):
            if bodies[i].mass:
                ax.plot(
                    bodies[i].x,
                    bodies[i].y,
                    bodies[i].z,
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
    def calculateDistance(x0, x1, y0, y1, z0, z1):
        """
        Calculates the distance between two bodies
        """
        return np.sqrt((x0 - x1) ** 2 + (y0 - y1) ** 2 + (z0 - z1) ** 2)

    @staticmethod
    def minDistance(body_1: Body, body_2: Body) -> float:
        """
        Calculates the minimum distance between two bodies in simulation
        """
        minimo = Utils.calculateDistance(body_1, body_2)
        nterms = len(body_1.x)
        for i in range(1, nterms):
            distance = Utils.calculateDistance(body_1, body_2, i)
            if distance < minimo:
                minimo = distance
        print(f"Minimum distance between {body_1.name} and {body_2.name}: {minimo} au")

    @staticmethod
    def maxDistance(body_1: Body, body_2: Body) -> float:
        """
        Calculates the maximum distance between two bodies in simulation
        """
        maximo = Utils.calculateDistance(body_1, body_2)
        nterms = len(body_1.x)
        for i in range(1, nterms):
            distance = Utils.calculateDistance(body_1, body_2, i)
            if distance > maximo:
                maximo = distance
        print(f"Maximum distance between {body_1.name} and {body_2.name}: {maximo} au")

    @staticmethod
    def printInformations() -> None:
        """
        Shows simulation informations
        """
        bodies = Config.bodies
        print(
            f"---------- {len(bodies)} bodies problem ----------\n"
        )
        for i in range(len(bodies)):
            print(f"---------- Body {i+1} ----------")
            print(bodies[i])
