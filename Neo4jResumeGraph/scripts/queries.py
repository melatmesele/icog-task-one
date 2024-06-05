from neo4j import GraphDatabase

class ResumeGraphQueries:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def find_skills_acquired_during_education(self):
        with self.driver.session() as session:
            result = session.read_transaction(self._find_skills)
            for record in result:
                print(record["s.name"])

    @staticmethod
    def _find_skills(tx):
        query = """
        MATCH (p:Person)-[:STUDIED_AT]->(e:Education)-[:USED]->(s:Skill)
        RETURN DISTINCT s.name;
        """
        result = tx.run(query)
        return result

    def list_jobs_using_skill(self, skill_name):
        with self.driver.session() as session:
            result = session.read_transaction(self._list_jobs, skill_name)
            for record in result:
                print(f"{record['exp.title']} at {record['exp.company']} ({record['exp.years']})")

    @staticmethod
    def _list_jobs(tx, skill_name):
        query = """
        MATCH (p:Person)-[:WORKED_AT]->(exp:Experience)-[:USED]->(s:Skill {name: $skill_name})
        RETURN exp.title, exp.company, exp.years;
        """
        result = tx.run(query, skill_name=skill_name)
        return result

if __name__ == "__main__":
    uri = "bolt://localhost:7687"
    user = "neo4j"
    password = "password"
    rgq = ResumeGraphQueries(uri, user, password)
    print("Skills acquired during education:")
    rgq.find_skills_acquired_during_education()
    print("\nJobs where Python was used:")
    rgq.list_jobs_using_skill("Python")
    rgq.close()
