let countryfield = $('#id_default_country').val();
if(!countrySelected) {
    $('#id_default_country').css('color', '#83C5BE');
};
$('#id_default_country').change(function() {
    countrySelected = $(this).val();
    if(!countrySelected) {
        $(this).css('color', '#83C5BE');
    } else {
        $(this).css('color', '#006D77');
    }
});
