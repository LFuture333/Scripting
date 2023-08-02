console.log('Serve-side code running');

const express = require('express');

const app = express();


//Server file from the public directory
app.use(express.static('public'));

//start the express web server listening on 8080
app.listen(8080, () => {
    console.log('Listening on 8080');

});

//Server the homepage 
app.get('/', (req, res) => {

    res.sendFile(___dirname + '/index.html');
});