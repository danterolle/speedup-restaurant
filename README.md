# SpeedUp Restaurant!

Iterazioni da approfondire

* Prenotazione dei tavoli
* Gestione degli ordini
* Contabilità

## Prenotazione dei tavoli:

Il Cliente può prenotare il tavolo tramite l'applicazione web.

Il Cliente può chiamare l'Amministratore al ristorante per la prenotazione.

Il Cliente prenota il tavolo sul posto.

L'Amministratore gestisce le prenotazioni dall'applicazione web.

## Gestione degli ordini:

Il Cliente sceglie una o più portate tramite un menù.

Il Cliente conferma l'Ordine tramite l'applicazione web.

L'Ordine viene ricevuto dal Cuoco.

Il Cuoco elabora l'Ordine.

L'Ordine viene consegnato al Cliente.

## Contabilità

Il Cliente decide se pagare dall'applicazione web oppure in cassa.

L'Amministratore gestisce il pagamento degli ordini che avviene in contanti.


## 1.1 Introduzione

SpeedUp Restaurant! è un'applicazione web che offre delle funzionalità per automatizzare la gestione delle prenotazioni dei tavoli, la gestione degli ordini e la contabilità di un ristorante. 
I clienti possono prenotarsi in vari modi: 

- chiamando l'amministratore del ristorante comunicando il cognome, numero di persone, data e ora.
- usando l'applicazione web seguendo due passaggi in sequenza, in primis scegliendo il numero di persone, la data, l'orario e in secundis aggiungendo cognome, telefono, email.

Eventuali note sono opzionali ma possono essere comunicate in tutte e due le modalità. Inoltre il cliente ha la libertà di prenotare il proprio tavolo direttamente sul posto. Ogni modalità di prenotazione viene comunque gestita dall'amministratore che interagisce col software.

I clienti, una volta seduti al tavolo, possono visionare le portate direttamente dall'applicazione web e scegliere le categorie e le portate del menù da inserire all'interno del proprio ordine. Il cuoco elabora l'ordine ricevuto che successivamente viene consegnato al cliente. Il cliente può decidere di inviare un ordine e aggiungerlo a quello precedente. Eventualmente può anche modificare l'ordine già in lista.
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

- L'Amministratore del locale: gestire le prenotazioni e l'eventuale contabilità

### 5. Riepilogo delle caratteristiche del sistema

Il sistema deve possedere le seguenti caratteristiche:

- Permettere la prenotazione dei tavoli
- L'invio dell'email con i dati della prenotazione tramite codice QR
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
| Amministratore | Gestore delle prenotazioni e della contabilità della struttura                  |
| Cliente        | L'utente che usufruisce dei servizi di ristorazione                             |
| Cuoco          | La persona incaricata di elaborare gli ordini                                   |

## Modello dei casi d'uso

### 1. Requisiti

SpeedUp Restaurant! è un'applicazione web per la gestione di ristoranti. L'applicazione deve occuparsi della gestione delle prenotazioni e degli ordini dei Clienti e anche della contabilità.

SpeedUp Restaurant! permette ai Clienti di prenotare un tavolo della struttura ed effettuare uno o più ordini. L'applicazione deve occuparsi della gestione del ristorante:

- Inserimento di una nuova prenotazione con i relativi dati del Cliente.
- Aggiornamento della prenotazione con modifica di orario, data e numero di persone o eventuale annullamento.
- Consentire all'Amministratore di ricevere e visualizzare le prenotazioni per nome del Cliente, data e orario.
- Consentire all'Amministratore di ricevere e visualizzare gli ordini per tavolo.
- Permettere al Cliente di inviare e modificare l'Ordine finché esso non sia stato commissionato al Cuoco.
- Gestione del pagamento da parte del Cliente tramite l'applicazione o in cassa.
- Consentire all'Amministratore di ricevere e visualizzare i pagamenti per nome del Cliente, data e orario.

### 2. Obiettivi e casi d'uso

### 3. Casi d'uso

Tra tutti i casi d’uso individuati, si è scelto di fornire una descrizione in formato dettagliato per i seguenti casi d’uso:

