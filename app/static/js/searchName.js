function searchName() {
    var input = document.getElementById("search_name");
    var filter = input.value.toUpperCase();
    var lis = document.getElementsByTagName('li');
    for (var i = 0; i < lis.length; i++) {
        var name = lis[i].getElementsByClassName('name')[0].innerHTML;
        if (name.toUpperCase().indexOf(filter) >= 0)
            lis[i].style.display = 'list-item';
        else
            lis[i].style.display = 'none';
    }
}


