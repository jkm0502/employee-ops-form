from flask import Flask, render_template_string, request, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def serve_order_form():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'order_form.html')

@app.route('/gift-form')
def serve_gift_form():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'employee_gift_form.html')

if __name__ == '__main__':
    app.run(debug=True)
