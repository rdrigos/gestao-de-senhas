
import random


tamanho_senha = int(input("Digite o tamanho da Senha desejada : "))

caracteres = ["a", "A", "b", "B", "c", "C", "d", "D", "e", "E", "f", "F", "g", "G", "h", "H", "i", "I", "j", "J", "k",
              "K", "l", "L", "m", "M", "n", "N", "o", "O", "p", "P", "q", "Q", "r", "R", "s", "S", "t", "T", "u", "U",
              "v", "V", "w", "W", "x", "X", "y", "Y", "z", "Z", "!", "@", "#", "$", "%", "&", "(", ")", "1", "2", "3",
              "4", "5", "6", "7", "8", "9", "0", "*"]
senha = ""

if tamanho_senha >= 8:
    for i in range(tamanho_senha):
        senha = senha + random.choices(caracteres)[0]
    print("Nova senha criada, não se esqueça de anota-lá!\n", senha)
else:
    print("A senha deve conter no mínimo 8 caracteres!")
