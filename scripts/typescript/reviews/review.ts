let reviewOpen = false;

function openCloseReview(targetId: string): void {
    let review = document.getElementById(targetId);
    reviewOpen = !reviewOpen;
    if (productOpen) {
        review.classList.add("review_bodyOpen");
        review.classList.remove("review_bodyClosed");
    } else {
        review.classList.add("review_bodyClosed");
        review.classList.remove("review_bodyOpen");
    };
};

function updateReview(id: number): void {
    let name = (document.getElementById("reviewName" + id) as HTMLInputElement)?.value;
    let category = (document.getElementById("reviewCategory" + id) as HTMLInputElement)?.value;
    let country = (document.getElementById("reviewCountry" + id) as HTMLInputElement)?.value;
    let materials = (document.getElementById("reviewMaterials" + id) as HTMLInputElement)?.value;
    let image_url = (document.getElementById("reviewImageUrl" + id) as HTMLInputElement)?.value;
    let taste = (document.getElementById("reviewTaste" + id) as HTMLInputElement)?.value;
    let aroma = (document.getElementById("reviewAroma" + id) as HTMLInputElement)?.value;
    let weight = (document.getElementById("reviewWeight" + id) as HTMLInputElement)?.value;
    let price = (document.getElementById("reviewPrice" + id) as HTMLInputElement)?.value;
    let note = (document.getElementById("reviewNote" + id) as HTMLInputElement)?.value;
    let vote = (document.getElementById("reviewVote" + id) as HTMLInputElement)?.value;

    fetch(`/api/reviews/${id}`, {
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
            price: price,
            note: note,
            vote: vote,
            created_by: localStorage.getItem("user_id")
        })
    })
    .then(() => {
        alert("Review updated successfully");
        window.location.reload();
    })
    .catch(err => console.log(err));
};

function deleteReview(id: number): void {
    fetch(`/api/reviews/${id}`, {
        method: "DELETE",
        headers: {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
    })
    .then(() => {
        alert("Review deleted successfully");
        window.location.reload();
    })
    .catch(err => console.log(err));
};