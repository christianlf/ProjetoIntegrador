# Programa para o Calculo do Preço de Venda
#
#
#Conexão Oracle
import oracledb 

try:    
    connection = oracledb.connect(
    user = "BD150224225",
    password = "Yzumv3",
    dsn = "172.16.12.14/xe"
    )
    cursor = connection.cursor()
#
except oracledb.DatabaseError as erro:
    # Lida com erros de conexão com o banco de dados
    print("\033[42m\n\n\n\t\t\t\t\t\033[41m ERRO ao conectar ao banco de dados:\033[0m\033[42m\n\t\t\t\t \033[41mLigue Para a Central\033[0m\033[42m\n\t\t\t\t \033[41m\033[47m\033[30m(98) 9 70294839\033[0m\033[42m\n\n\033[0m")
    

def verificacao (menssagem, tipo):
    while True:
        try:
            user_input = tipo(input(menssagem))
            return user_input
        
        except ValueError:    
            print("Entrada inválida. Por favor, Tente Novamente.\n")

#Função 
def buscarProdutos(tabela_produtos):

    cursor.execute("SELECT * FROM produtospi ")
    produtos = cursor.fetchone() #Retorna os valores da tabela

    while produtos is not None:

        codigo_produto= produtos[0]
        lista_produtos = produtos[1:]
        tabela_produtos[codigo_produto] = lista_produtos
        produtos = cursor.fetchone()
        
    return tabela_produtos   

def listar_produtos():

    global contador

    print("\n[1] Único Produto \n[2] Listar Todos os Produtos")
    opção_BD = verificacao ("\n\033[47m\033[30mEscolha a Opção Desejada: \033[0m",int)#\033[47m Codigo pra definir cor de fundo,\033[30m Define cor do texto como preta
    while opção_BD not in [1, 2]:
            opção_BD = verificacao ("\n\033[47m\033[30mEscolha a Opção Desejada: \033[0m",int)#\033[47m Codigo pra definir cor de fundo,\033[30m Define cor do texto como preta
    
    #Se BD = 1, aprensa um único produto.
    if opção_BD ==  1 :

        codigo_produto = verificacao('\n\033[47m\033[30mDigite o Código do Produto: \033[0m',int)
        listaUnica = tabela_produtos.get(codigo_produto)

        if listaUnica is None:
            print("Nenhum produto encontrado.")
            return
        else:
            nome_produto = listaUnica[0]
            descricao_produto = listaUnica[1]
            CP = listaUnica[2]
            CF = listaUnica[3] 
            CV = listaUnica[4] 
            IV = listaUnica[5] 
            ML = listaUnica[6]   
            Calculo(codigo_produto, nome_produto, descricao_produto, CP, CF, CV, IV, ML)
            print("-" * 55 )
            print("\033[31m[1] Excluir\033[0m \n\033[33m[2] Editar\033[0m  \n[0]Sair")
            contador=1
            num = int(input("\n\033[47m\033[30mOpção Desejada: \033[0m"))
            while num not in [1, 2 ,0]:
                print("\n\t\033[41mERRO\033[0m\n")
                num = int(input("\n\033[47m\033[30mOpção Desejada: \033[0m"))

            if num == 1:
                contador=1
                codigo_produto = None
                apagarProdutos(codigo_produto)
                return
            if num == 2:
                contador=1
                editarProdutos(codigo_produto)
                return 
            if num == 0:
                return
            else:
                print("Produto não encontrado.")
                codigo_produto = verificacao('\n\033[47m\033[30mDigite o Código do Produto: \033[0m',int)
                listaUnica = tabela_produtos.get(codigo_produto)
                
    #Se BD == 2, busca todos os produtos.
    elif opção_BD == 2:

        for codigo, produto in tabela_produtos.items():
            codigo_produto = codigo
            nome_produto = produto[0]
            descricao_produto = produto[1]
            CP = produto[2]
            CF = produto[3]
            CV = produto[4]
            IV = produto[5]
            ML = produto[6]
            Calculo(codigo_produto, nome_produto, descricao_produto, CP, CF, CV, IV, ML)

        print("\033[31m[1] Excluir Produto \033[0m \n\033[33m[2] Editar Produto \033[0m\n[0]Sair")
        contador = 1
        
        num = verificacao("\n\033[47m\033[30mOpção Desejada: \033[0m",int)

        while num not in [1, 2,0]:
            print("\n\t\033[41mERRO\033[0m\n")
            num = verificacao("\n\033[47m\033[30mOpção Desejada: \033[0m",int)
        if num == 1:
            contador=1
            apagarProdutos(codigo_produto)
            return
        if num == 2:
            contador=1
            editarProdutos(codigo_produto)
            return
        if num == 0:
            return
    else:
        print("Nenhum produto encontrado.")

