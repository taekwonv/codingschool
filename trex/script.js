var cvs = document.getElementById("canvas");
var ctx = cvs.getContext("2d");

// load images
var trex = new Image();
var bg = new Image();
var cactus = new Image();

trex.src = "trex2.png";
bg.src = "bg.png";
cactus.src = "cactus.png";

var land = 192;
var trexX = 10;
var trexY = 145;
var cactusY = 145;
var gravity = 1.2;
var score = 0;
var threshold = 125;
var level = 1;
var objects = [];
objects[0] = {
	x: cvs.width,
	y: cactusY
};
var jumpsteps = [];

document.addEventListener("keydown", jump);

function jump() {
	if (trexY + trex.height >= land) {
		jumpsteps = [10, 10, 10, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1, 1, 1, 1]
	}
}

function draw() {
	// Draw background
	ctx.drawImage(bg, 0, 0);

	// Draw cactus
	for (var i = 0; i < objects.length; i++) {
		if (objects[i].x + cactus.width >= 0) {
			ctx.drawImage(cactus, objects[i].x, objects[i].y)
		} 
		else continue;

		objects[i].x --;

		if (objects[i].x == threshold) {
			objects.push({
				x: cvs.width + Math.floor(Math.random()* Math.floor(30)),
				y: cactusY
			});

			if (score != 0 && score % 50 == 0) {
				threshold += 20;
				level += 1;
			}
		}

		if (trexX + trex.width >= objects[i].x && trexX < objects[i].x + cactus.width && trexY + trex.height >= objects[i].y) {
			ctx.drawImage(trex, trexX, trexY);
			ctx.fillStyle = "#000";
			ctx.font = "20px Verdana";
			ctx.fillText("Oh Trex!!", 100, cvs.height / 2 - 50);
			ctx.font = "15px Verdana";
			ctx.fillText("Score : " + score + "  Level: " + level, 100, cvs.height / 2);
			ctx.fillText("Press F5 to continue!", 100, cvs.height / 2 + 20);
			return;
		}

		if (objects[i].x == 5) {
			score += 10;
		}
	}
	
	// Recycle objects
	while (!objects.length > 0){
		if (objects[0].x + cactus.width < 0)
			objects.shift();
	}
	
	// Drwa T-rex
	ctx.drawImage(trex, trexX, trexY);

	if (jumpsteps.length > 0) {
		trexY -= jumpsteps[0];
		jumpsteps.shift();		
	}
	else if (trexY + trex.height < land) {		
		trexY += gravity;
		trexY = Math.min(trexY, land - trex.height);
	}
	
	ctx.fillStyle = "#000";
	ctx.font = "10px Verdana";
	ctx.fillText("Score : " + score, 10, cvs.height - 20);
	ctx.fillText("Level : " + level, 10, cvs.height - 10);

	requestAnimationFrame(draw);
}

draw();