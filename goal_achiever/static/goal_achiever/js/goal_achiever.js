$(document).ready(function() {
    var count = sessionStorage.length.toString();
    console.log(count);
    $('#new-goal').click(function() {
        $('div#create-goal-form').css('display', 'block');
        sessionStorage.setItem('n', 'n');
    });
    $('.btn.cancel').click(function() {
        $('div#create-goal-form').css('display', 'none');
        sessionStorage.clear();
    });
    $('.goal-form').on('submit', function() {
        sessionStorage.setItem(count, 'n');
        count += 1;
    });
    if (sessionStorage.length > 0) {
        $('div#create-goal-form').css('display', 'block');
    } else {
        $('div#create-goal-form').css('display', 'none');
    }
    count = 0;
});