import math as m
angulo = float(input('Digite o valor do ângulo: '))
seno = m.sin(m.radians(angulo))
cosseno = m.cos(m.radians(angulo))
tangente = m.tan(m.radians(angulo))

print(f'O ângulo de {angulo} tem o SENO de {seno:.2f}')
print(f'O ângulo de {angulo} tem o COSSENO de {cosseno:.2f}')
print(f'O ângulo de {angulo} tem a TANGENTE de {tangente:.2f}')