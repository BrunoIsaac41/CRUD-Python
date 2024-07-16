import json
import time 
from categorias import *


class InterfaceUsuario() :
    
    def __init__(self) :
        
        self.acao = int
        self.opcao1 = int
        self.ListaDicionarios = []
        self.categoria = str
        self.codigo_valido = bool
        self.cpf_valido = bool
        
        
# FUNÇÕES
    
    # Função Excluir
    def Excluir(self):
        with open("dad.json", "r") as reading:
            dadosJson = json.load(reading)
        
        
        while True:
            ListaPorCategoria =[]

            for i in dadosJson:
                if i["Categoria"] == self.categoria:
                    ListaPorCategoria.append(i)
                        
            if len(ListaPorCategoria) == 0:
                print(f"Não há {self.categoria}.")
                break

                    
            print(f"--------------- Exclusão ---------------")
            print(f"\nLista completa: \nDigite 'Encerrar' para finalizar.\n")
           
            for i in ListaPorCategoria:
                print(f"{i}")

            cod_excluir = input(f"\nQual o código do(a): {self.categoria} que deseja excluir? ")

            if cod_excluir.lower() == "encerrar":
                print("Processo encerrado.")
                break

            item_encontrado = False
            for i in ListaPorCategoria:
                if  i["Codigo"] == cod_excluir:
                    dadosJson.remove(i)
                    time.sleep(2)
                    item_encontrado = True
                    
                print(f"O(a) {self.categoria} foi excluído.")
                break

            if not item_encontrado:
                print("O valor não está na lista.\nDigite um valor que esteja na lista.")
                time.sleep(2)
            
            categoria_vazia = True
            for i in dadosJson:
                if i["Categoria"] == self.categoria:
                    categoria_vazia = False
                    break

            if categoria_vazia:
                print(f"Todos os {self.categoria} foram excluídos.")
                break

        with open("dad.json", "w") as wr:
            json.dump(dadosJson, wr)


        #Função Salvar Arquivo    
    def salvar_arquivo(self,ValorParaSalvar):
        
        try: 
            with open('dad.json','r')as f1:
                lista= json.load(f1) 
                lista.extend(ValorParaSalvar)
                with open("dad.json", "w") as f2:
                    json.dump(lista,f2, indent=1)
       
        except Exception :
            with open("dad.json", "w") as f3:
                json.dump(ValorParaSalvar,f3, indent=1)


    #Função Cadastrar
    def Cadastrar(self):
        with open("dad.json", "r") as reading:
            dadosJson = json.load(reading)
       
        while True:
            nome=input(f"Digite o nome do(a) {self.categoria}:")
            self.verificar_codigo_Cadastrar(dadosJson)# ---> self.codigo
            if self.codigo_existente:
                continue
            
            if self.opcao1 == 1:
                self.verificar_Cpf() ; # -----> self.cpf :
                estudante = Estudantes(self.categoria, self.cpf, self.codigo, nome)
                self.ListaDicionarios.append(estudante.dicio)
                print(f"{self.categoria} incluído(a) com sucesso.")
                break
                
            elif self.opcao1 == 2 :   
                self.verificar_Cpf() ; # -----> self.cpf :
                professor = Professores(self.categoria, self.cpf, self.codigo, nome)
                self.ListaDicionarios.append(professor.dicio)
                print(f"{self.categoria} incluído(a) com sucesso.")
                break
            
            elif self.opcao1 == 3:
                semestre = int(input(f"Digite o semestre do(a) {repr(nome)}:"))
                cpf = ""
                diciplina = Diciplinas(self.categoria, semestre, nome, self.codigo, cpf)
                self.ListaDicionarios.append(diciplina.dicio)
                print(f"{self.categoria} incluído(a) com sucesso.")
                break
            
            elif self.opcao1 == 4:
                qtdAlunos = input(f"Digite a quantidade de alunos do(a) {repr(nome)}")
                turma = Turmas(self.categoria, nome, qtdAlunos, self.codigo)
                self.ListaDicionarios.append(turma.dicio)
                print(f"{self.categoria} incluído(a) com sucesso.")
                break

            elif self.opcao1 == 5 :
                tempo =  input("Digite o tempo corrente da matricula:")
                data = input("Digite a data de efetuação da matricula:")
                matricula = Matriculas(self.codigo, nome , self.categoria, cpf, data, tempo)
                self.ListaDicionarios.append(matricula.dicio)
                print(f"{self.categoria} incluído(a) com sucesso.")
            
        

