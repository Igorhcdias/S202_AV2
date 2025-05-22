from neo4j import GraphDatabase

class Database:
    def __init__(self, uri, user, password):
        self._driver = GraphDatabase.driver(uri, auth=(user, password))
    
    def close(self):
        self._driver.close()
    
    def execute_query(self, query, parameters=None):
        with self._driver.session() as session:
            result = session.run(query, parameters)
            return [record.data() for record in result]

# ===== QUESTÃO 1 =====
def questao_01(db):
    print("\n=== QUESTÃO 1 ===")
    
    # 1. Professor Renzo
    query1 = """
    MATCH (t:Teacher {name: "Renzo"})
    RETURN t.ano_nasc AS ano_nascimento, t.cpf AS cpf
    """
    print("\n1. Professor Renzo:")
    print(db.execute_query(query1))
    
    # 2. Professores com M
    query2 = """
    MATCH (t:Teacher)
    WHERE t.name STARTS WITH "M"
    RETURN t.name AS nome, t.cpf AS cpf
    """
    print("\n2. Professores com M:")
    print(db.execute_query(query2))
    
    # 3. Nomes de cidades
    query3 = """
    MATCH (c:City)
    RETURN c.name AS nome_cidade
    """
    print("\n3. Cidades:")
    print(db.execute_query(query3))
    
    # 4. Escolas (150-550)
    query4 = """
    MATCH (s:School)
    WHERE s.number >= 150 AND s.number <= 550
    RETURN s.name AS nome_escola, s.address AS endereco, s.number AS numero
    """
    print("\n4. Escolas (150-550):")
    print(db.execute_query(query4))

# ===== QUESTÃO 2 =====
def questao_02(db):
    print("\n=== QUESTÃO 2 ===")
    
    # 1. Professor mais jovem/velho
    query1 = """
    MATCH (t:Teacher)
    RETURN min(t.ano_nasc) AS mais_velho, max(t.ano_nasc) AS mais_jovem
    """
    print("\n1. Professores (jovem/velho):")
    print(db.execute_query(query1))
    
    # 2. Média de população
    query2 = """
    MATCH (c:City)
    RETURN avg(c.population) AS media_habitantes
    """
    print("\n2. Média de habitantes:")
    print(db.execute_query(query2))
    
    # 3. Cidade com CEP 37540-000
    query3 = """
    MATCH (c:City {cep: "37540-000"})
    RETURN replace(c.name, 'a', 'A') AS nome_modificado
    """
    print("\n3. Cidade (CEP 37540-000):")
    print(db.execute_query(query3))
    
    # 4. 3ª letra dos professores
    query4 = """
    MATCH (t:Teacher)
    RETURN substring(t.name, 2, 1) AS terceira_letra
    """
    print("\n4. 3ª letra dos professores:")
    print(db.execute_query(query4))

if __name__ == "__main__":
    db = Database("neo4j+s://SEU_SERVIDOR", "neo4j", "SUA_SENHA")
    questao_01(db)
    questao_02(db)
    db.close()