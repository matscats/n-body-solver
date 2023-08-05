import os
import json
from Body import Body


class Config:
    # Newton's gravtational constant * solar mass * year² / u.a³
    G = 1.32712440018e20 * 3.1558149e7**2 / 1.495978707e11**3
    # Tamanho do passo (anos)
    h = 0.00001
    # Tempo inicial (anos)
    ti = 0
    # Tempo final (anos)
    tf = 12
    # Número de corpos na simulação
    N: int
    # Lista de todos os corpos da simulação
    bodies = []

    def setData() -> None:
        """
        Prepara os dados dos corpos
        """
        json_file = os.path.join("projects", "params.json")
        with open(json_file) as file:
            data = json.load(file)
            Config.N = len(data)
            for i in range(Config.N):
                new_body = data[f"body_{i + 1}"]
                Config.bodies.append(Body(new_body))
