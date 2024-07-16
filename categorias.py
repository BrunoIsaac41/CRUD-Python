class Categorias():
    def __init__(self, cpf : int, codigo: str, nome: str, categoria:str) :
        self.cpf = cpf
        self.codigo= codigo
        self.nome = nome
        self.categoria = categoria
        self.CriarDicionario()
        
        
        

    def CriarDicionario (self):
        self.dicio = {"Categoria": self.categoria,
                           "Nome": self.nome,
                           "Codigo": self.codigo,
                        "CPF": self.cpf}
        
                        
        return self.dicio
    


#Objeto Professor    
class Professores(Categorias): 
    def __init__(self, categoria:"Professores", cpf : int, codigo: str, nome: str):
        super().__init__(cpf, codigo, nome, categoria)
        self.dicio
        
    def CriarDicionario(self):
        return super().CriarDicionario()


#Objeto Estudantes    
class Estudantes(Categorias):
    def __init__(self,categoria :"Estudantes" ,cpf : int, codigo: str, nome: str):
        super().__init__(cpf,codigo,nome,categoria)
        
    def CriarDicionario(self):
        return super().CriarDicionario()
        


  
class Diciplinas(Categorias):
    def __init__(self,categoria: "Diciplinas", semestre : int, nome: str , codigo: str , cpf = ""):
        self.semestre = semestre
        super().__init__(cpf, codigo, nome, categoria)
        

    def CriarDicionario(self):
        super().CriarDicionario()
        self.dicio["Semestre"]= self.semestre
        del self.dicio["CPF"]
        
        
        
class Turmas(Categorias):
    def __init__(self,categoria : "Turmas", nome: str, qtdAlunos : int, codigo: str, cpf = "" ):
        self.qtdAlunos = qtdAlunos
        super().__init__(cpf,codigo,nome,categoria)
        
    
        
    def CriarDicionario(self):
        super().CriarDicionario()
        self.dicio["Qtd Alunos"]= self.qtdAlunos
        del self.dicio["CPF"]
        

class Matriculas(Categorias):
    def __init__(self , codigo : str  ,nome : str , categoria : "Matriculas" , cpf : int , data :  str, prazo : str):
       self.data = data
       self.prazo = prazo
       super().__init__(cpf,codigo,nome,categoria)
       
        

    def CriarDicionario(self):
        super().CriarDicionario()
        self.dicio["Prazo para terminar"]= self.prazo
        self.dicio["Data da matricula"] = self.data
        del self.dicio["CPF"]
        del self.dicio["Nome"]

        


        

            
