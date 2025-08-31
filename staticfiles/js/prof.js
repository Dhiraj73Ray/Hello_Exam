function viewImage() {
  alert("Viewing image (implement modal later)");
}

function changeImage() {
  alert("Trigger file input for image change (not implemented)");
}

function removeImage() {
  const img = document.querySelector('.profile-img');
  img.src = '/static/images/default-profile.jpg'; // fallback image
  alert("Profile image removed");
}

function enableEditing() {
  alert("Enable edit mode (future implementation)");
}


document.addEventListener("DOMContentLoaded", function () {
    const saveBtn = document.querySelector(".btn-primary");
    if (saveBtn) {
        saveBtn.addEventListener("click", () => {
            alert("Changes saved (demo only)!");
        });
    }
});
