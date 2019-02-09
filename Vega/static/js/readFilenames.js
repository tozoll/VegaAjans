//Reads filenamesin a folder 
    const testFolder = '../img/logo';
    const fs = require('fs');

    fs.readdir(testFolder, (err, files) => {
        files.forEach(file => {
            console.log(` <img src="/img/logo/${file}" alt="${file}" class="references__item">`);           
        });
    });

