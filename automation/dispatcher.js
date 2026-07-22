const fs = require('fs');
const path = require('path');

class NexalNodeDispatcher {
    constructor() {
        this.statusFile = path.join(__dirname, '../logs/status.json');
    }

    broadcast() {
        const state = {
            system: "NEXAL_INTELLIGENCE",
            state: "READY_FOR_DEPLOYMENT",
            timestamp: new Date().toISOString()
        };

        fs.writeFileSync(this.statusFile, JSON.stringify(state, null, 2));
        console.log(`[DISPATCHER] State broadcast saved to: ${this.statusFile}`);
    }
}

const dispatcher = new NexalNodeDispatcher();
dispatcher.broadcast();
