# Distributed Inventory
This project aims to provide backend services for a distributed inventory management system.

# Useful Links
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [Flask SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
- [Flask Migrate](https://flask-migrate.readthedocs.io/en/latest/)
- [Virtualenv](https://virtualenv.pypa.io/en/stable/user_guide.html)

# System Dependencies
- `postgresql`
- `python`

# Running Locally
- Clone or download this repository.
- Create a postgres database
- In the project root, create a `.env` file and add the following
```
FLASK_APP=wsgi.py
FLASK_ENV=development

DATABASE_URL=<your-database-url>
```
- In the project root, create and activate a virtual environment
```
virtualenv venv

source venv/bin/activate
```
- Next, install dependencies listed in `requirements.txt`
```
pip install -r requirements.txt
```

