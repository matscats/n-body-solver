from Config import G
import numpy as np

class Body:

    def __init__(self, body_cfg) -> None:
        """
        Class constructor
        """
        self.pos = body_cfg['pos']
        self.vel = body_cfg['vel']
        self.mass = body_cfg['mass']
        self.size = body_cfg['size']
        self.name = body_cfg['name']
        self.x = []
        self.y = []
        self.z = []

    def __str__(self) -> str:
        return f"""
        Posição inicial: {list(self.pos)} u.a;
        Velocidade Inicial: {list(self.vel)} u.a/ano;
        Massa: {self.mass} massa solar;
        Raio: {self.size} u.a;
        """

    def acceleration(self, pos_1, pos_2, m_1, m_2) -> float:
        """
        Returns the acceleration of the body
        """
        pos_dif_1 = self.pos - pos_1
        pos_dif_2 = self.pos - pos_2
        return (-1) * (G * (m_1 * (pos_dif_1) / np.linalg.norm(pos_dif_1) ** 3 + 
                            m_2 * (pos_dif_2) / np.linalg.norm(pos_dif_2) ** 3))
