function deleteProductFromWishList(id: number): void {
    fetch(`/api/products/${id}`, {
        method: "DELETE",
        headers: {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
    })
    .then(() => {
        alert("Product deleted successfully");
        window.location.reload();
    })
    .catch(err => console.log(err));
};

let productOpen = false;

function openCloseProduct(targetId: string): void {
    let product = document.getElementById(targetId);
  productOpen = !productOpen;
    if (productOpen) {
        product.classList.add("product_bodyOpen");
        product.classList.remove("product_bodyClosed");
    } else {
        product.classList.add("product_bodyClosed");
        product.classList.remove("product_bodyOpen");
    };
};