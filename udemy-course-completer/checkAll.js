// open all accordions
// assuming all accordions are initially closed
accordions = document.querySelectorAll(".accordion-panel--panel-toggler--UP46Q")
for (var i = 0, len = accordions.length; i < len; i=i+2) {
    accordions[i].click();
}
// check (click) all unchecked boxes
checkboxes = document.querySelectorAll(".ud-real-toggle-input")
for (var i = 0, len = checkboxes.length; i < len; i++) {
    checkbox = checkboxes[i]
    if (checkbox.checked == false) {
        checkbox.click();
    }
}