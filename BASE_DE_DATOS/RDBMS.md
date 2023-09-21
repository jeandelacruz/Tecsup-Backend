# Base de datos

- Conjunto estructurado, donde vamos a almacenar
  información, de la cual iremos gestionandolo mas adelante.

## Componentes claves

- Datos: La información que almacenamos.
- Tablas: Es donde los datos guardados se organizaran.
- Motor de BD (DBMS): Es el software que se usara para interactuar con la BD.
- Índices: Estructuras que mejoran la velocidad de consultas realizadas a la BD.
- Claves (KEY): Campos especificos que ayudan a identificar un registro unico.

## Diseño de BD

Debemos crear un sistema, donde vamos a guardar las ventas relacionados con diferentes productos (libros).

1. Crear la BD (tienda_virtual)
2. Definir las tablas:
   - ventas
     - id_venta
     - nombre_cliente
     - libro_comprado
     - autor
     - precio
     - direccion_cliente

| id_venta | nombre_cliente   | libro_comprado | autor   | precio | direccion_cliente     |
| -------- | ---------------- | -------------- | ------- | ------ | --------------------- |
| 1        | Rolando Silva    | Libro A        | Autor X | 100.00 | Calle 123, Ciudad X   |
| 2        | Rolando Silva    | Libro B        | Autor Y | 150.00 | Calle 123, Ciudad X   |
| 3        | Wilson Callisaya | Libro A        | Autor X | 100.00 | Avenida 789, Ciudad Z |

- Redundancia: La dirección de Rolando Silva, la combinación del Libro A con Autor X se repiten.
- Si Rolando Silva cambia de dirección, deberiamos actualizar todos los registros del mismo.
- Si un libro cambia de precio, debemos actualizar todos los registros del mismo.

## Normalización

- Eliminar la redundancia de datos (los mismos datos almacenados en varios lugares).
- Asegurar la dependencia logica (los datos que estan relacionados se almacenan juntos).
- Facilitar la inserción, modificación y eliminación de datos.

### Primera Forma Normal (1NF)

Cada columna de una tabla tiene un valor unico y cada registro es identificado de manera unica.

### Segunda Forma Normal (2NF)

Todos sus atributos no claves dependen completamente de la clave primaria.

### Tercera Forma Normal (3NF)

Todos sus atributos no clave dependen completamente de la clave primaria y no de atributos no clave.

## Normalización de la tabla Ventas

**Tabla: Clientes**

| id_cliente | nombres          | direccion             |
| ---------- | ---------------- | --------------------- |
| 1          | Rolando Silva    | Calle 123, Ciudad X   |
| 2          | Wilson Callisaya | Avenida 789, Ciudad Z |

**Tabla: Libros**

| id_libro | titulo  | autor_id | precio |
| -------- | ------- | -------- | ------ |
| 1        | Libro A | 1        | 100.00 |
| 2        | Libro B | 2        | 150.00 |

**Tabla: Autor**

| id_autor | nombres |
| -------- | ------- |
| 1        | Autor X |
| 2        | Autor Y |

**Tabla: Ventas**

| id_venta | id_cliente | id_libro |
| -------- | ---------- | -------- |
| 1        | 1          | 1        |
| 2        | 1          | 2        |
| 3        | 2          | 1        |

# DDL

## Comandos en Terminal

- Listar las base de datos: **\l** o **\list**
- Seleccionar base de datos: **\c nombre_bd**
- Listar las tablas de mi BD (posterior a seleccionar): **\dt**
- Listar los campos de una tabla: **\d nombre_tabla**

## Comandos de DDL

1. CREATE: Utilizado para crear objetos en la BD, como tablas, vistas, indices, etc.

```sql
-- Ejemplo para crear una BD
CREATE DATABASE nombre_bd;

-- Ejemplo para crear una tabla
CREATE TABLE nombre_tabla (
    -- Se detalla los campos
    -- https://www.ibiblio.org/pub/Linux/docs/LuCaS/Tutoriales/NOTAS-CURSO-BBDD/notas-curso-BD/node134.html
    -- nombre_campo tipo_dato opciones
);
```

2. DROP: Elimina objetos de la BD.

```sql
-- Ejemplo para eliminar una BD
DROP DATABASE nombre_bd;
```

3. ALTER: Modificar los objetos de la BD.

```sql
ALTER TABLE nombre_tabla -- comandos
-- ADD -> AGREGAR
-- RENAME -> RENOMBRAR

-- Ejemplo
-- Agregar una columna nueva
ALTER TABLE nombre_tabla ADD COLUMN nombre_campo tipo_dato;

-- Renombrar una columna
ALTER TABLE nombre_table RENAME COLUMN nombre_columna TO nombre_columna_nuevo;
```

4. RENAME: Cambiar el nombre de un objeto.

```sql
ALTER TABLE nombre_tabla RENAME TO nombre_tabla_nuevo;
```
