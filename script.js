let isFirst = true;

  setInterval(() => {
    document.getElementById("walk").src = isFirst ? "assets\\soul_walk.png" : "assets\\soul_notwalk.png";
    isFirst = !isFirst;
  }, 100); 