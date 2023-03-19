from flask import Flask, flash, render_template, request

app = Flask(__name__)
app.secret_key = 'secret_key'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        
        if name and age:
            flash('登録に成功しました!')
            flash('これからよろしくお願いいたします!')
        else:
            flash('登録に失敗しました。')
            flash('名前・年齢を入力してください。')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)