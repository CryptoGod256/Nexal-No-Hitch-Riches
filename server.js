const express = require('express');
const app = express();
const stripe = require('stripe')(process.env.STRIPE_SECRET_KEY);

// Serve static frontend files from project root
app.use(express.static(__dirname));
app.use(express.json());

// Health check route
app.get('/health', (req, res) => {
    res.json({ status: 'active', gateway: 'Nexal Secure Payment Gateway' });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Nexal Secure Payment Gateway active on port ${PORT}`);
});

// --- NEXAL DATA CENTER: SOCIAL HUB API ---
app.get('/api/social-feed', (req, res) => {
    // Serving live ecosystem status to the front-end nodes
    res.json({
        events: [
            { title: "B2B Client Authenticated", desc: "Enterprise handshake confirmed inside the Nexal data center.", time: "Just now" },
            { title: "SaaS Pipeline Active", desc: "Data synchronization protocol successful.", time: "12 mins ago" }
        ]
    });
});
