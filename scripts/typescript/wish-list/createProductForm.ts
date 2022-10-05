function createProductInWishList(): void {
    let name = (document.getElementById("createProductName") as HTMLInputElement)?.value;
    let category = (document.getElementById("createProductCategory") as HTMLInputElement)?.value;
    let country = (document.getElementById("createProductCountry") as HTMLInputElement)?.value;
    let materials = (document.getElementById("createProductMaterials") as HTMLInputElement)?.value;
    let image_url = (document.getElementById("createProductImageUrl") as HTMLInputElement)?.value;
    let taste = (document.getElementById("createProductTaste") as HTMLInputElement)?.value;
    let aroma = (document.getElementById("createProductAroma") as HTMLInputElement)?.value;
    let weight = (document.getElementById("createProductWeight") as HTMLInputElement)?.value;
    let quantity = (document.getElementById("createProductQuantity") as HTMLInputElement)?.value;
    let price = (document.getElementById("createProductPrice") as HTMLInputElement)?.value;

    fetch(`/api/products`, {
        method: "POST",
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
        alert("Product created successfully");
        window.location.reload();
    })
    .catch(err => console.log(err));
};