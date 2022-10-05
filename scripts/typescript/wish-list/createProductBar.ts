let openCloseStatus = false;

function openProductForm(): void {
    openCloseStatus = !openCloseStatus;
    let targetForm = document.getElementById("productForm");
    if (openCloseStatus) {
        targetForm.classList.add("createProductForm_bodyOpen");
        targetForm.classList.remove("createProductForm_bodyClosed");
    } else {
        targetForm.classList.remove("createProductForm_bodyOpen");
        targetForm.classList.add("createProductForm_bodyClosed");
    };
};