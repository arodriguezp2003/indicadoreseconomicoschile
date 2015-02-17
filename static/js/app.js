var app = angular.module('servicio',['monedachile']);

	app.controller('IndicadoresController', ['$scope','$http', 
		function($scope, $http){
		
		$scope.nombre = "Nombre del Campo";
		$scope.valor = "Valor del Campo"

		$scope.indicadores = [];

		$http.get('/api').success(function(data){
			$scope.indicadores = data;

			$scope.indicadores.splice(-1,4);


		})

		$scope.Calcular1 = function() {
			var peso = $scope.txtPeso;

			angular.forEach($scope.indicadores,function(item,index){
				if (item.name =="Dolar") {
					
				}
							
			})

		}
	}])