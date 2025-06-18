const submitBtn = document.getElementById("submit");
const result = document.getElementById("result");

submitBtn.addEventListener("click", decypher);

async function decypher() {
    const formData  = new FormData();

    formData.append("key",  document.getElementById("key").value);
    formData.append("secret", document.getElementById("secret").value);

    fetch("/decypher", {
        method: "POST",
        body: formData
    })
        .then((response) => {
            return response.json()
        })
        .then((data) => {
            result.innerHTML = data.result || "Error!";
        });
}