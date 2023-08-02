import numpy as np


class Body:
    def __init__(self, body_cfg) -> None:
        self.pos = np.array(body_cfg["pos"])
        self.vel = np.array(body_cfg["vel"])
        self.mass = body_cfg["mass"]
        self.size = body_cfg["size"]
        self.name = body_cfg["name"]
        self.color = body_cfg["color"]
        self.x = []
        self.y = []
        self.z = []

    def __str__(self) -> str:
        return f"""
        Corpo celeste: {self.name};
        Posição inicial: {list(self.pos)} u.a;
        Velocidade Inicial: {list(self.vel)} u.a/ano;
        Massa: {self.mass} massa solar;
        Raio: {self.size} u.a;
        """
