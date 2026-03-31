from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
        <head><title>My Python App</title></head>
        <body style="font-family: Arial; text-align: center; margin-top: 50px;">
            <h1>Hello, World! 🚀</h1>
            <p>Mera Python app Git aur mod_wsgi ke through successfully deploy ho gaya hai!</p>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run()
