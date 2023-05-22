from random import sample

def porcentagem_casal():
    #valor final contém esses números
    vf = "0123456789"

    #quantidade de digitos
    digitos = 2

    #resultado que é mostrado na tela
    resultado = "".join(sample(vf, digitos))
    print(resultado)

def resultado_mensagem():
    mensagem = 'porcentagem de amor entre'
    return mensagem
