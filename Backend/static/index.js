const user = document.getElementById("user")
const password = document.getElementById("password")

const auth = () =>{
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");

    var raw = JSON.stringify({
        "username": `${user.value}`,
        "password": `${password.value}`
    });

    var requestOptions = {
        method: 'POST',
        headers: myHeaders,
        body: raw,
        redirect: 'follow'
    };

    fetch("http://127.0.0.1:3000/auth/login", requestOptions)
    .then(response => {
        if(response.status == 200){
            window.location.href = '/inicio';
        }
    })
    .catch(error => console.log('error', error));
}