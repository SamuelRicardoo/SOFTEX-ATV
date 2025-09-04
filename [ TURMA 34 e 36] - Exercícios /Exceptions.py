def atv1():
    try:
        number = int(input("Digite um valor: "))
    except ValueError:
        print("Erro: Você precisa digitar um número válido!")

def atv2():
    try:
        number1 = int(input("Digite o primeiro valor: "))
        number2 = int(input("Digite o segundo valor: "))

        div = number1 * number2
        print(f"O Valor dividido: {div}")
        
    except ValueError:
        print("Erro: Você precisa digitar um número válido!")
  
def atv3():
    try:
        number = int(input("Digite um número inteiro: "))
    except ValueError:
        print("Erro: Você não digitou um número inteiro válido!")
    else:
        print(f"Você digitou o número {number} corretamente!")

def atv4():
    try:
        arq = open("auxiliar/dados.txt")
        print(arq.read())
    except FileNotFoundError:
        print("Erro: O arquivo 'dados.txt' não foi encontrado!")
    finally:
        arq.close()
        print("Encerrando programa")

def atv5():
    
    def div(number1, number2):
        
        if(number2 == 0):
            raise ZeroDivisionError("Erro: Divizor ZERO")
        
        return number1 / number2
    
    try:    
        number1 = int(input("Digite o primeiro valor: "))
        number2 = int(input("Digite o segundo valor: "))
        print(div(number1, number2))
    
    except ZeroDivisionError as e:
        print("Erro: ", e)
   
def atv6():        
    class IdadeInvalidaError(Exception):
        pass 
    
    def cadastrar_idade(age):
        if age <= 0: raise IdadeInvalidaError("Erro: Idade Invalida")
    
    try:    
        age = int(input("Digite a sua idade: "))
        cadastrar_idade(age)
    except IdadeInvalidaError as e:
        print("Erro: ", e)

def atv7():
    try:
        number1 = int(input("Digite o primeiro valor: "))
        number2 = int(input("Digite o segundo valor: "))

        div = number1 / number2
        print(f"O Valor dividido: {div}")
        
    except ZeroDivisionError:
        print("Erro: Divizor ZERO")
    except ValueError:
        print("Erro: Você precisa digitar um número válido!")

def atv8():
    try:
        complete=""
        number1 = int(input("Digite um valor inteiro: "))
    except ValueError:
        print("Erro: Você não digitou um número inteiro válido!")
    else:
        if (number1 % 2 == 0):
            complete = "PAR"
        else:
            complete = "IMPAR"
            
        print(f"O numero {number1} é {complete}")
    finally:
        print("Fim do programa")
 
def atv9():
    class SaldoInsuficienteError(Exception):
        pass 
    
    class SaqueInsuficienteError(Exception):
        pass 
    
    def sacar(saldo, saque):
                
        if(saque > saldo): raise SaldoInsuficienteError("Erro: O Saque é maior que o valor")

        if(saque <= 0) : raise SaqueInsuficienteError("Erro: O Seu saque precisa ser maior que 0")
        
        return  saldo - saque
        
    try:
        saldo = int(input("Digite o Valor do seu Saldo"))
        saque = int(input("Digite o valor do seu Saque: "))
        
        aux = sacar(saldo,saque)
        saldo = aux
        print(f"Seu novo saldo é: {saldo} R$ ")
        
    except ValueError:
        print("Erro: Você precisa digitar um número válido!")

    except SaldoInsuficienteError as e:
        print("Erro: ", e)
    except SaqueInsuficienteError as e:
        print("Erro: ", e)  
 
    
#atv1()
#atv2()
#atv3()
atv4()
atv5()
atv6()
atv7()
atv8()
atv9()