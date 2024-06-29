# ProjetoIntegrador:Controle de Estoque

Resumo:

Este projeto desenvolve um programa em Python para calcular o preço de venda de produtos com base em dados armazenados em um banco de dados Oracle. O programa realiza operações de criptografia e descriptografia nas descrições dos produtos, calcula diversos parâmetros financeiros e permite a manipulação dos registros de produtos.

Sumário
1.	Introdução
2.	Instalação
3.	Uso
4.	Funcionalidades
5.	Contribuição
6.	Licença

Introdução

Este projeto foi desenvolvido com o intuito de facilitar o cálculo do preço de venda de produtos, considerando custos fixos, variáveis, impostos e rentabilidade esperada. Utiliza um banco de dados Oracle para armazenar e gerenciar os dados dos produtos, e implementa criptografia nas descrições dos produtos para garantir a segurança das informações.

Instalação:

Pré-requisitos
•	Python 3.x
•	Biblioteca oracledb
•	Banco de dados Oracle
Passos para instalação
1.	Clone o repositório:
git clone https://github.com/christianlf/ProjetoIntegrador.git
2.	Navegue até o diretório do projeto:
cd ProjetoIntegrador
3.	Instale as dependências necessárias:
pip install oracledb
4.	Configure a conexão com o banco de dados Oracle no código:
python
connection = oracledb.connect(
    user="seu_usuario",
    password="sua_senha",
    dsn="seu_dsn"
)

Uso:

Para executar o programa, basta rodar o arquivo principal:
python nome_do_arquivo.py

O programa oferece um menu interativo para cadastro, edição, exclusão e listagem de produtos, além de calcular o preço de venda e exibir informações detalhadas dos produtos.

Funcionalidades:
•	Cadastro de Produtos: Permite cadastrar novos produtos no banco de dados.
•	Listagem de Produtos: Exibe um ou todos os produtos cadastrados.
•	Edição de Produtos: Permite editar informações dos produtos cadastrados.
•	Exclusão de Produtos: Remove produtos do banco de dados.
•	Cálculo de Preço de Venda: Calcula o preço de venda com base nos custos e margens informadas.
•	Criptografia e Descriptografia: Criptografa e descriptografa a descrição dos produtos para garantir segurança.

Contribuição:

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

Passos para contribuir
1.	Faça um fork do projeto.
2.	Crie uma branch para sua feature (git checkout -b feature/sua-feature).
3.	Commit suas alterações (git commit -m 'Adiciona nova feature').
4.	Faça push para a branch (git push origin feature/sua-feature).
5.	Abra um Pull Request.
Licença:
Este projeto está licenciado sob a MIT License.

Autor:
Nome - https://www.linkedin.com/in/christian-lindoso-froz
Email: christianlindoso18@gmail.com
