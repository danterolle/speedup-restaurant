from flask import Flask, render_template, request, redirect
from datetime import datetime

app = Flask(__name__)

# lista per memorizzare le prenotazioni
reservations = []

# lista per memorizzare gli ordini
orders = []


# pagina iniziale
@app.route('/')
def index():
    return render_template('index.html')


# pagina per prenotare un tavolo
@app.route('/reserve', methods=['GET', 'POST'])
def reserve():
    if request.method == 'POST':
        # recupera i dati dalla richiesta
        name = request.form['name']
        surname = request.form['surname']
        email = request.form['email']
        phone = request.form['phone']
        num_people = request.form['num_people']
        date = request.form['date']
        time = request.form['time']
        notes = request.form['notes']

        # crea un oggetto prenotazione
        reservation = {
            'name': name,
            'surname': surname,
            'email': email,
            'phone': phone,
            'num_people': num_people,
            'date': date,
            'time': time,
            'notes': notes
        }

        # aggiunge la prenotazione alla lista
        reservations.append(reservation)

        return redirect('/reservations')
    else:
        return render_template('reserve.html')


# pagina per visualizzare tutte le prenotazioni
@app.route('/reservations')
def view_reservations():
    return render_template('reservations.html', reservations=reservations)


# pagina per visualizzare il menù
@app.route('/menu')
def menu():
    menu_items = [
        {'name': 'Pizza Margherita', 'price': 10},
        {'name': 'Lasagna', 'price': 12},
        {'name': 'Spaghetti Bolognese', 'price': 11},
        {'name': 'Cotoletta alla Milanese', 'price': 15},
    ]
    return render_template('menu.html', menu_items=menu_items)


# pagina per inviare un ordine
@app.route('/order', methods=['POST'])
def order():
    # recupera i dati dalla richiesta
    table_number = request.form['table_number']
    items = request.form.getlist('items')

    # crea un oggetto ordine
    order = {
        'table_number': table_number,
        'items': items,
        'time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'total_price': calculate_total_price(items)
    }

    # aggiunge l'ordine alla lista
    orders.append(order)

    return redirect('/orders')


# funzione per calcolare il prezzo totale dell
def calculate_total_price(items):
    menu_items = [
        {'name': 'Pizza Margherita', 'price': 10},
        {'name': 'Lasagna', 'price': 12},
        {'name': 'Spaghetti Bolognese', 'price': 11},
        {'name': 'Cotoletta alla Milanese', 'price': 15},
    ]

    total_price = 0
    for item in items:
        for menu_item in menu_items:
            if item == menu_item['name']:
                total_price += menu_item['price']
    return total_price
