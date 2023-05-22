import os

import openai
from flask import Flask, redirect, render_template, request, url_for

# flask --app app run --host 0.0.0.0 --port 5001

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/home", methods=("GET", "POST"))
@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        category = request.form["category"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(category),
            max_tokens=1000,
            temperature=0,
            top_p=1,
            n=1,
            # decription below
            # n = 1 means that we only want one response
        )
        print(response)
        return redirect(url_for("index", result=response.choices[0].text))


    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(category):
    return """Create an HTML table of the top 5 {}.""".format(category.capitalize())


'''
"""Return the number of people that live in the following city as a number
    City: Houston, Texas
    Value: 2,356,000
    City: Austin

    Value: 1,356,000
    City: San Antonio
    Value:
    """
'''