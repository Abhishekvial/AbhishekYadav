function analyze() {
  const input = document.getElementById("input").value.trim();
  const loader = document.getElementById("loader");
  const result = document.getElementById("result");

  if (!input) {
    alert("Please enter a vulnerability description.");
    return;
  }

  loader.style.display = "block";
  result.style.display = "none";

  fetch('http://127.0.0.1:8000/analyze', {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ description: input })
  })
  .then(res => res.json())
  .then(data => {
    document.getElementById("risk").textContent = data.risk;
    document.getElementById("confidence").textContent = `${data.confidence}%`;
    document.getElementById("features").textContent = data.features.join(", ");

    loader.style.display = "none";
    result.style.display = "block";
  })
  .catch(err => {
    loader.style.display = "none";
    alert("Error communicating with backend. Please try again.");
    console.error(err);
  });
}
