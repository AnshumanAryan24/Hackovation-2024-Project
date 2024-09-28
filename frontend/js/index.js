function printPDF(searchquery) {
  fetch(`http://127.0.0.1:5000/pdfparsingtool?pdfpath=${searchquery}`)
    .then((response) => response.text())
    .then((data) => {
      console.log(
        "-------------------------------------------------------------------\n"
      );
      console.log(data);

<<<<<<< HEAD
      // Store the data in sessionStorage
      sessionStorage.setItem("pdfData", data);

      // Redirect to flashcards.html
      window.location.href = "flashcards.html";
    })
    .catch((error) => console.error("Error:", error));
}
=======
function getFile() {
    console.log(fileBtn.value);
    // return fileBtn.files[0];
}
>>>>>>> c55cb565f0bbb5e6d9d0349b8e26e589cc405b63
