//Servidor con express js
//importar paquetes
const express = require('express');

//CREAR EL SERVIDOR
const app=express();
//PARAMETROS PERMIT
app.use(express.urlencoded({extended:true}));
//Creamos una ruta para mostrar
app.get('/', (req, res)=>{
    console.log("Llega a la raiz");
    res.send('<h1>Bienvenido a mi pagina</h1>')
});
//Crear una ruta de contacto
app.get("/contact",(req,res)=>{
    const {name, email} = req.body
    console.log(`Nombre: ${name}`);
    console.log(`Correo electronico: ${email}`);
    res.send(`
        <h1>Contacto</h1>
        <p>El nombre es ${name} </p>
        
        `);

});



const puerto=3000;
const host="localhost";
//Inicializar el servidor
app.listen(puerto ,host , ()=>{
    console.log(`Servidor activo http://${host}:${puerto}`);
});






