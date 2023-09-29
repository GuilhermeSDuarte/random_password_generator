import random
import string
# Define o tamanho da senha
tamanho = 16
# É pego um caractere aleatório.
chars = string.ascii_letters + string.digits + '!@#$%&*()-+=,.:/?'
# Gera de forma randomica.
rnd = random.SystemRandom()
# Gera uma senha de 16 dígitos com caracteres aleatórios.
print(''.join(rnd.choice(chars) for i in range(tamanho)))
