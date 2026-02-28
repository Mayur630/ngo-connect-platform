document.addEventListener("DOMContentLoaded", function () {
  const searchInput = document.querySelector("#searchbar");
  if (searchInput) {
    searchInput.placeholder = "Search by name, user, campaign, or status";
  }

  const currentPath = window.location.pathname || "";
  if (currentPath.includes("/admin/")) {
    document.body.classList.add("ngo-admin-active");
  }
});
