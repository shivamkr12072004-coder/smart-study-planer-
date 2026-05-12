from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':

        subjects = request.form['subjects']

        subjects_list = [s.strip() for s in subjects.split(',')]

        timetable = []

        day = 1

        for sub in subjects_list:

            if day % 2 == 0:
                timetable.append(
                    (f"Day {day}", sub, "6:00 AM - 8:00 AM")
                )

            else:
                timetable.append(
                    (f"Day {day}", sub, "7:00 PM - 9:00 PM")
                )

            day += 1

        return render_template(
            'result.html',
            timetable=timetable
        )

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)