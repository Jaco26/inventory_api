# Purpose
All database-related business logic should be defined inside a database controller.

# Function Naming and Prefixes
To help maintain code readability, database controller function names should be prefixed according to the guidelines below.

- `get`: Read any combination of records
- `create`: Create new record(s)
- `update`: Update record(s)
- `upsert`: Attempt to update a record. If it does not exist, create it.
- `delete`: Delete a record

- `add`: When you want to create a many-to-many relationship between two previously created records
- `remove`: When you want to remove a many-to-many relationship between two previously created records
