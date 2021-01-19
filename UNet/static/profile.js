const search_bar = document.getElementById("search-form-explore");


window.addEventListener('click', function(e){   
    if (search_bar.contains(e.target)){
        search_bar.id = "search-form-explore-active";
    } else{
      search_bar.id = "search-form-explore";
    }
}, false);
