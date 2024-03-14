//Obtener la hoja de calculo con datos
var hojaCalculo=SpreadsheetApp.getActiveSpreadsheet();
//Obtene la hoja de configuraciones
var hojaConfiguracion=hojaCalculo.getSheetByName("Configuracion");

//Funcion que se activa cuando tengamos una solicitud POST
function doPost(evento) {
    var datosEvento=JSON.parse(evento.postData.contents);
    //Llamar a la funcion para enviarMensajeBot con los datos obtenido y guardarlos en las respuestas
    var respuesta=enviarMensajeBot(JSON.stringify(datosEvento));
}
//Funcion para enviar el mesaneje a telegram
function enviarMensajeBotTelegram(mensaje,numero,api,token,imagen){
    try{
        var opciones={}
        if(mensaje){
            opciones={
                'headers':{"Content-Type": "application/json"},  
                'method':'POST',
                'payload':JSON.stringify({
                    "method": "sendMessage", 
                    "chat_id":numero,
                    "text": mensaje,
                    "parse_mode": "HTML",
                }) 
            };
        }
        var respuesta=UrlFetchApp.fetch(api+"bot"+token+"/",opciones);
        var jsonRespuesta=JSON.parse(respuesta.getContentText());
    }catch(error){

    }
}

//Funcion para enviar mensajes al bot
function enviarMensajeBot(mensaje){
    var respuestaJSON={}
    try{
        //El mensaje que se enviar a telegram
        var mensajeJSON=JSON.parse(mensaje);
        var token=hojaConfiguracion.getRange(2,12).getValue();
        var api=hojaConfiguracion.getRange(2,11).getValue();
        var numeroDestino=mensajeJSON.message.chat.id;
        if(!mensajeJSON.message.text||mensajeJSON.message.text==="/start"){
            return;
        }
        //Buscar el mensaje
        var mensajeBuscar=mensajeJSON.message.text;
        //El manejo del historial de conversaciones
        var cache=CacheService.getScriptCache();
        var conversaciones=[];
        if(cache.get("conversaciones"+numeroDestino)!=null){
            conversaciones=JSON.parse(cache.get("conversaciones"+numeroDestino));
        }
        //Palabras para volver activar el bot
        if(hojaConfiguracion.getRange(2,1).getValue().toUpperCase().includes(mensajeBuscar.toUpperCase())){
            mensajeBuscar="Hola CHATBOT";
            conversaciones=[];
        }

        var respuestaNotificacion=JSON.parse(eventoNotificacion(mensajeBuscar,JSON.stringify(conversaciones)));
        if((respuestaNotificacion.message).toUpperCase().includes("PEDIDO_A123")){
            var hojaSolicitud=hojaCalculo.getSheetByName("Solicitud");
            var codigo="SOL_"+hojaSolicitud.getLastRow()+1;
            hojaSolicitud.appendRow([codigo,numeroDestino,new Date(),JSON.stringify(conversaciones)]);
            respuestaNotificacion.message="Gracias por realizar su pedido, el codigo del pedido es:"+codigo;
            conversaciones=[];
        }else{
            conversaciones.push({"entrada":mensajeBuscar,"salida":respuestaNotificacion.message});
        }
        enviarMensajeBotTelegram(respuestaNotificacion.message,numeroDestino,api,token,"");

        cache.put('conversaciones'+numeroDestino, JSON.stringify(conversaciones), 600);
        respuestaJSON.status="";
        respuestaJSON.message="Exito";
}catch(error){
    respuestaJSON.status="-1";
    respuestaJSON.message=error.toString();
}
return JSON.stringify(respuestaJSON);

};

//Funcion para la notificacion//
function eventoNotificacion(){

}