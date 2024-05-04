print("\n\n ________________________________________________")
print("|\t\tSistema Iniciado\t\t|")
print("|_______________________________________________|\n")
quant_produtos=int(input("Quantos produtos quer cadastrar:"))
while quant_produtos>0:
   for i in range(quant_produtos):
      estoque={}
      print("\n\n ________________________________________________")
      print("|\t\tCadastrar Produto\t\t|")
      print("|_______________________________________________|\n")
      codigo_produto=int(input("Digite codigo do produto:\n"))
      nome_produto=str(input("Nome do Produto:\n"))
      desc_produto=str(input("Descrição do Produto:\n"))
      CP=int(input("Valor do produto:\n"))
      CF=int(input("Custo fixo do produto:\n"))
      CV=int(input("Comissão de vendas:\n"))
      IV=int(input("Impostos:\n"))
      ML=int(input("Quanto de rentabilidade:"))
      estoque[codigo_produto]={'Nome':nome_produto,
                              'Descriçao':desc_produto, 
                              'CP':CP,
                              'CF':CF,
                              'CV':CV,
                              'IV':IV,
                              'ML':ML}
      contador=CP+CF+CV+IV+ML
      while ML>100:
        print("Sua rentabilidade n pode ser maior q 100%")
        ML=int(input("Digite novamente"))

      while contador >100:
         print('\nPor favor digite novamente os valores, a soma entre os valores n pode ser superior a 100.\n')
         codigo_produto=int(input("Digite codigo do produto:\n"))
         nome_produto=str(input("Nome do Produto:\n"))
         desc_produto=str(input("Descrição do Produto:\n"))
         CP=int(input("Valor do produto:\n"))
         CF=int(input("Custo fixo do produto:\n"))
         CV=int(input("Comissão de vendas:\n"))
         IV=int(input("Impostos:"))
         ML=(input("Quanto de rentabilidade:"))
       
         estoque[codigo_produto]={'Nome':nome_produto,
                                  'Descriçao':desc_produto, 
                                   'CP':CP,
                                   'CF':CF,
                                   'CV':CV,
                                   'IV':IV,
                                   'ML':ML}
         contador=CP+CF+CV+IV+ML
      print("\n\n ________________________________________________")
      print("|\t\tPRODUTO CADASTRADO\t\t|")
      print("|_______________________________________________|\n")
      print("Deseja exibir o calculo?\n[1]SIM\n[2]NÂO")
      exibir_calculo=int(input("Resposta:"))
   while exibir_calculo !=1 or exibir_calculo !=2:
      print("Deseja exibir o calculo?\n[1]SIM\n[2]NÂO")
      exibir_calculo=input("Digite 1 para SIM e 2 para NÂO:")
   if exibir_calculo ==2:
      print("\n\n ________________________________________________")
      print("|\t\tSISTEMA ENCERRADO\t\t|")
      print("|_______________________________________________|\n")
   if exibir_calculo ==1:
      for codigo_produto, produto in estoque.items():
         PV = produto['CP'] / (1 - ((produto['CF'] + produto['CV'] + produto['IV'] + produto['ML']) / 100))
       
     
     #Formula Calcluo Preço de Venda
         PV = CP / ( 1 - ( ( CF + CV + IV + ML) / (100) ) )

    #Cáloulos das % e valores
    #%Preço de venda
         PV1 = (PV /PV) * 100

    #%Custo do produto
         CPP = (produto['CP'] / PV) * 100

    #Receita bruta 
         RC = PV - produto['CP']

    #% Receita bruta
         RC1 = (RC / PV) * 100

    #% Custo fixo
         CF1= (CF*PV) / 100
         CF1 = (produto['CF'] * PV) / 100

    #% Comissão de vendas
         CV1  = ( produto [ 'CV' ] *  PV ) /  100
   

    #% Impostos
         IV1 = (produto['IV'] * PV) / 100

    # Outros custos
         OC = produto['CF'] + produto['CV'] + produto['IV']

    # %Outros custos
         OCP = (OC * PV) / 100

    #Rentabilidade
         RENT = produto['CP'] + OC
         rent = PV - RENT
 
    #% Rentabilidade
         RENT1 = (produto['ML'] * PV) / 100
        #Tabela
         print("----------------------------------------------------------------------")
         print('\t\t\t',produto['Nome'], produto['Descriçao'])
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
        
         print("\n\n\n")