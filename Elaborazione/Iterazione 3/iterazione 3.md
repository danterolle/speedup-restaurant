# Iterazione 3, Analisi

Per l’iterazione 3, sono stati scelti i seguenti requisiti:

- lo scenario principale di successo del caso d’uso UC2 (Gestione degli ordini)

Questo capitolo descrive l’analisi svolta nell’iterazione 3, mentre il capitolo successivo descrive l’attività di progettazione.

# Caso d'uso UC2

### UC2.1 Modello di dominio

In questa iterazione, del caso d’uso UC2 è di interesse lo scenario principale di successo, nella sua interezza. Da esso è possibile identificare le seguenti classi concettuali:

- Cliente: attore primario, che interagisce direttamente con il sistema

- SUR: rappresenta l'applicazione web SpeedUp Restaurant!

- Portata: il piatto che viene ordinato dal cliente

- Prenotazione: accordo in cui si riserva o si garantisce l'utilizzo dei servizi del ristorante

![modello di dominio](./modello%20di%20dominio.png)

### UC2.2 Diagramma di sequenza di sistema

![SSD UC2](./SSD%20UC2.png)

### UC2.3 Contratti delle operazioni

#### scegliPortata

| Operazione                 | scegliPortata()                                                                                                                                                                         |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Riferimenti                | Caso d'uso: Gestione degli ordini                                                                                                                                                       |
| Pre-condizioni             | - Amministratore deve avere abilitato l'accesso alle ordinazioni per il tavolo                                                                                                          |
| Post-condizioni            | - è stata creata una nuova istanza p di portata<br> - gli attributi della portata p sono stati inizializzati<br> - p è stata associatata a Cliente tramite l'associazione elencoPortate |


#### inserimentoPortata

| Operazione                 | inserimentoPortata(idTavolo, listaPortate[Portata])                                                                                                                                                                                                                          |
|----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Riferimenti                | Caso d'uso: Gestione degli ordini                                                                                                                                                                                                                                            |
| Pre-condizioni             | - La lista delle portate non deve essere vuota<br> - deve essere stata creata la mappa elencoOrdini                                                                                                                                                                          |
| Post-condizioni            | - è stata creata l'associazione tra Cliente e SUR denominata elencoOrdini<br> - è stata aggiornata la lista delle portate all'interno di elencoOrdini relativo ad un determinato idTavolo<br> - è stato inviato un messaggio di conferma dell'avvenuta ricezione dell'ordine |

# Iterazione 3, Progettazione

## Diagrammi d'interazione
### Diagrammi di sequenza

![scegliPortata](./SD%20scegliPortata.png)
![inserimentoPortata](./SD%20inserimentoPortata.png)

### Diagrammi delle classi

![diagramma delle classi](./diagramma%20delle%20classi.png)
