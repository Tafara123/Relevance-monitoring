from flask import Flask, render_template, request, jsonify
import mysql.connector

app = Flask(__name__)

# Connect to MySQL database
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Rosenheim123',
    database='ai_tools_responses'
)
mycursor = mydb.cursor()


@app.route('/')
def index():
    # Retrieve all distinct keywords and models from the database
    mycursor.execute("SELECT DISTINCT keyword_id FROM sources")
    keywords = [row[0] for row in mycursor.fetchall()]

    mycursor.execute("SELECT DISTINCT model FROM sources")
    models = [row[0] for row in mycursor.fetchall()]

    return render_template('index.html', keywords=keywords, models=models)


@app.route('/filtered_data', methods=['POST'])
def filtered_data():
    """
    Retrieves filtered data from the database based on keyword and model.
    """
    # Get filter criteria from the request
    filter_criteria = request.json

    # Prepare the SQL query based on the filter criteria
    sql = "SELECT * FROM sources WHERE 1=1"
    if 'keyword' in filter_criteria:
        keyword = filter_criteria['keyword']
        sql += f" AND keyword_id = '{keyword}'"

    if 'model' in filter_criteria:
        model = filter_criteria['model']
        sql += f" AND model = '{model}'"

    # Execute the SQL query
    mycursor.execute(sql)
    results = mycursor.fetchall()

    # Convert the results to a list of dictionaries
    data = []
    for row in results:
        data.append({
            'id': row[0],
            'date': row[1],
            'keyword_id': row[2],
            'model': row[3],
            'domain': row[4],
            'position': row[5]
        })

    # Return the filtered data as JSON
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
