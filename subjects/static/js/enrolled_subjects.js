function toggleButton(cardElement, event) {
  event.stopPropagation(); // prevent outer click listener from firing

  // Hide all buttons
  document.querySelectorAll(".card-btn").forEach(btn => {
    btn.style.display = "none";
  });

  // Show only clicked card's button
  const btn = cardElement.querySelector(".card-btn");
  btn.style.display = "block";
}

// Hide when clicking outside
document.addEventListener("click", function() {
  document.querySelectorAll(".card-btn").forEach(btn => {
    btn.style.display = "none";
  });
});
