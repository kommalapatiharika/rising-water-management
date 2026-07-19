from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    water_level = 40
    temperature = 28
    humidity = 75
    alert = "No Flood Alerts"

    return render_template(
        'index.html',
        water_level=water_level,
        temperature=temperature,
        humidity=humidity,
        alert=alert
    )

if __name__ == '__main__':
    app.run(debug=True)