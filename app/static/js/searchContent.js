function searchContent() {
    var input = document.getElementById("search_content");
    var filter = input.value.toUpperCase();
    var lis = document.getElementsByTagName('li');
    for (var i = 0; i < lis.length; i++) {
        var content = lis[i].getElementsByClassName('content')[0].innerHTML;
        if (content.toUpperCase().indexOf(filter) >= 0)
            lis[i].style.display = 'list-item';

        else
            lis[i].style.display = 'none';
    }
}
