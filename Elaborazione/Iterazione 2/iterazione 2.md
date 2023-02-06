# Iterazione 2, Analisi

Per l’iterazione 2, si è considerata l'estensione del caso d'uso UC1 (Inserimento di una nuova prenotazione mediante l'applicazione).

Il Cliente può modificare la prenotazione fino a due ore prima dell'orario immesso:
1. Il Cliente sceglie l'opzione "modifica prenotazione"
2. Il Cliente sceglie la prenotazione da modificare
3. Il Cliente può modificare l'orario, la data e il numero di persone
4. Il sistema registra le modifiche apportate alla prenotazione
5. Il sistema indica di aver finito  

Si rende noto che, in fase implementativa, sarebbe possibile creare una lista apposita per la gestione delle prenotazioni in stato di modifica.

Questo capitolo descrive l’analisi svolta nell’iterazione 2, mentre il capitolo successivo descrive l’attività di progettazione.

## Caso d'uso UC1

### UC1.1 Modello di dominio

In questa iterazione, del caso d’uso UC1 è d'interesse lo scenario principale di successo, nella sua interezza. Da esso è possibile identificare le seguenti classi concettuali:

- Cliente: attore primario, che interagisce direttamente con il sistema

- SUR: rappresenta l'applicazione web SpeedUp Restaurant!

- Tavolo: componente fisico che viene prenotato dal cliente

- Prenotazione: accordo in cui si riserva o si garantisce l'utilizzo dei servizi del ristorante

![modello di analisi](./modello%20di%20analisi.png)

### UC1.2 Diagramma di sequenza di sistema

![SSD UC1](./SSD%20estensione%20UC1.png)

### UC1.3 Contratti delle operazioni

#### getPrenotazione

| Contratti delle operazioni |                                                                           |
|----------------------------|---------------------------------------------------------------------------|
| Operazione                 | getPrenotazione(cod)                                                      |
| Riferimenti                | Caso d'uso: Inserimento di una nuova prenotazione mediante l'applicazione |
| Pre-condizioni             | -                                                                         |
| Post-condizioni            | -                                                                         |

#### modificaPrenotazione

| Contratti delle operazioni |                                                                           |
|----------------------------|---------------------------------------------------------------------------|
| Operazione                 | modificaPrenotazione(data, ora, num_persone)                              |
| Riferimenti                | Caso d'uso: Inserimento di una nuova prenotazione mediante l'applicazione |
| Pre-condizioni             | - esiste la prenotazione                                                  |
| Post-condizioni            | -                                                                         |

#### confermaModificaPrenotazione

| Contratti delle operazioni |                                                                                              |
|----------------------------|----------------------------------------------------------------------------------------------|
| Operazione                 | confermaModificaPrenotazione()                                                               |
| Riferimenti                | Caso d'uso: Inserimento di una nuova prenotazione mediante l'applicazione                    |
| Pre-condizioni             | - sono stati modificati i dettagli di una prenotazione                                       |
| Post-condizioni            | - la prenotazione, contenuta nell'elenco delle prenotazioni, è stata aggiornata con successo |

# Iterazione 2, Progettazione

## Diagrammi d'interazione
### Diagrammi di sequenza

![getPrenotazione](./SD%20getPrenotazione.png)
![modificaPrenotazione](./SD%20modificaPrenotazione.png)
![confermaModificaPrenotazione](./SD%20confermaModificaPrenotazione.png)

### Diagrammi delle classi

![modello di progettazione](./modello%20di%20progettazione.png)