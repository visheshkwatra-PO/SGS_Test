from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")
        # For now, just print in console — later you can save to DB or send email
        print(f"New message from {name} ({email}): {message}")
        return "Thanks for contacting us! We'll get back to you soon."
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
