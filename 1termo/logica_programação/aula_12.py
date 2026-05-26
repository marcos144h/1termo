2

while True:
    try:
       quantidade_de_pessoas=int(input("quantas pessoas tem no elevador?"))
       andar_atual=int(input("qual seu andar atual"))
       andar_destino = int(input("qual o andar que voce deseja ir?>"))
       if andar_destino > andar_atual:
           print("subindo...")
           print("chegou ao andar destino")
       elif andar_destino < andar_atual:
           print("descendo..")
           print("chegou ao andar destino")
       else:
           print("voce ja esta nesse andar.")
       break 

    except ValueError:
     print("Entrada inválida. Por favor, insira um número válido.")

     