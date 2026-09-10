import os
from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector

app = Flask(__name__)
app.secret_key = "inventory-secret"


def get_db():
    return mysql.connector.connect(
        host=os.getenv("MYSQL_HOST", "mysql"),
        user=os.getenv("MYSQL_USER", "root"),
        password=os.getenv("MYSQL_PASSWORD", "adeel"),
        database=os.getenv("MYSQL_DB", "inventory_db")
    )


@app.route("/")
def index():
    db = get_db()
    cursor = db.cursor(dictionary=True)

    cursor.execute("SELECT * FROM products ORDER BY id DESC")
    products = cursor.fetchall()

    cursor.close()
    db.close()

    return render_template("index.html", products=products)


@app.route("/add", methods=["POST"])
def add_product():

    name = request.form["name"]
    category = request.form["category"]
    quantity = request.form["quantity"]
    price = request.form["price"]

    db = get_db()
    cursor = db.cursor()

    query = """
        INSERT INTO products
        (name, category, quantity, price)
        VALUES (%s, %s, %s, %s)
    """

    cursor.execute(
        query,
        (name, category, quantity, price)
    )

    db.commit()

    cursor.close()
    db.close()

    flash("Product added successfully!")

    return redirect(url_for("index"))


@app.route("/delete/<int:product_id>", methods=["POST"])
def delete_product(product_id):

    db = get_db()
    cursor = db.cursor()

    cursor.execute(
        "DELETE FROM products WHERE id = %s",
        (product_id,)
    )

    db.commit()

    cursor.close()
    db.close()

    flash("Product deleted!")

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )