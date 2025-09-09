##ATV 3 e ATV 5
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        
    def get_marca(self):
        return self.marca

    def set_marca(self, nova_marca):
        self.marca = nova_marca
    
    def modelo(self):
        return self.__modelo

    def set_modelo(self, novo_modelo):
        self.modelo = novo_modelo
    
    def ano(self):
        return self.__ano

    def set_ano(self, novo_ano):
        self.ano = novo_ano
    
    def apresentar (self):
        print(f"Carro da Marca {self.marca} do modelo {self.modelo} e ano {self.ano}")
        
carro1 = Carro("Toyota", "Corolla", 2020)
carro2 = Carro("Honda", "Civic", 2022)
carro3 = Carro("Ford", "Mustang", 2023)

carro1.apresentar()
carro2.apresentar()
carro3.apresentar()

print("Alterando o Carro 1")
carro1.set_marca("BMW")
carro1.set_ano(2025)

carro1.apresentar()