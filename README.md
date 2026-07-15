# Sistema de Gerenciamento e Simulação de Poços de Petróleo

Este repositório apresenta o desenvolvimento de um sistema de gerenciamento e simulação de poços de petróleo em Python. A aplicação permite o cadastro de poços, autenticação de operadores, controle da produção, transferência de volume entre poços, previsão de declínio da produção e gerenciamento administrativo.

A implementação deste projeto foi baseada em um projeto anterior cujo tema era um sistema bancário, reaproveitando sua estrutura principal e adaptando a lógica de negócio para o contexto da indústria do petróleo. Durante esse processo, foram modificados os modelos de dados, as operações do sistema e as regras de funcionamento para representar um ambiente simplificado de gestão de poços de produção.

---

## Funcionalidades

O sistema possui dois níveis de acesso:

### 1. Engenheiro de Campo

* Autenticação por ID do poço e senha;
* Consulta das informações do próprio poço;
* Registro da produção diária;
* Transferência de volume entre poços;
* Simulação da previsão de declínio da produção (DCA);
* Logoff.

### 2. Gerente de Produção

* Relatório geral dos poços cadastrados;
* Descomissionamento (remoção) de poços;
* Logoff.

Além dessas operações, o sistema permite o cadastro de novos poços e permanece em execução até que o usuário escolha encerrar o programa.

---

## Organização do Código

| Arquivo      | Responsabilidade                                   |
| ------------ | -------------------------------------------------- |
| `main.py`    | Controla o fluxo do programa e os menus.           |
| `sistema.py` | Implementa toda a lógica das operações do sistema. |
| `poco.py`    | Define a classe `Poco` e seus atributos.           |

---

## Modelo de Dados

Cada poço é representado por um objeto contendo:

* ID do poço;
* Campo de produção;
* Taxa anual de declínio;
* Senha do operador;
* Produção acumulada (bbl).

Os poços são armazenados em uma lista utilizada como banco de dados em memória durante a execução do programa.

---

## Lógica Implementada

### Registro de Produção

A produção diária registrada pelo operador é adicionada à produção acumulada do poço.

```text
Produção acumulada = Produção atual + Produção diária
```

### Fluxo de Escoamento

O sistema permite a transferência de barris entre poços cadastrados, verificando previamente a existência do poço de destino e a disponibilidade de volume para a operação.

```text
Origem = Origem - Volume transferido
Destino = Destino + Volume transferido
```

### Previsão de Declínio

A estimativa da produção futura utiliza o modelo de declínio exponencial:

 ```text
P = P0 × (1 - d)^t
```

Onde:

* **P** = produção estimada;
* **P₀** = produção atual;
* **d** = taxa anual de declínio;
* **t** = tempo em anos.

A aplicação calcula automaticamente a previsão de produção para os cinco anos seguintes.

---

## Conceitos Aplicados

* Programação Orientada a Objetos (POO);
* Modularização do código;
* Manipulação de listas;
* Estruturas condicionais e de repetição;
* Tratamento de exceções (`try` / `except`);
* Validação de entradas do usuário.
