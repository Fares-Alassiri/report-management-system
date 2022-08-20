function searchGroup() {
    var input = document.getElementById("search_group");
    var filter = input.value.toUpperCase();
    var lis = document.getElementsByTagName('li');
    for (var i = 0; i < lis.length; i++) {
        var group = lis[i].getElementsByClassName('group')[0].innerHTML;
        if (group.toUpperCase().indexOf(filter) >= 0)
            lis[i].style.display = 'list-item';

        else
            lis[i].style.display = 'none';
    }
}
