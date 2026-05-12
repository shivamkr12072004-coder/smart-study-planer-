from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        subjects = request.form.get("subjects")
        days = int(request.form.get("days"))

        subject_list = subjects.split(",")

        timetable = []

        for i in range(days):

            timetable.append({
                "day": f"Day {i+1}",
                "subject": subject_list[i % len(subject_list)].strip(),
                "time": "Morning" if i % 2 == 0 else "Evening"
            })

        return render_template(
            "result.html",
            timetable=timetable
        )

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
