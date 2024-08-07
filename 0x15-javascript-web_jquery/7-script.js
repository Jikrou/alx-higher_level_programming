$(document).ready(function () {
  const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';

  $.ajax({
    url,
    dataType: 'json',
    success: function (data) {
      $('#character').text(data.name);
    },
    error: function (error) {
      console.error('Error fetching character:', error);
      $('#character').text('Error fetching character data');
    }
  });
});
