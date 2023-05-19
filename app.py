from random import sample

#valor final contém esses números
vf = "0123456789"

#quantidade de digitos
digitos = 2

#resultado que é mostrado na tela
resultado = "".join(sample(vf, digitos))
print(resultado)
