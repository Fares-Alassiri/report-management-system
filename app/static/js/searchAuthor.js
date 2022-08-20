function searchAuthor() {
    var input = document.getElementById("search_author");
    var filter = input.value.toUpperCase();
    var lis = document.getElementsByTagName('li');
    for (var i = 0; i < lis.length; i++) {
        var author = lis[i].getElementsByClassName('author')[0].innerHTML;
        if (author.toUpperCase().indexOf(filter) >= 0)
            lis[i].style.display = 'list-item';

        else
            lis[i].style.display = 'none';
    }
}
