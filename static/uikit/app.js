document.addEventListener("DOMContentLoaded", function () {
  // Highlight code if you're using a syntax highlighter
  if (typeof hljs !== "undefined") {
    hljs.highlightAll();
  }

  // Select all alert elements
  const alerts = document.querySelectorAll(".alert");

  alerts.forEach((alert, index) => {
    // Hide the message after 3 seconds
    setTimeout(() => {
      alert.style.display = "none";
    }, 3000); // 3000ms = 3 seconds

    // Only show the first message
    if (index > 0) {
      alert.style.display = "none";
    }
  });
});
