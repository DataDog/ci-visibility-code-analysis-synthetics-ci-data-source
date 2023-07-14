# demo-static-analysis-python

## Setup
Bootstrap the project

1. Create a virtual environment `python -mvenv venv`
2. Use the virtual environment `source venv/bin/activate`
3. Install all dependencies `pip install -r requirements.txt`
4. Init the database `rm -f db.sqlite ;  sqlite3 db.sqlite < init.sql`

Start the project:

```shell
flask --app service run
```

