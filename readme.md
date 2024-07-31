# Implementación de una Lista Enlazada en Python

Este proyecto implementa una lista enlazada simple en Python, dividida en dos módulos principales: `Node` y `LinkedList`, y un archivo `__main__.py` para pruebas.

## Estructura del Proyecto

linked_list/
│
├── node.py
├── linked_list.py
└── main.py


### Descripción de los Módulos

- **node.py**: Define la clase `Node`, que representa un nodo en la lista enlazada. Cada nodo contiene un valor (`value`) y un puntero al siguiente nodo (`next`).

- **linked_list.py**: Define la clase `LinkedList`, que maneja la lista enlazada. Incluye métodos para agregar, eliminar, mostrar, y manipular nodos en la lista. Los métodos principales incluyen:
  - `add(value, position)`: Agrega un nodo en una posición específica.
  - `delete(value)`: Elimina un nodo que contiene el valor especificado.
  - `display()`: Muestra todos los valores en la lista enlazada.
  - `shift()`: Elimina el primer nodo de la lista.
  - `unshift(value)`: Agrega un nodo al principio de la lista.
  - `push(value)`: Agrega un nodo al final de la lista.

### Archivo Principal
- **__main__.py**: Este archivo se utiliza para probar la funcionalidad de la lista enlazada. Incluye ejemplos de cómo usar los diferentes métodos de la clase `LinkedList`.

## Ejecución del programa
1. **Agregar un Nodo**: Puedes agregar un nodo en una posición específica utilizando el método `add(value, position)`.
2. **Eliminar un Nodo**: Para eliminar un nodo con un valor específico, usa el método `delete(value)`.
3. **Mostrar la Lista**: Para mostrar todos los nodos en la lista enlazada, utiliza el método `display()`.
4. **Manipulación de Nodos**:
   - `shift()`: Elimina el primer nodo de la lista y devuelve su valor.
   - `unshift(value)`: Agrega un nuevo nodo al principio de la lista.
   - `push(value)`: Agrega un nuevo nodo al final de la lista.

Para ejecutar el archivo principal y probar la implementación, navega al directorio del proyecto y ejecuta:

```bash
python3 __main__.py
```
Este comando ejecutará el archivo __main__.py y mostrará ejemplos de cómo usar los métodos de la clase LinkedList.

¡Espero que esta implementación te sea útil para entender y trabajar con listas enlazadas en Python!
