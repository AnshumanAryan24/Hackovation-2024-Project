document.addEventListener("DOMContentLoaded", () => {
  const cardsContainer = document.querySelector(".cards");
  let currentIndex = 0;
  const cardsPerPage = 5; // Adjust the number of cards to display at once

  // Fetch JSON data
  fetch("../data.json") // Adjust path if necessary
    .then((response) => response.json())
    .then((data) => {
      const cardsData = data.compiler_design;

      // Function to render cards
      function renderCards(startIndex) {
        // Clear existing cards
        cardsContainer.innerHTML = "";
        // Create card elements
        for (
          let i = startIndex;
          i < startIndex + cardsPerPage && i < cardsData.length;
          i++
        ) {
          const card = document.createElement("div");
          card.className =
            "card mb-10 bg-gradient-to-l from-[#aaa] to-[#555] rounded-[100px] w-[80%] h-[100%] flex flex-wrap justify-center items-center text-[40px] transition transform hover:scale-105 animate-fadeInUp";
          card.id = `card${i + 1}`;
          card.innerHTML = `<strong>${cardsData[i].name}</strong>: ${cardsData[i].description}`;
          cardsContainer.appendChild(card);
        }
      }

      // Initial render
      renderCards(currentIndex);

      // Button event listeners
      document.getElementById("prev-btn").addEventListener("click", () => {
        if (currentIndex > 0) {
          currentIndex -= cardsPerPage;
          renderCards(currentIndex);
        }
      });

      document.getElementById("next-btn").addEventListener("click", () => {
        if (currentIndex + cardsPerPage < cardsData.length) {
          currentIndex += cardsPerPage;
          renderCards(currentIndex);
        }
      });
    })
    .catch((error) => console.error("Error loading JSON data:", error));
});
