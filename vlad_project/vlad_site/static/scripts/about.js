document.addEventListener("DOMContentLoaded", function() {
    const sections = document.querySelectorAll("section");

    sections.forEach(section => {
        section.addEventListener("mouseover", function() {
            section.style.backgroundColor = "#f0f8ff";
        });

        section.addEventListener("mouseout", function() {
            section.style.backgroundColor = "transparent";
        });
    });
});