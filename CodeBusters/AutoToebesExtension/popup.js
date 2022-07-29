let inputs = document.getElementsByTagName('input');

let loadTest = document.getElementById('loadTest');

// When the button is clicked, inject setPageBackgroundColor into current page
loadTest.addEventListener("click", async () => {
    let questions = "";
    for (let i = 1; i <= inputs.length; i++) {
        let element = inputs[i-1];
        let count = element.value;
        let arg = document.getElementById(element.id + "Hint").value;
        for (let j = 0; j < count; j++)
            questions += i + "-" + arg + "|";
    }
    questions = questions.substring(0, questions.length - 1);

    let [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
  
    chrome.scripting.executeScript({
      target: { tabId: tab.id },
      function: ImportTest,
      args: [questions],
    });
  });
  
  // The body of this function will be executed as a content script inside the current page
  function ImportTest(questions) {
    console.log(questions);
    if (!window.location.href.includes("https://toebes.com/codebusters/TestGenerator.html"))
        alert("Please run extension from https://toebes.com/codebusters/TestGenerator.html.");
    document.getElementById('importurl').click();
    document.getElementById('xmlurl').value = 'https://bobbbbbbb.pythonanywhere.com/test.json?Epic&' + questions; 
    document.getElementById('okimport').enabled = true; 
    document.getElementById('okimport').click();
    console.log("imported test!");
}