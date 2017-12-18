$(document).ready(function() {

  $(function() {
    $('.loading_wrap').fadeOut(1000, function() {
      $('#mega-container').fadeIn(2000);
      $('body').addClass('makeSquareGreen');
    });
  });

  var canvas = document.querySelector('canvas');
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;
  var c = canvas.getContext('2d');

  var piTwo = Math.PI * 2;
  var v = 70;

  function Circle(x, y, dx, dy, radius, fill, stroke) {

    this.x = x;
    this.y = y;
    this.dx = dx;
    this.dy = dy;
    this.radius = radius;
    this.fill = fill;
    this.stroke = stroke;

    this.draw = function() {
      c.beginPath();
      c.arc(this.x, this.y, this.radius, 0, piTwo, false);
      c.fillStyle = this.fill;
      c.strokeStyle = this.stroke;
      c.lineWidth = 0.75;
      c.stroke()
      c.fill();
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
        var stroke = json[i]["proto"]  
        var x = Math.random() * innerWidth;
        var y = Math.random() * innerHeight;
        var dx =  velocity;
        var dy = velocity;
        
        circleArray.push(new Circle(x, y , dx, dy, radius, fill, stroke));

      }
    });

  function animate() {
    requestAnimationFrame(animate);
    c.clearRect(0, 0, innerWidth, innerHeight);

    for (var i = 0; i < circleArray.length; i++) {
          circleArray[i].update();
    }

    // WORDS ARE IMPORTANT
    c.fillStyle = "#0000008f"
    c.fillRect((canvas.width / 2) - 155 ,(canvas.height / 2.29),275,135)    
    c.fill();

    c.font = "bold 40px Arial";
    c.fillStyle = "red";
    c.fillText(" C ", (canvas.width / 2) - 155, (canvas.height / 2));
    c.fillStyle = "orange";
    c.fillText(" O ", (canvas.width / 2) - 123 , (canvas.height / 2));
    c.fillStyle = "yellow";
    c.fillText(" L ", (canvas.width / 2) - 89, (canvas.height / 2));
    c.fillStyle = "green";
    c.fillText(" O ", (canvas.width / 2) - 63, (canvas.height / 2));
    c.fillStyle = "blue";
    c.fillText(" R ", (canvas.width / 2) - 29 , (canvas.height / 2));

    c.fillStyle = "white";
    c.fillText("  T    ", (canvas.width / 2) - 8.6, (canvas.height / 2));
    c.fillText("    H  ", (canvas.width / 2) - 2, (canvas.height / 2));
    c.fillText("        E", (canvas.width / 2) - 10, (canvas.height / 2));
    c.fillText(" I N N A N E T ", (canvas.width / 2) - 150, (canvas.height / 1.85));

    c.font = "bold 19.5px Arial";
    c.fillText(" created by 2hands10fingers ", (canvas.width / 2) - 150, (canvas.height / 1.75));
    c.fillStyle = "black;"

  }
    
  animate();

});
