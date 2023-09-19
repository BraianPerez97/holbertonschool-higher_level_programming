// Wait for the HTML document to be fully loaded before executing JavaScript code
document.addEventListener("DOMContentLoaded", function () {
    // Get references to the buttons and the list
    const addItemButton = document.getElementById("add_item");
    const removeItemButton = document.getElementById("remove_item");
    const clearListButton = document.getElementById("clear_list");
    const myList = document.querySelector(".my_list");

    // Add an event listener to the "Add item" button
    addItemButton.addEventListener("click", function () {
      // Create a new list item element
      const newItem = document.createElement("li");
      // Set the text content of the new item to "Item"
      newItem.textContent = "Item";
      // Append the new item to the list
      myList.appendChild(newItem);
    });

    // Add an event listener to the "Remove item" button
    removeItemButton.addEventListener("click", function () {
      // Get a reference to the last item in the list
      const lastItem = myList.lastChild;
      // Check if there is a last item in the list
      if (lastItem) {
        // Remove the last item from the list
        myList.removeChild(lastItem);
      }
    });

    // Add an event listener to the "Clear list" button
    clearListButton.addEventListener("click", function () {
      // Remove all the child elements (list items) from the list
      myList.innerHTML = "";
    });
  });
