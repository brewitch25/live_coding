
#include <iostream>
using namespace std;


// Enunciado:
// Crea una funcion que reciba coordenadas (x, y) y verifique si estan dentro de los limites
// de una matriz de tamaño filas x columnas. Imprime si la posicion es valida o no.


// PISTA: Esta funcion debe retornar true si la posicion esta dentro de los limites
// DESARROLLAR ESTA FUNCION
bool esPosicionValida(int x, int y, int filas, int columnas)
{
    if(x >= 0 && x < columnas && y >= 0 && y < filas) {
        return true;
    } else {
        return false;
    }
    // TODO: Verificar que x este dentro del rango de columnas
    // TODO: Verificar que y este dentro del rango de filas
    // TODO: Retornar true solo si AMBAS condiciones se cumplen
}

int main()
{
    int filas, columnas;

    // Pedir al usuario el numero de filas y columnas
    cout << "Ingrese el numero de filas: "; cin >> filas;
    cout << "Ingrese el numero de columnas: "; cin >> columnas;
    
    int x, y;
    // Pedir al usuario las coordenadas x e y
    cout << "Ingrese coordenada x (columna): "; cin >> x;
    
    cout << "Ingrese coordenada y (fila): "; cin >> y;
    

    // Usar la funcion para verificar si la posicion es valida
    if (esPosicionValida(x, y, filas, columnas)) {
        cout <<"Es posicion valida" << endl;
    } else {
        cout <<"Es posicion invalida, fuera de los limites" << endl;
    }
    // TODO: Mostrar mensaje de posicion valida ej: la posicion (x, y) esta dentro del laberinto
    // TODO: Mostrar mensaje de posicion invalida, ej: la posicion (x, y) esta fuera del laberinto

    return 0;
}
