#camelCase snake_case PascalCase
#quando a bolinha tá branca é pq não tá salvo (apertar ctrl s p salvar)
#nome = ["Ryanne", "Gabriel", "Suzy"]

# print(nome[1]) 
# if(type(input("coloque o primeiro numero da calculadora")) == str):
#     print("por favor, coloque um numero e nao um texto")
# primeiro_valor = int(input("primeiro_valor"))
# segundo_valor = int(input("segundo_valor"))
# calculo = primeiro_valor * segundo_valor
# print(calculo)
idade = int(input('Digite sua idade: '))
if idade >= 10 and idade < 20:
    print('Você é adolescente')
elif idade >= 20 and idade < 30:
    print('Você é jovem')
elif idade >= 30 and idade <= 100:
    print('Você é adulto')
else:
    print('Valor não encontrado!')
