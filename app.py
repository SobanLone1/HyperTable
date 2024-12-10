from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simulated user database (in memory)
users = []

# Home page route where user can choose to register or login
@app.route('/')
def home():
    return render_template('index.html')

# Registration route
@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        # Gather form data
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']
        location = request.form['location']
        
        # Simulate storing the user data (you can add this to a database in a real app)
        users.append({'name': name, 'phone': phone, 'email': email, 'location': location})

        # After registration, redirect to the login page
        return redirect(url_for('login'))

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email_or_username = request.form['email_or_username']
        password = request.form['password']
        
        # Simulate user authentication (in a real app, validate password, etc.)
        return redirect(url_for('main_program'))

    return render_template('login.html')

# Main program route
@app.route('/main')
def main_program():
    return render_template('main_program.html')

if __name__ == '__main__':
    app.run(debug=True)
