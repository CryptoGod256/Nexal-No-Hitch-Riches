const fs = require('fs');
const path = require('path');

class NexalPipelineSync {
    constructor() {
        this.manifestPath = path.join(__dirname, '../social-hub/index.html');
    }

    verifyManifest() {
        if (fs.existsSync(this.manifestPath)) {
            console.log(`[NEXAL PIPELINE] Social hub manifest verified at: ${this.manifestPath}`);
        } else {
            console.log(`[NEXAL PIPELINE] Warning: Social hub manifest missing.`);
        }
    }
}

const sync = new NexalPipelineSync();
sync.verifyManifest();
