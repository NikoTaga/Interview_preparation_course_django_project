//
// $(document).ready(function() {
//     $('.js-create-good').on('click', function () {
//         $.get(this.getAttribute("data-url"), function (data) {
//             $("#modal-good").modal("show");
//             $("#modal-good .modal-content").html(data.html_form);
//     })
// })
//     $("#modal-good").on("submit", ".js-good-create-form", function () {
//         $.post(this.getAttribute("action"), function (data) {
//         if (data.form_is_valid) {
//                   $("#goods-list tbody").html(data.html_good_list);
//           $("#modal-good").modal("hide");
//         }
//         else {
//           $("#modal-good .modal-content").html(data.html_form);
//         }
// })
//
//    })
// })


//
$(function () {

  /* Код функций */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-good").modal("show");
      },
      success: function (data) {
        $("#modal-good .modal-content").html(data.html_form);
      }
    });
  };

  var saveForm = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $("#good-table tbody").html(data.html_good_list);
          $("#modal-good").modal("hide");
        }
        else {
          $("#modal-good .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };

  /* Подключение функций */

  $(".js-create-good").click(loadForm);
  $("#modal-good").on("submit", ".js-good-create-form", saveForm);

});