#Essa Def é responsavel pelo calculo e for
def Calculo(codigo_produto, nome_produto, descricao_produto, CP, CF, CV, IV, ML):
    #Formula Calculo Preço de Venda

    descricao_produto = descriptografar(descricao_produto, alfabeto,chave)

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
    elif RENT1 > 0:
        print('\033[33m'+'Lucro: Baixo'+ '\033[0m') #33m imprime em cor amarela
    elif RENT1 == 0:
        print('Lucro: Em Equilibrio'+ '\033[0m')
        print("-" * 55 )
    else:
        print('\033[31m'+'Em Prejuizo'+ '\033[0m') #31m imprime em cor vermelha
        print("-" * 55 )

def criptografia(descricao_cadastro,alfabeto,chave):
    texto_cifrado = ''
    vetorNome = []

    if len(descricao_cadastro) % 2 != 0:
        descricao_cadastro += descricao_cadastro[-1]

    for char in descricao_cadastro:
        posicao = alfabeto.find(char)
        vetorNome.append(posicao)

    for i in range(0, len(vetorNome), 2):
        par = vetorNome[i:i+2]
        cifrado_par = [0, 0]
        for j in range(2):
            cifrado_par[j] = (chave[j][0] * par[0] + chave[j][1] * par[1]) % 26
        texto_cifrado += alfabeto[cifrado_par[0]] + alfabeto[cifrado_par[1]]

    return texto_cifrado

