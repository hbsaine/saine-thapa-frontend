from flask import Flask, render_template, request
import requests

app = Flask(__name__)

api_url = "https://colbert-salary-api-cgawbyc6fah3b0g8.eastus-01.azurewebsites.net"


@app.route("/")
def index():
    return render_template("index.html", predicted_salary=None)


@app.route("/predict", methods=["POST"])
def predict():
    payload = {
        "age": int(request.form["age"]),
        "gender": int(request.form["gender"]),
        "country": int(request.form["country"]),
        "highest_deg": int(request.form["highest_deg"]),
        "coding_exp": int(request.form["coding_exp"]),
        "title": int(request.form["title"]),
        "company_size": int(request.form["company_size"]),
    }
    response = requests.post(f"{api_url}/predict", json=payload)
    predicted_salary = response.json().get("predicted_salary")
    return render_template("index.html", predicted_salary=predicted_salary)


if __name__ == "__main__":
    app.run(debug=True)
