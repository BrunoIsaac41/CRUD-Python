from interface import *

class Menudeopcoes:
    def __init__(self) :
        #self.Interface = interface.interface_usuario()
        self.MenuOpcoes()
        
        
    def MenuOpcoes(self):
         interface_usuario = InterfaceUsuario()
         while True:
            print("******************************** Menu de Ações*********************************\n")

            print(" (0)Sair\n","(1)Incluir\n","(2)Excluir\n","(3)Editar\n","(4)Listar\n")
            acao_valor=int(input("Qual ação deseja executar?"))
            interface_usuario.acao = acao_valor
            
            # Se input errado:
            if interface_usuario.acao == 0:
                print("Saindo...")
                break   
            
            if interface_usuario.acao > 4  :
                print("Valor incorreto.")
                
            if interface_usuario.acao <=4 and interface_usuario.acao >=1 :
            
                # Menu de Categorias             
                print("--------------------Menu de Categorias de Gerenciamento-----------------------")
                
                print(" (0)Sair\n", "(1)Estudantes\n","(2)Professores\n","(3)Diciplinas\n","(4)Turmas\n","(5)Matrículas\n")
                
                opcao_valor=int(input("Qual categoria deseja executar?"))
                interface_usuario.opcao1 = opcao_valor

                if 0 == interface_usuario.opcao1:
                    print("O sistema foi interrompido. Saindo..")
                    break
                
                if interface_usuario.opcao1 <= 5:
                    #Definindo a categoria do objeto.
                    if interface_usuario.opcao1 == 1 : interface_usuario.categoria = "Estudante"
                    if interface_usuario.opcao1 == 2 : interface_usuario.categoria = "Professor"
                    if interface_usuario.opcao1 == 3 : interface_usuario.categoria = "Diciplina"
                    if interface_usuario.opcao1 == 4 : interface_usuario.categoria = "Turma"
                    if interface_usuario.opcao1 == 5: interface_usuario.categoria = "Matricula"
                   

                    
                    if interface_usuario.acao == 1 :
                        interface_usuario.Cadastrar()
                        
                    elif interface_usuario.acao ==2:
                        interface_usuario.Excluir()

                    elif interface_usuario.acao == 3:
                        interface_usuario.Editar()
                        

                    elif interface_usuario.acao == 4:
                        interface_usuario.Listar()     
                    
                    
                if interface_usuario.opcao1 > 5 :
                    print("valor inválido")
                    
            