from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return '<h1>Hello World :)</h1>'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"


@app.route('/f')
@app.route('/f/<celsius>')
def convert(celsius=""):
    return f"{celsius} degrees celsius is {convert_celsius_to_fahrenheit(float(celsius))} degrees fahrenheit"



def convert_celsius_to_fahrenheit(celsius):
    """Convert temperature in Celsius to Fahrenheit."""
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


if __name__ == '__main__':
    app.run()
