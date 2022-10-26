# comando input(): quero permitir que 
# o usuário digite algo...
nome = input("Digite seu nome: ")
#pede a idade para o usario "Qual sua idade
idade = int(input("Digite sua idade: "))

#comando de saída..exibir na tela
print(f"Boa noite, seu nome é {nome}")
#exiba "Sua idade é..."
print("Sua idadee é {}".format(idade))

#e se eu quisesse mostrar o DOBRO da idade informada?
dobro = idade * 2
print("O dobro da idade informada é {}".format(dobro))

#Estrutura condicional - o famoso "SE" (if)
#Se a pessoa for maior de idade, mostre "Você é maior de idade, ótimo! Já pode beber ou dirigir"
if idade >= 18:
  print("Você é maior de idade, ótimo! Já pode beber ou dirigir")
