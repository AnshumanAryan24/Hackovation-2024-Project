// function printPDF() {
//     var number = 'BCSE302P_DATABASE-SYSTEMS-LAB_LO_1.0_70_BCSE302P.pdf';
//     fetch(`http://127.0.0.1:8800/parse?number=${number}`)
//         .then(response => response.json())
//         .then(data => {
//             console.log("object\n");
//             console.log(data.result);
//         })
//         .catch(error => console.error('Error:', error));
// }

// printPDF()

async function printPDF() {
    const number = 'BCSE302P_DATABASE-SYSTEMS-LAB_LO_1.0_70_BCSE302P.pdf';
    try {
        const response = await fetch(`http://127.0.0.1:8800/parse?number=${number}`, {
            method: 'GET',
            headers: {
                accept: 'application/json', // Adjust as needed
            },
        });

        if (!response.ok) {
            throw new Error(`Error! Status: ${response.status}`);
        }

        const result = await response.json();
        console.log('Parsed result:', result);
    } catch (err) {
        console.error('Error:', err);
    }
}

printPDF();
