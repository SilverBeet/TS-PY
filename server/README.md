### Server Setup

Requirements:
  Python3,
  Pip3,
  Sqlite

### Dependencies
```
pip install flask flask_sqlalchemy flask_cors
```

### Create db

Python in cmd
```
>>> from api import db
>>> db.create_all()
```

#### Run server
```
python api.py
```
