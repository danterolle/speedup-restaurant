$(document).ready(function() {
    $('#prenotazione-form').submit(function(event) {
        // Impediamo al form di essere inviato normalmente
        event.preventDefault();

        // Otteniamo i dati del form
        var formData = {
            'nome': $('input[name=nome]').val(),
            'cognome': $('input[name=cognome]').val(),
            'email': $('input[name=email]').val(),
            'telefono': $('input[name=telefono]').val(),
            'num_persone': $('input[name=num_persone]').val(),
            'data': $('input[name=data]').val(),
            'ora': $('input[name=ora]').val(),
            'note': $('textarea[name=note]').val()
        };

        // Inviamo i dati al backend Flask tramite AJAX
        $.ajax({
            type: 'POST',
            url: '/prenotazione',
            data: formData,
            dataType: 'text',
            success: function(result) {
                // Visualizziamo il risultato nella pagina
                $('#risultato').text(result);
            },
            error: function(xhr, status, error) {
                // In caso di errore, visualizziamo un messaggio
                $('#risultato').text('Si è verificato un errore durante l\'invio della prenotazione.');
            }
        });
    });
});