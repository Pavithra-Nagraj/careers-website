from flask import Flask, render_template

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'Frontend Developer',
  'location': 'Bangalore',
  'Salary': 'Rs 15000'
}, {
  'id': 2,
  'title': 'Frontend Developer',
  'location': 'Bangalore',
  'Salary': 'Rs 15000'
}, {
  'id': 3,
  'title': 'Frontend Developer',
  'location': 'Bangalore',
  'Salary': 'Rs 15000'
}, {
  'id': 4,
  'title': 'Frontend Developer',
  'location': 'Bangalore',
  'Salary': 'Rs 15000'
}]


@app.route("/")
def hello_word():
  return render_template('home.html', jobs=JOBS, company_name='JOVIAN')


print(__name__)
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
