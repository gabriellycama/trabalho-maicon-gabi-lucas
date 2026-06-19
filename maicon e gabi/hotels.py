class Hotel:
    def __init__(self, hotel, quarto, numero, valor_diaria,):
        self.__hotel = hotel         
        self.__quarto = quarto        
        self.__numero = numero        
        self.__valor_diaria = valor_diaria
        self.__total_pago = 0         
        self.__noites_reservadas = 0
    def exibir_conta(self):
       print(f"--- Extrato - {self.__hotel} ---")   
       print(f"Quarto: {self.__numero} {self.__quarto}")
       print(f"Total de noites escolhidas: {self.__noites_reservadas} noite")    
       print(f"Total acumulado a pagar: {self.__total_pago:.2f}")

    def reservar_noites(self, quantidade_noites):
        if quantidade_noites <= 0:
            print("Quantidade de noites inválida!")
        else:
            custo = quantidade_noites * self.__valor_diaria
            self.__total_pago += custo
            self.__noites_reservadas += quantidade_noites 
            print(f"{quantidade_noites} noite reservada com sucesso!")


    def verificar_disponibilidade(self):
        if self.__numero <= 55:
            return (f"O quarto {self.__numero} esta disponivel.")
        else:
            return (f"O quarto {self.__numero} esta ocupado no momento.")
        
    @property
    def hotel(self):
        return self.__hotel