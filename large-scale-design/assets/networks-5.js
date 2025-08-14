let simulationActive = false;
let queueLevel = 0;
let packetsDropped = 0;
let congestionSignals = 0;
let packetId = 0;

function updateMetrics() {
  document.getElementById('queueUtil').textContent = Math.round((queueLevel / 6) * 100) + '%';
  document.getElementById('packetsDropped').textContent = packetsDropped;
  document.getElementById('congestionSignals').textContent = congestionSignals;
}

function updateCongestionIndicator() {
  const indicator = document.getElementById('congestionIndicator');
  if (queueLevel <= 2) {
    indicator.className = 'congestion-indicator normal';
    indicator.textContent = 'Normal Traffic';
  } else if (queueLevel <= 4) {
    indicator.className = 'congestion-indicator warning';
    indicator.textContent = 'Moderate Load';
  } else {
    indicator.className = 'congestion-indicator critical';
    indicator.textContent = 'Congestion!';
  }
}

function updateQueue() {
  const slots = document.querySelectorAll('.queue-slot');
  slots.forEach((slot, index) => {
    slot.className = 'queue-slot';
    if (index < queueLevel) {
      if (index < 4) {
        slot.classList.add('filled');
      } else {
        slot.classList.add('overflow');
      }
    }
  });
  updateCongestionIndicator();
}

function createPacket(startElement, endElement, isCongested = false) {
  const packet = document.createElement('div');
  packet.className = 'packet' + (isCongested ? ' congested' : '');
  packet.id = 'packet' + packetId++;
  const startRect = startElement.getBoundingClientRect();
  const diagramRect = document.getElementById('networkDiagram').getBoundingClientRect();
  packet.style.left = (startRect.left - diagramRect.left + startRect.width/2) + 'px';
  packet.style.top = (startRect.top - diagramRect.top + startRect.height/2) + 'px';
  document.getElementById('networkDiagram').appendChild(packet);
  return packet;
}

function animatePacket(packet, endElement, callback) {
  const endRect = endElement.getBoundingClientRect();
  const diagramRect = document.getElementById('networkDiagram').getBoundingClientRect();
  setTimeout(() => {
    packet.style.left = (endRect.left - diagramRect.left + endRect.width/2) + 'px';
    packet.style.top = (endRect.top - diagramRect.top + endRect.height/2) + 'px';
    setTimeout(() => {
      if (packet.parentNode) {
        packet.parentNode.removeChild(packet);
      }
      if (callback) callback();
    }, 800);
  }, 100);
}

function sendPacket(fromEndpoint, toEndpoint, delay = 0) {
  setTimeout(() => {
    if (!simulationActive) return;
    const fromEl = document.getElementById(fromEndpoint);
    const toEl = document.getElementById(toEndpoint);
    const switchEl = document.getElementById('switch');
    fromEl.classList.add('sending');
    setTimeout(() => fromEl.classList.remove('sending'), 500);
    if (queueLevel >= 6) {
      packetsDropped++;
      congestionSignals++;
      const droppedPacket = createPacket(fromEl, switchEl, true);
      animatePacket(droppedPacket, switchEl, () => {
        document.getElementById('statusText').textContent = 
          'Packet dropped due to queue overflow! Congestion signal sent to ' + fromEndpoint + '.';
      });
      updateMetrics();
      return;
    }
    queueLevel++;
    updateQueue();
    const packet = createPacket(fromEl, switchEl, queueLevel > 4);
    animatePacket(packet, switchEl, () => {
      setTimeout(() => {
        if (queueLevel > 0) {
          queueLevel--;
          updateQueue();
          const outPacket = createPacket(switchEl, toEl, queueLevel > 4);
          animatePacket(outPacket, toEl);
          if (queueLevel > 4) {
            congestionSignals++;
            document.getElementById('statusText').textContent = 
              'Queue congestion detected! ECN signal sent to endpoints.';
          }
        }
        updateMetrics();
      }, Math.random() * 500 + 200);
    });
  }, delay);
}

