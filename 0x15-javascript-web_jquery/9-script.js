$(document).ready(function () {
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

  $.ajax({
    url,
    dataType: 'json',
    success: function (data) {
      $('#hello').text(data.hello);
    },
    error: function (error) {
      console.error('Error fetching translation:', error);
      $('#hello').text('Error fetching translation');
    }
  });
});
