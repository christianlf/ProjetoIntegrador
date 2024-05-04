codigo_produto=int(input("Digite codigo do produto:\n"))
nome_produto=str(input("Nome do Produto:\n"))
desc_produto=str(input("Descrição do Produto:\n"))
CP=int(input("Valor do produto:\n"))
CF=int(input("Custo fixo do produto:\n"))
CV=int(input("Comissão de vendas:\n"))
IV=int(input("Impostos:\n"))
ML=int(input("Quanto de rentabilidade:"))
PV = CP / (1 - ((CV + IV + ML) / 100))
       
     
     #Formula Calcluo Preço de Venda
PV = CP / ( 1 - ( ( CF + CV + IV + ML) / (100) ) )

    #Cáloulos das % e valores
    #%Preço de venda
PV1 = (PV /PV) * 100

    #%Custo do produto
CPP = (CP / PV) * 100

    #Receita bruta 
RC = PV - CP

    #% Receita bruta
RC1 = (RC / PV) * 100

    #% Custo fixo
CF1= (CF*PV) / 100
CF1 = (CF * PV) / 100

    #% Comissão de vendas
CV1  = ( CV*  PV ) /  100
   

    #% Impostos
IV1 = (IV * PV) / 100

    # Outros custos
OC = CF + CV + IV

    # %Outros custos
OCP = (OC * PV) / 100

    #Rentabilidade
RENT = CP + OC
rent = PV - RENT
 
    #% Rentabilidade
RENT1 = (ML* PV) / 100
        #Tabela
print("----------------------------------------------------------------------")
print('----------------------------------------------------------------------')
print(f"Descrição\t\t\t Valor \t\t\t %")
print('----------------------------------------------------------------------')
print(f"Preço de venda\t\t\t R${PV:.2f}\t\t{PV1:.2f} %")
print('----------------------------------------------------------------------')
print(f"Preço do produto\t\t R${CP:.2f}\t\t{CPP:.2f} %")
print('----------------------------------------------------------------------')
print(f"RECEITA BRUTA\t\t\t R${RC:.2f}\t\t{RC1:.2f} %")
print('----------------------------------------------------------------------')
print(f"CUSTO FIXO\t\t\t R${CF1:.2f}\t\t{CF:.2f} %")
print('----------------------------------------------------------------------')
print(f"COMISSÃO DE VENDAS\t\t R${CV1:.2f}\t\t\t{CV:.2f} %")
print('----------------------------------------------------------------------')
print(f"IMPOSTOS\t\t\t R${IV1:.2f}\t\t\t{IV:.2f} %")
print('----------------------------------------------------------------------')
print(f"OUTROS CUSTOS\t\t\t R${OCP:.2f}\t\t{OC:.2f} %")
print('----------------------------------------------------------------------')
print(f"RENTABILIDADE\t\t\t R${RENT1:.2f}\t\t{ML:.2f} %")
print('----------------------------------------------------------------------')

         #Tabela de Lucros
 
if RENT1 > 20:
      print('\033[34m'+'Lucro: Alto'+ '\033[0m') #34m imprime em cor azul

elif RENT1 >= 10 and RENT1 <= 20:
      print('\033[32m'+'Lucro: Medio'+ '\033[0m') #32m imprime em cor verde

 
elif RENT1 > 0 and RENT1 < 10:
      print('\033[33m'+'Lucro: Baixo'+ '\033[0m') #33m imprime em cor amarela

elif RENT1 == 0:
      print('Lucro: Em Equilibrio'+ '\033[0m')

else:
      print('\033[31m'+'Em Prejuizo'+ '\033[0m') #31m imprime em cor vermelha
        