def inverso_modular(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def matriz_inversa_2x2(chave):
    determinante = chave[0][0] * chave[1][1] - chave[0][1] * chave[1][0]
    determinante = determinante % 26
    inverso_det = inverso_modular(determinante, 26)

    if inverso_det is None:
        raise ValueError("A matriz-chave não tem inversa em módulo 26.")

    return [[chave[1][1] * inverso_det % 26, -chave[0][1] * inverso_det % 26],
            [-chave[1][0] * inverso_det % 26, chave[0][0] * inverso_det % 26]]

def descriptografar(texto_cifrado, alfabeto, chave):
    texto_descriptografado = ''
    vetorCifrado = []
    chave_inversa = matriz_inversa_2x2(chave)

    for char in texto_cifrado:
        posicao = alfabeto.find(char)
        vetorCifrado.append(posicao)

    for i in range(0, len(vetorCifrado), 2):
        par = vetorCifrado[i:i+2]
        descriptografado_par = [0, 0]
        for j in range(2):
            descriptografado_par[j] = (chave_inversa[j][0] * par[0] + chave_inversa[j][1] * par[1]) % 26
        texto_descriptografado += alfabeto[descriptografado_par[0]] + alfabeto[descriptografado_par[1]]

    return texto_descriptografado

def cadastroProdutos(tabela_produtos): 
    print("-" * 55)
    print ("Cadastro de Produto")
    print("-" * 55)
    nome_cadastro = verificacao("\nNome do Produto: ",str)
    nome_cadastro = nome_cadastro.upper()

    descricao_cadastro = verificacao("Descrição do Produto: ",str)
    descricao_cadastro = descricao_cadastro.upper()

    codigo_cadastro = verificacao("Cadastre o Código Para o Produto: ", int)
    if codigo_cadastro in tabela_produtos:
        print("O código do produto já está sendo utilizado em outro produto.")
        codigo_cadastro = verificacao("Cadastre o Código Para o Produto Novamente: ", int)

    custo_cadastro = verificacao("Custo do Produto: ", float)
    comissao_cadastro = verificacao("Qual a Taxa de Comissão de Vendas: ", float)
    fixo_cadastro = verificacao("Qual a Taxa de Custo Fixo: ", float)
    impostos_cadastro = verificacao("Qual a Taxa de Impostos: ", float)
    rentabilidade_cadastro = verificacao("Rentabilidade Esperada: ", float)
    descricao_cadastro = descricao_cadastro.upper()

    print("-" * 55)
    print("\t\tREVEJA AS INFORMAÇÕES")
    print(f'{nome_cadastro:^50}\n{descricao_cadastro:^50}')
    print("-" * 55)

    print(f"PREÇO DE AQUISIÇÃO\t\tR${custo_cadastro :.1f}REAIS")
    print(f"CUSTO FIXO       \t\t{fixo_cadastro} %")
    print(f"COMISSÃO DE VENDAS\t\t{comissao_cadastro} %")
    print(f"IMPOSTOS          \t\t{impostos_cadastro} %")
    print(f"RENTABILIDADE     \t\t{rentabilidade_cadastro} %")
    print("-" * 55)
    print("DESEJA CONFIRMAR AS OPÇÕES ?")
    print("[SIM] CONFIRMAR\n[NÃO] CANCELAR")
    print("-" * 55)

    tela_cadastro = verificacao("Opção Desejada: ",str)
    tela_cadastro = tela_cadastro.lower()
    
    if tela_cadastro == 'sim':

        #Criptografia da descrição. 
        texto_cifrado = criptografia(descricao_cadastro,alfabeto,chave)
        
        cursor.execute(f'''INSERT INTO produtospi VALUES({codigo_cadastro},'{nome_cadastro}','{texto_cifrado}',
                {custo_cadastro},{fixo_cadastro},{comissao_cadastro},{impostos_cadastro},{rentabilidade_cadastro})'''
                )
        cursor.execute("commit") #Confirma o Cadastro e Registra os Dados no Banco de Dados
        print("-"*55)
        print("Cadastro Concluido.")
        print("[1] Cadastrar Outro Produto\n[2]Sair")
        print("-"*55)

        opcao_cadastro = verificacao ("Opção Desejada: ",int)
        while opcao_cadastro not in [1, 2,0]:#Verificação de entrada
                print("\n\t\033[41mERRO\033[0m\n")
                opcao_cadastro = verificacao ("Opção Desejada: ",int)
        if opcao_cadastro == 1 :
            cadastroProdutos(tabela_produtos)

        elif opcao_cadastro == 2:
             return

        else:
            print("Opção Incorreta, Digite uma Opção Fornecida")
            print("[1] Cadastrar Outro Produto \n [2] Sair do Cadastro ")

    elif tela_cadastro == 'nao' or tela_cadastro == 'não':
        print("[1]Recomeçar Cadastro \n[2]Sair do Cadastro de Produto")
        opcao_cadastro = verificacao ("Opção Desejada: ",int)

        if opcao_cadastro == 1 :
            cadastroProdutos()

        elif opcao_cadastro == 2:
             return

        else:
            print("Opção Digitada Incorreta, Digite uma Opção Fornecida")
            print("[1] Recomeçar Cadastro \n[2] Sair do Cadastro ")       

    else:
        print("Por Favor, Escolha as Opções [SIM] ou [NÃO]")
        tela_cadastro = input ("Opção Desejada: ")     

def editarProdutos(codigo_produto=None):

    global contador
    print("\n")
    print("_"*55)
    print("\t\tEditar Produto")
    print("-"*55)
    
    if codigo_produto is None:
        print("Antes de Editar os Dados do Produto, Reveja as Informações do Produto.\n")
        print("\033[32m[1] Continuar \033[0m\n\033[31m[0] Voltar \033[0m")
        Verificar_Dados=verificacao("\033[47m\033[30mOpção Desejada: \033[0m",int)

        while Verificar_Dados not in[1,0]:#Verificação de entrada
            print("\t\033[41mERRO\033[0m\n")
            print("\033[32m[1]Visualizar\033[0m\n\033[31m[2]Continuar\033[0m\n[0]Voltar")
            Verificar_Dados=verificacao("\033[47m\033[30mOpção Desejada: \033[0m",int)

        if Verificar_Dados ==0:#Verificar dados ==0 volta para tela inicial do programa
            return
        
        elif Verificar_Dados==1:#Verificar dados ==1 volta para tela de pesquisa do programa
            contador=1
            
    if contador == 1:
        print("\033[32m\n[1]Nome\n[2]Descricao\n[3]Custo Do Produto\n[4]Comissão\n[5]Custo Fixo\n[6]Impostos\n[7]Rentabilidade\n[0]Voltar\033[0m")
        opcao_editar =verificacao("\033[47m\033[30mDigite o Campo Desejado: \033[0m",int)
        
        while opcao_editar not in[1,2,3,4,5,6,7,0]:
            opcao_editar =verificacao ("\033[47m\033[30mDigite o Campo Desejado: \033[0m",int)

        if opcao_editar ==0 :#Condição pra volta pra tela inicial
            return
            
        if codigo_produto is None and opcao_editar!=0:
            codigo_produto = verificacao("\n\033[47m\033[30mDigite o Código do Produto que Deseja Editar: \033[0m", int)    
            listaUnica = tabela_produtos.get(codigo_produto)

            if listaUnica is None:
                print("Nenhum produto encontrado.")
                return
            
        if opcao_editar == 1:
            Campo_Nome = input("Nome desejado: ")
            
            cursor.execute(f"UPDATE produtospi SET nome_produto = '{Campo_Nome}' WHERE codigo_produto = {codigo_produto}")
            cursor.execute("commit")

        elif opcao_editar ==2:
            Campo_Descriçao= input("Descrição Desejada: ")
            Campo_Descriçao = Campo_Descriçao.upper()
            texto_cifrado = criptografia(Campo_Descriçao,alfabeto,chave)
            
            cursor.execute(f"UPDATE produtospi SET descricao_produto = '{texto_cifrado}' WHERE codigo_produto = {codigo_produto}")
            cursor.execute("commit")

        elif opcao_editar ==3:
            Campo_CustoP=float(input("Custo do produto desejado: "))

            cursor.execute(f"UPDATE produtospi SET CP = '{Campo_CustoP}' WHERE codigo_produto = {codigo_produto}")
            cursor.execute("commit")
        
        elif opcao_editar ==4:
            Campo_Comissão=float(input("Comição Desejada: "))
            cursor.execute(f"UPDATE produtospi SET CV = '{Campo_Comissão}' WHERE codigo_produto = {codigo_produto}")
            cursor.execute("commit")

        elif opcao_editar ==5:
            Campo_CustoF=float(input("Custo Fixo Desejado: "))
            cursor.execute(f"UPDATE produtospi SET CF = '{Campo_CustoF}' WHERE codigo_produto = {codigo_produto}")
            cursor.execute("commit")
        
        elif opcao_editar ==6:
            Campo_Imposto=float(input("Impostos Desejado: "))
            cursor.execute(f"UPDATE produtospi SET IV = '{Campo_Imposto}' WHERE codigo_produto = {codigo_produto}")
            cursor.execute("commit")

        elif opcao_editar ==7:
            campoRentabilidade=float(input("Rentabilidade Desejada: "))
            cursor.execute(f"UPDATE produtospi SET ML = '{campoRentabilidade}' WHERE codigo_produto = {codigo_produto}")
            cursor.execute("commit")
        if opcao_editar!=0:
            print("_"*55)
            print("\t   \033[42mAlteração Bem Sucedida\033[0m")
            print("-"*55)   
            print("\033[32m[1]Editar Outro Pedido\033[0m\n[0]Voltar")
            confirmar_editar= verificacao("\033[47m\033[30mOpção Desejada: \033[0m",int)

            if confirmar_editar==1:
                editarProdutos()#Condição ir pro setor de edição

            elif confirmar_editar == 0:
                return 

# Função para apagar produtos
def apagarProdutos(codigo_produto):
    global contador
    
    if contador == 0 and codigo_produto == None:  # Mudança 1: Verificação do código do produto e do contador
        print("\n")
        print("_"*55)
        print("\t\t   Excluir Produto")
        print("-"*55)
        print("Antes de excluir dados da tabela, sugerimos pesquisar primeiro.\n")
        print("\033[31m[1] Continuar\033[0m\n\033[32m[2] Visualizar\033[0m\n[0] Voltar")
        Verificar_Dados = verificacao("\033[47m\033[30mOpção Desejada: \033[0m", int)

        while Verificar_Dados not in [1, 2, 0]:  # Mudança 2: Verificação de entrada
            print("\n\t\033[41mERRO\033[0m\n")
            Verificar_Dados = verificacao("\033[47m\033[30mOpção Desejada: \033[0m", int)

        if Verificar_Dados == 1:
            codigo_produto = verificacao("Digite o código do produto a ser excluído: ", int)
            contador = 1

        elif Verificar_Dados == 2:
            listar_produtos()

        elif Verificar_Dados == 0:
            return

    if contador == 1:
        
        if codigo_produto is not None:
            codigo_produto = verificacao("Digite o código do produto a ser excluído: ", int)     
        cursor.execute(f"SELECT * FROM produtospi WHERE codigo_produto = {codigo_produto}")
        produtos = cursor.fetchone()  #Busca o produto pelo código no Banco de Dados

        if produtos is None:  # Se não houver nenhum produto retornado
            print("_"*55)
            print("\t   \033[41mProduto não encontrado\033[0m")
            print("-"*55)
            return  # Retorna caso o produto não seja encontrado

        cursor.execute(f"DELETE FROM produtospi WHERE codigo_produto = {codigo_produto}")
        cursor.execute("commit")

        print("_"*55)
        print("\t   \033[42mDeletado Com Sucesso\033[0m")
        print("-"*55)
        print("\033[32m[1] Deletar Outro Produto\033[0m\n[0] Voltar")
        confirmar_excluir = verificacao("\033[47m\033[30mOpção Desejada: \033[0m", int)

        while confirmar_excluir not in [1, 0]:
            print("\n\t\033[41mERRO\033[0m\n")
            confirmar_excluir = verificacao("\033[47m\033[30mOpção Desejada: \033[0m", int)

        if confirmar_excluir == 1:
            contador = 1
            codigo_produto = verificacao("Digite o código do produto a ser excluído: ", int)  # Solicita o código do produto
            apagarProdutos(codigo_produto)
            return
        
        else:
            return
            


def telaMenu():
    print("\n")
    print("_"*55)
    print("\t   Programa Controle de Estoque")
    print("-"*55)
    print("\033[32m[1] Classificação de Lucros \033[0m  \n[2] Cadastro de Produto \n\033[33m[3] Alteração de Produtos \033[0m \n\033[31m[4] Exclusão de Produtos\033[0m\n[0] Voltar\n")
    num_tela = verificacao("\033[47m\033[30mEscolha a Opção Desejada: \033[0m", int)
    return num_tela

# Variáveis globais
contador = 0
tabela_produtos = {}
lista_produtos = []
alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' #string alfabeto
chave = [[4, 3], [1, 2]]

# Fluxo principal do programa
num_tela = telaMenu()
while num_tela != 0:
    
    tabela_produtos = buscarProdutos(tabela_produtos)

    while num_tela not in [1, 2, 3, 4]:
        print("Entrada inválida. Por favor, tente novamente.")
        num_tela = verificacao("\033[47m\033[30mEscolha a Opção Desejada: \033[0m", int)

    if num_tela == 1:
        listar_produtos()

    elif num_tela == 2:
        cadastroProdutos(tabela_produtos)

    elif num_tela == 3:
        editarProdutos()

    elif num_tela == 4:
        codigo_produto = None
        apagarProdutos(codigo_produto)

  

    num_tela = telaMenu()

        
cursor.close()
connection.close()