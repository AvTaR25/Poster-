from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
        <head>
            <title>My Python App</title>
            <style>
                body { font-family: Arial, sans-serif; text-align: center; margin-top: 50px; background-color: #f4f4f9; }
                .container { background: white; padding: 30px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); display: inline-block; }
                h1 { color: #333; }
                p { color: #666; font-size: 18px; }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Hello, World! 🚀</h1>
                <p>Mera Python app Git aur mod_wsgi ke through successfully deploy ho gaya hai!</p>
            </div>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)
