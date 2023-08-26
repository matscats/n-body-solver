import os
import json
from body import Body


class Config:
    # Newton's gravtational constant * solar mass * year² / u.a³
    G = 1.32712440018e20 * 3.1558149e7**2 / 1.495978707e11**3
    # Step size
    h = 0.0001
    # Initial time (years)
    ti = 0
    # Final time (years)
    tf = 10
    # Number of bodies in simulation
    N: int
    # List of all bodies in simulation
    bodies = []

    def setData() -> None:
        """
        Set data
        """
        json_file = os.path.join("projects", "params.json")
        with open(json_file) as file:
            data = json.load(file)
            Config.N = len(data)
            for i in range(Config.N):
                new_body = data[f"body_{i + 1}"]
                Config.bodies.append(Body(new_body))
