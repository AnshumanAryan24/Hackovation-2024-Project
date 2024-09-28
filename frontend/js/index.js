function printPDF(searchquery) {
  fetch(`http://127.0.0.1:5000/pdfparsingtool?pdfpath=${searchquery}`)
    .then((response) => response.text())
    .then((data) => {
      console.log(
        "-------------------------------------------------------------------\n"
      );
      console.log(data);

      // Store the data in sessionStorage
      sessionStorage.setItem("pdfData", data);

      // Redirect to flashcards.html
      window.location.href = "flashcards.html";
    })
    .catch((error) => console.error("Error:", error));
}
function getFile() {
  console.log(fileBtn.value);
  // return fileBtn.files[0];
}
