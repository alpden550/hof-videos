var delayTimer;
$('#id_search').keyup(function () {
  clearTimeout(delayTimer);
  $('#search_results').text('Loading...');

  delayTimer = setTimeout(function () {
    var text = $('#id_search').val();
    $.ajax({
      url: '/video/search/',
      data: {
        'search': text
      },
      dataType: 'json',
      success: function (data) {
        $('#search_results').text(data['Response']);
      }
    });
  }, 1000);
});
