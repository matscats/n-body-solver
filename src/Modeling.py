import numpy as np
from Body import Body
from Config import Config

class Modeling:
    
    @staticmethod
    def calculate_acceleration(index : int, cfg : Config) -> np.ndarray:
        """
        Calcula a aceleração do corpo[index] causada por todos os outros corpos
        """
        bodies = cfg.bodies
        acc = 0
        for i in range(cfg.N):
          if i != index:
            pos_dif = bodies[index].pos - bodies[i].pos
            acc += (-1) * (cfg.G * (bodies[i].mass * (pos_dif) / np.linalg.norm(pos_dif) ** 3))
        return acc

    @staticmethod
    def rungeKuttaStep(self, cfg : Config) -> None:
        """
        Calcula o próximo passo da EDO utilizando o método de Runge-Kutta de quarta ordem
        """
        bodies = cfg.bodies
        h = cfg.h

        k1_pos = np.zeros((cfg.N,3))
        k1_vel = np.zeros((cfg.N,3))
        k2_pos = np.zeros((cfg.N,3))
        k2_vel = np.zeros((cfg.N,3))
        k3_pos = np.zeros((cfg.N,3))
        k3_vel = np.zeros((cfg.N,3))
        k4_pos = np.zeros((cfg.N,3))
        k4_vel = np.zeros((cfg.N,3))

        for i in range(cfg.N):
          # Calculates acceleration
          acc_i = self.calculate_acceleration(bodies, i, cfg)

          # k1
          k1_pos[i] = bodies[i].vel * h
          k1_vel[i] = acc_i * h

          #k2
          k2_pos[i] = (bodies[i].vel + k1_vel[i] / 2) * h
          k2_vel[i] = acc_i * h

          # k3
          k3_pos[i] = (bodies[i].vel + k2_vel[i] / 2) * h
          k3_vel[i] = acc_i * h

          # k4
          k4_pos[i] = (bodies[i].vel + k3_vel[i]) * h
          k4_vel[i] = acc_i * h

          # Update
          bodies[i].pos += (k1_pos[i] + 2 * k2_pos[i] + 2 * k3_pos[i] + k4_pos[i]) / 6.0
          bodies[i].vel += (k1_vel[i] + 2 * k2_vel[i] + 2 * k3_vel[i] + k4_vel[i]) / 6.0

          # Saves
          bodies[i].x.append(bodies[i].pos[0])
          bodies[i].y.append(bodies[i].pos[1])
          bodies[i].z.append(bodies[i].pos[2])

    @staticmethod
    def checkColision(bodies : list[Body]) -> bool:
        """
        This method check if a colision ocurred between the bodies
        """
        colision = False
        n = len(bodies)
        for i in range(n):
           for j in range(n):
              if i != j:
                 if np.linalg.norm(bodies[i].pos - bodies[j].pos) < bodies[i].size + bodies[j].size:
                    colision = True
        return colision