function printPDF() {
  var number = "../../NLP/BCSE302P_DATABASE-SYSTEMS-LAB_LO_1.0_70_BCSE302P.pdf";
  fetch(` http://0.0.0.0:5000/pdfparsingtool?number=${number}`)
    .then((response) => response.text()).then((data) => {
      console.log(data);
    })
    .catch((error) => console.error("Error:", error));
}

printPDF();
