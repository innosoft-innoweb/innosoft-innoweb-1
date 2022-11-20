const span = document.getElementById("status")

// change color of the span depending on the status
const changeColor = (status) => {
    if (status === "Abierto") {
        span.style.color = "var(--clr-yellow)"
    } else if(status === "Finalizado") {
        span.style.color = "var(--clr-red)"
    } else {
        span.style.color = "var(--clr-green)"
    }
}


window.onload = (event) => {
    changeColor(span.innerText)
};