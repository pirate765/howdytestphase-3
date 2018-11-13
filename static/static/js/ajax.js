$(function() {
  $('#searchdestination').keyup(function() {
    if (!this.value.trim()) {
            $('#search-results').html('');
            return;
        }
    if( this.value.length < 2 ) return ;

    $.ajax({
      type: "POST",
      url: "/searchdestination/",
      data: {
        'search_destination_text' : $('#searchdestination').val(),
        'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
      },
      success: searchSuccess,
      dataType : 'html',
    });
  });
  $('#searchactivity').keyup(function() {
    if (!this.value.trim()) {
            $('#search-resultsactivity').html('');
            return;
        }
    if( this.value.length < 2 ) return;
    $.ajax({
      type: "POST",
      url: "/searchactivity/",
      data: {
        'search_activity_text' : $('#searchactivity').val(),
        'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
      },
      success: searchSuccess2,
      dataType : 'html',
    });
  });
});

function searchSuccess(data, textStatus, jqXHR)
{
  $('#search-results').html(data);
}

function searchSuccess2(data, textStatus, jqXHR)
{
  $('#search-resultsactivity').html(data);
}
