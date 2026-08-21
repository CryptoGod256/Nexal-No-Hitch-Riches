const express = require('express');
const cors = require('cors');
const path = require('path');
const app = express();
const PORT = process.env.PORT || 8080;

app.use(cors());
app.use(express.json());
app.use(express.static(path.join(__dirname, 'public')));

app.get('/api/health', (req, res) => {
    res.json({ status: 'online', system: 'Nexal Intelligence Core', timestamp: new Date() });
});

app.listen(PORT, () => {
    console.log(`🚀 Nexal Multiverse Server live on port ${PORT}`);
});
