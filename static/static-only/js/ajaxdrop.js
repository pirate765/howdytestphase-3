$(function activityform()() {
  $('#landform').on('change',function() {
    $.ajax({
      type: "GET",
      url: "/searchformactivity/",
      data: {
        'searchactivityform_text' : $('#landform').val(),
        'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
      },
      success: searchactivity,
      dataType : 'html',
    });
  });
});

function searchactivity(data, textStatus, jqXHR)
{
  $('#form-activity').html(data);
}
