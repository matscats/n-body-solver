import numpy as np

G = 1.32712440018e20 * 3.1558149e7 ** 2 / 1.495978707e11 ** 3 # Newton's gravtational constant * solar mass * year² / u.a³
h = 0.001 # Tamanho do passo (anos)
ti = 0 # Tempo inicial (anos)
tf = 200 # Tempo final (anos)

body_1_cfg = {
  'pos' : np.array([0.5 * 53.26/1.495, 0.0, 0.0]),
  'vel' : np.array([0.1 * 53.26/1.495 * 365.256/(79.91*365*0.51),0.1 * 53.26/1.495 * 365.256/(79.91*365*0.51),0.0]),
  'mass' : 1.1,
  'size' : 0.005,
  'name' : 'Alpha Centauri A'
}

body_2_cfg = {
  'pos' : np.array([-0.5 * 53.26/1.495, 0.0, 0.0]),
  'vel' : np.array([-0.5 * 53.26/1.495 * 365.256/(79.91*365*0.51),0.0,-1.0 * 53.26/1.495 * 365.256/(79.91*365*0.51)-0.01 * 53.26/1.495 * 365.256/(79.91*365*0.51)]),
  'mass' : 0.907,
  'size' : 0.00,
  'name' : 'Alpha Centauri B'
}

body_3_cfg = {
  'pos' : np.array([1000.0,1000.0,1000.0]),
  'vel' : np.array([0.0,0.0,0.0]),
  'mass' : 0.0,
  'size' : 0.005,
  'name' : 'none'
}