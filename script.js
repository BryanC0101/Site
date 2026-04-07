const background = document.querySelector(".background-space");

function createObject() {
    const obj = document.createElement("img");

    const images = [
        "static/images/ovni.gif",
        "static/images/planet.gif",
        "static/images/giphy.gif"
    ];

    obj.src = images[Math.floor(Math.random() * images.length)];
    obj.classList.add("object");

    //Fazer posição vertical aleatória
    obj.style.top = Math.random() * 80 + "vh";

    const duration = 8 + Math.random() * 10;
    obj.style.animationDuration = duration + "s";

    background.appendChild(obj);

    //remover depois da animação
    setTimeout(() => {
        obj.remove();
    }, duration * 1000);
}

// criar um a cada 10 segundos
setInterval(createObject, 10000);
createObject();