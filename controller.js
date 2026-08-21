const fs = require('fs');
const path = require('path');
const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

const logPath = path.join(__dirname, 'funnel-action.log');
const approvalPath = path.join(__dirname, 'controller-approval.log');

console.log("🛡️ Nexal Human-in-the-Loop Controller Initialized...");
console.log("Waiting for agent actions to review...\n");

function checkQueue() {
  if (!fs.existsSync(logPath)) {
    setTimeout(checkQueue, 3000);
    return;
  }

  const logs = fs.readFileSync(logPath, 'utf8').trim().split('\n\n');
  const lastAction = logs[logs.length - 1];

  if (!lastAction) {
    setTimeout(checkQueue, 3000);
    return;
  }

  console.log("----------------------------------------");
  console.log("🚨 PENDING AGENT ACTION DETECTED:");
  console.log(lastAction);
  console.log("----------------------------------------");

  rl.question("👉 Approve this action? (y/n): ", (answer) => {
    const decision = answer.trim().toLowerCase() === 'y' ? 'APPROVED' : 'DENIED';
    const timestampedDecision = `[${new Date().toISOString()}]: Action ${decision} by Controller\n`;
    
    fs.appendFileSync(approvalPath, timestampedDecision);
    console.log(`✅ Status Recorded: ${decision}\n`);

    // Wait before checking for the next action
    setTimeout(checkQueue, 10000);
  });
}

checkQueue();
