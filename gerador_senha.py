from random import choice


print('GERADOR DE SENHAS')

print('Quantos caracteres deseja definir sua senha?')
try:
    while True:
        n = int(input('Informe um valor entre 8 a 12: '))
        if n <8 or n >12:
            print('Erro, defina o valor correto de caracteres')
        else:
            break
    maius = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    minus = maius.lower()
    numer = '0123456789'
    caract = '!@#$%¨&*()-_+={[}]?'

    def safe_generator():
        senha_chairs = (maius + minus + numer + caract)
        senha = ''.join(choice(senha_chairs) for _ in range(n))
        return senha

    senha = safe_generator()
    print(f'A senha de {n} caracteres foi gerada com sucesso\n {senha} \n Guarde em um lugar seguro!!. ')
except:
    print("ERRO, não foi possivel definir senha")



