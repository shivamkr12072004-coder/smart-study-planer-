from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():

    if request.method == 'POST':

        subjects = request.form.get('subjects')
        hours = request.form.get('hours')
        date = request.form.get('date')

        subject_list = subjects.split(',')

        timetable = []

        for i, subject in enumerate(subject_list):

            timetable.append({
                "day": f"Day {i+1}",
                "subject": subject.strip(),
                "time": f"{hours} Hours"
            })

        return render_template(
            'result.html',
            timetable=timetable,
            date=date
        )

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
