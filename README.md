
<!-- TABLE OF CONTENTS -->
## Índice

* [Sobre o Projeto](#Sobre-o-Projeto)
  * [Feito com](#Feito-com)
* [Começando](#Começando)
  * [Pré-Requisitos](#Pré-Requisitos)
  * [Instalação](#instalação)
* [Da Estratégia](#Da-Estratégia)
* [Da Execução](#Da-Execução)
* [Contribuições Futuras](#Contribuições-Futuras)
* [Licensa](#Licensa)
* [Contato](#Contato)
* [Reconhecimentos](#Reconhecimentos)



<!-- ABOUT THE PROJECT -->
## Sobre o Projeto

Este projeto é referente ao desafio para a seleção da empresa ONCASE Intelligence Consulting para a utilização de um Web Crawling e Scraping que deverá colher os dados de quaisquer portais de notícias concorrentes.

O tema de notícias escolhido para este projeto foi "Música". Os sites escolhidos que contém notícias do tema foram:

* [Billboard](https://www.billboard.com/)
* [Fuse](https://www.fuse.tv/)
* [Loudwire](https://loudwire.com/)


### Feito com

* [MongoDB](https://www.mongodb.com/)
* [Scrapy](https://scrapy.org/)


<!-- GETTING STARTED -->
## Começando


### Pré-Requisitos

Para a execução do crawl e scraping, é necessário prosseguir com as seguintes instalações:

### Instalação

1. [MongoDB](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/)
2. Clone o repositório:
```sh
git clone https://github.com/rbbh/Oncase-challenge.git
```
3. Instale os pacotes do arquivo de requirements:
```sh
pip3 install -r requirements.txt
```

<!-- USAGE EXAMPLES -->
## Da Estratégia

O projeto foi todo feito com a utilização de plataformas Open Source com o intuito de ser escalável. O Scrapy foi escolhido pela sua integração com Python e por possuir uma documentação de fácil acesso, explicativa e com uma comunidade relativamente grande que posta tutoriais (todas as referências disponíveis na seção de "Reconhecimentos").

Além disso, para a base de dados, foi escolhido o MongoDB pela praticidade de integração com o Scrapy, já que vários tutoriais (incluindo a própria documentação do Scrapy) os utilizam conjuntamente.

A ideia é que deva-se colher todos os dados relevantes referentes às notícias dos sites. Mas, para um momento inicial, nos contentaremos apenas com os textos (as headlines) de cada notícia dos sites.


## Da Execução

O projeto ainda não se encontra funcional. Vários ajustes devem ser feitos em relação aos códigos de Scraping.

Houve uma dificuldade particular com os formatos dos XPath's. O Scrapy faz a "raspagem" dos dados dos websites através desse tipo de código, que é um código fonte para o formato xml que compõe os websites. 

Após resolvido isso, deverá ser providenciada uma verificação do arquivo de pipeline para a comunicação com a base de dados, já que essa também não se encontra funcional.

Feitas as melhorias necessárias, deverá ser feito um shell script para que o usuário final consiga realizar a estocagem de dados dos três sites de música na base de forma completamente automatizada.



<!-- CONTRIBUTING -->
## Contribuições Futuras

Este Repositório deverá ser feito Público num momento futuro com o aval da On Case, para que haja contribuições da comunidade de desenvolvimento e que, consequentemente, fará o projeto se escalar bem mais rápido.


<!-- LICENSE -->
## Licensa

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contato

LinkedIn: [Rafael Holanda](https://www.linkedin.com/in/rafael-b-holanda) 

E-mail:   holandaraf@gmail.com

Link do Projeto: [https://github.com/rbbh/Oncase-challenge.git](https://github.com/rbbh/Oncase-challenge.git)



<!-- ACKNOWLEDGEMENTS -->
## Reconhecimentos

Gostaria, acima de tudo, de agradecer à On Case pela oportunidade de realizar este desafio. Independente de tudo, aprender sobre a existência dos Web Crawling e Scraping's foi muito prazeroso e, apesar de desafiador, importantíssimo para minha formação como Cientista de Dados.

Além disso, segue as contribuições online que ajudaram a dar um bom norte para o projeto:

* [Blog que levou à escolha dos websites](https://blog.feedspot.com/music_news_websites/)
* [Documentação Oficial do Scrapy](https://doc.scrapy.org/en/latest/index.html)
* [Tutorial Utilizando MongoDB com Scrapy](https://realpython.com/web-scraping-with-scrapy-and-mongodb/)
* [Tutorial Utilizando MongoDB com Scrapy](https://alysivji.github.io/mongodb-pipelines-in-scrapy.html)






