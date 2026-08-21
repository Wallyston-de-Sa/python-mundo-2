# 🐍 Aula 09 — Estrutura de Repetição `for`

Nesta aula, aprendi a utilizar a estrutura de repetição `for` em Python.

As estruturas de repetição permitem executar um mesmo bloco de código várias vezes, evitando a necessidade de repetir manualmente as mesmas instruções.

---

## 📚 Estrutura de Repetição

Uma estrutura de repetição é utilizada quando precisamos executar uma ação mais de uma vez.

Com o `for`, podemos controlar quantas vezes determinado bloco será repetido.

A estrutura básica é:

```python
for variável in sequência:
    # Bloco que será repetido
```

O Python percorre cada elemento da sequência e executa o bloco de código.

---

## 🔢 Utilizando `range()`

Uma das formas mais utilizadas com `for` é através da função `range()`.

Exemplo:

```python
for contador in range(1, 6):
    print(contador)
```

Resultado:

```text
1
2
3
4
5
```

Nesse exemplo, o Python executa o bloco de código cinco vezes.

O valor final informado no `range()` não é incluído.

---

## 🧠 Funcionamento do `range()`

Podemos utilizar o `range()` de diferentes formas.

### Apenas o valor final

```python
for contador in range(5):
    print(contador)
```

Resultado:

```text
0
1
2
3
4
```

Quando utilizamos apenas um valor, a contagem começa em `0`.

---

### Valor inicial e valor final

```python
for contador in range(1, 6):
    print(contador)
```

A contagem começa em `1` e termina antes de `6`.

---

### Valor inicial, final e passo

Também podemos definir o intervalo entre cada número.

```python
for contador in range(0, 10, 2):
    print(contador)
```

Resultado:

```text
0
2
4
6
8
```

Nesse caso, o terceiro valor representa o passo da contagem.

---

## ⏪ Contagem regressiva

Também podemos utilizar valores negativos para fazer uma contagem regressiva.

```python
for contador in range(10, 0, -1):
    print(contador)
```

Resultado:

```text
10
9
8
7
6
5
4
3
2
1
```

O `-1` representa que a contagem será reduzida de um em um.

---

## 🔁 Repetindo uma ação

O `for` também pode ser utilizado para repetir qualquer tipo de ação.

```python
for contador in range(1, 4):
    print('Estudando Python!')
```

Resultado:

```text
Estudando Python!
Estudando Python!
Estudando Python!
```

O programa executa o `print()` três vezes.

---

## ⌨️ Entrada de dados dentro do `for`

Também podemos solicitar informações ao usuário durante uma repetição.

```python
for contador in range(1, 4):
    nome = input('Digite um nome: ')
    print('Olá, {}!'.format(nome))
```

Nesse exemplo, o programa solicita três nomes.

Cada repetição executa novamente o `input()` e o `print()`.

---

## 🔢 Utilizando o contador

A variável utilizada no `for` pode representar a posição ou quantidade atual da repetição.

```python
for contador in range(1, 6):
    print('Esta é a repetição número {}.'.format(contador))
```

Resultado:

```text
Esta é a repetição número 1.
Esta é a repetição número 2.
Esta é a repetição número 3.
Esta é a repetição número 4.
Esta é a repetição número 5.
```

---

## 🏨 Aplicação no HotelHub

A estrutura `for` poderá ser utilizada no HotelHub para repetir determinadas ações.

Por exemplo, cadastrar vários hóspedes:

```python
for contador in range(1, 4):
    nome = input('Nome do hóspede: ')
    print('Hóspede {} cadastrado.'.format(nome))
```

Nesse caso, o programa permite repetir o cadastro de hóspedes três vezes.

Com novos conhecimentos, essa estrutura poderá ser combinada com outras funcionalidades para tornar o HotelHub mais dinâmico.

---

## 🎯 O que aprendi

Nesta aula, aprendi:

- Utilizar a estrutura de repetição `for`.
- Repetir blocos de código.
- Utilizar a função `range()`.
- Definir valores iniciais e finais.
- Definir o passo da repetição.
- Criar contagens progressivas.
- Criar contagens regressivas.
- Repetir ações determinadas vezes.
- Utilizar entradas de dados dentro de uma repetição.
- Utilizar o contador durante a execução do programa.

---

> **A estrutura `for` permite repetir ações de forma controlada, tornando o código mais organizado e evitando repetições desnecessárias.**