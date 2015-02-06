var app = angular.module("servicio",[]);

	app.controller('IndicadoresController', ['$scope','$http', 
		function($scope, $http){
		
		$scope.nombre = "Nombre del Campo";
		$scope.valor = "Valor del Campo"

		$scope.indicadores = [];

		$http.get('http://127.0.0.1:5000/').success(function(data){
			$scope.indicadores = data;

			$scope.indicadores.splice(-1,4);


		})

		$scope.Calcular = function() {
			var peso = $scope.txtPeso;

			angular.forEach($scope.indicadores,function(item,index){
				if (item.name =="Dolar Observado ") {
					item.conversion = peso / parseInt(item.value) ;
				}
							
			})

		}
	}])