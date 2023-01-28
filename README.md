# SpeedUp Restaurant!

Iterazioni da approfondire

* Prenotazione dei tavoli
* Gestione degli ordini
* Contabilità

## Prenotazione dei tavoli:

Il Cliente può chiamare l'Addetto al Ristorante che si occupa delle prenotazioni.

Il Cliente può inviare una email seguendo un form di contatto all'indirizzo email del ristorante.

Il Cliente può prenotare il tavolo tramite un'applicazione web.

Il Cliente prenota il tavolo sul posto.

L'Addetto gestisce le prenotazioni tramite un indirizzo email oppure dall'applicazione web.

## Gestione degli ordini:

L'Addetto può decidere la categoria e le portate del proprio menù.

Il Cliente sceglie una o più portate tramite un menù.

Il Cliente invia l'Ordine all'Addetto tramite l'applicazione web.

L'Ordine viene ricevuto dall'Addetto che comunica le portate al Cuoco.

Il Cuoco elabora l'ordine.

L'Ordine viene consegnato al Cliente.

## Contabilità

Il Cliente decide se pagare dall'applicazione web oppure in cassa.

L'Amministratore gestisce il pagamento degli ordini, che avviene in contanti o via POS.


## 1.1 Introduzione

SpeedUp Restaurant! è un'applicazione web che offre delle funzionalità per automatizzare la gestione delle prenotazioni dei tavoli, la gestione degli ordini e la contabilità di un ristorante. 
I clienti possono prenotarsi in vari modi: 

- chiamando l'addetto del ristorante comunicando il cognome, numero di persone, data e ora.
- compilando un form di contatto predefinito contenente email, nome, cognome, numero di persone, data e ora.
- usando l'applicazione web seguendo due passaggi in sequenza, in primis scegliendo il numero di persone, la data, l'orario e in secundis aggiungendo cognome, telefono, email. 

Eventuali note sono opzionali ma possono essere comunicate in tutte e tre le modalità. Inoltre il cliente ha la libertà di prenotare il proprio tavolo direttamente sul posto. Ogni modalità di prenotazione viene comunque gestita dall'addetto che interagisce col software.

I clienti, una volta seduti al tavolo, possono visionare le portate direttamente dall'applicazione web e scegliere le categorie e le portate del menù da inviare all'addetto e di conseguenza comunicate al cuoco. Un ordine può riferirsi ad una o più persone. Il cuoco elabora l'ordine ricevuto che successivamente viene consegnato al cliente. Il cliente può decidere di inviare un nuovo ordine e aggiungerlo a quello precedente.
L'ordine precedentemente inviato genera automaticamente il costo totale, specificando il costo di ogni singola portata. Il cliente può decidere se effettuare il pagamento dall'applicazione web o direttamente in cassa.


## Documento di visione

### 1. Cronologia revisioni

### 2. Introduzione

Prevediamo la realizzazione di un’applicazione web di gestione per ristoranti, chiamata "SpeedUp Restaurant!", in grado di supportare la flessibilità delle regole di dominio. L’obiettivo dell’applicazione web è gestire la prenotazione di tavoli, la gestione degli ordini dei clienti e la contabilità di ciascun tavolo.

### 3. Posizionamento

#### 3.1 Opportunità di business

L'applicazione web si pone l’obiettivo di sostituire i tradizionali metodi di gestione non automatizzati dei ristoranti. In questo modo sarà possibile gestire dinamicamente la prenotazione dei tavoli, degli ordini e del pagamento.

#### 3.2 Formulazione del problema

Qualsiasi genere di ristorante potrebbe avere il problema di gestire un certo numero di prenotazioni e ordinazioni e quindi causare rallentamenti nel soddisfacimento del cliente rendendo problematica anche la gestione del personale e peggiorando la reputazione del locale.

#### 3.3. Formulazione della posizione del prodotto

Il software è rivolto ai ristoranti interessati ad automatizzare il loro sistema di gestione.

### 4. Descrizione delle parti interessate

#### 4.1 Obiettivi a livello dell’utente

Gli utenti necessitano di un sistema che soddisfi i seguenti obiettivi:

- l'Addetto: gestisce le prenotazioni e gli ordini
- L'Amministratore del locale: gestire la contabilità

### 5. Riepilogo delle caratteristiche del sistema

Il sistema deve possedere le seguenti caratteristiche:

- Permettere la prenotazione dei tavoli
- L'invio dell'email con i dati della prenotazione
- Visualizzazione della prenotazione
- Gestione e visualizzazione degli ordini
- Gestione del pagamento

## Glossario

| Termine        | Definizione                                                                     |
|----------------|---------------------------------------------------------------------------------|
| Tavolo         | Entità fisica che viene prenotata dal Cliente                                   |
| Prenotazione   | Accordo in cui si riserva o si garantisce l'utilizzo dei servizi del ristorante |
| Ordine         | Insieme di portate richieste dal Cliente                                        |
| Portata        | Un piatto servito in un determinato momento durante un pasto                    |
| Amministratore | Gestore della contabilità della struttura                                       |
| Addetto        | Gestore delle prenotazioni e delle ordinazioni                                  |
| Cliente        | L'utente che usufruisce dei servizi di ristorazione                             |
| Cuoco          | La persona incaricata di elaborare gli ordini                                   |

## Modello dei casi d'uso

### 1. Requisiti

SpeedUp Restaurant! è un'applicazione web per la gestione di ristoranti. L'applicazione deve occuparsi della gestione delle prenotazioni e degli ordini dei Clienti e anche della contabilità.

SpeedUp Restaurant! permette ai Clienti di prenotare un tavolo della struttura ed effettuare uno o più ordini. L'applicazione deve occuparsi della gestione del ristorante:

- Inserimento di una nuova prenotazione con i relativi dati del Cliente.
- Aggiornamento della prenotazione con modifica di orario, data e numero di persone o eventuale annullamento.
- Consentire all'Addetto di ricevere e visualizzare le prenotazioni per nome del Cliente, data e orario.
- Consentire all'Addetto di ricevere e visualizzare gli ordini per tavolo.
- Permettere al Cliente di inviare e modificare l'ordine finché esso non sia stato commissionato al Cuoco.
- Gestione del pagamento da parte del Cliente tramite l'applicazione o in cassa.
- Consentire all'Amministratore di ricevere e visualizzare i pagamenti per nome del Cliente, data e orario.

### 2. Obiettivi e casi d'uso

### 3. Casi d'uso

Tra tutti i casi d’uso individuati, si è scelto di fornire una descrizione in formato dettagliato per i seguenti casi d’uso:

- Inserimento di una nuova prenotazione
- Gestione degli ordini
- Gestione dei pagamenti

Per i restanti casi d’uso si fornisce una descrizione in formato breve.

### UC1: Inserimento di una nuova prenotazione
### UC2: Gestione degli ordini
### UC3: Gestione dei pagamenti

### UC4: Aggiornamento della prenotazione

Il Cliente può decidere di modificare o annullare una prenotazione relativa al proprio tavolo.

### UC5: Visualizzazione delle prenotazioni

L'Addetto ha la possibilità di visualizzare le prenotazioni relative ai tavoli e i dati inseriti dal Cliente.

### UC6: Visualizzazione dei pagamenti

L'Amministratore può visualizzare gli ordini da pagare e/o pagati.

## Regole di dominio