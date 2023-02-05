# Iterazione 1, Analisi

Per l’iterazione 1, sono stati scelti i seguenti requisiti:

- lo scenario principale di successo del caso d’uso UC1 (Inserimento di una nuova prenotazione mediante l'applicazione)

Questo capitolo descrive l’analisi svolta nell’iterazione 1, mentre il capitolo successivo descrive l’attività di progettazione.

## Caso d'uso UC1

### UC1.1 Modello di dominio

In questa iterazione, del caso d’uso UC1 è di interesse lo scenario principale di successo, nella sua interezza. Da esso è possibile identificare le seguenti classi concettuali:

- Cliente: attore primario, che interagisce direttamente con il sistema

- SUR: rappresenta l'applicazione web SpeedUp Restaurant!

- Tavolo: componente fisico che viene prenotato dal cliente

- Prenotazione: accordo in cui si riserva o si garantisce l'utilizzo dei servizi del ristorante

### UC1.2 Caso d’uso UC1, Diagramma di sequenza di sistema

![nome_immagine](URL_immagine)

### UC1.3 Caso d'uso UC1, contratti delle operazioni

| Contratti delle operazioni |                                                                                                                                                                           |
|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Operazione                 | inserimentoPrenotazione(nome, cognome, email, cellulare, num_persone, data, ora, note)                                                                                    |
| Riferimenti                | Caso d'uso: Inserimento di una nuova prenotazione mediante l'applicazione                                                                                                 |
| Pre-condizioni             | -                                                                                                                                                                         |
| Post-condizioni            | - è stata creata una nuova istanza p di prenotazione<br> - gli attributi di p sono stati inizializzati<br> - p è stata associatata a SUR tramite la prenotazione corrente |

# Iterazione 1, Progettazione