const NOTE_ELEMENT = document.getElementsByClassName("note-element");
NOTE_ELEMENT[0].onclick = onclickNote;

function onclickNote() {
    window.location.assign('editing_note');
}