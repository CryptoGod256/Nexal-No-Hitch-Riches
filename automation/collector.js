const fs = require('fs');
const path = require('path');

class NexalDataCollector {
    constructor() {
        this.logPath = path.join(__dirname, '../logs');
    }

    initLogDirectory() {
        if (!fs.existsSync(this.logPath)) {
            fs.mkdirSync(this.logPath, { recursive: true });
            console.log(`[COLLECTOR] Created log directory: ${this.logPath}`);
        } else {
            console.log(`[COLLECTOR] Log directory verified: ${this.logPath}`);
        }
    }
}

const collector = new NexalDataCollector();
collector.initLogDirectory();
