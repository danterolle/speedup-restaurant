from flask import Flask, render_template, request, redirect
from src.database import db, Reservation, Order

app = Flask(__name__)

# lista per memorizzare le prenotazioni
reservations = []

# lista per memorizzare gli ordini
orders = []


# pagina iniziale
@app.route('/')
def index():
    return render_template('index.html')


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


# pagina per prenotare un tavolo
@app.route('/reservations', methods=['GET', 'POST'])
def reservations():
    if request.method == 'POST':
        name = request.form['name']
        surname = request.form['surname']
        email = request.form['email']
        phone = request.form['phone']
        num_people = request.form['num_people']
        date = request.form['date']
        time = request.form['time']
        notes = request.form['notes']
        reservation = Reservation(name=name, surname=surname, email=email, phone=phone, num_people=num_people,
                                  date=date, time=time, notes=notes)
        db.session.add(reservation)
        db.session.commit()

        return redirect('/reservations')
    else:
        reservations = Reservation.query.all()
        return render_template('reservations.html', reservations=reservations)


# pagina per inviare un ordine
@app.route('/orders', methods=['GET', 'POST'])
def orders():
    if request.method == 'POST':
        table_number = request.form['table_number']
        items = request.form.getlist('items')
        total_price = calculate_total_price(items)
        order = Order(table_number=table_number, items=items, total_price=total_price, paid=False)
        db.session.add(order)
        db.session.commit()
        return redirect('/orders')

    else:
        orders = Order.query.all()
        return render_template('orders.html', orders=orders)


# funzione per calcolare il prezzo totale dell'ordine
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


@app.route('/orders')
def view_orders():
    return render_template('orders.html', orders=orders)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
