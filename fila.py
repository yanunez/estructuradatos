import os
os.system('cls' if os.name == 'nt' else 'clear')

fila = []

fila.append('Client 1')
fila.append('Client 2')
fila.append('Client 3')
fila.append('Client 4')
print("Los elementos en esta fila son:", fila)

cliente_atendido = fila.pop(0)
print("cliente atendido fue:", cliente_atendido)
print("Siguiente en la fila por atender es:", fila)