function startLightTraffic() {
  resetSimulation();
  simulationActive = true;
  document.getElementById('statusText').textContent = 'Light traffic simulation started. Packets flowing normally.';
  const sendInterval = setInterval(() => {
    if (!simulationActive) {
      clearInterval(sendInterval);
      return;
    }
    const endpoints = ['endpoint1', 'endpoint2', 'endpoint3', 'endpoint4'];
    const from = endpoints[Math.floor(Math.random() * endpoints.length)];
    let to = endpoints[Math.floor(Math.random() * endpoints.length)];
    while (to === from) {
      to = endpoints[Math.floor(Math.random() * endpoints.length)];
    }
    sendPacket(from, to);
  }, 1500);
}

function startHeavyTraffic() {
  resetSimulation();
  simulationActive = true;
  document.getElementById('statusText').textContent = 'Heavy traffic simulation started. Watch for queue buildup.';
  const sendInterval = setInterval(() => {
    if (!simulationActive) {
      clearInterval(sendInterval);
      return;
    }
    const endpoints = ['endpoint1', 'endpoint2', 'endpoint3', 'endpoint4'];
    for (let i = 0; i < 3; i++) {
      const from = endpoints[Math.floor(Math.random() * endpoints.length)];
      let to = endpoints[Math.floor(Math.random() * endpoints.length)];
      while (to === from) {
        to = endpoints[Math.floor(Math.random() * endpoints.length)];
      }
      sendPacket(from, to, i * 100);
    }
  }, 800);
}

function simulateCongestion() {
  resetSimulation();
  simulationActive = true;
  document.getElementById('statusText').textContent = 'Congestion scenario: Multiple hosts sending simultaneously!';
  for (let i = 0; i < 10; i++) {
    sendPacket('endpoint1', 'endpoint2', i * 50);
    sendPacket('endpoint3', 'endpoint4', i * 50 + 25);
  }
  setTimeout(() => {
      simulationActive = false;
  }, 5000);
}

function resetSimulation() {
  simulationActive = false;
  queueLevel = 0;
  packetsDropped = 0;
  congestionSignals = 0;
  packetId = 0;
  document.querySelectorAll('.packet').forEach(packet => packet.remove());
  updateQueue();
  updateMetrics();
  document.getElementById('statusText').textContent = 'Simulation reset. Ready for new traffic patterns.';
}

function initializeLines() {
  const switch1 = document.getElementById('switch');
  const endpoints = ['endpoint1', 'endpoint2', 'endpoint3', 'endpoint4'];
  const lines = ['line1', 'line2', 'line3', 'line4'];
  endpoints.forEach((endpoint, index) => {
    const endpointEl = document.getElementById(endpoint);
    const lineEl = document.getElementById(lines[index]);
    const switchRect = switch1.getBoundingClientRect();
    const endpointRect = endpointEl.getBoundingClientRect();
    const diagramRect = document.getElementById('networkDiagram').getBoundingClientRect();
    const x1 = switchRect.left - diagramRect.left + switchRect.width/2;
    const y1 = switchRect.top - diagramRect.top + switchRect.height/2;
    const x2 = endpointRect.left - diagramRect.left + endpointRect.width/2;
    const y2 = endpointRect.top - diagramRect.top + endpointRect.height/2;
    const length = Math.sqrt((x2-x1)**2 + (y2-y1)**2);
    const angle = Math.atan2(y2-y1, x2-x1) * 180/Math.PI;
    lineEl.style.width = length + 'px';
    lineEl.style.left = x1 + 'px';
    lineEl.style.top = y1 + 'px';
    lineEl.style.transform = `rotate(${angle}deg)`;
    lineEl.style.transformOrigin = '0 50%';
  });
}

window.addEventListener('load', initializeLines);
window.addEventListener('resize', initializeLines);
