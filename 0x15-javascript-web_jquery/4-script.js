$(document).ready(function () {
  $('#toggle_header').click(function () {
    const header = $('header');
    const currentClass = header.attr('class');

    if (currentClass === 'red') {
      header.removeClass('red').addClass('green');
    } else {
      header.removeClass('green').addClass('red');
    }
  });
});
