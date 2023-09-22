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

# DML

1. SELECT: Se usa para consultar y recuperar datos de una o mas tablas.

```sql
SELECT campo_1, campo_2 FROM nombre_tabla; -- Traer los registros solo con las columnas mencioanadas

SELECT * FROM nombre_tabla; -- Traer los registros con todas sus columnas
```

2. INSERT: Insertar o registrar datos en nuestras tablas.

```sql
INSERT INTO nombre_tabla (campos) VALUES (valores);
```

3. UPDATE: Modificar datos existentes de una tabla.

```sql
UPDATE nombre_tabla SET campo = nuevo_valor WHERE campo = valor;
```

4. DELETE: Elimina registros existentes de una tabla.

```sql
DELETE FROM nombre_tabla WHERE campo = valor;
```

## Ejercicios

### Ejercicio 1

1. Crear una base de datos llamada minimarket.
2. Crear 1 tabla llamada productos.
   - Los campos seran:
     - id
     - nombre
     - precio
3. Ejecutar los 3 comandos de DML (SELECT, INSERT, UPDATE)

## JOINS

1. INNER JOIN: Devuelve las filas cuando hay al menos una relacion.

```sql
SELECT * FROM tabla_uno INNER JOIN tabla_dos ON tabla_uno.campo_uno = tabla_dos.pk; -- pk -> PRIMARY KEY
```

2. LEFT JOIN: Devuelve todas las filas de la tabla izquierda y solo las de coincidencia de la tabla derecha.

```sql
SELECT * FROM tabla_uno LEFT JOIN tabla_dos ON tabla_uno.campo_uno = tabla_dos.pk; -- pk -> PRIMARY KEY
```

3. RIGHT JOIN: Devuelve todas las filas de la tabla derecha y las coincidencias de la tabla izquierda.

```sql
SELECT * FROM tabla_uno RIGHT JOIN tabla_dos ON tabla_uno.campo_uno = tabla_dos.pk; -- pk -> PRIMARY KEY
```

4. FULL JOIN: Devuelve todas las filas tenga una coincidencia o no.

```sql
SELECT * FROM tabla_uno FULL JOIN tabla_dos ON tabla_uno.campo_uno = tabla_dos.pk; -- pk -> PRIMARY KEY
```

---

2 TABLAS

1. inventario_2022: Contener todos los productos y la cantidad en el año 2022.
2. inventario_2023: Contener todos los productos y la cantidad en el año 2023.

- Los productos que estaban en stock en el 2022 pero no en el 2023.
- Los productos que estaban en stock en el 2023 pero no en el 2022.
- Los productos que estaban en stock en ambos años.

```sql
SELECT
COALESCE(iv_d.producto, iv_t.producto) as producto,
iv_d.cantidad as cantidad_2022,
iv_t.cantidad as cantidad_2023
FROM inventario_2022 iv_d
FULL JOIN inventario_2023 iv_t ON iv_d.producto = iv_t.producto;
```
