# Database file, to create and store database information

DIALECT = "postgresql"

USER = "postgres"
PASSWORD = "928187"
HOST = "localhost"
PORT = "5432"
DATABASE_NAME = "blogdb"

DATABASE_URL = f"{DIALECT}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE_NAME}"