function printPDF() {
    var number = "BCSE302P_DATABASE-SYSTEMS-LAB_LO_1.0_70_BCSE302P.pdf";
    fetch(`http://127.0.0.1:5000/pdfparsingtool?number=${number}`)
        .then(response => response.json())
        .then(data => {
            console.log("object\n");
            console.log(data.result);
        })
        .catch(error => console.error('Error:', error));
}

printPDF()