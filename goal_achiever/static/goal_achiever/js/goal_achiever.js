$(document).ready(function () {
  var csrftoken = $.cookie('csrftoken');

  // controls which form is active
  var control = '';
  var controlDiv = null;

  // controls if or which item page is active
  var itemPk = '';
  var itemType = '';
  if ($('#item-selected').length) {
    itemPk = $('#item-selected').attr('pk')
    itemType = $('#item-selected').attr('item')
  }

  var deleted = [];
  var created = [];
  var newItemId = -1;

  function itemIsValid(n, d) {
    if (n != '' && d != '') {
      var existingNames = $(controlDiv).find('span.name');
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

  function addItem(n, d) {
    if (itemIsValid(n, d)) {
      created.push({ name: n, description: d });
      $(controlDiv).find('.new-items').prepend(`
                <div id="`+ newItemId + `" class="container-2 item">
                    <span class="name">`+ n + `</span>
                    <span id="`+ n + `" class="delete-new">X</button>
                </div>`);
      newItemId--;
    }
  }

  $('.btn.edit').on('click', function () {
    // disables edit buttons
    $('.btn.edit').attr('disabled', true);
    // controls which form is active
    controlDiv = this.closest('.form-control');
    control = $(controlDiv).attr('name');
    // shows a new item form and delete buttons
    $(controlDiv).children('.container-form').css('display', 'block');
    $(controlDiv).find('.delete').css('display', 'inline-block');
  });

  $('.btn.add').on('click', function () {
    var name = $(controlDiv).find('#id_name').val();
    var description = $(controlDiv).find('#id_description').val();
    addItem(name, description);
    // clears input fields
    $(controlDiv).find('#id_name').val('');
    $(controlDiv).find('#id_description').val('');
  });

  $('.item > .delete').on('click', function (e) {
    var itemId = e.target.classList[1];
    if ($.inArray(itemId, deleted) == -1) {
      // selects a item to remove
      $(controlDiv).find('#item_name-' + itemId).css('text-decoration', 'line-through');
      deleted.push(itemId);
      e.target.textContent = 'R';
    } else {
      // deselects a item to remove
      $(controlDiv).find('#item_name-' + itemId).css('text-decoration', 'none');
      deleted = $.grep(deleted, function (value) {
        return value != itemId;
      });
      e.target.textContent = 'X';
    }
  });

  $('.new-items').on('click', '.delete-new', function (e) {
    // deletes not saved item
    var newItemId = e.target.parentElement.id;
    var newItemName = e.target.id;
    var result = created.filter(obj => {
      return obj.name !== newItemName;
    });
    created = result;
    $('#' + newItemId).remove();
  });

  $('.btn.save').on('click', function () {
    // saves goal list changes
    if (created.length !== 0 || deleted.length !== 0) {
      $.ajax({
        type: "POST",
        url: 'http://localhost:8000/goal_achiever/add_delete_items/',
        data: {
          'csrfmiddlewaretoken': csrftoken,
          'control': control,
          'Q': created.length,
          'C': created,
          'D': deleted,
          // passes data if item page is active, else '' (empty string)
          'item': itemType,
          'item_pk': itemPk,
        },
        dataType: "json",
        success: function (response) {
          console.log('success', response);
          location.reload();
        }
      });
    }
  });

  $('.btn.cancel').on('click', function () {
    // hides a form and delete buttons
    $('div.container-form').css('display', 'none');
    $('.item > .delete').css('display', 'none');

    // restores delete indicators
    for (var i = 0; i < $('.delete').length; i++) {
      $('.delete')[i].textContent = 'X';
    }
    $('.name').css('text-decoration', 'none');

    // clears unsaved new items
    $('.new-items').empty();

    // resets form control
    control = null;
    controlDiv = null;

    // enables edit buttons
    $('.btn.edit').attr('disabled', false);

    // clears all temporary data
    deleted = [];
    created = [];
    newItemId = -1
  });
});
