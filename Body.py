from Config import G
import numpy as np

class Body:

    def __init__(self, pos, vel, mass, size) -> None:
        """
        Constutor da classe
        """
        self.pos = pos
        self.vel = vel
        self.mass = mass
        self.size = size
        self.x = []
        self.y = []
        self.z = []

    def acceleration(self, pos_1, pos_2, m_1, m_2) -> float:
        """
        Retorna a aceleração do corpo
        """
        pos_dif_1 = self.pos - pos_1
        pos_dif_2 = self.pos - pos_2
        return (-1) * (G * (m_1 * (pos_dif_1) / np.linalg.norm(pos_dif_1) ** 3 + 
                            m_2 * (pos_dif_2) / np.linalg.norm(pos_dif_2) ** 3))
