<?php
    $cuentas=[
        [
            "username"=>"admin",
            "password"=>"admin",
            "balance"=>100
        ],
        [
            "username"=>"user",
            "password"=>"user",
            "balance"=>200
        ]
        ];
if(isset($_POST["username"]) && isset($_POST["password"])){
    $username=$_POST["username"];
    $password=$_POST["password"];

    foreach($cuentas as $cuenta){
        if($cuenta["username"]==$username && $cuenta["password"]==$password){
            session_start();
            $_SESSION["username"]=$username;
            $_SESSION["password"]=$password;
            $_SESSION["balance"]=$cuenta["balance"];
            header("Location: menu.php");
            exit();
            
        }
    }
}

?>