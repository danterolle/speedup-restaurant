# Iterazione 1, Analisi

Per l’iterazione 1, sono stati scelti i seguenti requisiti:

- lo scenario principale di successo del caso d’uso UC1 (Inserimento di una nuova prenotazione mediante l'applicazione)

Questo capitolo descrive l’analisi svolta nell’iterazione 1, mentre il capitolo successivo descrive l’attività di progettazione.

## Caso d'uso UC1

### UC1.1 Modello di dominio

In questa iterazione, del caso d’uso UC1 è d'interesse lo scenario principale di successo, nella sua interezza. Da esso è possibile identificare le seguenti classi concettuali:

- Cliente: attore primario, che interagisce direttamente con il sistema

- SUR: rappresenta l'applicazione web SpeedUp Restaurant!

- Tavolo: componente fisico che viene prenotato dal cliente

- Prenotazione: accordo in cui si riserva o si garantisce l'utilizzo dei servizi del ristorante

![modello di dominio](./modello%20di%20dominio.png)

### UC1.2 Diagramma di sequenza di sistema

![SSD UC1](./SSD%20UC1.png)

### UC1.3 Contratti delle operazioni

#### inserimentoPrenotazione

| Operazione                 | inserimentoPrenotazione(nome, cognome, email, cellulare, num_persone, data, ora, note)                                                                                    |
|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Riferimenti                | Caso d'uso: Inserimento di una nuova prenotazione mediante l'applicazione                                                                                                 |
| Pre-condizioni             | -                                                                                                                                                                         |
| Post-condizioni            | - è stata creata una nuova istanza p di prenotazione<br> - gli attributi di p sono stati inizializzati<br> - p è stata associatata a SUR tramite la prenotazione corrente |

#### confermaInserimento

| Operazione                 | confermaPrenotazione()                                                                         |
|----------------------------|------------------------------------------------------------------------------------------------|
| Riferimenti                | Caso d'uso: Inserimento di una nuova prenotazione mediante l'applicazione                      |
| Pre-condizioni             | - è in corso l'inserimento della prenotazione p                                                |
| Post-condizioni            | - è stata associata l'istanza p di prenotazione corrente a SUR tramite l'associazione gestisce |

# Iterazione 1, Progettazione

## Diagrammi d'interazione
### Diagrammi di sequenza

![inserimentoPrenotazione](./SD%20inserimentoPrenotazione.png)
![confermaPrenotazione](./SD%20confermaInserimento.png)

### Diagrammi delle classi

![diagramma delle classi](./diagramma%20delle%20classi.png)

# Iterazione 1, Refactoring

Dopo un'attenta analisi al modello di dominio, si è notato che, per la semplificazione del progetto, la classe Tavolo può essere eliminata
e l'ID del Tavolo può essere reintegrato all'interno della classe Cliente. Una prenotazione può riferirsi solo ad un tavolo.

## UC1.1 Modello di dominio

![modello di dominio](./refactoring/modello%20di%20dominio.png)

## Diagramma delle classi

![diagramma delle classi](./refactoring/diagramma%20delle%20classi.png)

