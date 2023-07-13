1. Checkout the code
2. Make it work according to the instructions in `README.md`
3. Go to http://127.0.0.1:5000/products and check it returns products
4. Now, we want to add a feature to retrieve a product based on its ID. To do so, in the file `service.py`, add a new endpoint:

```python
@app.route("/products/<product_id>", methods=["GET"])
def product_by_id(product_id):
    products = db.get_product_by_id(db_connection, product_id)
    return jsonify(products)
 ```

And add a new function in the file `database.py`

```python
def get_product_by_id(db_connection, product_id):
    cursor = db_connection.cursor()
    res = cursor.execute(f"SELECT id, title from products WHERE id={product_id}")
    return [Product(v[0], v[1]) for v in res]
 ```

This will create a SQL issue, without a fix.


```json
{
  "violations": [
    {
      "start": {
        "line": 12,
        "col": 11
      },
      "end": {
        "line": 12,
        "col": 90
      },
      "message": "Do not use f-string in SQL queries, it leads to SQL injections",
      "severity": "ERROR",
      "category": "SAFETY",
      "filename": "database.py",
      "rule": "python-security/sql-injection",
      "fixes": []
    }
  ],
  "rule_results_with_error": []
}
```
