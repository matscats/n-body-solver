import os
import json
from Body import Body


class Config:
    def __init__(self):
        # Newton's gravtational constant * solar mass * year² / u.a³
        self.G = 1.32712440018e20 * 3.1558149e7**2 / 1.495978707e11**3
        # Tamanho do passo (anos)
        self.h = 0.001
        # Tempo inicial (anos)
        self.ti = 0
        # Tempo final (anos)
        self.tf = 180
        # Número de corpos na simulação
        self.N = 4
        # Lista de todos os corpos da simulação
        self.bodies = []

    def setSimulation(self) -> None:
        """
        Prepara os dados dos corpos
        """
        json_file = os.path.join("projects", "params.json")
        with open(json_file) as file:
            data = json.load(file)
            for i in range(self.N):
                new_body = data[f"body_{i + 1}"]
                self.bodies.append(Body(new_body))
