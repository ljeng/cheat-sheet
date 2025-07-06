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
}

function init() {
}

function drawNode(node) {
}

function drawMessage(msg) {
}

function animate() {
}

window.addEventListener('resize', init);
resetButton.addEventListener('click', init);
window.onload = init;
