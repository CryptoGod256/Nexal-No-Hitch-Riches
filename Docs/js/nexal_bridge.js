const NEXAL_BRIDGE = {
    pollInterval: 5000, 
    lastSignalId: null,
    retryCount: 0,
    maxRetries: 5,

    async fetchTelemetry() {
        try {
            const response = await fetch('/api/signals.json');
            if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
            const data = await response.json();
            
            // Reset retry count on successful fetch
            this.retryCount = 0;

            if (data.id !== this.lastSignalId) {
                this.lastSignalId = data.id;
                console.log("[NEXAL BRIDGE] New signal detected & synchronized:", data);
                this.dispatchSignalEvent(data);
            }
        } catch (error) {
            this.retryCount++;
            console.error(`[NEXAL BRIDGE ERROR] Stream interrupted (Attempt ${this.retryCount}/${this.maxRetries}):`, error.message);
            
            if (this.retryCount >= this.maxRetries) {
                console.warn("[NEXAL BRIDGE] Max retries reached. Backing off poll frequency.");
                this.pollInterval = 15000; // Backoff to 15s
            }
        }
    },

    dispatchSignalEvent(data) {
        const event = new CustomEvent('nexaSignal', { detail: data });
        window.dispatchEvent(event);
    }
};

// Initialize resilient polling loop
setInterval(() => NEXAL_BRIDGE.fetchTelemetry(), NEXAL_BRIDGE.pollInterval);
console.log("[NEXAL BRIDGE] Resilient polling and event dispatch engine initialized.");
