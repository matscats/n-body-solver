import numpy as np
import Body

cm_coords = {
  'x' : [],
  'y' : [],
  'z' : []
}

def rungeKuttaStep(body_1 : Body, body_2 : Body, body_3 : Body, h : float) -> None:
  """
  Updates one step of Runge Kutta method
  """
  # Primeiro passo
  # Corpo 1
  k1_r_1 = body_1.vel
  k1_v_1 = body_1.acceleration(body_2.pos, body_3.pos, body_2.mass, body_3.mass)
  # Corpo 2
  k1_r_2 = body_2.vel
  k1_v_2 = body_2.acceleration(body_1.pos, body_3.pos, body_1.mass, body_3.mass)
  # Corpo 3
  k1_r_3 = body_3.vel
  k1_v_3 = body_3.acceleration(body_1.pos, body_2.pos, body_1.mass, body_2.mass)
  # Segundo passo
  # Corpo 1
  k2_r_1 = body_1.vel + h/2 * k1_v_1
  k2_v_1 = body_1.acceleration(body_2.pos + h/2 * k1_r_2, body_3.pos + h/2 * k1_r_3, body_2.mass, body_3.mass)
  # Corpo 2
  k2_r_2 = body_2.vel + h/2 * k1_v_2
  k2_v_2 = body_2.acceleration(body_1.pos + h/2 * k1_r_1, body_3.pos + h/2 * k1_r_3, body_1.mass, body_3.mass)
  # Corpo 3
  k2_r_3 = body_3.vel + h/2 * k1_v_3
  k2_v_3 = body_3.acceleration(body_1.pos + h/2 * k1_r_1, body_2.pos + h/2 * k1_r_2, body_1.mass, body_2.mass)
  # Terceiro passo
  # Corpo 1
  k3_r_1 = body_1.vel + h/2 * k2_v_1
  k3_v_1 = body_1.acceleration(body_2.pos + h/2 * k2_r_2, body_3.pos + h/2 * k2_r_3, body_2.mass, body_3.mass)
  # Corpo 2
  k3_r_2 = body_2.vel + h/2 * k2_v_2
  k3_v_2 = body_2.acceleration(body_1.pos + h/2 * k2_r_1, body_3.pos + h/2 * k2_r_3, body_1.mass, body_3.mass)
  # Corpo 3
  k3_r_3 = body_3.vel + h/2 * k2_v_3
  k3_v_3 = body_3.acceleration(body_1.pos + h/2 * k2_r_1, body_2.pos + h/2 * k2_r_2, body_1.mass, body_2.mass)
  # Quarto passo
  # Corpo 1
  k4_r_1 = body_1.vel + h * k3_v_1
  k4_v_1 = body_1.acceleration(body_2.pos + h * k3_r_2, body_3.pos + h * k3_r_3, body_2.mass, body_3.mass)
  # Corpo 2
  k4_r_2 = body_2.vel + h * k3_v_2
  k4_v_2 = body_2.acceleration(body_1.pos + h * k3_r_1, body_3.pos + h * k3_r_3, body_1.mass, body_3.mass)
  # Corpo 3
  k4_r_3 = body_3.vel + h * k3_v_3
  k4_v_3 = body_3.acceleration(body_1.pos + h * k3_r_1, body_2.pos + h * k3_r_2, body_1.mass, body_2.mass)
  # Atualiza
  # Corpo 1
  body_1.vel += (k1_v_1 + 2 * k2_v_1 + 2 * k3_v_1 + k4_v_1) / 6.0 * h
  body_1.pos += (k1_r_1 + 2 * k2_r_1 + 2 * k3_r_1 + k4_r_1) / 6.0 * h
  body_1.x.append(body_1.pos[0])
  body_1.y.append(body_1.pos[1])
  body_1.z.append(body_1.pos[2])
  # Corpo 2
  body_2.vel += (k1_v_2 + 2 * k2_v_2 + 2 * k3_v_2 + k4_v_2) / 6.0 * h
  body_2.pos += (k1_r_2 + 2 * k2_r_2 + 2 * k3_r_2 + k4_r_2) / 6.0 * h
  body_2.x.append(body_2.pos[0])
  body_2.y.append(body_2.pos[1])
  body_2.z.append(body_2.pos[2])
  # Corpo 3
  body_3.vel += (k1_v_3 + 2 * k2_v_3 + 2 * k3_v_3 + k4_v_3) / 6.0 * h
  body_3.pos += (k1_r_3 + 2 * k2_r_3 + 2 * k3_r_3 + k4_r_3) / 6.0 * h
  body_3.x.append(body_3.pos[0])
  body_3.y.append(body_3.pos[1])
  body_3.z.append(body_3.pos[2])

def checkColision(body_1, body_2, body_3) -> bool:
  """
  This method check if a colision ocurred between the bodies
  """
  colision = False
  if np.linalg.norm(body_1.pos - body_2.pos) < body_1.size + body_2.size:
    colision = True
  if np.linalg.norm(body_1.pos - body_3.pos) < body_1.size + body_3.size:
    colision = True
  if np.linalg.norm(body_2.pos - body_3.pos) < body_2.size + body_3.size:
    colision = True
  return colision

def calculateCenterOfMass(body_1 : Body, body_2 : Body, body_3 : Body) -> None:
  """
  This method calculates the center of mass for the system of three bodies
  """
  center_of_mass = (body_1.mass * body_1.pos + body_2.mass * body_2.pos +
                    body_3.mass * body_3.pos) / (body_1.mass + body_2.mass +
                                                 body_3.mass)
  cm_coords['x'].append(center_of_mass[0])
  cm_coords['y'].append(center_of_mass[1])
  cm_coords['z'].append(center_of_mass[2])