$(document).ready(function() {
    var csrftoken = $.cookie('csrftoken');
    
    var deleted = [];
    var created = [];
    var newGoalId = -1;

    function itemIsValid (n, d) {
        if (n != '' && d != '') {
            var existingNames = $('span.name');
            for (var i = 0; i < existingNames.length; i++) {
                if (n === existingNames[i].innerText) {
                    console.log('This name already exists!');
                    return false;
                }
            }
            return true;
        } else {
            console.log('fill the form, motherfucker!')
            return false;
        }
    }

    function addItem (n, d) {
        if (itemIsValid(n, d)) {
            created.push({n, d});    
            $('#new-items').prepend(`
                <div id="`+ newGoalId +`" class="container-2 item">
                    <span class="name">`+ n +`</span>
                    <span id="`+ n +`" class="delete-new">X</button>
                </div>
            `);
            newGoalId--;
        }
    }

    $('.btn.edit').on('click', function() {
        // show a new item form and delete buttons
        $('div.container-form').css('display', 'block');
        $('.item > .delete').css('display', 'inline-block');
        // TODO: remove next line after finishing multiple submit functionality
        sessionStorage.setItem('n', 'n');
    });

    $('.btn.add').on('click', function() {
        var name = $('#id_name').val();
        var description = $('#id_description').val();
        addItem(name, description);

        // clear input fields
        $('#id_name').val('');
        $('#id_description').val('');
    });

    $('.item > .delete').on('click', function(e) {
        var goalId = e.target.classList[1];
        if ($.inArray(goalId, deleted) == -1) {
            // select a goal (TODO: item) to remove
            $('#goal_name-' + goalId).css('text-decoration', 'line-through');
            deleted.push(goalId);
            e.target.textContent = 'R';
        } else {
            // deselect a goal (TODO: item) to remove
            $('#goal_name-' + goalId).css('text-decoration', 'none');
            deleted = $.grep(deleted, function(value) {
                return value != goalId;
            });
            e.target.textContent = 'X';
        }
    });

    $('#new-items').on('click', '.delete-new', function(e) {
        // delete not saved item
        var newGoalId = e.target.parentElement.id;
        var newGoalName = e.target.id;
        var result = created.filter(obj => {
            return obj.name !== newGoalName;
        });
        created = result;
        $('#' + newGoalId).remove();
    });

    $('.btn.save').on('click', function () {
        // save goal list changes
        console.log(created);
        console.log(deleted);
            $.ajax({
                type: "POST",
                url: 'http://localhost:8000/goal_achiever/goal_list/save/',
                data: {
                    'C': created,
                    'D': deleted,
                    'csrfmiddlewaretoken': csrftoken,
                },
                dataType: "json",
                success: function (response) {
                    console.log('success', response);
                    location.reload();
                }
            });
    });

    $('.btn.cancel').on('click', function() {
        // hide a form and delete buttons
        $('div.container-form').css('display', 'none');
        $('.item > .delete').css('display', 'none');
        
        // restore delete indicators
        for (var i = 0; i < $('.delete').length; i++) {
            $('.delete')[i].textContent = 'X';  
        }
        $('.name').css('text-decoration', 'none');

        // clear unsaved new items
        $('#new-items').empty();

        // clear all temporary data
        sessionStorage.clear();
        deleted = [];
        created = [];
        newGoalId = -1
    });

    // TODO: remove this if/else after finishing multiple submit functionality
    if (sessionStorage.length > 0) {
        $('div.container-form').css('display', 'block');
        $('.item > .delete').css('display', 'inline-block');
    } else {
        $('div.container-form').css('display', 'none');
        $('.item > .delete').css('display', 'none');
    }
});