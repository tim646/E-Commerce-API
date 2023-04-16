var script = document.createElement('script');
script.src = 'https://code.jquery.com/jquery-3.6.3.min.js'; // Check https://jquery.com/ for the current version
document.getElementsByTagName('head')[0].appendChild(script);

$(document).ready(function () {
    // checks admin form is course model
    if ($('form#course_form').length == 1) {
        // checks if is_top is checked
        if (document.getElementById('id_is_top').checked) {
            $('div.field-top_cover_image').css('display', 'block');
            $('label[for="id_top_cover_image"]').html('Top Cover Image <span class="text-red">*</span>');
        } else {
            $('div.field-top_cover_image').css('display', 'none');
        }
        // track is_top checkbox is clicked
        $('#id_is_top').change(function () {
            if (document.getElementById('id_is_top').checked) {
                $('div.field-top_cover_image').css('display', 'block');
                $('label[for="id_top_cover_image"]').html('Top Cover Image <span class="text-red">*</span>');

            } else {
                $('div.field-top_cover_image').css('display', 'none');
            }
        });

    }
});