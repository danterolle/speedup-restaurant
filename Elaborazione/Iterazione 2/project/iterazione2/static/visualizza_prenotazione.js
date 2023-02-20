$(function() {
    const urlParams = new URLSearchParams(window.location.search);
    const idPrenotazione = urlParams.get('id');

    if (idPrenotazione) {
        $.get(`/visualizza-prenotazione/${idPrenotazione}`)
            .done(function (data) {
                $('p#email').text(data[1]);
                $('p#telefono').text(data[2]);
                $('p#nome').text(data[3]);
                $('p#cognome').text(data[4]);
                $('p#num_persone').text(data[5]);
                $('p#data').text(data[6]);
                $('p#ora').text(data[7]);
                $('p#note').text(data[8]);
            })
            .fail(function () {
                alert("Errore durante il recupero dei dati della prenotazione.");
            });
    }
});
