$(document).ready(function() {
  $('#search-btn').on('click', function(e) {
    e.preventDefault();
    let searchText = $('#search-box').val();
    $.ajax( {
      url: '/products?search_filter=' + searchText,
      type: 'GET',
      success: function(resp) {
        let newHtml = resp.data.map(d => {
          return `<div class="well product">
                      <a href="/products/${d.id}">
                        <img class="product-img" src="${d.firstImage}" />
                        <h4>${d.name}</h4>
                        <p>${d.price}</p>                   
                      </a>
                  </div>`
        });
        $('.products').html(newHtml.join(''));
        $('search-box').val('')
      },
      error: function(xhr, status, error) {
        // TODO: show toastr
        console.error(error);
      }
    })
  });
});