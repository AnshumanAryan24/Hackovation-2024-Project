function printPDF() {
  var number = "BCSE209L_MACHINE-LEARNING_TH_1.0_71_BCSE209L_66 ACP.pdf";
  fetch(` http://0.0.0.0:5000/pdfparsingtool?number=${number}`)
    .then((response) => {
      console.log(response);
    })
    .catch((error) => console.error("Error:", error));
}

printPDF();
