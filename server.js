require("dotenv").config();
const express = require('express');
const path = require('path');
const app = express();
const PORT = process.env.PORT || 3000;

// Initialize Stripe with your environment secret key
const stripe = require('stripe')(process.env.STRIPE_SECRET_KEY);

// Middleware
app.use(express.json());

// Serve static frontend files from the nexus_hub directory using absolute pathing
app.use(express.static(path.join(__dirname, 'nexus_hub')));

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'nexus_hub', 'index.html'));
});

console.log("🚀 Nexal Headless Intelligence Engine Initialized");

// 1. Headless Traffic & Client Execution Endpoint
app.post('/api/v1/execute', (req, res) => {
    const { client, task, budget, tier } = req.body;
    console.log(`\n📦 [TRAFFIC INBOUND] Client: ${client || 'Anonymous'} | Tier: ${tier || 'Standard'}`);
    
    const executionId = 'NX-' + Math.floor(Math.random() * 900000 + 100000);
    res.status(200).json({
        status: "SUCCESS",
        executionId: executionId,
        message: "Nexal autonomous pipeline triggered successfully",
        tier: tier || "Standard",
        timestamp: new Date().toISOString()
    });
});

// 2. Stripe Checkout Session Creator for Live Revenue Retainers
app.post('/api/v1/create-checkout-session', async (req, res) => {
    try {
        const { tierName, amount } = req.body;
        const session = await stripe.checkout.sessions.create({
            payment_method_types: ['card'],
            mode: 'subscription',
            line_items: [
                {
                    price_data: {
                        currency: 'usd',
                        product_data: {
                            name: tierName || 'Nexal Intelligence Growth Tier',
                        },
                        unit_amount: amount || 9900, // Default $99.00 / month
                        recurring: {
                            interval: 'month',
                        },
                    },
                    quantity: 1,
                },
            ],
            success_url: 'https://nexalintelligence.com/success?session_id={CHECKOUT_SESSION_ID}',
            cancel_url: 'https://nexalintelligence.com/cancel',
        });

        console.log(`\n💳 [CHECKOUT CREATED] Session ID: ${session.id}`);
        res.json({ url: session.url });
    } catch (error) {
        console.error('Stripe Checkout Error:', error.message);
        res.status(500).json({ error: error.message });
    }
});

// 3. Stripe Webhook Handler for Real-Time Retainers & Revenue
app.post('/api/v1/webhook', express.raw({type: 'application/json'}), (req, res) => {
    const event = req.body;
    console.log(`\n🔔 [STRIPE EVENT] Received event type: ${event.type}`);
    res.json({ received: true });
});

// Start Server
app.listen(PORT, () => {
    console.log(`🌐 Nexal API Gateway live on port ${PORT}`);
});

