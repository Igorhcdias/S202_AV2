from neo4j import GraphDatabase

class TeacherCRUD:
    def __init__(self, uri, user, password):
        self._driver = GraphDatabase.driver(uri, auth=(user, password))
    
    def close(self):
        self._driver.close()
    
    def create(self, name, ano_nasc, cpf):
        with self._driver.session() as session:
            return session.run(
                "CREATE (t:Teacher {name: $name, ano_nasc: $ano_nasc, cpf: $cpf}) RETURN t",
                {"name": name, "ano_nasc": ano_nasc, "cpf": cpf}
            ).single()
    
    def read(self, name):
        with self._driver.session() as session:
            return session.run(
                "MATCH (t:Teacher {name: $name}) RETURN t",
                {"name": name}
            ).single()
    
    def update(self, name, newCpf):
        with self._driver.session() as session:
            return session.run(
                "MATCH (t:Teacher {name: $name}) SET t.cpf = $newCpf RETURN t",
                {"name": name, "newCpf": newCpf}
            ).single()
    
    def delete(self, name):
        with self._driver.session() as session:
            session.run(
                "MATCH (t:Teacher {name: $name}) DELETE t",
                {"name": name}
            )