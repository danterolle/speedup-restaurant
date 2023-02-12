# Iterazione 4, Analisi

Per l’iterazione 4, si è considerata l'estensione del caso d'uso UC2 (Gestione degli ordini).

Il Cliente può modificare il proprio Ordine fino a quando l'Ordine non è passato dallo stato di ordinato allo stato di elaborazione:
1. Il Cliente sceglie l'opzione "modifica ordine"
2. Il Cliente inserisce il codice ID dell'Ordine
3. L'Ordine viene aggiungo in una lista dedicata agli ordini in fase di modifica
4. Il Cliente può aggiungere e/o rimuovere a piacimento le portate dall'Ordine
5. Il sistema registra le modifiche apportate all'Ordine
6. Il sistema indica di aver finito

Questo capitolo descrive l’analisi svolta nell’iterazione 4, mentre il capitolo successivo descrive l’attività di progettazione.

# Estensione Caso d'uso UC2

### UC2.1 Modello di dominio

In questa iterazione viene considerata l'estensione del caso d’uso UC2. Da esso è possibile identificare le seguenti classi concettuali:

- Cliente: attore primario, che interagisce direttamente con il sistema

- SUR: rappresenta l'applicazione web SpeedUp Restaurant!

- Portata: il piatto che viene ordinato dal cliente

- Prenotazione: accordo in cui si riserva o si garantisce l'utilizzo dei servizi del ristorante

![modello di dominio](./modello%20di%20dominio.png)

### UC2.2 Diagramma di sequenza di sistema

![SSD estensione UC2](./SSD%20estensione%20UC2.png)

### UC2.3 Contratti delle operazioni

#### getOrdine

| Operazione      | getOrdine(idTavolo)                    |
|-----------------|----------------------------------------|
| Riferimenti     | Caso d'uso: Gestione degli ordini      |
| Pre-condizioni  | - deve esistere un ordine per idTavolo |
| Post-condizioni | -                                      |

#### modificaOrdine

| Operazione      | modificaOrdine(listaPortate[Portata]) |
|-----------------|---------------------------------------|
| Riferimenti     | Caso d'uso: Gestione degli ordini     |
| Pre-condizioni  | - esiste l'ordine                     |
| Post-condizioni | -                                     |

#### confermaModificaOrdine

| Operazione      | confermaModificaOrdine()                                                                                      |
|-----------------|---------------------------------------------------------------------------------------------------------------|
| Riferimenti     | Caso d'uso: Gestione degli ordini                                                                             |
| Pre-condizioni  | -                                                                                                             |
| Post-condizioni | - è stata eliminata la lista precedente relativa all'idTavolo ed è stata inserita con successo la lista nuova |

# Iterazione 4, Progettazione

## Diagrammi d'interazione
### Diagrammi di sequenza

![getOrdine](./SD%20getOrdine.png)
![modificaOrdine](./SD%20modificaOrdine.png)
![confermaModificaOrdine](./SD%20confermaModificaOrdine.png)

### Diagrammi delle classi

![diagramma delle classi](./diagramma%20delle%20classi.png)
