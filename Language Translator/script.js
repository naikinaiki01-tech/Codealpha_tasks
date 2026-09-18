document.getElementById("translate").onclick = function() {

    let text = document.getElementById("text").value;

    let source = document.getElementById("source").value;

    let target = document.getElementById("target").value;

    if (text == "") {
        alert("Please enter some text.");
        return;
    }

    let url = "https://api.mymemory.translated.net/get?q="
        + encodeURIComponent(text)
        + "&langpair="
        + source
        + "|"
        + target;

    fetch(url)
        .then(response => response.json())
        .then(data => {

            let translation = data.responseData.translatedText;

            document.getElementById("result").innerText = translation;

        })
        .catch(error => {

            document.getElementById("result").innerText =
                "Translation failed.";

        });
};