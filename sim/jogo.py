print("Bem vindo ao jogo de adivinhaçao")
import random

numero_secreto=random.randint(1,10)

max_tentativa=3
print("Tente adivinhar o numero entre 1 e 10")


for tentativas in range(1,max_tentativa+1):
      palpite = int(input("Digite seu palpite: "))
      tentativas += 1
      if palpite == numero_secreto:
        print ("Parabens voce acertou!")
      elif palpite < numero_secreto:
        print ("Muito baixo,tente novamente")   
      else:
        print("Muito alto,tente novamente")

if palpite != numero_secreto:
   print ("Fim do jogo.O numero era: ",numero_secreto) 
       