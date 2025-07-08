const canvas = document.getElementById('simulationCanvas');
const ctx = canvas.getContext('2d');
const container = document.getElementById('canvas-container');
const resetButton = document.getElementById('resetButton');
let nodes = [];
let messages = [];
const NUM_NODES = 7;
let animationFrameId;

const NODE_STATE = {INITIAL: 'gray',
  PROPOSING: '#22c55e',
  ACKNOWLEDGED: '#eab308',
  FAULTY: '#ef4444',
  COMMITTED: '#10b981'};

function resizeCanvas() {
  canvas.width = container.clientWidth;
  canvas.height = container.clientHeight;
}

function init() {
  resizeCanvas();
  nodes = [];
  messages = [];
  const radius = Math.min(canvas.width, canvas.height) * 0.4;
  const center = { x: canvas.width / 2, y: canvas.height / 2 };
  for (let i = 0; i < NUM_NODES; i++) {
    const angle = (i / NUM_NODES) * 2 * Math.PI;
    nodes.push({
      id: i,
      x: center.x + radius * Math.cos(angle),
      y: center.y + radius * Math.sin(angle),
      state: NODE_STATE.INITIAL,
      isFaulty: false,
      acks: new Set()});
  }
  nodes[NUM_NODES - 1].isFaulty = true;
  nodes[NUM_NODES - 1].state = NODE_STATE.FAULTY;
  nodes[0].state = NODE_STATE.PROPOSING;
  setTimeout(() => {
    nodes[0].acks.add(0);
    for (let i = 1; i < NUM_NODES; i++) {
      messages.push({from: nodes[0],
      to: nodes[i],
      progress: 0,
      speed: 0.5 + Math.random() * 1.5,
      type: 'PROPOSE'});
    }
  }, 1000);
  if (animationFrameId) cancelAnimationFrame(animationFrameId);
  animate();
}

function drawNode(node) {
  const nodeRadius = Math.min(canvas.width, canvas.height) * 0.06;
  ctx.beginPath();
  ctx.arc(node.x, node.y, nodeRadius, 0, 2 * Math.PI);
  ctx.fillStyle = node.state;
  ctx.fill();
  ctx.strokeStyle = '#9ca3af';
  ctx.lineWidth = 2;
  ctx.stroke();
  if (node.isFaulty) {
    ctx.beginPath();
    ctx.moveTo(node.x - nodeRadius / 2, node.y - nodeRadius / 2);
    ctx.lineTo(node.x + nodeRadius / 2, node.y + nodeRadius / 2);
    ctx.moveTo(node.x + nodeRadius / 2, node.y - nodeRadius / 2);
    ctx.lineTo(node.x - nodeRadius / 2, node.y + nodeRadius / 2);
    ctx.strokeStyle = 'white';
    ctx.lineWidth = 3;
    ctx.stroke();
  }
}

function drawMessage(msg) {
  const dx = msg.to.x - msg.from.x;
  const dy = msg.to.y - msg.from.y;
  const x = msg.from.x + dx * msg.progress / 100;
  const y = msg.from.y + dy * msg.progress / 100;
  ctx.beginPath();
  ctx.arc(x, y, 5, 0, 2 * Math.PI);
  ctx.fillStyle = 'white';
  ctx.fill();
}

function animate() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  for (let i = messages.length - 1; i >= 0; i--) {
    const msg = messages[i];
    msg.progress += msg.speed;
    if (msg.progress >= 100) {
      const recipient = msg.to;
      if (!recipient.isFaulty) {
        if (msg.type === 'PROPOSE' && recipient.state === NODE_STATE.INITIAL) {
          recipient.state = NODE_STATE.ACKNOWLEDGED;
          for (const node of nodes)
            if (node.id !== recipient.id)
              messages.push({from: recipient,
                to: node,
                progress: 0,
                speed: 0.5 + Math.random() * 1.5,
                type: 'ACK',
                originator: recipient.id});
        } else if (msg.type === 'ACK') recipient.acks.add(msg.originator);
      }
      messages.splice(i, 1);
    } else drawMessage(msg);
  }
  nodes.forEach(drawNode);
  animationFrameId = requestAnimationFrame(animate);
}

window.addEventListener('resize', init);
resetButton.addEventListener('click', init);
window.onload = init;