- Inserimento di una nuova prenotazione
- Gestione degli ordini
- Gestione dei pagamenti

Per i restanti casi d’uso si fornisce una descrizione in formato breve.

### UC1: Inserimento di una nuova prenotazione mediante l'applicazione

| Nome del caso d'uso              | UC1: Inserimento di una nuova prenotazione              |
|----------------------------------|---------------------------------------------------------|
| Portata                          | Applicazione SpeedUp Restaurant!                        |
| Livello                          | Obiettivo utente                                        |
| Attore primario                  | Cliente                                                 |
| Parti interessate e interessi    | - Cliente: vuole inserire una nuova prenotazione<br> - Applicazione SpeedUp Restaurant!: registra le informazioni relative alla prenotazione |
| Pre-condizioni                   | Il Cliente deve avere l'accesso ad un browser web e un'email |
| Garanzia di successo             | L'inserimento dei dati relativi alla prenotazione è andato a buon fine. Il sistema ha registrato le informazioni sulla prenotazione |
| Scenario principale di successo  | 1. Il Cliente vuole inserire una nuova prenotazione<br> 2. Il Cliente sceglie l'opzione "Prenota un tavolo"<br> 3. Il Cliente inserisce email, numero di telefono, nome, cognome, numero di persone, data e ora<br> 4. Il sistema registra le informazioni della prenotazione<br> 5. Il sistema genera un codice QR ad ogni nuova prenotazione<br> 6. Il sistema invia il codice QR contente i dati della prenotazione all'email del Cliente<br> 7. Il sistema indica di aver finito |
| Estensione                       | Il Cliente può modificare la prenotazione fino a 2 (due) ore prima dell'orario immesso:<br> 1. Il Cliente sceglie l'opzione "modifica prenotazione"<br> 2. Il Cliente sceglie la prenotazione da modificare<br> 3. Il Cliente può modificare l'orario, la data e il numero di persone<br> 4. Il sistema registra le modifiche apportate alla prenotazione<br> 5. Il sistema indica di aver finito |
| Frequenza di ripetizione | Potrebbe essere ininterrotta |

### UC2: Gestione degli ordini

| Nome del caso d'uso              | UC2: Gestione degli ordini                              |
|----------------------------------|---------------------------------------------------------|
| Portata                          | Applicazione SpeedUp Restaurant!                        |
| Livello                          | Obiettivo utente                                        |
| Attore primario                  | Cliente                                                 |
| Parti interessate e interessi    | - Cliente: visiona e sceglie le portate dal menù<br> - Applicazione SpeedUp Restaurant!: registra le informazioni relative all'Ordine<br> - Cuoco: elabora l'Ordine<br> - Addetto: consegna l'Ordine elaborato |
| Pre-condizioni                   | Il Cliente è prenotato e deve essere connesso alla rete internet per visualizzare il menù |
| Garanzia di successo             | L'inserimento di un nuovo Ordine è andato a buon fine. Il sistema ha registrato le informazioni all'Ordine e l'Ordine è stato elaborato |
| Scenario principale di successo  | 1. Il Cliente accede all'applicazione web<br> 2. Il Cliente sceglie l'opzione "visualizza menù"<br> 3. Il Cliente sceglie le varie portate<br> 4. Il Cliente effettua l'Ordine<br> 5. Il sistema registra le informazioni relative all'Ordine<br> 6. Il sistema conferma la ricezione dell'Ordine mostrandolo al Cliente tramite un ID<br> 7. L'Ordine viene inserito nella lista degli ordini da elaborare del Cuoco<br> 8. Il Cuoco elabora l'Ordine<br> 9. Il Cuoco comunica all'Addetto di aver elaborato l'Ordine<br> 10. L'Addetto consegna l'Ordine al Cliente<br> 11. L'Addetto aggiorna la lista degli ordini consegnati |
| Estensione                       | Il Cliente può modificare il proprio Ordine fino a quando l'Ordine non è passato dallo stato di ordinato allo stato di elaborazione:<br> 1. Il Cliente sceglie l'opzione "modifica ordine"<br> 2. Il Cliente inserisce il codice ID dell'Ordine<br> 3. L'Ordine viene aggiungo in una lista dedicata agli ordini in fase di modifica<br> 4. Il Cliente può aggiungere e/o rimuovere a piacimento le portate dall'Ordine<br> 5. Il sistema registra le modifiche apportate all'Ordine<br> 6. Il sistema indica di aver finito |
| Requisiti speciali | L'operazione di modifica dell'Ordine non deve superare i 10 minuti |
| Frequenza di ripetizione | Circa 100 ordini al giorno |

