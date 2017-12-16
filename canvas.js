$(document).ready(function() {

  var canvas = document.querySelector('canvas');
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;
  var c = canvas.getContext('2d');

  piTwo = Math.PI * 2;
  var v = 70;

  function Circle(x, y, dx, dy, radius, fill) {
    this.x = x;
    this.y = y;
    this.dx = dx;
    this.dy = dy;
    this.radius = radius;
    this.fill = fill;

    this.draw = function() {
      c.beginPath();
      c.arc(this.x, this.y, this.radius, 0, piTwo, false);
      c.fillStyle = this.fill;
      c.fill();

      c.fillStyle = "black";
      c.font = "bold 40px Arial";
      c.fillText("THE INNANET", (canvas.width / 2) - 150, (canvas.height / 2));
    }

    this.update = function() {
      this.x += this.dx;
      this.y += this.dy;
      if (this.x + this.radius > innerWidth || this.x - this.radius < 0) { this.dx = -this.dx; }
      if (this.y + this.radius > innerHeight || this.y - this.radius < 0) { this.dy = -this.dy; }

      this.draw();
    }
  }

  var circleArray = [];

  function getArray() {
      return $.getJSON('objects.json');
  }

  getArray().done(function(json) {
    
      for (var i = 0; i < json.length; i++) {
        var fill = json[i]["color"]; 
        var velocity = json[i]["velocity"];
        var radius = json[i]["size"];  
        var x = Math.random() * innerWidth;
        var y = Math.random() * innerHeight;
        var dx =  velocity;
        var dy = velocity;
        circleArray.push(new Circle(x, y , dx, dy, radius, fill));
      }
    });

  function animate() {
    requestAnimationFrame(animate);
    c.clearRect(0, 0, innerWidth, innerHeight);

    for (var i = 0; i < circleArray.length; i++) {
          circleArray[i].update();
    }
  }

  animate();

});
