const NOTE_ELEMENT = document.getElementsByClassName("note-element");
const TOP_BUTTONS = document.getElementsByClassName("top_buttons");

NOTE_ELEMENT[0].onclick = onclickNote;
TOP_BUTTONS[0].onclick = onclickTopButtons;

function onclickNote() {
    window.location.assign('editing_note');
}
function onclickTopButtons() {
    window.location.assign('editing_note');
}