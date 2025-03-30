* Projeto de Consulta de Operadoras de Planos de Saúde

Este projeto tem como objetivo criar uma aplicação completa para consulta de operadoras de planos de saúde, permitindo que os usuários visualizem informações detalhadas sobre as operadoras, 
como CNPJ, Razão Social, e Registro ANS. O sistema é composto por um backend em Python (usando o framework Flask), um banco de dados MySQL e um frontend desenvolvido com Vue.js. 
A aplicação faz consultas em uma base de dados que foi inicialmente populada a partir de arquivos CSV.


> Criação e Configuração do Banco de Dados MySQL

Para armazenar os dados importados dos arquivos CSV, foi criado um banco de dados MySQL. Nele, foi configurada a tabela demonstracoes_contabeis, que passou a armazenar os dados
das operadoras, e uma tabela operadoras_ativas, que contém informações sobre as operadoras de planos de saúde ativas.
Foram criadas queries analíticas para responder a perguntas importantes sobre as operadoras, como:

Quais as operadoras com maiores despesas no último trimestre?

Quais as operadoras com maiores despesas no último ano?

Essas queries foram executadas e ajustadas conforme a necessidade.


> Desenvolvimento do Servidor Backend em Python

Em seguida, foi criado um servidor em Python utilizando o framework Flask. O servidor foi configurado para fornecer rotas de API para realizar consultas ao banco de dados MySQL.
Foi criada uma rota para listar os CNPJs das operadoras e outra para retornar dados completos sobre a operadora, como Registro ANS, CNPJ e Razão Social.

O servidor Flask interage diretamente com o banco de dados MySQL para realizar as consultas e retornar os resultados desejados no formato JSON.


> Criação da Interface Web com Vue.js

Para a interface do usuário, foi utilizado Vue.js, um framework JavaScript que facilita a criação de interfaces web interativas. A interface foi projetada para permitir ao usuário 
visualizar a lista de operadoras de planos de saúde e buscar operadoras através de um botão que dispara uma requisição ao servidor Python e exibe os dados no navegador.
Foi criada uma estrutura simples de componentes Vue, onde a ListaOperadoras.vue exibe os resultados das consultas feitas ao servidor, 
e a App.vue serve como o ponto de entrada da aplicação.


> Integração Frontend e Backend


A comunicação entre o frontend e o backend foi realizada utilizando Axios, biblioteca que facilita a realização de requisições HTTP no Vue.js.
A partir do frontend, foi enviado um pedido ao servidor Python para buscar os dados das operadoras, que foram então exibidos na interface web.


> Desenvolvimento e Testes com o Postman

Após a implementação da interface e do servidor, foi criada uma coleção no Postman para testar as APIs. O Postman foi utilizado para verificar se o servidor estava
respondendo corretamente às requisições, garantindo que os dados retornados estivessem corretos.
Foram feitas requisições GET para verificar se o servidor Python estava retornando as operadoras de forma correta e se a busca por operadoras específicas estava funcionando adequadamente.








