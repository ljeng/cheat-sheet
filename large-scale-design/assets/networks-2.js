let systemState = {
  nodes: ['healthy', 'failed', 'healthy'],
  leader: 1
};

function simulateFailure() {
  const healthyNodes = systemState.nodes.map((state, index) => 
    state === 'healthy' ? index : -1
  ).filter(index => index !== -1);
  
  if (healthyNodes.length > 0) {
    const randomIndex = healthyNodes[Math.floor(Math.random() * healthyNodes.length)];
    systemState.nodes[randomIndex] = 'failed';
    updateDisplay();
    setTimeout(() => {
      alert(`Node ${randomIndex + 1} has failed! System is adapting...`);
    }, 500);
  }
}

function simulateRecovery() {
  const failedNodes = systemState.nodes.map((state, index) => 
    state === 'failed' ? index : -1
  ).filter(index => index !== -1);
  if (failedNodes.length > 0) {
    const randomIndex = failedNodes[Math.floor(Math.random() * failedNodes.length)];
    systemState.nodes[randomIndex] = 'healthy';
    updateDisplay();
    setTimeout(() => {
      alert(`Node ${randomIndex + 1} has recovered and rejoined the system!`);
    }, 500);
  }
}

function resetSystem() {
  systemState.nodes = ['healthy', 'failed', 'healthy'];
  updateDisplay();
}

function updateDisplay() {
  const allScenarios = document.querySelectorAll('.scenario');
  allScenarios.forEach((scenario, scenarioIndex) => {
    const nodes = scenario.querySelectorAll('.node');
    nodes.forEach((node, nodeIndex) => {
      const state = systemState.nodes[nodeIndex];
      if (!state) return;
      const statusIndicator = node.querySelector('.status-indicator');
      node.classList.remove('healthy', 'failed', 'promoting');
      if (statusIndicator) {
        statusIndicator.classList.remove('online', 'offline');
      }
      node.classList.add(state);
      if (statusIndicator) {
        statusIndicator.classList.add(state === 'healthy' ? 'online' : 'offline');
      }
    });
    if (scenarioIndex === 1) {
      const arrows = scenario.querySelectorAll('.arrow');
      arrows.forEach((arrow, arrowIndex) => {
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
  const healthyCount = systemState.nodes.filter(state => state === 'healthy').length;
  const failedCount = systemState.nodes.filter(state => state === 'failed').length;
  const metricCards = document.querySelectorAll('.metric-value');
  if (metricCards.length >= 2) {
    metricCards[0].textContent = healthyCount;
    metricCards[1].textContent = failedCount;
  }
}

setInterval(() => {
  const heartbeats = document.querySelectorAll('.heartbeat');
  heartbeats.forEach(hb => {
    hb.style.animation = 'none';
    setTimeout(() => {
      hb.style.animation = 'heartbeat 1s infinite';
    }, 10);
  });
}, 2000);
