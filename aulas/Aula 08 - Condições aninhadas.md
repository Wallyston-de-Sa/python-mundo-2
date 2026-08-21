# 🐍 Aula 08 — Condições Aninhadas

Nesta aula, aprendi a utilizar **estruturas condicionais** para criar programas capazes de tomar diferentes decisões de acordo com as condições estabelecidas.

As estruturas condicionais permitem controlar o caminho que o programa seguirá.

---

## 📚 Estrutura `if` e `else`

A estrutura mais simples é:

```python
if condição:
    # Executado se a condição for verdadeira
else:
    # Executado se a condição for falsa
```

O bloco `if` será executado quando a condição for verdadeira. Caso contrário, o bloco `else` será executado.

---

## 🔀 Condições Aninhadas

Quando um programa precisa analisar mais de duas possibilidades, podemos utilizar o `elif`.

```python
if condição1:
    # Executa se a condição1 for verdadeira
elif condição2:
    # Executa se a condição2 for verdadeira
else:
    # Executa caso nenhuma condição anterior seja verdadeira
```

A estrutura segue uma sequência de verificações:

```text
if
↓
elif
↓
elif
↓
else
```

O Python verifica as condições na ordem em que foram escritas. Quando encontra uma condição verdadeira, executa aquele bloco e não continua verificando os próximos `elif` ou `else`.

---

## 🧠 Exemplo

```python
nome = input('Qual é o seu nome? ')

if nome == 'Wallyston':
    print('Que nome bonito!')
elif nome == 'Maria' or nome == 'João':
    print('Seu nome é bastante popular!')
elif nome in ('Ana', 'Carla', 'Fernanda'):
    print('Belo nome!')
else:
    print('Seu nome é normal.')
```

Nesse exemplo, o programa analisa diferentes possibilidades para o nome informado.

---

## 🔗 Operadores Lógicos

Durante as condições, podemos utilizar operadores para combinar ou verificar diferentes possibilidades.

### `or`

O operador `or` retorna verdadeiro quando pelo menos uma das condições é verdadeira.

```python
if nome == 'João' or nome == 'Maria':
    print('Nome encontrado!')
```

Também pode ser escrito de forma mais organizada:

```python
if nome in ('João', 'Maria'):
    print('Nome encontrado!')
```

---

## 🔍 Operador `in`

O operador `in` verifica se determinado valor está presente em uma sequência.

```python
if nome in ('Ana', 'Maria', 'Carla'):
    print('Nome encontrado!')
```

Nesse caso, o programa verifica se a variável `nome` corresponde a algum dos valores da sequência.

---

## ⚠️ Importância da ordem das condições

A ordem das condições é importante.

```python
idade = int(input('Digite sua idade: '))

if idade >= 18:
    print('Maior de idade.')
elif idade >= 65:
    print('Idoso.')
else:
    print('Menor de idade.')
```

Nesse exemplo existe um problema: uma pessoa com 70 anos também possui idade maior que 18. Como a primeira condição já é verdadeira, o Python não chega ao `elif`.

Uma forma correta seria:

```python
if idade >= 65:
    print('Idoso.')
elif idade >= 18:
    print('Maior de idade.')
else:
    print('Menor de idade.')
```

Por isso, é importante pensar na ordem das verificações.

---

## 🎨 Condições e cores

As condições também podem ser utilizadas junto com cores no terminal para melhorar a apresentação das respostas.

```python
cores = {
    'limpa': '\033[m',
    'verde': '\033[32m',
    'vermelho': '\033[31m'
}

idade = int(input('Digite sua idade: '))

if idade >= 18:
    print('{}Acesso permitido!{}'.format(
        cores['verde'],
        cores['limpa']
    ))
else:
    print('{}Acesso não permitido!{}'.format(
        cores['vermelho'],
        cores['limpa']
    ))
```

Nesse exemplo:

- 🟢 Verde representa uma situação positiva ou permitida.
- 🔴 Vermelho representa uma situação negativa ou não permitida.

---

## 🏨 Aplicação no HotelHub

As condições aninhadas podem ser utilizadas para que o HotelHub tome decisões diferentes de acordo com as informações fornecidas.

Por exemplo:

```text
Quarto disponível?
│
├── Sim
│   └── Reserva liberada
│
└── Não
    └── Reserva indisponível
```

Com o avanço dos estudos, essa lógica permitirá criar funcionalidades mais completas e interativas para o projeto.

---

## 🎯 O que aprendi

Nesta aula, aprendi:

- Utilizar estruturas condicionais.
- Trabalhar com `if`.
- Trabalhar com `elif`.
- Trabalhar com `else`.
- Criar condições com diferentes possibilidades.
- Entender como o Python verifica as condições.
- Compreender a importância da ordem das condições.
- Utilizar o operador lógico `or`.
- Utilizar o operador `in`.
- Criar programas capazes de tomar decisões diferentes conforme os dados recebidos.

---

> **Condições permitem que um programa analise situações e escolha diferentes caminhos para sua execução.**