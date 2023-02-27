# SpeedUp Restaurant!

Progetto per l'esame di Ingegneria del Software.

## Table of Contents

1. [Get Started](#get-started)
2. [Setup](#setup)
3. [File Structure](#file-structure)
4. [How to start it](#how-to-start-it)
5. [Unit Testing](#unit-testing)

## Get Started

Per la fase di elaborazione sono presenti diverse iterazioni, ognuna delle quali contiene una cartella dedicata 
all'implementazione di ogni componente dell'applicazione. Dentro ogni cartella si può trovare un file `.asta` per i diagrammi UML e tutti gli screenshot riguardanti la progettazione.

Riassumendo, dentro ogni cartella **iterazione** si troverà:

````
├── Iterazione 3
│  ├── Iterazione3.asta
│  ├── SD inserimentoPortata.png
│  ├── SD scegliPortata.png
│  ├── SSD UC2.png
│  ├── diagramma delle classi.png
│  ├── iterazione 3.md
│  ├── modello di dominio.png
│  └── project
````

Nell'iterazione 5 sono state aggiunte tutte le funzionalità specificate nei casi d'uso rimanenti ma non analizzati nel dettaglio come i primi tre.
È possibile vedere le due regole di dominio R1 ed R2 applicate nei file riguardanti l'iterazione 5, in particolare nel metodo `visualizzaCostoTotale` contenuto dentro `sur.py`, dove R1 ed R2 sono state aggiunte e commentate. 

## Setup

Ogni parte di questa applicazione è stata interamente scritta in Python 3.10 (con l'ausilio di Pycharm per la gestione e il test dell'applicazione) su piattaforme MacOS e Ubuntu,
quindi per prima cosa occorrerà installare Python 3.10 (o versione 3 precedente/successiva come Python 3.11). 
Essendo scritta in puro Python, non necessita di librerie esterne ad eccezione di `qrcode` in quanto necessaria per la creazione di un codice QR.

Seppur non necessario, è consigliato l'uso di un ambiente virtuale come venv per ogni iterazione, ad esempio:

````
$ cd speedup-restaurant/Elaborazione/Iterazione 3/project/iterazione3
$ python3.10 -m venv venv
$ source venv/bin/activate
````

Per installare il modulo `qrcode`, si può procedere da Pycharm stesso oppure da terminale usando il package manager `pip` nella versione 3:

````
$ pip3 install qrcode
````

Nei successivi sottocapitoli verrà mostrato come avviare e testare l'applicazione per ogni iterazione. 

### File Structure

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

## How to start it

Dopo il setup iniziale, basta semplicemente navigare all'interno della cartella riguardante l'iterazione che si desidera provare, ad esempio:

````
$ cd speedup-restaurant/Elaborazione/Iterazione 3/project/iterazione3
````

E usare Python per avviarla

````
$ python3.10 app.py
````

## Unit Testing

Per quanto riguarda le unit tests si è usato il framework unittest e si possono provare dal terminale (oppure da Pycharm stesso) seguendo questi step:

````
$ cd speedup-restaurant/Elaborazione/Iterazione 3/project/iterazione3
$ python3.10 -m unittest test_app.TestCliente.test_cliente
````

- `test_app` è il file a cui si accede.
- `TestCliente` è la classe che conterrà i test relativi a quella specifica classe.
- `test_client` è il nome specifico della unit test da provare.

Output previsto:

````
╭─ ~/Py/speedup-restaurant/Elaborazione/Iterazione 3/project/iterazione3
╰─ python3.10 -m unittest test_app.TestCliente.test_cliente          
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
````

Altro esempio:

````
$ python3.10 -m unittest test_app.TestSUR.test_inserimentoPrenotazione
````

**Nota importante**: le unit tests sono state provate singolarmente e non tutte insieme, ogni metodo è stato provato indipendentemente dagli altri per assicurare un corretto e stabile funzionamento.
