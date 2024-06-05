from neo4j import GraphDatabase

class ResumeGraph:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def create_graph(self):
        with self.driver.session() as session:
            session.write_transaction(self._create_nodes_and_relationships)

    @staticmethod
    def _create_nodes_and_relationships(tx):
        tx.run("""
        // Clear existing data
        MATCH (n) DETACH DELETE n;

        // Create Person node
        CREATE (p:Person {
            name: 'Melat Mesele', 
            email: 'melat1993m@gmail.com', 
            phone: '+251 904 684 256', 
            location: 'Addis Ababa, Ethiopia', 
            linkedin: 'https://www.linkedin.com/in/melat-mesele-68a4b8222/', 
            github: 'https://github.com/melatmesele', 
            birthdate: '30/12/2000', 
            gender: 'female'
        });

        // Create Education nodes and relationships
        CREATE (edu:Education {
            degree: 'Bachelor of Science in Software Engineering', 
            institution: 'Addis Ababa University', 
            start_year: '2019', 
            end_year: '2024'
        });
        CREATE (p)-[:STUDIED_AT]->(edu);

        // Create Experience nodes and relationships
        CREATE (exp1:Experience {
            title: 'Front-End Developer', 
            company: 'Freelance', 
            start_date: '09/2023', 
            end_date: '01/2024', 
            location: 'Addis Ababa, Ethiopia',
            description: 'Developed and deployed a website that tracks finance and generates reports for a private company.'
        });
        CREATE (exp2:Experience {
            title: 'Full Stack Web Developer', 
            company: 'Super Consult PLC', 
            start_date: '03/2023', 
            end_date: '09/2023', 
            location: 'Addis Ababa, Ethiopia',
            description: 'Worked with tools like Jira, GitHub, and Slack to improve communication and project tracking.'
        });
        CREATE (exp3:Experience {
            title: 'Backend Developer', 
            company: 'project', 
            start_date: '10/2023', 
            end_date: 'present', 
            location: 'Addis Ababa, Ethiopia',
            description: 'Developing a coding practice and exam platform for Addis Ababa University freshmen students.'
        });
        CREATE (p)-[:WORKED_AT]->(exp1);
        CREATE (p)-[:WORKED_AT]->(exp2);
        CREATE (p)-[:WORKED_AT]->(exp3);

        // Create Skill nodes and relationships
        CREATE (skill1:Skill {name: 'Nodejs', type: 'Technical'});
        CREATE (skill2:Skill {name: '.Net Core', type: 'Technical'});
        CREATE (skill3:Skill {name: 'React', type: 'Technical'});
        CREATE (skill4:Skill {name: 'MongoDB', type: 'Technical'});
        CREATE (skill5:Skill {name: 'MySQL', type: 'Technical'});
        CREATE (skill6:Skill {name: 'Typescript', type: 'Technical'});
        CREATE (skill7:Skill {name: 'javascript', type: 'Technical'});
        CREATE (skill8:Skill {name: 'python', type: 'Technical'});
        CREATE (p)-[:HAS_SKILL]->(skill1);
        CREATE (p)-[:HAS_SKILL]->(skill2);
        CREATE (p)-[:HAS_SKILL]->(skill3);
        CREATE (p)-[:HAS_SKILL]->(skill4);
        CREATE (p)-[:HAS_SKILL]->(skill5);
        CREATE (p)-[:HAS_SKILL]->(skill6);
        CREATE (p)-[:HAS_SKILL]->(skill7);
        CREATE (p)-[:HAS_SKILL]->(skill8);

        // Create Extracurricular nodes and relationships
        CREATE (extra:Extracurricular {
            activity: 'Addis Coder', 
            role: 'Data Structure And Algorithm Assistant', 
            start_date: '07/2023', 
            end_date: '08/2023', 
            description: 'Assisted students in understanding and implementing various data structures and algorithms.'
        });
        CREATE (p)-[:PARTICIPATED_IN]->(extra);

        // Create Certification nodes and relationships
        CREATE (cert1:Certification {name: 'Huawei Seed For The Future'});
        CREATE (cert2:Certification {name: 'My Digital World'});
        CREATE (cert3:Certification {name: 'Orange Digital Center Ethiopia'});
        CREATE (cert4:Certification {name: 'Addis Coder'});
        CREATE (p)-[:HAS_CERTIFICATION]->(cert1);
        CREATE (p)-[:HAS_CERTIFICATION]->(cert2);
        CREATE (p)-[:HAS_CERTIFICATION]->(cert3);
        CREATE (p)-[:HAS_CERTIFICATION]->(cert4);

        // Create Language nodes and relationships
        CREATE (lang1:Language {name: 'Amharic', proficiency: 'native'});
        CREATE (lang2:Language {name: 'English', proficiency: 'Fluent'});
        CREATE (p)-[:SPEAKS]->(lang1);
        CREATE (p)-[:SPEAKS]->(lang2);

        // Create Interest nodes and relationships
        CREATE (int1:Interest {name: 'scientific/mystery movie'});
        CREATE (int2:Interest {name: 'reading books'});
        CREATE (p)-[:HAS_INTEREST]->(int1);
        CREATE (p)-[:HAS_INTEREST]->(int2);
        """)

if __name__ == "__main__":
    uri = "bolt://localhost:7687"
    user = "neo4j"
    password = "password"
    rg = ResumeGraph(uri, user, password)
    rg.create_graph()
    rg.close()
