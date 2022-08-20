function searchEditor() {
    var input = document.getElementById("search_editor");
    var filter = input.value.toUpperCase();
    var lis = document.getElementsByTagName('li');
    for (var i = 0; i < lis.length; i++) {
        var editor = lis[i].getElementsByClassName('editor')[0].innerHTML;
        if (editor.toUpperCase().indexOf(filter) >= 0)
            lis[i].style.display = 'list-item';

        else
            lis[i].style.display = 'none';
    }
}
