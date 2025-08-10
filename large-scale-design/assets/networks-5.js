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
}

function simulateCongestion() {
}

function resetSimulation() {
}

function initializeLines() {
}

window.addEventListener('load', initializeLines);
window.addEventListener('resize', initializeLines);
