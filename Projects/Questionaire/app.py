from flask import Flask, render_template, request, redirect, url_for

# create app
app = Flask(__name__)

# route for start page
@app.route("/")
def index():
    return render_template('index.html')

# open file with data
file = open('static/answers.csv')
# read file
lines = file.readlines()
# reformat answers and save in list
answers= [ entry.strip("\n").split(",") for entry in lines ]
# close file
file.close()

# route for showing results
@app.route("/results")
def results():
    return render_template('results.html', answers=answers)

# route for retrieving new data
@app.route("/questions", methods=('GET', 'POST'))
def questions():
    if request.method == 'POST':
        # save answers
        save_answer(request.form)
        return redirect(url_for('results'))
    return render_template('questions.html')


# function to save answers from a form
def save_answer(form):
    # create list with answers
    new_answer = [form[attribute] for attribute in form]

    # write to file
    with open('static/answers.csv', 'a') as f:
        f.write(','.join(new_answer))
        f.write('\n')

    # append to current answers
    answers.append(new_answer)

if __name__ == "__main__":
    app.run()