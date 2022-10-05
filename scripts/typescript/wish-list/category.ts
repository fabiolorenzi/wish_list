function deleteCategory(id: number): void {
    fetch(`/api/categories/${id}`, {
        method: "DELETE",
        headers: {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
    })
    .then(() => {
        alert("Category delete successfully");
        window.location.reload();
    })
    .catch(err => console.log(err));
};