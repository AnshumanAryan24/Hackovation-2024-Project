document.addEventListener("DOMContentLoaded", () => {
  const cardsContainer = document.querySelector(".cards");
  let currentIndex = 0;

  fetch(` http://127.0.0.1:5000/pdfparse?pdfpath=${document.getElementById()}`)
    .then((response) => response.json())
    .then((data) => {
      const cardsData = data.compiler_design;

      function renderCard(index) {
        cardsContainer.innerHTML = "";

        if (index >= 0 && index < cardsData.length) {
          const card = document.createElement("div");
          card.className =
            "card mb-10 bg-gradient-to-l from-[#aaa] to-[#555] rounded-[100px] w-[70%] h-[80%] flex flex-wrap flex-col justify-center items-center text-[24px] transition transform hover:scale-105 animate-fadeInUp";
          card.id = `card${index + 1}`;
          card.innerHTML = `<strong>${cardsData[index].name}</strong> ${cardsData[index].description}`;
          cardsContainer.appendChild(card);
        }
      }

      renderCard(currentIndex);

      document.getElementById("prev-btn").addEventListener("click", () => {
        if (currentIndex > 0) {
          currentIndex -= 1;
          renderCard(currentIndex);
        }
      });

      document.getElementById("next-btn").addEventListener("click", () => {
        if (currentIndex + 1 < cardsData.length) {
          currentIndex += 1;
          renderCard(currentIndex);
        }
      });
    })
    .catch((error) => console.error("Error loading JSON data:", error));
});
