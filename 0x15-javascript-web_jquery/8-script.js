$(document).ready(function () {
  const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';

  $.ajax({
    url,
    dataType: 'json',
    success: function (data) {
      const movies = data.results; // Extract the movies array from the response
      const list = $('#list_movies');

      movies.forEach(function (movie) {
        const listItem = $('<li></li>').text(movie.title);
        list.append(listItem);
      });
    },
    error: function (error) {
      console.error('Error fetching movies:', error);
      $('#list_movies').text('Error fetching movie data');
    }
  });
});
