function updateLinks(): void {
    let userId = localStorage.getItem("user_id");

    let wishList = document.getElementById("dashboard_linkWishList");
    let review = document.getElementById("dashboard_linkReviews");

    wishList.setAttribute("href", `/wish-list?user=${userId}`);
    review.setAttribute("href", `/reviews?user=${userId}`);
};

document.addEventListener("DOMContentLoaded", () => {
    updateLinks();
});