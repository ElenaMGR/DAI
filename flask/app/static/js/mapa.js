function crearMarcas (json){
	var mapProp = {
		center: new google.maps.LatLng(37.1892986, -3.71804),
		zoom: 12,
	};
	var map = new google.maps.Map(document.getElementById("googleMap"), mapProp);

	var myMark;
	var textInfo;
	$.each(json, function (i, v) {	
		myMark = new google.maps.LatLng(v.Latitud, v.Longitud);
		marker = new google.maps.Marker({
			position: myMark,
			map,
			title: v.Localización});
		textInfo = "" + v.Localizacion + 
			"</br>  Fecha: " + v.Fecha + 
			"</br>  Hora: " + v.Hora + 
			"</br>  Magnitud: " + v.Magnitud + 
			"</br>  Intensidad: " + v.Intensidad + 
			"</br>  Profundidad: " + v.Profundidad;
		var infoWindow = new google.maps.InfoWindow({content:textInfo});
		google.maps.event.addListener(marker, 'mouseover', function() {
			infoWindow.open(map, this);
		});
	
		google.maps.event.addListener(marker, 'mouseout', function() {
			infoWindow.close();
		});
	});
}

function myMap (){
	$.ajax({
		// la URL para la petición
		url : 'api/terremotos',

		// especifica si será una petición POST o GET
		type : 'GET',

		// el tipo de información que se espera de respuesta
		dataType : 'json',

		// código a ejecutar si la petición es satisfactoria;
		// la respuesta es pasada como argumento a la función
		success : function(json) {
			crearMarcas(json);
		},

		// código a ejecutar si la petición falla;
		// son pasados como argumentos a la función
		// el objeto de la petición en crudo y código de estatus de la petición
		error : function(xhr, status) {
			alert('Error: '+status);
		},

		// código a ejecutar sin importar si la petición falló o no
		complete : function(xhr, status) {
			console.log('Petición realizada, estado: '+status);
		}
		
	});
}