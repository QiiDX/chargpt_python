from flask import Flask, render_template, Response

app = Flask(__name__)


@app.route('/')
def KeyPage():
    # 传递需要展示的内容到模板
    return render_template('test.html', content="")


@app.route('/keyGPT', methods=['get'])
def keyGPT():
    # 传递需要展示的内容到模板
    return Response("""print("Addition:", result_addition)
print("Subtraction:", result_subtraction)
print("Multiplication:", result_multiplication)
print("Division:", result_division)
""", mimetype="text/plain",)


if __name__ == '__main__':
    app.run(debug=True)
