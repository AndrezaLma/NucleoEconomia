from flask import Flask, request, render_template
import math

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        principal = float(request.form['principal'])
        rate = float(request.form['rate']) / 100
        time = float(request.form['time'])
        investment_type = request.form['investment_type']

        if investment_type == 'simple_interest':
            result = simple_interest(principal, rate, time)
        elif investment_type == 'compound_interest':
            result = compound_interest(principal, rate, time)
        else:
            result = "Invalid investment type"

        return render_template('result.html', result=result)
    return render_template('index.html')

def simple_interest(principal, rate, time):
    return principal * rate * time

def compound_interest(principal, rate, time):
    return principal * (1 + rate) ** time

if __name__ == '__main__':
    app.run(debug=True)