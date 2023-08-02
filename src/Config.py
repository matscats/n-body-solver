import os
import json

G = 1.32712440018e20 * 3.1558149e7 ** 2 / 1.495978707e11 ** 3 # Newton's gravtational constant * solar mass * year² / u.a³
h = 0.0001 # Tamanho do passo (anos)
ti = 0 # Tempo inicial (anos)
tf = 145 # Tempo final (anos)

json_file = os.path.join("projects", "params.json")
body_1_cfg, body_2_cfg, body_3_cfg = {}, {}, {}

with open(json_file) as file:
  data = json.load(file)
  body_1_cfg = data['body_1']
  body_2_cfg = data['body_2']
  body_3_cfg = data['body_3']
