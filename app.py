from flask import Flask, request, render_template_string
import pandas as pd
import io

app = Flask(__name__)

HTML_TEMPLATE = '''
<!doctype html>
<html>
<head>
    <title>PandaMuncher 🐼🍽️</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            text-align: center;
            margin: 0;
            padding-top: 60px;
            background-color: #f4f4f4;
        }
        .container {
            max-width: 800px;
            margin: auto;
            padding: 20px;
            background-color: white;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        textarea {
            width: 100%;
            max-width: 100%;
            min-width: 100%;
            box-sizing: border-box;
        }
        .logo {
            width: 100%;
            max-width: 500px;
            margin: auto;
            display: block;
        }
        input[type=submit] {
          background-color: #4CAF50; /* Green background */
          color: white; /* White text */
          padding: 12px 24px; /* Padding around the text */
          border: none; /* No border */
          border-radius: 4px; /* Rounded corners */
          cursor: pointer; /* Cursor changes to a hand symbol when hovered */
          font-size: 16px; /* Larger font size */
          transition: background-color 0.3s ease; /* Smooth transition for hover effect */
      }

      input[type=submit]:hover {
          background-color: #45a049; /* Slightly darker green background on hover */
      }
    </style>
    <link rel="icon" href="/static/favicon.png">
</head>
<body>
  <div class="container">
      <h1>Welcome to PandaMuncher! 🐼</h1>
      <p>Feed me some data, and watch me munch through it! 📊🍽️</p>
      <form method="post">
        <textarea name="data" rows="10">{{ data }}</textarea><br>
        <input type="submit" value="Munch Data 🍪">
      </form>
      {% if result %}
        <h2>Munched Result: 📈</h2>
        <p>{{ result }}</p>
      {% endif %}
  </div>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    initial_data = "A,B,C\n1,2,3\n4,5,6\n7,8,9"  # Pre-filled data

    if request.method == 'POST':
        data = request.form['data']
        df = pd.read_csv(io.StringIO(data))
        result = f"Mean of column 'B': {df['B'].mean()} 🧮"
    else:
        data = initial_data

    return render_template_string(HTML_TEMPLATE, data=data, result=result)

if __name__ == '__main__':
    app.run(debug=True)
