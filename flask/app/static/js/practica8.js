// Activar o desactivar el modo nocturno
function cambiarModo(){
	$( ".bg-light" ).each(function() {
		if (!($( this ).is("#mainNavbar")))
			$( this ).toggleClass('bg-dark');
	});
	
	if ($( "#mainNavbar" ).is('.navbar-light'))
		$( "#mainNavbar" ).addClass('navbar-dark bg-dark').removeClass('navbar-light bg-light');
	else
		$( "#mainNavbar" ).addClass('navbar-light bg-light').removeClass('navbar-dark bg-dark');
	
	$( "#tableP8" ).toggleClass('table-dark');
}

// Crear la tabla
function crearTabla (json){
	let htmlString = ''
		$.each(json, function (i, v) {
			htmlString += `<tr id="${v.id}">
				<td>${v.imdb}</td>
				<td>${v.title}</td>
				<td>${v.year}</td>
				<td>
					<button class="btn btn-danger m-1" onclick="Pulso('${v.id}')">
						<img src="/static/images/delete.png" width="33" height="33" alt="Delete" loading="lazy"
							title="Delete">
					</button>
				</td>
			</tr>`
		});
		$( "#tbodyP8" ).append(htmlString);
}

// Click en el botón eliminar
function Pulso(value) {
	// Para poner otra vez funciones jQuery en el DOM actual
	$(function () {
		
	console.log(value)
	$( "#spinner-table" ).addClass("spinner-border");
	$( "#tbodyP8" ).empty();
	$.ajax({
		// la URL para la petición
		url : 'api/movies/'+value,

		// especifica si será una petición POST o GET
		type : 'DELETE',

		// el tipo de información que se espera de respuesta
		dataType : 'json',

		// código a ejecutar si la petición es satisfactoria;
		// la respuesta es pasada como argumento a la función
		success : function(json) {
			alert('Registro eliminado con id: '+json.id);
			peticionServidor();
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

	});
};

function peticionServidor (){
	$.ajax({
		// la URL para la petición
		url : 'api/movies',

		// especifica si será una petición POST o GET
		type : 'GET',

		// el tipo de información que se espera de respuesta
		dataType : 'json',

		// código a ejecutar si la petición es satisfactoria;
		// la respuesta es pasada como argumento a la función
		success : function(json) {
			crearTabla(json);
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
			$( "#spinner-table" ).removeClass("spinner-border");
		}
		
	});
}



// código jQuery que se ejecuta al cargar la página
$(function () {

	// evento para cuando cambia el valor introducido en un <input id="buscar" $gt;
	$('#buscar').change(function(){
		let value = $(this).val()
		console.log(value)
		$( "#spinner-table" ).addClass("spinner-border");
		$( "#tbodyP8" ).empty();
		$.ajax({
			// la URL para la petición
			url : `api/movies?title=${value}`,

			// especifica si será una petición POST o GET
			type : 'GET',

			// el tipo de información que se espera de respuesta
			dataType : 'json',

			// código a ejecutar si la petición es satisfactoria;
			// la respuesta es pasada como argumento a la función
			success : function(json) {
				crearTabla(json);
			},

			// código a ejecutar si la petición falla;
			// son pasados como argumentos a la función
			// el objeto de la petición en crudo y código de estatus de la petición
			error : function(xhr, status) {
				alert('Error: '+JSON.parse(xhr.responseText).error);
			},

			// código a ejecutar sin importar si la petición falló o no
			complete : function(xhr, status) {
				console.log('Petición realizada, estado: '+status);
				$( "#spinner-table" ).removeClass("spinner-border");
			}
			
		});
	});
});


$(document).ready(function(){
	peticionServidor();
})