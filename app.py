from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('email.html')

@app.route('/preview', methods=['POST'])
def preview():
    name = request.form['name']
    position = request.form['position']
    company = request.form['company']
    response_type = request.form['response']

    if response_type == "accept":
        email_text = f"""
Dear {name},

Thank you for considering me for the {position} position at {company}.
I am pleased to accept the opportunity and look forward to joining your team.

Best regards,
Adarsh Kumar
"""
    else:
        email_text = f"""
Dear {name},

Thank you for reaching out regarding the {position} role at {company}.
I appreciate the opportunity, but I will not be able to proceed at this time.

Warm regards,
Adarsh Kumar
"""

    return render_template('preview.html', email=email_text)

if __name__ == '__main__':
    app.run(debug=True)