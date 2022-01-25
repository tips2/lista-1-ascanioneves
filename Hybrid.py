Duas_rodas = False
Pequeno = False
Motocicleta = False
MotoStreet = False
Quatro_rodas = False
Carro = False
Chopper = False

def fatos():
  global Quatro_rodas, Pequeno
  Quatro_rodas = True
  Pequeno = True

if __name__ == "__main__":
  fatos()
  k = 0
  while k < 10:
    if(Duas_rodas and Motocicleta):
      Quatro_rodas = True

    if(Duas_rodas and MotoStreet):
      Chopper = True

    if(Chopper):
      Pequeno = True 
    
    if(Carro):
      print(f'(Carro) = Sim\n')
      break

    if(Quatro_rodas and Pequeno):
      Carro = True

    if(Duas_rodas):
      Motocicleta = True
      Motostreet = True
    k += 1
  else:
    print(f'(Carro) = Não\n')