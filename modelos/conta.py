class Conta:
    contas = []
    _id_counter = 0
    
    def __init__(self, nome, conta, categoria,):
        self._nome = nome
        self._conta = conta 
        self._categoria = categoria
        Conta._id_counter += 1
        self._id = Conta._id_counter
        self._saldo = 0
        Conta.contas.append(self)        
        
        
    def mostrar_info(self):
        print(f"Nome: {self._nome}")
        print(f"Conta: {self._conta}")
        print(f"Categoria: {self._categoria}")
        print(f"ID:{self._id}")
        print(f"Saldo: {self._saldo:.2f}")
    
    @classmethod
    def listar_contas(cls):
        print("LISTAS DE CONTAS CADASTRADAS: ")
        print(" ")
        print(f"{"Nome da Conta".ljust(25)} | {"Categoria".ljust(25)} | {"Conta".ljust(25)} | {"ID".ljust(25)}")
        print("-" * 100)
        
        for contas in cls.contas:
            print(f"{contas._nome.ljust(25)} | {contas._categoria.ljust(25)} | {contas._conta.ljust(25)} | {str(contas._id).ljust(25)} ")
            
    @classmethod
    def buscar_id(cls, id_procurado):
        for conta in cls.contas:  
            if conta._id == id_procurado: 
               return conta  
           
        return None  
   
   
              