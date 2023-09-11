document.addEventListener("DOMContentLoaded", () => {
    const headerElement = document.querySelector("header");
    const changeColorButton = document.querySelector("#changeColorButton");

    changeColorButton.addEventListener("click", () => {
        headerElement.style.color = "#FF0000"; // Color Red
    });
});
