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
        var results = '';
        $('#search_results').text('');

        results += '<div class="row">'

        data['items'].forEach(function(video) {
          results += '<div class="col-md-4 mt-3"><div class="card mb-4 shadow-sm">';
          results += '<iframe width="100%" height="200" src="https://www.youtube.com/embed/'+video['id']['videoId']+'" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
          results += '</div></div>'
        });

        results += '</div>'

        $('#search_results').append(results);
      }
    });
  }, 1000);
});
