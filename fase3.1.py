
#
#Conexão Oracle
import oracledb 
try:

    
    connection = oracledb.connect(
        user = "BD150224438",
        password = "Yxcjw1",
        dsn = "172.16.12.14/xe"
    )
    print('Conectado')
    cursor = connection.cursor()
#
#Inicio do Programa
    def telaMenu():
        
        print("\n") 
        print("_"*55)
        print("\t   Programa Controle de Estoque")
        print("-"*55)
        print ("\033[32m[1] Visualizar Produto \033[0m   \n[2] Cadastrar Produto \n\033[33m[3] Editar Produto\033[0m \n\033[31m[4] Apagar Produto\033[0m\n")
        num_tela = Verificação("\033[47m\033[30mEscolha a Opção Desejada: \033[0m",int)#\033[47m Codigo pra definir cor de fundo,\033[30m Define cor do testo como preta
        while num_tela not in [1, 2,3,4]:
                print("\n\t\033[41mERRO\033[0m\n")
                print ("\033[32m[1] Visualizar Produto \033[0m   \n[2] Cadastrar Produto \n\033[33m[3] Editar Produto\033[0m \n\033[31m[4] Apagar Produto\033[0m\n")
                num_tela = Verificação("\033[47m\033[30mEscolha a Opção Desejada: \033[0m",int)#\033[47m Codigo pra definir cor de fundo,\033[30m Define cor do testo como preta
        return num_tela
    #Def para tratar os erros sobre as entradas


    def Verificação(message, data_type):
        while True:
           try:
               user_input = data_type(input(message))
               return user_input
           except ValueError:
               print("Entrada inválida. Por favor, tente novamente.\n")

    #Def responsavel pela busca de produtos no banco de dados
    def buscarProdutos():
        global num_tela, contador,designerTabela# tornando as variaveis global
        print("\n")
        print("_"*55)
        print("\t\t   Banco de Dados")
        print("-"*55)
        cursor.execute("SELECT * FROM proodutos")
        produtos = cursor.fetchall()  # Obter todos os produtos
        #Função para saber se o cliente desejava buscar apenas um produto ou todos
        print("\n[1] Busca Simplificada\n[2] Exibir Completo")
        opção_BD =Verificação("\n\033[47m\033[30mEscolha a Opção Desejada: \033[0m",int)#\033[47m Codigo pra definir cor de fundo,\033[30m Define cor do testo como preta
        while opção_BD not in [1, 2]:
                print("\n\t\033[41mERRO\033[0m\n")
                opção_BD =Verificação("\n\033[47m\033[30mEscolha a Opção Desejada: \033[0m",int)#\033[47m Codigo pra definir cor de fundo,\033[30m Define cor do testo como preta
        #Modelo de banco de dados apresentado desejado
        print("\n[1] Tabela Horizonral \n[2] Tabela vertical ")
        designerTabela=Verificação("\n\033[47m\033[30mEscolha a Opção Desejada: \033[0m",int)
        #Aqui vai ser onde o trabalho de pesquisa simplificada vai ser feito
        if opção_BD == 1:
            codigo_produto = Verificação('\n\033[47m\033[30mDigite o Código do Produto: \033[0m',int)
            cursor.execute(f"SELECT * FROM proodutos WHERE codigo = {codigo_produto}")
            produto = cursor.fetchone()
            if produto:
                nome_produto = produto[1]
                descricao_produto = produto[2]
                CP = produto[3]
                CF = produto[4]
                CV = produto[5]
                IV = produto[6]
                ML = produto[7]
                Opção_BD(codigo_produto, nome_produto, descricao_produto, CP, CF, CV, IV, ML)
                print("-" * 55 )
                print("\033[31m[1] Excluir\033[0m \n\033[33m[2] Editar\033[0m  \n[0]Sair")
                contador=1
                num = int(input("\n\033[47m\033[30mOpção Desejada: \033[0m"))
                while num_tela not in [1, 2,0]:
                    print("\n\t\033[41mERRO\033[0m\n")
                    num = int(input("\n\033[47m\033[30mOpção Desejada: \033[0m"))
                
                if num == 1:
                   apagarProdutos()
                if num == 2:
                
                   editarProdutos()
                if num == 0:
                   telaMenu()
            else:
                print("Produto não encontrado.")
        #Aqui vai ser onde o sistema vai fazer o trabalho de buscar todos os produtos do BD     
        elif opção_BD == 2:
            if produtos:
                for produto in produtos:
                    codigo_produto = produto[0]
                    nome_produto = produto[1]
                    descricao_produto = produto[2]
                    CP = produto[3]
                    CF = produto[4]
                    CV = produto[5]
                    IV = produto[6]
                    ML = produto[7]
                    Opção_BD(codigo_produto, nome_produto, descricao_produto, CP, CF, CV, IV, ML)
                print("\033[31m[1] Excluir\033[0m \n\033[33m[2] Editar\033[0m  \n[0]Sair")
                contador=1
                num = int(input("\n\033[47m\033[30mOpção Desejada: \033[0m"))
                while num not in [1, 2,0]:
                    print("\n\t\033[41mERRO\033[0m\n")
                    num = Verificação("\n\033[47m\033[30mOpção Desejada: \033[0m",int)
                if num == 1:
                    apagarProdutos()
                if num == 2:
                    editarProdutos()
                if num == 0:
                    telaMenu()
                
            else:
                print("Nenhum produto encontrado.")

    #Essa Def é responsavel por guarda toda a logica do calculo de rentabilidade, e tbm ela armazena o designer desejado pelo usuario
    def Opção_BD(codigo_produto, nome_produto, descricao_produto, CP, CF, CV, IV, ML):
            global designerTabela,cabeçalho
            pass
            #Formula Calculo Preço de Venda
            PV = CP / ( 1 - ( ( CF + CV + IV + ML) / (100) ) )
            #Cáloulos das % e valores
            #%Preço de venda
            PV1= (PV/PV) * 100
            #%Custo do produto
            CPP= (CP/PV) * 100
            #Receita bruta 
            RC= PV - CP
            #% Receita bruta
            RC1= (RC/PV) * 100
            #% Custo fixo
            CF1= (CF*PV) / 100
            #% Comissão de vendas
            CV1= (CV*PV) / 100
            #% Impostos
            IV1= (IV*PV) / 100
            # Outros custos
            OC= CF+ CV+ IV
            # %Outros custos
            OCP= (OC*PV) / 100
            #Rentabilidade
            RENT= CP+ OC
            rent=PV-RENT
            #% Rentabilidade
            RENT1= (ML*PV) / 100
            #
            #Tabela Horizontal
            if designerTabela==1:
                print("-" * 55)
                print(f"Codigo do Produto:  {codigo_produto}")
                print("-" * 55)
                print(f"{nome_produto:^50}")
                print(f"{descricao_produto:^50}")
                print("-" * 55)
                print(f"{'Descrição':<20}{'Valor':>15}{'%':>15}")
                print("-" * 55)
                print(f"{'Preço de venda':<20}R${PV:>15.2f}{PV1:>15.2f} %")
                print("-" * 55)
                print(f"{'Preço do produto':<20}R${CP:>15.2f}{CPP:>14.1f} %")
                print("-" * 55)
                print(f"{'RECEITA BRUTA':<20}R${RC:>15.2f}{RC1:>15.2f} %")
                print("-" * 55)
                print(f"{'CUSTO FIXO':<20}R${CF1:>15.2f}{CF:>15.2f} %")
                print("-" * 55)
                print(f"{'COMISSÃO DE VENDAS':<20}R${CV1:>15.2f}{CV:>15.2f} %")
                print("-" * 55)
                print(f"{'IMPOSTOS':<20}R${IV1:>15.2f}{IV:>15.2f} %")
                print("-" * 55)
                print(f"{'OUTROS CUSTOS':<20}R${OCP:>15.2f}{OC:>15.2f} %")
                print("-" * 55)
                print(f"{'RENTABILIDADE':<20}R${RENT1:>15.2f}{ML:>14.1f} %")
                print("-" * 55 )
                #
                #Tabela de Lucros
                if RENT1 > 20:
                    print('\033[34m'+'Lucro: Alto'+ '\033[0m') #34m imprime em cor azul
                    print("-" * 55 )
                    
                elif RENT1 >= 10 and RENT1 <= 20:
                    print('\033[32m'+'Lucro: Medio'+ '\033[0m ') #32m imprime em cor verde
                    print("-" * 55 )
                    
                elif RENT1 > 0 and RENT1 < 10:
                    print('\033[33m'+'Lucro: Baixo'+ '\033[0m') #33m imprime em cor amarela
                elif RENT1 == 0:
                    print('Lucro: Em Equilibrio'+ '\033[0m')
                    print("-" * 55 )
                    
                else:
                    print('\033[31m'+'Em Prejuizo'+ '\033[0m') #31m imprime em cor vermelha
                    print("-" * 55 )
            
            #tabela vertical   
            if designerTabela==2:
                if cabeçalho==1:
                    print("\t\t\t","_" * 55)
                    print("\t\t\t\t\t\033[32mInformações do Produto\033[0m")
                    print("\t\t\t","-" * 55)
                    print("\n\033[47m\033[30mCódigo\tNome\tDescrição\t\tPV\tCP\tRB\tCF\tCV\tIV\tOC\tML\033[0m")
                    print("\033[32m_\033[0m" * 120)
                    cabeçalho=cabeçalho+1
                
                print(f"\033[47m\033[30m{codigo_produto}\033[0m\t{nome_produto}\t{descricao_produto}\t    {PV:>15.2f}\t{CP:.2f}\t{RC1:.2f}\t{CF:.2f}\t{CV:.2f}\t{IV:.2f}\t{OC:.2f}\t{ML:.2f}\033[0m")
                print("\033[32m-\033[0m" * 120)
                if RENT1 > 20:
                    print('\033[34m'+'Lucro: Alto'+ '\033[0m') #34m imprime em cor azul
                    print("-" * 55 )
                    
                elif RENT1 >= 10 and RENT1 <= 20:
                    print('\033[32m'+'Lucro: Medio'+ '\033[0m ') #32m imprime em cor verde
                    print("-" * 55 )
                    
                elif RENT1 > 0 and RENT1 < 10:
                    print('\t\t\t\t\t\t\t\t\t\t\t\t\t\t\033[33m'+'Lucro: Baixo'+ '\033[0m') #33m imprime em cor amarela
                elif RENT1 == 0:
                    print('Lucro: Em Equilibrio'+ '\033[0m')
                    print("-" * 55 )
                    
                else:
                    print('\033[31m'+'Em Prejuizo'+ '\033[0m') #31m imprime em cor vermelha
                    print("-" * 55 )
        
    
            
    def cadastroProdutos():
    
                
        print ("Cadastro de Produto")
        nome_cadastro = input("Nome do Produto: ",)
        descricao_cadastro = input("Descrição do Produto: ",)
        codigo_cadastro = Verificação("Cadastre o Código Para o Produto: ", int)
        custo_cadastro = Verificação("Custo do Produto: ", float)
        comissao_cadastro = Verificação("Qual a Taxa de Comissão de Vendas: ", float)
        fixo_cadastro = Verificação("Qual a Taxa de Custo Fixo: ", float)
        impostos_cadastro = Verificação("Qual a Taxa de Impostos: ", float)
        rentabilidade_cadastro = Verificação("Rentabilidade Esperada: ", float)

        cursor.execute(f'''INSERT INTO PROODUTOS VALUES({codigo_cadastro},'{nome_cadastro}','{descricao_cadastro}',
                {custo_cadastro},{fixo_cadastro},{comissao_cadastro},{impostos_cadastro},{rentabilidade_cadastro})'''
                )
        
        print("-"*55)
        print ("\t\tReveja as Informações")
        print(f'\t{nome_cadastro :^50},\n{descricao_cadastro:^50}')
        print("-"*55)

        print(f"Preço de Aquisição\t\tR${custo_cadastro :.1f}")
        print(f"Custo Fixo       \t\t{fixo_cadastro} %")
        print(f"Comissão de Vendas\t\t{comissao_cadastro} %")
        print(f"Impostos          \t\t{impostos_cadastro} %")
        print(f"Rentabilidade     \t\t{rentabilidade_cadastro} %")

        print("Deseja Confirmar as Opções ?")
        print("[SIM] Confirmar \n[NÃO] Cancelar")
        tela_cadastro = Verificação("Opção Desejada: ",str)
        tela_cadastro.lower()
        
        if tela_cadastro == 'sim':
            cursor.execute("commit") #Confirma o Cadastro e Registra os Dados no Banco de Dados
            print("Cadastro Concluido.")
            print("[1] Cadastrar Outro Produto\n[2]Sair")
            
            opcao_cadastro = Verificação ("Opção Desejada: ",int)
            while opcao_cadastro not in [1, 2,0]:#Verificação de entrada
                    print("\n\t\033[41mERRO\033[0m\n")
                    opcao_cadastro = Verificação ("Opção Desejada: ",int)
            if opcao_cadastro == 1 :
                cadastroProdutos()

            elif opcao_cadastro == 2:
                telaMenu()
    
            else:
                print("Opção Digitada Incorreta, Digite uma Opção Fornecida")
                print("[1] Cadastrar Outro Produto \n [2]Sair do Cadastro de Produto")

        elif tela_cadastro == 'nao' or tela_cadastro == 'não':
            print("[1] Recomeçar Cadastro \n[2] Sair do Cadastro de Produto")
            opcao_cadastro = Verificação ("Opção Desejada: ",int)

            if opcao_cadastro == 1 :
                cadastroProdutos()

            elif opcao_cadastro == 2:
                num_tela = telaMenu(num_tela)
    
            else:
                print("Opção Digitada Incorreta, Digite uma Opção Fornecida")
                print("[1] Recomeçar Cadastro \n[2] Sair do Cadastro de Produto")       

        else:
            print("Opção Digitada Incorreta, Por Favor escolha entre [SIM] ou [NÃO]")
            tela_cadastro = input ("Opção Desejada: ")
                

    def editarProdutos():
        global num_tela, contador
        print("\n")
        print("_"*55)
        print("\t\t   Editar Produto")
        print("-"*55)
        num_tela=3
        if num_tela==3:
            if num_tela==3 and contador==0:
                print("\n\t\t\t\033[42mATENÇÃO!!!\033[0m\n\n")
                print("Antes de Editar os Dados do Produto, Sugerimos Pesquisar as Informações do Produto.\n")
                print("\033[32m[1]Visualizar\033[0m\n\033[31m[2]Continuar\033[0m\n[0]Voltar")
                Verificar_Dados=Verificação("\033[47m\033[30mOpção Desejada: \033[0m",float)

                if Verificar_Dados != 1 and Verificar_Dados != 2 and Verificar_Dados != 3:#Verificação de entrada
                    print("\t\033[41mERRO\033[0m\n")
                    Verificar_Dados=Verificação("\033[47m\033[30mOpção Desejada: \033[0m",float)

                elif Verificar_Dados ==0:#Verificar dados ==0 volta para tela inicial do programa
                    telaMenu()

                elif Verificar_Dados==1:#Verificar dados ==1 volta para tela de pesquisa do programa

                    tabela_produtos = buscarProdutos()
                    editarProdutos()

                elif Verificar_Dados == 2:
                    contador=1
                    editarProdutos()
            if num_tela==3 and contador==1:
                print("\033[32m\n[1]Nome\n[2]Descricao\n[3]Custo Do Produto\n[4]Comissão\n[5]Custo Fixo\n[6]Impostos\n[7]Rentabilidade\n[0]Voltar\033[0m")
                opcao_editar =Verificação("\033[47m\033[30mDigite o Campo Desejado: \033[0m",int)
                while opcao_editar not in[1,2,3,4,5,6,7,0]:
                    opcao_editar =Verificação("\033[47m\033[30mDigite o Campo Desejado: \033[0m",int)
                codigo_produto=Verificação("\n\033[47m\033[30mCodigo Do Produto: \033[0m",int)

                if opcao_editar == 1:
                    Campo_Nome=input("Pra qual nome voçê deseja alterar: ")
                    cursor.execute(f"UPDATE Proodutos SET Nome = '{Campo_Nome}' WHERE codigo = {codigo_produto}")
                    cursor.execute("commit")

                elif opcao_editar ==2:
                    Campo_Descriçao=input("Descrição Desejada: ")
                    cursor.execute(f"UPDATE Produtos SET descricao_produto = '{Campo_Descriçao}' WHERE codigo_produto = {codigo_produto}")
                    cursor.execute("commit")

                elif opcao_editar ==3:
                    Campo_CustoP=float(input("Custo do produto desejado: "))

                    cursor.execute(f"UPDATE Produtos SET CP = '{Campo_CustoP}' WHERE codigo_produto = {codigo_produto}")
                    cursor.execute("commit")
                
                elif opcao_editar ==4:
                    Campo_Comissão=float(input("Comição Desejada: "))

                    cursor.execute(f"UPDATE Produtos SET CV = '{Campo_Comissão}' WHERE codigo_produto = {codigo_produto}")
                    cursor.execute("commit")
            
                elif opcao_editar ==5:
                    Campo_CustoF=float(input("Custo Fixo Desejado: "))
                    cursor.execute(f"UPDATE Produtos SET CF = '{Campo_CustoF}' WHERE codigo_produto = {codigo_produto}")
                    cursor.execute("commit")
                
                elif opcao_editar ==6:
                    Campo_Imposto=float(input("Impostos Desejado: "))
                    cursor.execute(f"UPDATE Produtos SET IV = '{Campo_Imposto}' WHERE codigo_produto = {codigo_produto}")
                    cursor.execute("commit")
            
                elif opcao_editar ==7:
                    campoRentabilidade=float(input("Rentabilidade Desejada: "))
                    cursor.execute(f"UPDATE Produtos SET ML = '{campoRentabilidade}' WHERE codigo_produto = {codigo_produto}")
                    cursor.execute("commit")
                elif opcao_editar ==0 :
                    telaMenu()#Condição pra volta pra tela inicial
            if opcao_editar>0 and opcao_editar<8: 
                    print("_"*55)
                    print("\t   \033[42mAlteração Bem Sucedida\033[0m")
                    
                    print("-"*55)   
                    print("\033[32m[1]Editar Outro Pedido\033[0m\n[0]Voltar")
                    confirmar_editar=Verificação("\033[47m\033[30mOpção Desejada: \033[0m",int)

                    if confirmar_editar==1:
                        editarProdutos()#Condição ir pro setor de edição
                    else:
                        telaMenu()#Condição pra volta pra tela inicial
    def apagarProdutos():
        global num_tela, contador
        print("\n")
        print("_"*55)
        print("\t\t   Excluir Produto")
        print("-"*55)
        
        if num_tela==4 and contador==0:#vai entra nesse loop se a variavel contador for 0,Isso significar q n vizualizou primeiro a tabela
                print("\n\t\t\t\033[42mATENÇÃO!!!\033[0m\n\n")
                print("Antes De voçê Excluir Dados Da Tabela Sugerimos Pesquisar Primeiro.\n")
                print("\033[31m[1]Continuar\033[0m\n\033[32m[2]Visualizar\033[0m\n[0]Voltar")
                Verificar_Dados=Verificação("\033[47m\033[30mOpção Desejada: \033[0m",int)
                while Verificar_Dados not in [1, 2,0]:#Verificação de entrada
                    print("\n\t\033[41mERRO\033[0m\n")
                    Verificar_Dados=int(input("\033[47m\033[30mOpção Desejada: \033[0m"))
                if Verificar_Dados==1:
                    contador=1
                    apagarProdutos()
                elif Verificar_Dados==2:
                    buscarProdutos()
                elif Verificar_Dados==0:
                    telaMenu()
        if num_tela==4 and contador>=1:
                print("\nDigite o Codigo do Produto para Realizar Procedimento\n")
                codigo_excluir=Verificação("\n\033[47m\033[30mDigite o codigo: \033[0m",int)

                cursor.execute(f"DELETE FROM Proodutos WHERE codigo = {codigo_excluir}")
                cursor.execute("commit")
                if codigo_excluir>=0:
                    print("_"*55)
                    print("\t   \033[42mDeletado Com Susesso\033[0m")
                    print("-"*55) 
                    print("\033[32m[1]Deletar Outro Produto\033[0m\n[0]Voltar")
                    confirmar_excluir=Verificação("\033[47m\033[30mOpção Desejada: \033[0m",int)
                    while confirmar_excluir not in [1,0]:#Verificação de entrada
                        print("\n\t\033[41mERRO\033[0m\n")
                        confirmar_excluir=Verificação("\033[47m\033[30mOpção Desejada: \033[0m",int)
                    if confirmar_excluir ==1:
                        
                        contador=contador+1
                        apagarProdutos()
                    else:
                        telaMenu #Condição pra volta pra tela inicial
        print("\n\t\t\033[42mATENÇÃO!!!\033[0m\n\n")
        print("Voçê Deseja Mesmo Excluir Dados Da Tabela?\n\033[32m[1]SIM\033[0m\n\033[31m[2]NÃO\033[0m")
        tela_excluir=Verificação("\n\033[47m\033[30mOpção Desejada:\033[0m",int)

        while tela_excluir not in [1,2,0]:#Verificação de entrada
            print("\n\t\033[41mERRO\033[0m\n")
            tela_excluir=Verificação("\n\033[47m\033[30mOpção Desejada:\033[0m",int)
            while tela_excluir not in [1,0]:#Verificação de entrada
                print("\n\t\033[41mERRO\033[0m\n")
                tela_excluir=Verificação("\n\033[47m\033[30mOpção Desejada:\033[0m",int)
        if tela_excluir ==1:
            print("\nDigite o Codigo do Produto para Realizar Procedimento\n")
            codigo_excluir=Verificação("\n\033[47m\033[30mDigite o Codigo:\033[0m",int)
            cursor.execute(f"DELETE FROM Produtos WHERE codigo_produto = {codigo_excluir}")
            cursor.execute("commit")

            print("_"*55)
            print("\t   \033[42mDeletado Com Susesso\033[0m")
            print("-"*55)
            print("\033[32m[1]Deletar Outro Produto\033[0m\n[2]Voltar")
            tela_excluir = Verificação("\033[47m\033[30mOpção Desejada: \033[0m",int)
            while tela_excluir not in [1,0]:#Verificação de entrada
                print("\n\t\033[41mERRO\033[0m\n")
                tela_excluir=Verificação("\n\033[47m\033[30mOpção Desejada:\033[0m",int)
        elif tela_excluir == 2:
            num_tela = telaMenu(num_tela)
            
    num_tela = telaMenu()
    while num_tela != 0:
        cabeçalho=1
        contador=0
        if num_tela == 1:
            
            buscarProdutos()
            

        elif num_tela == 2: 
            cadastroProdutos()
            

        elif num_tela == 3:
            
            editarProdutos()
            

        elif num_tela == 4:
            apagarProdutos()
            
except oracledb.DatabaseError as e:
    # Lida com erros de conexão com o banco de dados
    print("\033[42m\n\n\n\t\t\t\t\t\033[41m ERRO ao conectar ao banco de dados:\033[0m\033[42m\n\t\t\t\t\t\t\033[41mLigue Para a Central\033[0m\033[42m\n\t\t\t\t\t\t   \033[41m\033[47m\033[30m(98) 9 70294839\033[0m\033[42m\n\n\033[0m")
cursor.close()
connection.close()