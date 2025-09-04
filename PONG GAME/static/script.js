const canvas = document.getElementById('pongCanvas');
const ctx = canvas.getContext('2d');

const WIDTH = canvas.width;
const HEIGHT = canvas.height;

// Paddle settings
const PADDLE_WIDTH = 12;
const PADDLE_HEIGHT = 80;
const PADDLE_MARGIN = 20;
const PADDLE_SPEED = 6; // For AI

// Ball settings
const BALL_SIZE = 14;
const BALL_SPEED = 5;

// Game objects
let leftPaddle = {
    x: PADDLE_MARGIN,
    y: HEIGHT / 2 - PADDLE_HEIGHT / 2,
    width: PADDLE_WIDTH,
    height: PADDLE_HEIGHT
};

let rightPaddle = {
    x: WIDTH - PADDLE_MARGIN - PADDLE_WIDTH,
    y: HEIGHT / 2 - PADDLE_HEIGHT / 2,
    width: PADDLE_WIDTH,
    height: PADDLE_HEIGHT
};

let ball = {
    x: WIDTH / 2 - BALL_SIZE / 2,
    y: HEIGHT / 2 - BALL_SIZE / 2,
    vx: BALL_SPEED * (Math.random() > 0.5 ? 1 : -1),
    vy: BALL_SPEED * (Math.random() > 0.5 ? 1 : -1),
    size: BALL_SIZE
};

let leftScore = 0;
let rightScore = 0;

// Mouse control for left paddle
canvas.addEventListener('mousemove', function (e) {
    const rect = canvas.getBoundingClientRect();
    let mouseY = e.clientY - rect.top;
    leftPaddle.y = mouseY - leftPaddle.height / 2;
    // Keep paddle within bounds
    leftPaddle.y = Math.max(0, Math.min(HEIGHT - leftPaddle.height, leftPaddle.y));
});

// Reset ball to center
function resetBall(direction = 1) {
    ball.x = WIDTH / 2 - BALL_SIZE / 2;
    ball.y = HEIGHT / 2 - BALL_SIZE / 2;
    ball.vx = BALL_SPEED * direction * (Math.random() > 0.5 ? 1 : -1);
    ball.vy = BALL_SPEED * (Math.random() > 0.5 ? 1 : -1);
}

// Draw everything
function draw() {
    ctx.clearRect(0, 0, WIDTH, HEIGHT);

    // Draw paddles
    ctx.fillStyle = '#fff';
    ctx.fillRect(leftPaddle.x, leftPaddle.y, leftPaddle.width, leftPaddle.height);
    ctx.fillRect(rightPaddle.x, rightPaddle.y, rightPaddle.width, rightPaddle.height);

    // Draw ball
    ctx.fillStyle = '#0ff';
    ctx.fillRect(ball.x, ball.y, ball.size, ball.size);

    // Draw scores
    ctx.font = '32px Segoe UI, Arial';
    ctx.fillStyle = '#fff';
    ctx.fillText(leftScore, WIDTH / 4, 50);
    ctx.fillText(rightScore, WIDTH * 3 / 4, 50);
}

// Update game state
function update() {
    // Ball movement
    ball.x += ball.vx;
    ball.y += ball.vy;

    // Wall collision
    if (ball.y <= 0) {
        ball.y = 0;
        ball.vy *= -1;
    }
    if (ball.y + ball.size >= HEIGHT) {
        ball.y = HEIGHT - ball.size;
        ball.vy *= -1;
    }

    // Paddle collision (left)
    if (
        ball.x <= leftPaddle.x + leftPaddle.width &&
        ball.y + ball.size >= leftPaddle.y &&
        ball.y <= leftPaddle.y + leftPaddle.height
    ) {
        ball.x = leftPaddle.x + leftPaddle.width;
        ball.vx *= -1;
        // Add a little randomness
        ball.vy += (Math.random() - 0.5) * 2;
    }

    // Paddle collision (right)
    if (
        ball.x + ball.size >= rightPaddle.x &&
        ball.y + ball.size >= rightPaddle.y &&
        ball.y <= rightPaddle.y + rightPaddle.height
    ) {
        ball.x = rightPaddle.x - ball.size;
        ball.vx *= -1;
        ball.vy += (Math.random() - 0.5) * 2;
    }

    // Score detection
    if (ball.x < 0) {
        rightScore++;
        resetBall(1);
    }
    if (ball.x + ball.size > WIDTH) {
        leftScore++;
        resetBall(-1);
    }

    // AI for right paddle (simple follow the ball)
    let targetY = ball.y + ball.size / 2 - rightPaddle.height / 2;
    if (rightPaddle.y < targetY) {
        rightPaddle.y += PADDLE_SPEED;
        if (rightPaddle.y > targetY) rightPaddle.y = targetY;
    } else if (rightPaddle.y > targetY) {
        rightPaddle.y -= PADDLE_SPEED;
        if (rightPaddle.y < targetY) rightPaddle.y = targetY;
    }
    // Stay in bounds
    rightPaddle.y = Math.max(0, Math.min(HEIGHT - rightPaddle.height, rightPaddle.y));
}

function gameLoop() {
    update();
    draw();
    requestAnimationFrame(gameLoop);
}

gameLoop();