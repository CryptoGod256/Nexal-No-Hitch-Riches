const NEXAL_BRIDGE = {
    pollInterval: 5000, 
    lastSignalId: null,

    async fetchTelemetry() {
        try {
            const response = await fetch('/api/signals.json');
            const data = await response.json();
            if (data.id !== this.lastSignalId) {
                this.lastSignalId = data.id;
                console.log("NEXAL: New signal detected", data);
            }
        } catch (error) {
            console.error("NEXAL Bridge Error: Stream interrupted");
        }
    }
};
setInterval(() => NEXAL_BRIDGE.fetchTelemetry(), NEXAL_BRIDGE.pollInterval);
