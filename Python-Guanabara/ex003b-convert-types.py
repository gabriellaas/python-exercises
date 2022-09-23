# conversão de tipos dentro de um determinado input:
# boolean: se estiver vazio = False, se preenchido = True
m = bool(input('Digite um valor: '))
print(m)

# input já é uma string, mas caso necessário:
n = str(input('Digite um valor: '))
print(n)

# float
o = float(input('Digite um valor: '))
print(o)

# int
p = int(input('Digite um valor: '))
print(p)

# para saber o tipo da variável, usar type:
q = int(input('Digite um valor: '))
print(type(q))

# para saber se a variável é tal coisa, usar variavel.is...:
# isalpha = é letra? / isnumeric = é número? / isalnum = é número e/ou letra?
# isupper = está tudo em caixa alta?
r = input('Digite algo: ')
print(r.isalpha())
print(r.isnumeric())
print(r.isalnum())
print(r.isupper())
