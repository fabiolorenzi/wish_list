let openCloseStatus = false;

function openProductForm(): void {
    openCloseStatus = !openCloseStatus;
    let targetForm = document.getElementById("productForm");
    if (openCloseStatus) {
        targetForm.classList.add("openProductForm");
    } else {
        targetForm.classList.remove("openProductForm");
    };
};