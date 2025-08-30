document.querySelectorAll("#folderList li").forEach(li => {
  li.addEventListener("click", function(e) {
    // Ignore if clicked upload icon
    if (e.target.classList.contains("bi-upload")) return;

    // remove active from all
    document.querySelectorAll("#folderList li").forEach(x => x.classList.remove("active"));
    // add active to clicked
    this.classList.add("active");

    const category = this.dataset.category;
    document.querySelectorAll("#filePanel .file-item").forEach(item => {
      if (category === "all" || item.dataset.category === category) {
        item.style.display = "block";
      } else {
        item.style.display = "none";
      }
    });
  });
});