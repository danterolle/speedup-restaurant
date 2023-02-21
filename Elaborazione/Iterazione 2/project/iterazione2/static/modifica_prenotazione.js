function modificaPrenotazione(id) {
  var num_persone = document.getElementById('num_persone').value;
  var data = document.getElementById('data').value;
  var ora = document.getElementById('ora').value;

  var xhr = new XMLHttpRequest();
  xhr.onreadystatechange = function() {
    if (xhr.readyState === XMLHttpRequest.DONE) {
      if (xhr.status === 200) {
        // La richiesta è andata a buon fine
        var response = xhr.responseText;
        console.log(response);
      } else {
        // La richiesta ha fallito
        console.log('Errore nella richiesta');
      }
    }
  };
  xhr.open('POST', '/modifica-prenotazione/' + id, true);
  xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
  var dataToSend = 'num_persone=' + encodeURIComponent(num_persone) +
                   '&data=' + encodeURIComponent(data) +
                   '&ora=' + encodeURIComponent(ora);
  xhr.send(dataToSend);
}
