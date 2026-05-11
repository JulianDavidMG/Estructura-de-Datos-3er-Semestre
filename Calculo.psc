Algoritmo Notas
	Definir Examen_Final, Work_In_Out, Proyecto_Final, Promedio_Ponderado Como Real
	Escribir 'Ingresa la nota del Examen_Final: '
	Leer Examen_Final
	Escribir 'Ingresa la nota del Proyecto_Final: '
	Leer Proyecto_Final
	Escribir 'Ingresa la nota del Work_In_Out: '
	Leer Work_In_Out
	Promedio_Ponderado <- Examen_Final*0.50+Proyecto_Final*0.25+Work_In_Out*0.25
	Escribir 'La nota del tercer corte es: ', Promedio_Ponderado
FinAlgoritmo

Algoritmo sin_titulo
	Definir Celsius, Farenheit Como Real;
	Escribir "Ingresa Grados Celsius: ";
	Leer Celsius;
	Farenheit=(Celsius*(9/5))+32;
	Escribir Celsius, " Los grados Celsius son ", Farenheit, " Grados Farenheit";

FinAlgoritmo


Algoritmo Notas
	Definir Examen_Final, Work_In_Out, Proyecto_Final, Promedio_Ponderado Como Real
	Escribir 'Ingresa la nota del Examen_Final: '
	Leer Examen_Final
	Escribir 'Ingresa la nota del Proyecto_Final: '
	Leer Proyecto_Final
	Escribir 'Ingresa la nota del Work_In_Out: '
	Leer Work_In_Out
	Promedio_Ponderado <- Examen_Final*0.50+Proyecto_Final*0.25+Work_In_Out*0.25
	Escribir 'La nota del tercer corte es: ', Promedio_Ponderado
FinAlgoritmo


Algoritmo sin_titulo
	Definir Numero Como Entero;
	Escribir "Ingresa un N�mero: ";
	Leer Numero;
	
	Si Numero % 2 = 0 Entonces
		Escribir "El numero " , Numero, " Es par";
	SiNo
		Escribir "El numero " , Numero, " Es Impar";
	FinSi
FinAlgoritmo


Algoritmo sin_titulo
	Definir Numero, factorial, i Como Entero;
	Escribir "Ingresa un numero: ";
	Leer Numero;
	factorial= 1;
	Para i=1 Hasta Numero Con Paso 1 Hacer
		factorial=factorial*i;
	FinPara
	Escribir "El factorial de ", Numero, " es ", factorial;
FinAlgoritmo


lgoritmo ResolverEcuacionCuadratica
	//Declaraci�n de variables
	Definir a,b,c,discriminante Como Real;
	//Entrada de usuario para las constantes a,b,c
	Escribir "Ingrese el valor de a: "
	Leer a
	Escribir "Ingrese el valor de b: "
	Leer b
	Escribir "Ingrese el valor de c: "
	Leer c
	//calcula el discriminante
	discriminante= b*2 - 4*a*c
	//Calcula las dos raices resultantes
	raiz1=(-b + raiz(discriminante)) / (2*a);
	raiz2=(-b - raiz(discriminante)) / (2*a);
	//Muestra las raices al usuario
	Escribir "Las raices de la ecuaci�n cuadratica son: "
	Escribir "Raiz 1: ",raiz1;
	Escribir "Raiz 2: ",raiz2;
FinAlgoritmo