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

function updateProductInWishList(id: number): void {
    let name = (document.getElementById("productName") as HTMLInputElement)?.value;
    let category = (document.getElementById("productCategory") as HTMLInputElement)?.value;
    let country = (document.getElementById("productCountry") as HTMLInputElement)?.value;
    let materials = (document.getElementById("productMaterials") as HTMLInputElement)?.value;
    let image_url = (document.getElementById("productImageUrl") as HTMLInputElement)?.value;
    let taste = (document.getElementById("productTaste") as HTMLInputElement)?.value;
    let aroma = (document.getElementById("productAroma") as HTMLInputElement)?.value;
    let weight = (document.getElementById("productWeight") as HTMLInputElement)?.value;
    let quantity = (document.getElementById("productQuantity") as HTMLInputElement)?.value;
    let price = (document.getElementById("productPrice") as HTMLInputElement)?.value;

    fetch(`/api/products/${id}`, {
        method: "PUT",
        headers: {
            "Accept": "application/json",
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            name: name,
            category: category,
            country: country,
            materials: materials,
            image_url: image_url,
            taste: taste,
            aroma: aroma,
            weight: weight,
            quantity: quantity,
            price: price,
            created_by: localStorage.getItem("user_id")
        })
    })
    .then(() => {
        alert("Product updated successfully");
        window.location.reload();
    })
    .catch(err => console.log(err));
};