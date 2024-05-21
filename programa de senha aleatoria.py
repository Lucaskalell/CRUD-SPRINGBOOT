import random
import string

def gerar_senha(tamanho=5):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

nova_senha = gerar_senha()
print("Sua nova senha aleatória:", nova_senha)