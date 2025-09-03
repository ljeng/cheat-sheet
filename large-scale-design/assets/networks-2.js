let systemState = {
  nodes: ['healthy', 'failed', 'healthy'],
  leader: 1
};

function simulate(states, message) {
  const nodes = systemState.nodes.map((state, index) => 
    state === states[0] ? index : -1).filter(index =>
    index !== -1);
  if (nodes.length) {
    const i = nodes[Math.floor(Math.random() * nodes.length)];
    systemState.nodes[i] = states[1];
    updateDisplay();
    setTimeout(() => {
      alert(`Node ${i + 1} has ` + message);
    }, 500);
  }
}

function simulateFailure() {
  simulate(['healthy', 'failed'], `failed! System is adapting...`);
}

function simulateRecovery() {
  simulate(['failed', 'healthy'], `recovered and rejoined the system!`);
}

function resetSystem() {
  systemState.nodes = ['healthy', 'failed', 'healthy'];
  updateDisplay();
}

function updateDisplay() {
  const allScenarios = document.querySelectorAll('.scenario');
  allScenarios.forEach((scenario, scenarioIndex) => {
    scenario.querySelectorAll('.node').forEach((node, nodeIndex) => {
      const state = systemState.nodes[nodeIndex];
      if (!state) return;
      const statusIndicator = node.querySelector('.status-indicator');
      node.classList.remove('healthy', 'failed', 'promoting');
      if (statusIndicator)
        statusIndicator.classList.remove('online', 'offline');
      node.classList.add(state);
      if (statusIndicator)
        statusIndicator.classList.add(state === 'healthy' ? 'online' : 'offline');
    });
    if (scenarioIndex === 1) {
      scenario.querySelectorAll('.arrow').forEach((arrow, arrowIndex) => {
        if (arrowIndex === 1) {
          if (systemState.nodes[1] === 'failed') {
            arrow.classList.add('blocked');
            arrow.textContent = '✗';
          } else {
            arrow.classList.remove('blocked');
            arrow.textContent = '→';
          }
        }
      });
    }
  });
  const failedCount = systemState.nodes.filter(state
    => state === 'failed').length;
  const metricCards = document.querySelectorAll('.metric-value');
  if (metricCards.length >= 2) {
    metricCards[0].textContent = systemState.nodes.filter(state =>
      state === 'healthy').length;
    metricCards[1].textContent = failedCount;
  }
}

setInterval(() => {
  document.querySelectorAll('.heartbeat').forEach(hb => {
    hb.style.animation = 'none';
    setTimeout(() => {
      hb.style.animation = 'heartbeat 1s infinite';
    }, 10);
  });
}, 2000);
