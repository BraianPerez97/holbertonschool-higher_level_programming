document.addEventListener("DOMContentLoaded", function () {
    const languageCodeSelect = document.getElementById("language_code");
    const translateButton = document.getElementById("btn_translate");
    const helloDiv = document.getElementById("hello");

    translateButton.addEventListener("click", function () {
      const selectedLanguage = languageCodeSelect.value;

      if (!selectedLanguage) {
        // No language selected, display an error message
        helloDiv.textContent = "Please choose a language.";
        return;
      }

      // Fetch the translation from the API
      fetch(`https://hellosalut.stefanbohacek.dev/?lang=${selectedLanguage}`)
        .then((response) => {
          if (!response.ok) {
            throw new Error("Network response was not ok");
          }
          return response.text();
        })
        .then((translation) => {
          // Display the translation in the helloDiv
          helloDiv.textContent = translation;
        })
        .catch((error) => {
          // Handle errors
          console.error("Error:", error);
          helloDiv.textContent = "An error occurred.";
        });
    });
  });
