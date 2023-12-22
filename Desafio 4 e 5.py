# Desafio 3 e 4 fazendo conta com dados

n1= int(input('Digite valor: '))
n2= int(input('Outro valor: '))
soma= n1+n2
print('A soma de {}+{} é igual, {}'.format(n1,n2,soma))

# Segundo desafio utilizar cola da aula ex005

a= input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(a))
print('È uma letra maíuscula?' , a.isupper())
print('È uma letra minuscula?' , a.islower())
print('É alfa númerico?' , a.isalnum())
print('Tem somente letras?' , a.isalpha())
print('Foi digitado somente numeral?' , a.isnumeric())
