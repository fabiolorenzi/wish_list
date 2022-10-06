let categoryReviewOpen = false;

function openCloseCategoryReview(targetId: string): void {
    let category = document.getElementById(targetId);
    categoryReviewOpen = !categoryReviewOpen;
    if (categoryReviewOpen) {
        category.classList.add("category_bodyOpen");
        category.classList.remove("category_bodyClosed");
    } else {
        category.classList.add("category_bodyClosed");
        category.classList.remove("category_bodyOpen");
    };
};