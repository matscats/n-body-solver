import numpy as np


class Body:
    """
    Represents a body
    """
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
        Celestial body: {self.name};
        Initial position: {list(self.pos)} au;
        Initial velocity: {list(self.vel)} au/year;
        Mass: {self.mass} solar mass;
        Radius: {self.size} au;
        """
