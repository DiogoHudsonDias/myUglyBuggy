
function UglyRedirect(strUrl) {
    window.location.href = strUrl;
};

        $('#confirm-delete').on('show.bs.modal', function(e) {
            $(this).find('.btn-ok').attr('href', $(e.relatedTarget).data('href'));

            $('.txtMensagem').html('Registro: <strong>' + $(e.relatedTarget).data('href2') + '</strong>');



        });