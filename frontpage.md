# webxlcrf

Sopra puoi fare l'upload del tuo file struttura; si tratta di un file
`.xlsx` che specifica la struttura del dataset desiderato. Puoi
crearlo a partire da questo
[template](https://github.com/lbraglia/xlcrf/raw/main/examples/blank_template.xlsx)
bianco, seguendo le istruzioni di cui sotto. Alcuni esempi possono esser usati come test/ispirazione:
[esempio1](https://github.com/lbraglia/xlcrf/raw/main/examples/esempio1.xlsx),
[esempio2](https://github.com/lbraglia/xlcrf/raw/main/examples/esempio2.xlsx).

In generale un file struttura si compone di:
- tanti **fogli dati** quanti sono quelli desiderati nel file finale;
  in
  [esempio1](https://github.com/lbraglia/xlcrf/raw/main/examples/esempio1.xlsx)
  si ha solamente il foglio `pazienti`, mentre in
  [esempio2](https://github.com/lbraglia/xlcrf/raw/main/examples/esempio2.xlsx)
  (un dataset lievemente più complesso) i fogli `pazienti`, `lesioni`
  e `valutazioni`;
- un foglio `modalita_output`, per gli elenchi/risposte a tendina che si 
  desidereranno implementare nei fogli dati.

### Compilazione dei fogli di dati
Ciascun foglio dati include tante righe quante sono le colonne che si
desidera avere nel file finale. Il contenuto dei campi è di seguito
specificato:
- `variabile`: inserire qui il nome della variabile (minuscolo,
  separata da underscore);
- `tipo`: `intero`, `decimale`, `data` o `ora` per avere i tipi
  numerici; inserire `elenco` per implementare una tendina; inserire
  `testo` per avere un campo senza validazione (es note)
- `id_elenco`: inserire qui l'`id_elenco` di interesse per
  implementare la tendina (rinvenibile nella scheda
  `modalita_output`).
- `criterio`: specifica il check di validazione dati applicato in sede
  di data entry per i tipi numerici. Si può specificare 
  `tra` (compreso tra `minimo` e `massimo`),
  `non compreso tra` (non compreso tra `minimo` e `massimo`),
  `==` (uguale alla colonna `valore`),
  `!=` (diverso dalla colonna `valore`),
  `>` (maggiore della colonna `valore`),
  `<` (minore della colonna `valore`),
  `>=` (maggiore o uguale della colonna `valore`),
  `<=` (minore o uguale della colonna `valore`).
- `valore`: valore da applicare per `criterio` a `==`, `!=`, `>`, `<`, `>=`,
  `<=`;
- `minimo`, `massimo`: valori da applicare per `tra` e `non compreso tra`;
- `input_titolo`: titolo del fumetto di suggerimento (massimo 32 caratteri);
- `input_messaggio`: corpo del testo del fumetto di
  suggerimento. Inserire qui suggerimenti per la compilazione;
- `errore_messaggio`: corpo del testo del messaggio di errore,
  suggerire i vincoli applicati all'inserimento.

### Compilazione `modalita_output`
Si compone di due colonne, `id_elenco` e `modalita` e serve per
implementare le tendine (domande con risposte a scelta da un elenco
predefinito) nel file finale. Se ad esempio desideriamo preparare tre
tipi di tendine, etichettandole `sino` (utilizzabile per diverse domande)
`sesso` e `titstu` compileremo come segue:


| id_elenco | modalita   |
|-----------|------------|
|	sino    |    Sì      |
|   sino    |    No      |
|  sesso    |   Maschio  |
| sesso     |   Femmina  |
| titstu    | elementare |
| titstu    |    media   |
| titstu    |  superiore |
| titstu    | università |

Richiameremo poi gli `id_elenco` dove opportuno nei fogli dati (es
`sino` sarà posto in tutte le domande che vogliamo siano compilabili
con un Sì/No).


### Limitazioni di Excel (ed `xlcrf`)
Nonostante questa webapp permetta la creazione di file molto
funzionali ad una raccolta pulita e veloce dei dati, vi sono alcune
limitazioni insite in Excel e nello strumento retrostante (pacchetto
[xlcrf](https://pypi.org/project/xlcrf/)) di cui è utile essere a
conoscenza.  Per quanto riguarda Excel:
- considerando i formati numerici (intero, decimale, data, ora), se si imposta
  solamente il tipo e non un criterio di accettabilità Excel
  purtroppo non implementa il controllo (questo anche se il file/check
  viene impostato a mano); ossia Excel non è in grado di controllare
  che sia inserito un numero (al posto di una stringa), qualunque esso
  sia.  Un facile workaround è impostare criteri di validazione
  estremamente laschi: ad esempio se si vuole validare che sia una
  data ad essere inserita, si richiede una data `>= 1/1/1900` (detto
  criterio varia in base al caso specifico, ovviamente), per un'ora `>=
  00:00:00` (formato `HH:MM:SS`);
- Excel non effettua validazione su copia/incolla, solo su inserimento
  da tastiera.
Per quanto riguarda `xlcrf`:
- attualmente, per scelta, i file creati dal software controllano
  l'input sino alla riga 10000 (imporre limiti all'inserimento ha un
  costo in termini di dimensione del file creato, maneggevolezza e
  possibilità di corruzione dati). Questo non toglie che si possa
  inserire (in maniera non validata) oltre tale riga, ma se a monte si
  reputa necessaria una tale quantità di righe probabilmente Excel non
  è lo strumento indicato per questa raccolta ed è opportuno valutare
  soluzioni dedicate/ad-hoc.
