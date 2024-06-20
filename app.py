from flask import Flask, render_template, request, redirect, url_for
import datetime

app = Flask(__name__)

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}"

contacts = []

def add_contact(name, phone, email):
    contact = Contact(name, phone, email)
    contacts.append(contact)

def view_contacts():
    return contacts

def update_contact(name, new_phone, new_email):
    for contact in contacts:
        if contact.name == name:
            contact.phone = new_phone
            contact.email = new_email
            return True
    return False

def delete_contact(name):
    global contacts
    contacts = [contact for contact in contacts if contact.name != name]
    return True

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']
        add_contact(name, phone, email)
        return redirect(url_for('view'))
    return render_template('add_contact.html')

@app.route('/view')
def view():
    return render_template('view_contacts.html', contacts=view_contacts())

@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        name = request.form['name']
        new_phone = request.form['new_phone']
        new_email = request.form['new_email']
        if update_contact(name, new_phone, new_email):
            return redirect(url_for('view'))
        else:
            return "Contact not found", 404
    return render_template('update_contact.html')

@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method == 'POST':
        name = request.form['name']
        delete_contact(name)
        return redirect(url_for('view'))
    return render_template('delete_contact.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