#  Função editar para dados complexos:
    def Editar(self):
        
        with open ("dad.json","r") as f1:
            dadosJson= json.load(f1)

        
        while True:
            self.ListaPorCategoria = []
            for i in dadosJson:
                if i["Categoria"] == self.categoria:
                    self.ListaPorCategoria.append(i)
                    break
            print(f"\nLista completa:\nDigite 'Encerrar' para finalizar.\n")
            
            for i in self.ListaPorCategoria:
                print(f"{i}")
                        
            if len(self.ListaPorCategoria) == 0:
                print(f"Não há {self.categoria}.")
                break
        
            #Veificação do Codigo.
            self.verificar_codigo_Editar()
            
            if self.codigo_valido:                        
                chave_editar = input(f"\nQual a chave de valores que deseja editar?:")   
                
                if chave_editar.lower() == 'encerrar':
                    print("Processo encerrado") 
                    break
                
                #Verificação chave.
                chave_valida = None
                for i in self.lista_verificados:
                    for key in i:
                        if chave_editar == key :
                            chave_valida = True
                        
                #Se a chave existir.
                if chave_valida == True:
                        
                    if chave_editar == "CPF":
                        self.verificar_Cpf()
                        if self.cpf_valido == True:
                            i[chave_editar] = self.cpf
                            break
                        continue
                        
                    
                    if chave_editar =="Codigo":
                        self.verificar_codigo_Cadastrar()
                        #Se existir:
                        if self.codigo_existente:
                            continue
                        #Se não:
                        else: i[chave_editar] = self.codigo
                        
                        
                    else:
                        novo_dado = input(f"Digite o(a) novo dado para {chave_editar}: ")
                        i[chave_editar] = novo_dado
                    
                    print(f"Edição concluída com sucesso:{i}")
                    break

                    
                    
                else:
                    print("Chave inválida.\nRecomeçe o processo.\n====================")
                    break
            else:
                print("Codigo inválido, digite novamente.") 
                break

        with open ("dad.json","w") as f2:
            json.dump(dadosJson,f2,indent=1)
            
                
            

    # Função Listar
    def Listar (self):
        with open ('dad.json','r') as f1:
            Lista = json.load(f1)
        
        print("----------- Listagem ----------")
        while True:
            ListaPorCategoria = []
            for i in Lista:
                if i["Categoria"] == self.categoria:
                    ListaPorCategoria.append(i)
             
                if len(Lista) == 0:
                    print("A lista está vazia.")
           
            print(f"Segue a Lista de {self.categoria}s:\n ")
            for i in ListaPorCategoria:
                print(i)
            break

    
    def verificar_Cpf(self):

        while True :
            self.cpf = int (input(f"Digite o CPF do Estudante sem dígitos e sem traços: "))
            
            if len(str(self.cpf)) <11: 
                print("\n******CPF inválido.\n Recomeçe o processo.******\n")
                self.cpf_valido =  False
            
            elif self.cpf == str: 
                print("\n******CPF inválido\n Recomeçe o processo.******\n")
                self.cpf_valido =  False
            
            else: self.cpf_valido = True
                

            break

    def verificar_codigo_Editar(self):
        self.lista_verificados = []
        
        codigo = input(f"\nQual o código do(a) {self.categoria} que deseja editar?\n=========================")
        
        for i in self.ListaPorCategoria:
            if codigo == i["Codigo"] :
                print(i["Codigo"])
                self.codigo_valido =  True
                self.lista_verificados.append(i)
                
                
        
            else:
                print("Codigo não está no cadastro que você selecionou. \nDigite novamente.")
                self.codigo_valido = False
                
            
    
    def verificar_codigo_Cadastrar(self):
        self.codigo_existente =  False
        while True:
            self.codigo = (input(f"Digite o novo código {self.categoria}: "))
            with open ("dad.json", "r") as read:
                dados = json.load(read)
            for i in dados:
                if self.codigo == i["Codigo"]:
                    self.codigo_existente = True
            if self.codigo_existente:
                print("\n--------Código já existente. Recomece o processo.---------")
                break
            else:
                break
            
        

        


