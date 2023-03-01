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

Le unit tests riguardanti le classi Cliente e Prenotazione mirano a testare la corretta inizializzazione degli oggetti Cliente e Prenotazione, verificando che i valori degli attributi corrispondano a quelli attesi.

Quelle invece riguardanti la classe SUR si assicurano di:

- `test_singleton` verifica che il metodo getInstance() restituisca sempre lo stesso oggetto. Questo assicura che l'oggetto SUR sia implementato come un singleton, ovvero che ne esista sempre una sola istanza all'interno dell'applicazione.
- `test_inserimentoPrenotazione` verifica che il metodo inserimentoPrenotazione() aggiunga correttamente una nuova prenotazione all'interno dell'oggetto SUR. In particolare, verifica che la lunghezza dell'elenco delle prenotazioni aumenti di uno dopo l'inserimento di una nuova prenotazione. 
- `test_confermaInserimento` verifica che il metodo registri correttamente la conferma di una prenotazione, usa il metodo assertLogs() per verificare che il metodo confermaInserimento() registri correttamente un messaggio di log con il livello di log "INFO". Viene poi verificato che il messaggio di log contenga le informazioni relative alla prenotazione confermata, come l'id della prenotazione, la data, l'ora, il numero di persone e i dati del cliente.
- `test_generaCodiceQR` verifica che il metodo crei correttamente un file contenente il codice QR relativo alla prenotazione appena inserita. Invoca il metodo generaCodiceQR() della classe SUR, il quale dovrebbe generare un file `.png` contenente il codice QR della prenotazione appena inserita. Viene poi verificato che il file è stato effettivamente creato, verificando che il path del file esista effettivamente.
- `test_elencaPrenotazioni` dove vengono inserite due prenotazioni di esempio utilizzando il metodo inserimentoPrenotazione(), quindi si verifica che l'output di elencaPrenotazioni sia uguale a quello atteso. L'output atteso viene definito nella variabile expected_output. Per catturare l'output del metodo elencaPrenotazioni, si utilizza la classe io.StringIO e il metodo redirect_stdout.
- `test_cercaPrenotazione` qui viene inserita una prenotazione per un cliente di nome "Mario Rossi" e viene effettuata una ricerca sulla base dell'email fornita al momento della prenotazione. Se la ricerca ha esito positivo, vengono confrontati i dati della prenotazione trovata con quelli attesi, mediante una serie di asserzioni, per verificare che siano corretti.
- `test_modificaPrenotazione` dopo essere stata inserita una prenotazione con dati specifici poi viene effettuata una modifica alla prenotazione, cambiando l'orario e l'ID del tavolo. Successivamente, viene verificato che i dati della prenotazione siano stati modificati correttamente attraverso l'utilizzo del metodo cercaPrenotazione.
- `test_inserimentoPortata` dopo essere state inserite delle prenotazioni, successivamente vengono inserite anche delle portate per due tavoli diversi. Viene poi inserita una portata già esistente per il primo tavolo, in modo da verificare che l'inserimento di portate esistenti non crei duplicati. Infine, vengono verificati alcuni attributi delle portate inserite nei tavoli, come l'ID, il nome e il prezzo, per assicurarsi appunto che siano corretti.
- `test_modificaOrdine` controlla se la funzione modificaOrdine modifica correttamente l'ordine di un tavolo, rimuovendo o aggiungendo portate. Il test inizia inserendo una prenotazione e delle portate in un tavolo, e poi esegue una modifica all'ordine di quel tavolo. Alla fine viene verificato che le modifiche siano state effettuate correttamente.
- `test_visualizzaCostoTotale` qui vengono effettuate alcune operazioni sul sistema, come l'inserimento di prenotazioni, l'inserimento di portate e la modifica dell'ordine di una prenotazione. Successivamente, viene richiamata la funzione visualizzaCostoTotale per le prenotazioni 1 e 2, e i risultati vengono confrontati con dei valori attesi usando l'asserzione assertEqual.
- `test_visualizzaCostoTotaleUpdated` questa unit test è uguale alla precedente, ma in più vengono verificate le funzionalità nel calcolare il costo totale di un ordine, rispettando le regole di dominio R1 e R2.
- `test_effettuaPagamento` qui viene inserita una prenotazione e una portata, poi viene modificato l'ordine aggiungendo una portata. Il test calcola il costo totale dell'ordine e quindi esegue il pagamento. Infine, il test verifica che il costo totale dell'ordine sia uguale al prezzo delle portate e che il pagamento sia stato effettuato con successo.
- `test_annullaPrenotazione` dopo aver inserito una prenotazione, essa poi viene annullata fornendo l'email del cliente associata alla prenotazione stessa. Successivamente, viene verificato che la lista di prenotazioni del sistema SUR sia ridotta di una sola prenotazione rispetto a quella iniziale.
- `test_visualizzaPagamenti` crea una prenotazione con una portata e un pagamento, e verifica che il metodo visualizzaPagamenti() restituisca None. Se il test fallisse, significherebbe che il metodo visualizzaPagamenti() non restituisce il valore atteso.

Per quanto riguarda lo sviluppo delle unit tests si è usato il framework **unittest** e si possono provare dal terminale (oppure da Pycharm stesso) seguendo questi step:

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
