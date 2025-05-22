from neo4j import GraphDatabase
from teacher_crud import TeacherCRUD

# URI examples: "neo4j://localhost", "neo4j+s://xxx.databases.neo4j.io"
URI = "neo4j+s://c7a6bf48.databases.neo4j.io"
AUTH = ("neo4j", "LpFoI5KNznD-eJ-TsY0risbm_DCRO50iMiecJKOYZ-c")

driver = GraphDatabase.driver(URI, auth=AUTH)

try:
    with driver.session() as session:
        resultado = session.run("RETURN '🚀 Conexão bem-sucedida!'").single()
        print(resultado[0])
except Exception as e:
    print(f"Erro ao conectar: {e}")
finally:
    driver.close()


class TeacherCLI:
    def __init__(self):
        self.crud = TeacherCRUD("neo4j+s://SEU_SERVIDOR", "neo4j", "SUA_SENHA")
    
    def run(self):
        while True:
            print("\n=== MENU TEACHER CRUD ===")
            print("1. Criar Professor")
            print("2. Buscar Professor")
            print("3. Atualizar CPF")
            print("4. Deletar Professor")
            print("5. Sair")
            
            opcao = input("Escolha: ")
            
            if opcao == "1":
                self._create_teacher()
            elif opcao == "2":
                self._read_teacher()
            elif opcao == "3":
                self._update_teacher()
            elif opcao == "4":
                self._delete_teacher()
            elif opcao == "5":
                self.crud.close()
                break
            else:
                print("Opção inválida!")
    
    def _create_teacher(self):
        name = input("Nome: ")
        ano_nasc = int(input("Ano nascimento: "))
        cpf = input("CPF: ")
        self.crud.create(name, ano_nasc, cpf)
        print("Professor criado!")
    
    def _read_teacher(self):
        name = input("Nome: ")
        print(self.crud.read(name))
    
    def _update_teacher(self):
        name = input("Nome: ")
        new_cpf = input("Novo CPF: ")
        print(self.crud.update(name, new_cpf))
    
    def _delete_teacher(self):
        name = input("Nome: ")
        self.crud.delete(name)
        print("Professor deletado!")

if __name__ == "__main__":
    cli = TeacherCLI()
    cli.run()