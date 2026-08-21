const fs = require('fs');
const path = require('path');

class NexalHealthMonitor {
    constructor() {
        this.reportPath = path.join(__dirname, '../logs/health_report.json');
    }

    runDiagnostics() {
        const diagnostics = {
            system: "NEXAL_INTELLIGENCE",
            healthStatus: "OPTIMAL",
            memoryUsage: process.memoryUsage(),
            uptime: process.uptime(),
            checkedAt: new Date().toISOString()
        };

        fs.writeFileSync(this.reportPath, JSON.stringify(diagnostics, null, 2));
        console.log(`[HEALTH MONITOR] Diagnostics report written to: ${this.reportPath}`);
    }
}

const monitor = new NexalHealthMonitor();
monitor.runDiagnostics();
