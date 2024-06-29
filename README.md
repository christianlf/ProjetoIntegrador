

# ProjetoIntegrador: Controle de Estoque

## Resumo

Este projeto desenvolve um programa em Python para calcular o preço de venda de produtos com base em dados armazenados em um banco de dados Oracle. O programa realiza operações de criptografia e descriptografia nas descrições dos produtos, calcula diversos parâmetros financeiros e permite a manipulação dos registros de produtos.

## Sumário

- Introdução
- Instalação
- Uso
- Funcionalidades
- Contribuição
- Licença

## Introdução

Este projeto foi desenvolvido com o intuito de facilitar o cálculo do preço de venda de produtos, considerando custos fixos, variáveis, impostos e rentabilidade estimada. Utiliza um banco de dados Oracle para armazenar e gerenciar os dados dos produtos e implementa criptografia nas descrições dos produtos para garantir a segurança das informações.

## Instalação

### Pré-requisitos
- Python 3.x
- Biblioteca oracledb
- Banco de dados Oracle

### Passos para instalação

Clone o repositório:

```bash
git clone https://github.com/christianlf/ProjetoIntegrador.git
cd ProjetoIntegrador

## Instale as dependências necessárias:
pip install oracledb
##Configure a conexão com o banco de dados Oracle no código:
import oracledb

connection = oracledb.connect(
    user="seu_usuario",
    password="sua_senha",
    dsn="seu_dsn"
)
## Uso:

Para executar o programa, basta rodar o arquivo principal:
python nome_do_arquivo.py


O programa oferece um menu interativo para cadastro, edição, exclusão e listagem de produtos, além de calcular o preço de venda e exibir informações detalhadas dos produtos.

Funcionalidades
Cadastro de Produtos: Permite cadastrar novos produtos no banco de dados.
Listagem de Produtos: Exibe um ou todos os produtos cadastrados.
Edição de Produtos: Permite editar informações dos produtos cadastrados.
Exclusão de Produtos: Remove produtos do banco de dados.
Cálculo de Preço de Venda: Calcula o preço de venda com base nos custos e margens informadas.
Criptografia e Descriptografia: Criptografa e descriptografa a descrição dos produtos para garantir segurança.
Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

##  Passos para contribuir:

Faça um fork do projeto.
Crie uma branch para sua feature (git checkout -b feature/sua-feature).
Commit suas alterações (git commit -m 'Adiciona nova feature').
Faça push para a branch (git push origin feature/sua-feature).
Abra um Pull Request.

## Licença:
Este projeto está licenciado sob a MIT License.

## Autor
Nome - https://www.linkedin.com/in/christian-lindoso-froz
Email: christianlindoso18@gmail.com




