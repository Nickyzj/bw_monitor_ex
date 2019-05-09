$(document).ready(function () {
    $('.btn-secondary').on('click', function () {
        $('.btn-secondary').attr('disabled', true);
        var rfctype = $(this).attr('rfctype');
        var log_id = $(this).attr('log_id');
        var variante = $(this).attr('variante');
        req = $.ajax({
            url: '/monitor/rfc_call/' + rfctype + '/' + log_id + '/' + variante,
            type: 'GET',
            success: function (result) {
                $("#ajax_status").html(result);
                req = $.ajax({
                    url: '/data/execute/ajax_update',
                    type: 'GET',
                    success: function (result) {
                        $("#ajax_status").html(result);
                        $('.btn-secondary').attr('disabled', false);
                    }
                });
            },
            timout : 5000,
            error : function () {
                $("#ajax_status").html("Timeout");
                $('.btn-secondary').attr('disabled', false);
            }
        });
    });
});

setInterval(function () {
    $.ajax({
       url : '/monitor/last_update',
        type : 'GET',
        success : function (result) {
           $('#last_update').text(result);
        }
    });
}, 3000)