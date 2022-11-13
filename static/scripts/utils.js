const span = document.getElementById("status")

// change color of the span depending on the status
const changeColor = (status) => {
    if (status === "Abierto") {
        span.style.color = "orange"
    } else if(status === "Cerrado") {
        span.style.color = "red"
    } else {
        span.style.color = "green"
    }
}


window.onload = (event) => {
    changeColor(span.innerText)
};