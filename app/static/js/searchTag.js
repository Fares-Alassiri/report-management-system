function searchTag() {
    var input = document.getElementById("search_tag");
    console.log(input);
    var filter = input.value.toUpperCase();
    var lis = document.getElementsByTagName('li');
    for (var i = 0; i < lis.length; i++) {
        var tag = lis[i].getElementsByClassName('tag')[0].innerHTML;
        console.log(tag);
        if (tag.toUpperCase().indexOf(filter) >= 0)
            lis[i].style.display = 'list-item';
        else
            lis[i].style.display = 'none';
    }
}
