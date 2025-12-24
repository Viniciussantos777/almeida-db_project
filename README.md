# almeida-db_project
This is a project made by Vinicius_Santos

## What is it?
Almeida_DB_project is a database management application built with Python and SQLite, designed to query, manage, and analyze data using SQL.

## Why are you doing this?
Because I'm currently doing a course about Data-Bases and to improve my experiences with this tecnology is needed a project about this topic.

## What is needed to play this project?
Python - 3.13.9 is currently been used by me
SQLite - Is integrated with python

### Obs:
I used SQLite because is more light and do not need a servidor in a small project like this.

*Missão do Projeto:*

> Desenvolver um sistema de banco de dados relacional voltado à análise energética de cidades globais, com foco em eficiência, sustentabilidade e tomada de decisões estratégicas.

---

*Objetivo (motivo):*

> Construir um *banco de dados relacional capaz de consolidar, organizar e permitir consultas eficientes* sobre consumo energético, fontes utilizadas, impacto ambiental e investimentos em infraestrutura de diversas cidades do mundo.

> Esse banco será usado para:
> - *Analisar padrões de consumo* por tipo de energia e região;
> - *Comparar cidades* em termos de eficiência energética e uso de renováveis;
> - Facilitar a criação de *dashboards e análises preditivas* no futuro.

---

*Motivo técnico:*
> O arquivo CSV atual não permite integrações, consultas SQL otimizadas ou estruturação adequada das relações entre entidades como *cidade*, *fonte de energia* e *ano de análise*.  
> Com um *modelo relacional bem estruturado*, poderá:
> - Evitar redundância de dados (normalização),
> - Permitir atualizações mais seguras,
> - Fazer análises cruzadas mais eficazes (ex: consumo × clima × indústria),
> - Escalar o sistema com facilidade no futuro (novas cidades, anos, indicadores).

---
22/12/2025

| Tabela            | PK                       | FKs                    | Atributos                     |
| ----------------- | ------------------------ | ---------------------- | ----------------------------- |
| cidade            | id_city                  | -                      | nome, pais                    |
| Ano_cidade        | id_city_ano              | id_city                | ano (2015,2016, ect)          |
| matriz_energetica | id_matriz                | -                      | nome (solar, nuclear ect.)    |
| Dados             | (id_city_ano, id_matriz) | id_city_ano, id_matriz | consumo, custo_unitario, etc. |

Utilizando https://app.diagrams.net/ como software para desenhar diagramas do banco de dados!

23/12/2025 - 
Durante meus estudos decido fazer um banco de dados do Modelo Entidade Relacional, dessa forma termino com 6 entidades que podem ser usadas para filtrar o query dentro do banco de dados. Mas percebo que a base de dados possuem valores duplicados, dessa forma preciso descobrir uma forma de filtrá-los de forma que não gere duplicidade de dados em meio aos cálculos dando crash no sistema...

| Tabela            | PK                       | FKs                    | Atributos                     |
| ----------------- | ------------------------ | ---------------------- | ----------------------------- |
| cidade            | id_city                  | -                      | nome, pais                    |
| Ano_cidade        | id_city_ano              | id_city                | ano (2015,2016, ect)          |
| matriz_energetica | id_matriz                | -                      | nome (solar, nuclear ect.)    |
| Industria         | id_industria             | id_city, id_matriz     | nome (Agro, financeiro etc.)  |
| Dados             | (id_city_ano, id_matriz) | id_city_ano, id_matriz | consumo, custo_unitario, etc. |

Fases de desenvolvimento de um banco de dados em suas fases iniciais:

    1)Contextualização (Delimitar o que o sistema fará e, principalmente, o que ele não fará.);

    2)Objetivação (O que se espera obter com esses dados? Quais perguntas o banco deve ser capaz de responder?);

    3)Intitulação (Dar nomes padronizados aos objetos do banco);

    4)Especificação de Requisitos (Levantamento técnico de quais dados precisam ser armazenados e quais as restrições que devem ser aplicadas a eles);

    5)Normalização (Aplicação de regras matemáticas e lógicas para evitar a redundância);

    6)Modelagem (Criação das representações visuais dos dados.);

    7)Trigramação (Técnica específica de padronização onde se utilizam prefixos ou sufixos de três letras [trigramas] para identificar a que grupo ou tabela um atributo pertence.);

    8)Dicionarização (Criação do Dicionário de Dados);

    9)Auditoria das fases de Análise e de Projeto Lógico do Sistema de Banco de Dados (Revisão e controle de qualidade. Antes de partir para a implementação física).


Pesquisar:
Dependência funcional
Dependência funcional total
Dependência funcional parcial