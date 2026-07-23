const fs = require('fs');
const path = require('path');

class NexalStreamProcessor {
    constructor() {
        this.metricsFile = path.join(__dirname, '../logs/metrics.json');
    }

    recordPulse() {
        const payload = {
            node: "AUTONOMOUS_ENGINE",
            status: "ACTIVE",
            epoch: Date.now()
        };
        
        fs.writeFileSync(this.metricsFile, JSON.stringify(payload, null, 2));
        console.log(`[PROCESSOR] Metric pulse recorded at: ${this.metricsFile}`);
    }
}

const processor = new NexalStreamProcessor();
processor.recordPulse();
