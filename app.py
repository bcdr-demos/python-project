from flask import Flask, request, render_template_string
import pandas as pd
import io

app = Flask(__name__)

HTML_TEMPLATE = '''
<!doctype html>
<html>
<head><title>PandaMuncher 🐼🍽️</title></head>
<body>
  <h1>Welcome to PandaMuncher! 🐼</h1>
  <p>Feed me some data, and watch me munch through it! 📊🍽️</p>
  <form method="post">
    <textarea name="data" rows="10" cols="50">{{ data }}</textarea><br>
    <input type="submit" value="Munch Data 🍪">
  </form>
  {% if result %}
    <h2>Munched Result: 📈</h2>
    <p>{{ result }}</p>
  {% endif %}
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

    return render_template_string(HTML_TEMPLATE, data=initial_data, result=result)

if __name__ == '__main__':
    app.run(debug=True)
