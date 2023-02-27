# SpeedUp Restaurant!

## Get Started

Per la fase di elaborazione sono presenti diverse iterazioni, ognuna delle quali contiene una cartella dedicata 
all'implementazione di ogni componente dell'applicazione. Dentro ogni cartella si può trovare un file .asta per i diagrammi UML e tutti gli screenshot riguardanti la progettazione.

Nell'iterazione 5 sono state aggiunte tutte le funzionalità specificate nei casi d'uso rimanenti ma non analizzati nel dettaglio come i primi tre.
È possibile vedere le due regole di dominio R1 ed R2 applicate nei file riguardanti l'iterazione 5, in particolare nel metodo visualizzaCostoTotale, dove R1 ed R2 sono state aggiunte e commentate. 

## How to use

Ogni parte di questa applicazione è stata interamente scritta in Python 3.10 (con l'ausilio di Pycharm per la gestione e il test dell'applicazione) su piattaforme MacOS e Ubuntu,
quindi per prima cosa occorrerà installare Python 3.10 (o versione 3 precedente/successiva). Essendo scritta in puro Python, non necessita di librerie esterne ad eccezione di `qrcode` in quanto necessaria per la creazione di un codice QR.

In tal caso, si può installa da Pycharm stesso, oppure da terminale usando il package manager `pip`:

````
$ pip3 install qrcode
````

Seppur non necessario, è consigliato l'uso di un ambiente virtuale come venv per ogni iterazione, ad esempio:

````
$ cd speedup-restaurant/Elaborazione/Iterazione 3/project/iterazione3
$ python3 -m venv venv
$ source venv/bin/activate
````

Nei successivi sottocapitoli verrà mostrato come avviare e testare l'applicazione per ogni iterazione. 

### File structure

Esempio della struttura del progetto di ogni singola iterazione:

````
project
└── iterazione3
    ├── __init__.py # necessario per inizializzare variabili e oggetti necessari al funzionamento dell'applicazione
    ├── app.py # contiene il menu dal quale è possibile provare SpeedUp Restaurant!
    ├── cliente.py # contiene la classe Cliente
    ├── portata.py # contiene la classe Portata
    ├── prenotazione.py # contiene la classe Prenotazione
    ├── sur.py # contiene il core dell'applicativo, tutti i metodi e relativi commenti
    └── test_app.py # contiene tutte le unit tests
````

### Start it

Dopo il setup iniziale, basta semplicemente navigare all'interno della cartella riguardante l'iterazione che si desidera provare, ad esempio:

````
$ cd speedup-restaurant/Elaborazione/Iterazione 3/project/iterazione3
````

E usare Python per avviarla

````
$ python3 app.py
````

## Unit test

Per quanto riguarda le unit tests, a parte l'uso grafico di Pycharm, si possono provando dal terminale seguendo questi step:

````
$ python3 -m unittest test_app.TestCliente.test_cliente
````

- `test_app` è il file a cui si accede.
- `TestCliente` è la classe che conterrà i test relativi a quella specifica classe.
- `test_client` è il nome specifico della unit test da provare.

Output previsto:

````
╭─ ~/Py/speedup-restaurant/Elaborazione/Iterazione 3/project/iterazione3
╰─ python3 -m unittest test_app.TestCliente.test_cliente          
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
````

**Nota importante**: le unit test sono state provate singolarmente e non tutte insieme, ogni funzione è stata provata indipendentemente dalle altre per assicurare un corretto e stabile funzionamento.
