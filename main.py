from flask import Flask, render_template_string
import random
import string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
 <style>
    body { 
        font-family: Arial, sans-serif; 
        text-align: center; 
        margin: 0; 
        height: 100vh;
        display: flex;
        justify-content: center;
        align-items: center;
        background-color: #282c36;
        color: white;
    }
    .container { 
        background: rgba(255, 255, 255, 0.1); 
        padding: 30px; 
        border-radius: 10px; 
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
    }
    input { 
        width: 95%; 
        padding: 10px; 
        margin: 10px 0; 
        text-align: center; 
        font-size: 18px;
        background: #fff;
        border: none;
        border-radius: 10px;
    }
    button { 
        padding: 10px 15px; 
        font-size: 16px; 
        cursor: pointer;
        border: none;
        background: #61dafb; 
        color: black;
        border-radius: 10px;
        transition: 0.1s;
    }
    button:hover {
        background: #21a1f1;
    }
</style>


</head>
<body>
    <div class="container">
        <h2>Password Generator for losers</h2>
        <input type="text" id="password" value="{{ password }}" readonly>
        <button onclick="window.location.reload()">Generate Password</button>
        <button onclick="copyPassword()">Copy</button>
    </div>
    <script>
        function copyPassword() {
            const passwordField = document.getElementById("password");
            passwordField.select();
            document.execCommand("copy");
        }
    </script>
</body>
</html>
"""

def generate_password(length=8):
    upper = random.choice(string.ascii_uppercase)
    lower = random.choice(string.ascii_lowercase)
    digit = random.choice(string.digits)
    special = random.choice(string.punctuation)
    all_chars = string.ascii_letters + string.digits + string.punctuation
    remaining = ''.join(random.choices(all_chars, k=length-4))
    password = list(upper + lower + digit + special + remaining)
    random.shuffle(password)
    return ''.join(password)

@app.route('/')
def index():
    password = generate_password()
    return render_template_string(HTML_TEMPLATE, password=password)

if __name__ == '__main__':
    app.run(debug=True)
