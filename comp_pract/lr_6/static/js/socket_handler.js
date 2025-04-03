const image = document.getElementById('view')
const serverResponse = document.getElementById('server_response');
const socket = io();

socket.on('connect', () => {
    console.log('Connected to WebSocket');
});

socket.on('send_size', (data) => {
    const message = document.createElement('p');
    message.textContent = data.width + 'x' +  data.height;
    serverResponse.appendChild(message);
});

socket.on('invalid_type', (data) => {
    console.log('Received:', data);
    const message = document.createElement('p');
    message.textContent = data.result;
    serverResponse.appendChild(message);
});

document.querySelector('input[type=file]').onchange = function() {
    const preview = document.querySelector("img");
    const file = document.querySelector("input[type=file]").files[0];
    const reader = new FileReader();

    reader.addEventListener(
        "load",
        () => {
        result = reader.result;
        preview.src = result
        socket.emit('upload_image',{'image':result,'name':file.name})
        },
        false,
    );

    if (file) {
        reader.readAsDataURL(file);
    }
};
