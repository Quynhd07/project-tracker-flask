"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template
import hackbright

app = Flask(__name__)


@app.route('/search')
def student_search():

    return render_template('student_search.html')


@app.route('/student')
def get_student():
    """Show information about a student."""

    github = request.args.get('github')

    first, last, github = hackbright.get_student_by_github(github)

    return render_template('student_info.html', first_name=first,
                                                last_name=last,
                                                github_user=github)

@app.route('/add_student')
def add_new_student():

    return render_template('add_student.html')


@app.route('/new_student', methods=['POST'])
def display_new_student():

    first = request.form.get('firstname')
    last = request.form.get('lastname')
    github = request.form.get('github')

    # first, last, github = 
    hackbright.make_new_student(first, last, github)

    return render_template('new_student.html', github=github)


if __name__ == '__main__':
    hackbright.connect_to_db(app)
    app.run(debug=True, host='0.0.0.0')
