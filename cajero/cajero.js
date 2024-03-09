const cuentas= [
    {
        "username": "admin",
        "password": "admin",
        "balance": 100
    },
    {
        "username": "user",
        "password": "user",
        "balance": 200
    },
    {
        "username": "user2",
        "password": "user2",
        "balance": 300
    }
]



document.getElementById('login').addEventListener('submit', function(e){
    e.preventDefault();
    const user = document.getElementById('user').value;
    const password = document.getElementById('password').value;
    IniciarSesion(user, password);
});





//Funcion para iniciar sesion
function IniciarSesion(username, password){
    //Obtener el usuario y la contraseña del usuario
    const user=cuentas.find(user => user.username === username&& user.password === password);
    if(user){
        alert(`Bienvenido ${user.username}`);
        window.location.href="cajero.html";
    }else{
        alert('Usuario o contraseña incorrectos');
    }
}


function IniciarSesion(username, password) {
  const cuentaEncontrada = cuentas.find(cuenta => cuenta.username === username && cuenta.password === password);
  if (cuentaEncontrada) {
    console.log('Inicio de sesión exitoso. Balance:', cuentaEncontrada.balance);
    //insertar el nombre y el saldo del usuario en el archivo html con el DOM en el archivo cajero.html
    document.getElementById('username').innerHTML = username;
    document.getElementById('balance').innerHTML = cuentaEncontrada.balance;




    // Lógica para redirigir al usuario a la página de inicio o realizar otras acciones después del inicio de sesión
  } else {
    console.log('Credenciales incorrectas. No se pudo iniciar sesión.');
    // Lógica para manejar credenciales incorrectas, como mostrar un mensaje de error al usuario
  }
}


