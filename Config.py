import numpy as np

G = 1.32712440018e20 * 3.1558149e7 ** 2 / 1.495978707e11 ** 3 # Newton's gravtational constant * solar mass * year² / u.a³
h = 0.0001 # Tamanho do passo
ti = 0 # Tempo inicial (anos)
tf = 0.5 # Tempo final (anos)

# Configurações do corpo 1:
pos_1 = np.array([0.0,0.0,0.0])
vel_1 = np.array([0.0,0.0,0.0])
mass_1 = 100000.0
size_1 = 0.1

# Configurações do corpo 2:
pos_2 = np.array([10.0,0.0,0.0]) 
vel_2 = np.array([0.0, np.sqrt(G * 100000.0 / 10), 0.0])
mass_2 = 1.0
size_2 = 0.1

# Configurações do corpo 3:
pos_3 = np.array([5.0,5.0,-3.0])
vel_3 = np.array([-0.9,0.1,-0.2])
mass_3 = 0.0
size_3 = 0.1