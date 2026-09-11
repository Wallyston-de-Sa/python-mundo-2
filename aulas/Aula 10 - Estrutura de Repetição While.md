# 🐍 Aula 14 — Estrutura de Repetição `while`

Nesta aula, aprendi a utilizar a estrutura de repetição `while` em Python.

O `while` permite repetir um determinado bloco de código **enquanto uma condição for verdadeira**.

Diferente do `for`, que normalmente é utilizado quando sabemos a quantidade de repetições, o `while` é especialmente útil quando a repetição depende de uma condição.

---

## 📚 Estrutura `while`

A estrutura básica é:

```python
while condição:
    # Bloco de código que será repetido
```

Enquanto a condição for verdadeira, o Python continuará executando o bloco.

Quando a condição se tornar falsa, a repetição será encerrada.

---

## 🔄 Exemplo simples

```python
contador = 1

while contador <= 5:
    print(contador)
    contador += 1
```

Resultado:

```text
1
2
3
4
5
```

A cada repetição, o valor de `contador` aumenta.

Quando `contador` passa a ser `6`, a condição:

```python
contador <= 5
```

deixa de ser verdadeira e o `while` termina.

---

## ⚠️ Cuidado com o loop infinito

É importante garantir que a condição do `while` possa se tornar falsa.

Por exemplo:

```python
contador = 1

while contador <= 5:
    print(contador)
```

Nesse caso, `contador` nunca muda.

A condição continuará sendo verdadeira e o programa ficará repetindo o bloco indefinidamente.

Por isso, normalmente precisamos alterar alguma variável dentro do `while`:

```python
contador += 1
```

---

## ⌨️ `while` com entrada de dados

O `while` é muito útil quando queremos continuar solicitando informações até que o usuário forneça uma resposta específica.

Exemplo:

```python
resposta = ''

while resposta != 'S':
    resposta = input('Digite S para continuar: ').upper()
```

O programa continuará perguntando enquanto a resposta for diferente de `S`.

Quando o usuário digitar `S`, a condição deixará de ser verdadeira e o programa continuará sua execução.

---

## 🔢 `while` com números

Também podemos utilizar o `while` para realizar contagens.

```python
numero = 1

while numero <= 10:
    print(numero)
    numero += 1
```

Nesse exemplo, o programa mostra os números de `1` até `10`.

---

## 🔁 Diferença entre `for` e `while`

Os dois podem realizar repetições, mas são utilizados em situações diferentes.

### `for`

É muito útil quando sabemos previamente quantas vezes queremos repetir algo.

```python
for c in range(1, 6):
    print(c)
```

Nesse caso, sabemos que serão realizadas 5 repetições.

### `while`

É mais indicado quando a repetição depende de uma condição.

```python
resposta = ''

while resposta != 'S':
    resposta = input('Deseja continuar? ').upper()
```

Aqui não sabemos quantas vezes o usuário precisará responder até digitar `S`.

---

## 🧠 `while` com condições

Podemos combinar `while` com `if`, `elif` e `else`.

```python
numero = 0

while numero != 5:
    numero = int(input('Digite um número: '))

    if numero < 5:
        print('O número é menor que 5.')
    elif numero > 5:
        print('O número é maior que 5.')
    else:
        print('Você acertou!')
```

Nesse exemplo, o programa continua funcionando até que o usuário digite `5`.

---

## 🎯 Condição de parada

Uma das partes mais importantes ao utilizar `while` é definir uma **condição de parada**.

Exemplo:

```python
while resposta != 'N':
    # Repetição
```

Nesse caso, `N` funciona como uma forma de indicar que o usuário deseja encerrar a repetição.

Esse conceito é muito utilizado em programas que precisam continuar funcionando até que o usuário escolha sair.

---

## 🏨 Aplicação no HotelHub

O `while` será muito útil para o HotelHub porque permitirá criar sistemas que continuam funcionando enquanto o usuário desejar.

Por exemplo, podemos imaginar um menu:

```text
========== HOTELHUB ==========

1 - Cadastrar hóspede
2 - Cadastrar quarto
3 - Fazer reserva
4 - Sair

Escolha uma opção:
```

O programa pode continuar mostrando o menu enquanto o usuário não escolher a opção de saída.

A estrutura poderá seguir uma lógica semelhante a:

```python
opcao = 0

while opcao != 4:
    # Mostrar menu
    # Receber opção
    # Executar ação
```

Com isso, o HotelHub começa a deixar de ser apenas uma sequência de exercícios e passa a se aproximar de um **sistema interativo**.

---

## 💡 O que diferencia o `while`

O `for` normalmente responde à pergunta:

> **"Quantas vezes preciso repetir?"**

Enquanto o `while` responde:

> **"Até quando preciso continuar?"**

Essa diferença ajuda a escolher qual estrutura utilizar em cada situação.

---

## 🎯 O que aprendi

Nesta aula, aprendi:

- Utilizar a estrutura de repetição `while`.
- Criar condições de repetição.
- Criar condições de parada.
- Alterar variáveis durante uma repetição.
- Evitar loops infinitos.
- Utilizar `while` com `input()`.
- Utilizar `while` com `if`, `elif` e `else`.
- Entender a diferença entre `for` e `while`.
- Criar repetições que dependem de uma condição.

---

> **O `while` permite que um programa continue executando uma tarefa enquanto determinada condição for verdadeira.**