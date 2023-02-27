# Iterazione 5, Analisi

Per l’iterazione 5, si è considerato lo scenario principale di successo del caso d’uso UC3 (Gestione dei pagamenti).

Questo capitolo descrive l’analisi svolta nell’iterazione 5, mentre il capitolo successivo descrive l’attività di progettazione.

# Caso d'uso UC3

### UC3.1 Modello di dominio

In questa iterazione viene considerata il caso d’uso UC3. Da esso è possibile identificare le seguenti classi concettuali:

- Cliente: attore primario, che interagisce direttamente con il sistema

- SUR: rappresenta l'applicazione web SpeedUp Restaurant!

- Portata: il piatto che viene ordinato dal cliente

- Prenotazione: accordo in cui si riserva o si garantisce l'utilizzo dei servizi del ristorante

![modello di dominio](./modello%20di%20dominio.png)

### UC3.2 Diagramma di sequenza di sistema

![SSD estensione UC2](./SSD%20UC3.png)

### UC3.3 Contratti delle operazioni

#### visualizzaCostoTotale

| Operazione      | visualizzaCostoTotale(idTavolo)        |
|-----------------|----------------------------------------|
| Riferimenti     | Caso d'uso: Gestione dei pagamenti     |
| Pre-condizioni  | - deve esistere un ordine per idTavolo |
| Post-condizioni | -                                      |

#### effettuaPagamento

| Operazione      | effettuaPagamento(idTavolo)                                                                                           |
|-----------------|-----------------------------------------------------------------------------------------------------------------------|
| Riferimenti     | Caso d'uso: Gestione dei pagamenti                                                                                    |
| Pre-condizioni  | - esiste l'ordine                                                                                                     |
| Post-condizioni | - è stato eliminato l'ordine con l'idTavolo specificato<br> - è stato ricevuto un messaggio di conferma del pagamento |

# Iterazione 5, Progettazione

## Diagrammi d'interazione
### Diagrammi di sequenza

![visualizzaCostoTotale](./SD%20visualizzaCostoTotale.png)
![effettuaPagamento](./SD%20effettuaPagamento.png)

### Diagrammi delle classi

![diagramma delle classi](./diagramma%20delle%20classi.png)
