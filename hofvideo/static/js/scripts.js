var delayTimer;
$('#id_search').keyup(function () {
  clearTimeout(delayTimer);
  $('#search_results').text('Loading...');
});
