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
}

function sendPacket(fromEndpoint, toEndpoint, delay = 0) {
}

function startLightTraffic() {
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
