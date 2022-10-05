function deleteCategory(id: number): void {
    fetch(`/api/categories/${id}`, {
        method: "DELETE",
        headers: {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
    })
    .then(() => {
        alert("Category deleted successfully");
        window.location.reload();
    })
    .catch(err => console.log(err));
};

let categoryOpen = false;

function openCloseCategory(targetId: string): void {
    let category = document.getElementById(targetId);
    categoryOpen = !categoryOpen;
    if (categoryOpen) {
        category.classList.add("category_bodyOpen");
        category.classList.remove("category_bodyClosed");
    } else {
        category.classList.add("category_bodyClosed");
        category.classList.remove("category_bodyOpen");
    };
};