### UC3: Gestione dei pagamenti

| Nome del caso d'uso              | UC3: Gestione dei pagamenti                             |
|----------------------------------|---------------------------------------------------------|
| Portata                          | Applicazione SpeedUp Restaurant!                        |
| Livello                          | Obiettivo utente                                        |
| Attore primario                  | Cliente                                          |
| Parti interessate e interessi    | - Cliente: paga l'Ordine<br> - Applicazione SpeedUp Restaurant!: registra le informazioni relative al pagamento<br> - Amministratore: registra le informazioni del pagamento all'interno dell'applicazione se esso avviene in contanti |
| Pre-condizioni                   | Il Cliente deve avere effettuato almeno un Ordine |
| Garanzia di successo             | Il pagamento è andato a buon fine. Il sistema ha registrato le informazioni del pagamento |
| Scenario principale di successo  | 1. Il Cliente accede all'applicazione web<br> 2. Il Cliente sceglie l'opzione "paga ordine"<br> 3. Il Cliente visualizza il costo totale dell'Ordine<br> 4. Il Cliente sceglie la modalità di pagamento<br> 5. Il Cliente effettua il pagamento<br> 6. Il sistema registra le informazioni dell'avvenuto pagamento<br> 7. Il sistema invia per email una ricevuta del pagamento<br> 8. Il sistema indica di aver finito |
| Estensione                       | Il Cliente può decidere di pagare in contanti:<br> 1. Il Cliente si reca in cassa<br> 2. Il Cliente comunica il codice ID dell'Ordine all'Amministratore<br> 3. Il Cliente effetta il pagamento in contanti<br> 4. L'Amministratore registra i dati del pagamento nel sistema<br> 5. L'Amministratore indica di aver finito |
| Elenco delle varianti tecnologiche e dei dati | Il Cliente può scegliere di effettuare il pagamento mediante carta Mastercard, VISA o PayPal |
| Frequenza di ripetizione | Circa 100 pagamenti al giorno |

### UC4: Inserimento di una nuova prenotazione in loco

Il Cliente ha la possibilità di effettuare una prenotazione di persona direttamente sul posto.

### UC5: Inserimento di una nuova prenotazione tramite telefonata

Il Cliente può chiamare il ristorante e comunicare all'Addetto la prenotazione.

### UC6: Annullamento della prenotazione

Il Cliente può decidere di annullare una prenotazione relativa al proprio tavolo.

### UC7: Visualizzazione delle prenotazioni

L'Addetto ha la possibilità di visualizzare le prenotazioni relative ai tavoli e i dati inseriti dal Cliente.

### UC8: Visualizzazione dei pagamenti

L'Amministratore può visualizzare gli ordini da pagare e/o pagati.

## Regole di dominio

| ID | Regola | Modificabilità | Sorgente | 
|----|--------|----------------|----------|
| R1 | Se la prenotazione è effettuata nei giorni festivi, viene applicato un sovrapprezzo del 10% su tutti gli ordini | Bassa | Politica interna del ristorante | 
| R2 | Se la prenotazione avviene nei giorni feriali, viene applicato uno sconto del 5% su ogni ordine che superi i 10 euro | Bassa | Politica interna del ristorante | 
| R3 | Se la prenotazione viene disdetta 10 minuti prima dell'effettivo orario comunicato, il Cliente viene inserito nella blocklist per 30 giorni | Bassa | Politica interna del ristorante |