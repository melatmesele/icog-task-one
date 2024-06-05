# Neo4j Resume Graph

This project aims to represent a resume using a graph database (Neo4j). The structure allows querying and analyzing relationships between various entities such as education, experience, skills, and more.

## Folder Structure

- **data/**: Contains the initial data file (`initial_data.txt`).
- **scripts/**: Python scripts to insert data and run queries.
- **neo4j/**: Cypher scripts for importing data and running queries.
- **README.md**: This file.
- **requirements.txt**: Python dependencies.

## Setup

1. Install Neo4j and start the server.
2. Install the required Python packages:

    ```sh
    pip install -r requirements.txt
    ```

3. Run the `insert_data.py` script to populate the database:

    ```sh
    python scripts/insert_data.py
    ```

4. Run the `queries.py` script to execute sample queries:

    ```sh
    python scripts/queries.py
    ```

## Queries

Sample queries are available in the `queries.cypher` file. You can run these directly in the Neo4j browser.
