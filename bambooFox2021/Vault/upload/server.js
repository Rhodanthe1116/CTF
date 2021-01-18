const express = require("express");

const app = express();
app.use(express.static('public'));

app.get('/', (_, res) => {
    res.sendFile('./index.html');
});

app.listen(5000, "0.0.0.0"); 