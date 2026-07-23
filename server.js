const http = require("http");
const fs = require("fs");
const path = require("path");

const PORT = process.env.PORT || 3000;

const server = http.createServer((req, res) => {
  const url = req.url;
  const method = req.method;

  // 1. WEB ROUTER (Clean URL Handling)
  if (method === "GET") {
    if (url === "/" || url === "/index.html") {
      return serveFile(res, "index.html", "text/html");
    }
    if (url === "/sector08" || url === "/cyber-lounge") {
      return serveFile(res, "index.html", "text/html");
    }
    
    // 2. API ENDPOINTS
    if (url === "/api/v1/status") {
      res.writeHead(200, { "Content-Type": "application/json" });
      return res.end(JSON.stringify({
        status: "ONLINE",
        system: "Nexal Intelligence Engine",
        timestamp: new Date().toISOString()
      }));
    }
  }

  // 3. WEBHOOK RECEIVER (OpenClaw & External Signals)
  if (method === "POST" && url === "/api/v1/webhook") {
    let body = "";
    req.on("data", chunk => { body += chunk.toString(); });
    req.on("end", () => {
      console.log("⚡ Webhook Event Received:", body);
      res.writeHead(200, { "Content-Type": "application/json" });
      return res.end(JSON.stringify({ received: true, status: "PROCESSED" }));
    });
    return;
  }

  // Fallback 404
  res.writeHead(404, { "Content-Type": "text/plain" });
  res.end("404: Nexal Intelligence Node Not Found");
});

function serveFile(res, filePath, contentType) {
  fs.readFile(path.join(__dirname, filePath), (err, data) => {
    if (err) {
      res.writeHead(500, { "Content-Type": "text/plain" });
      return res.end("Internal System Error");
    }
    res.writeHead(200, { "Content-Type": contentType });
    res.end(data);
  });
}

server.listen(PORT, () => {
  console.log(`🚀 Nexal Router Engine running on port ${PORT}`);
});
