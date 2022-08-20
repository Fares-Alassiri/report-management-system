function showAdvanceSearch() {
    elements = document.getElementsByClassName('advanceSearch');
    element1 = document.getElementsByClassName('hide')[0];
    element1.style.display = "block";
    element2 = document.getElementsByClassName('show')[0];
    element2.style.display = "none";
    console.log(elements);
    for (var i = 0; i < elements.length; i++) {
        elements[i].style.display = "flex";
    }
}

function hideAdvanceSearch() {
    elements = document.getElementsByClassName('advanceSearch');
    element1 = document.getElementsByClassName('hide')[0];
    element1.style.display = "none";
    element2 = document.getElementsByClassName('show')[0];
    element2.style.display = "block";
    console.log(elements);
    for (var i = 0; i < elements.length; i++) {
        elements[i].style.display = "none";
    }
}