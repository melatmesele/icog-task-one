// Query to find skills acquired during education
MATCH (p:Person)-[:STUDIED_AT]->(e:Education)-[:USED]->(s:Skill)
RETURN DISTINCT s.name;

// Query to list jobs where a specific skill was used
MATCH (p:Person)-[:WORKED_AT]->(exp:Experience)-[:USED]->(s:Skill {name: $skill_name})
RETURN exp.title, exp.company, exp.years;
