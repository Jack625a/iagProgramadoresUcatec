//Clase para calculadora
class calculadora{
    //Metodo para sumar
    static sumar(num1, num2){
        return num1 + num2;
    }
    //Metodo para restar
    static restar(num1, num2){
        return num1 - num2;
    }
    //Metodo para multiplicar
    static multiplicar(num1, num2){
        return num1 * num2;
    }
    //Metodo para dividir
    static dividir(num1, num2){
        return num1 / num2;
    }
    //Metodo para calcular el factorial
    static factorial(num1){
        let resultado = 1;
        for(let i = 1; i <= num1; i++){
            resultado *= i;
        }
        return resultado;
    }
    //Metodo para calcular la potencia
    static potencia(num1, num2){
        return Math.pow(num1, num2);
    }
    //Metodo para calcular la raiz cuadrada

}

