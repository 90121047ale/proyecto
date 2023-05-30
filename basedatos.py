CREATE DATABASE guarderia_can;

-- Creación de tabla propietario
CREATE TABLE propietario (
    id_propietario INT UNSIGNED PRIMARY KEY AUTO_INCREMENT, -- Identificador único del propietario
    nombre VARCHAR(50) NOT NULL, -- Nombre del propietario
    telefono INT UNSIGNED NOT NULL, -- Teléfono del propietario
    direccion VARCHAR(50) NOT NULL -- Dirección del propietario
);

-- Creación de tabla servicio
CREATE TABLE servicio (
    id_servicio INT UNSIGNED PRIMARY KEY AUTO_INCREMENT, -- Identificador único del servicio
    nombre VARCHAR(50) NOT NULL, -- Nombre del servicio
    precio INT UNSIGNED NOT NULL -- Precio del servicio
);

-- Creación de tabla empleado
CREATE TABLE empleado (
    id_empleado INT UNSIGNED PRIMARY KEY AUTO_INCREMENT, -- Identificador único del empleado
    nombre VARCHAR(50) NOT NULL, -- Nombre del empleado
    telefono INT UNSIGNED NOT NULL, -- Teléfono del empleado
    estado BOOLEAN NOT NULL -- Estado del empleado (activo/inactivo)
);

-- Creación de tabla factura 
CREATE TABLE factura (
    id_factura INT UNSIGNED PRIMARY KEY AUTO_INCREMENT, -- Identificador único de la factura
    id_servicio INT UNSIGNED NOT NULL, -- Identificador del servicio asociado a la factura
    total INT UNSIGNED NOT NULL, -- Total de la factura
    FOREIGN KEY (id_servicio) REFERENCES servicio(id_servicio) -- Clave foránea que referencia la tabla servicio
);
 
-- Creación de tabla mascota
CREATE TABLE mascota (
    id_mascota INT UNSIGNED PRIMARY KEY AUTO_INCREMENT, -- Identificador único de la mascota
    nombre VARCHAR(50) NOT NULL, -- Nombre de la mascota
    raza VARCHAR(50) NOT NULL, -- Raza de la mascota
    tipo VARCHAR(50) NOT NULL, -- Tipo de mascota (perro, gato, etc.)
    fecha_nacimiento DATE NOT NULL, -- Fecha de nacimiento de la mascota
    estado BOOLEAN NOT NULL, -- Estado de la mascota (activo/inactivo)
    id_propietario INT UNSIGNED NOT NULL, -- Identificador del propietario de la mascota
    FOREIGN KEY (id_propietario) REFERENCES propietario(id_propietario) -- Clave foránea que referencia la tabla propietario
);

-- Creación de tabla solicitud 
CREATE TABLE solicitud (
    id_solicitud INT UNSIGNED PRIMARY KEY AUTO_INCREMENT, -- Identificador único de la solicitud
    fecha_ejecucion DATE NOT NULL, -- Fecha de inicio de la solicitud
    fecha_final DATE NOT NULL, -- Fecha de finalización de la solicitud
    numero_horas INT UNSIGNED NOT NULL, -- Número de horas de la solicitud
    pago_horas INT UNSIGNED NOT NULL, -- Pago por horas de la solicitud
    id_servicio INT UNSIGNED NOT NULL, -- Identificador del servicio asociado a la solicitud
    id_mascota INT UNSIGNED NOT NULL, -- Identificador de la mascota asociada a la solicitud
    id_empleado INT UNSIGNED NOT NULL, -- Identificador del empleado asociado a la solicitud
    id_factura INT UNSIGNED NOT NULL, -- Identificador de la factura asociada a la solicitud
    FOREIGN KEY (id_servicio) REFERENCES servicio(id_servicio), -- Clave foránea que referencia la tabla servicio
    FOREIGN KEY (id_mascota) REFERENCES mascota(id_mascota), -- Clave foránea que referencia la tabla mascota
    FOREIGN KEY (id_empleado) REFERENCES empleado(id

-- Insertar datos en la tabla propietario
INSERT INTO propietario (nombre, telefono, direccion)
VALUES
    ('Juan Pérez', 123456789, 'Calle Principal 123'),
    ('María García', 987654321, 'Avenida Central 456'),
    ('Carlos López', 456789123, 'Calle Secundaria 789'),
    ('Laura Martínez', 321654987, 'Plaza Mayor 246'),
    ('Pedro Hernández', 654321987, 'Calle Tranquila 135'),
    ('Ana Torres', 789123456, 'Avenida Principal 789'),
    ('Sofía Rodríguez', 234567891, 'Calle Central 753'),
    ('Javier Ramírez', 918273645, 'Calle Principal 987'),
    ('Valeria Silva', 567891234, 'Avenida Secundaria 642'),
    ('Gabriel Vargas', 876543219, 'Calle Tranquila 753');

-- Insertar datos en la tabla servicio
INSERT INTO servicio (nombre, precio)
VALUES
    ('Paseo', 10),
    ('Baño', 20),
    ('Corte de pelo', 15),
    ('Guardería', 30),
    ('Vacunación', 25),
    ('Desparasitación', 12),
    ('Alimentación', 8),
    ('Adiestramiento', 40),
    ('Consulta veterinaria', 35),
    ('Corte de uñas', 10);

-- Insertar datos en la tabla empleado
INSERT INTO empleado (nombre, telefono, estado)
VALUES
    ('Luisa Morales', 654789123, 1),
    ('Andrés Castro', 321987654, 1),
    ('Fernanda Ríos', 789456123, 1),
    ('Diego Mendoza', 987123456, 1),
    ('Carolina Guzmán', 456321789, 1),
    ('Roberto Sánchez', 918546372, 1),
    ('Daniela Navarro', 273645189, 1),
    ('Martín Castro', 981237465, 1),
    ('Isabella Méndez', 546372918, 1),
    ('Ricardo Guerra', 546189273, 1);

-- Insertar datos en la tabla factura
INSERT INTO factura (id_servicio, total)
VALUES
    (1, 10),
    (2, 20),
    (3, 15),
    (4, 30),
    (5, 25),
    (6, 12),
    (7, 8),
    (8, 40),
    (9, 35),
    (10, 10);

-- Insertar datos en la tabla mascota
INSERT INTO mascota (nombre, raza, tipo, fecha_nacimiento, estado, id_propietario)
VALUES
    ('Max', 'Labrador Retriever', 'Perro', '2019-01-15', 1, 1),
    ('Luna', 'Persa', 'Gato', '2020-03-10', 1, 1),
    ('Rocky', 'Bulldog Francés', 'Perro', '2018-06-20', 1, 2),
    ('Milo', 'Siames', 'Gato', '2021-02-05',1,3);

/* Insertar datos en la tabla solicitud*/
INSERT INTO solicitud (fecha_ejecucion, fecha_final, numero_horas, pago_horas, id_servicio, id_mascota, id_empleado, id_factura)
VALUES 
       ('2022-05-20', '2022-05-25', 5, 50, 1, 1, 1, 1), 
       ('2023-05-22', '2023-05-23', 3, 30, 2, 2, 2, 2);
       ('2023-04-20', '2021-05-25', 5, 50, 1, 1, 1, 1), 
       ('2023-01-22', '2022-05-23', 3, 30, 2, 2, 2, 2);
       ('2023-04-20', '2022-05-25', 5, 50, 1, 1, 1, 1), 
       ('2023-05-22', '2023-02-23', 3, 30, 2, 2, 2, 2);
       ('2023-04-20', '2023-03-25', 5, 50, 1, 1, 1, 1), 
       ('2023-05-22', '2023-08-23', 3, 30, 2, 2, 2, 2);
       ('2023-03-20', '2023-09-25', 5, 50, 1, 1, 1, 1), 
       ('2023-05-22', '2023-05-23', 3, 30, 2, 2, 2, 2);


    -- Trigger para la tabla propietario: antes de la inserción, modificación o eliminación
-- Verifica que el teléfono sea un número de 9 dígitos y la dirección no esté vacía
CREATE TRIGGER propietario_validacion
BEFORE INSERT OR UPDATE ON propietario
FOR EACH ROW
BEGIN
    IF LENGTH(NEW.telefono) != 9 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'El teléfono debe ser un número de 9 dígitos';
    END IF;
    IF NEW.direccion = '' THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'La dirección no puede estar vacía';
    END IF;
END;

-- Trigger para la tabla servicio: después de la inserción, modificación o eliminación
-- Actualiza el precio máximo de los servicios en la tabla propietario
CREATE TRIGGER servicio_actualizar_precio_max
AFTER INSERT OR UPDATE OR DELETE ON servicio
FOR EACH ROW
BEGIN
    UPDATE propietario
    SET precio_maximo = (SELECT MAX(precio) FROM servicio);
END;

-- Trigger para la tabla empleado: después de la eliminación
-- Elimina las solicitudes asociadas al empleado eliminado
CREATE TRIGGER empleado_eliminar_solicitudes
AFTER DELETE ON empleado
FOR EACH ROW
BEGIN
    DELETE FROM solicitud WHERE id_empleado = OLD.id_empleado;
END;

-- Trigger para la tabla factura: antes de la inserción
-- Calcula el total de la factura como el precio del servicio multiplicado por el número de horas
CREATE TRIGGER factura_calcular_total
BEFORE INSERT ON factura
FOR EACH ROW
BEGIN
    SET NEW.total = (SELECT precio FROM servicio WHERE id_servicio = NEW.id_servicio) * (SELECT numero_horas FROM solicitud WHERE id_factura = NEW.id_factura);
END;

-- Trigger para la tabla mascota: antes de la eliminación
-- Verifica que la mascota no esté asociada a ninguna solicitud antes de eliminarla
CREATE TRIGGER mascota_verificar_solicitudes
BEFORE DELETE ON mascota
FOR EACH ROW
BEGIN
    IF EXISTS (SELECT * FROM solicitud WHERE id_mascota = OLD.id_mascota) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'La mascota está asociada a una solicitud y no puede ser eliminada';
    END IF;
END;

-- Trigger para la tabla solicitud: después de la inserción o modificación
-- Actualiza el estado del propietario de la mascota si la solicitud está completada
CREATE TRIGGER solicitud_actualizar_estado_propietario
AFTER INSERT OR UPDATE ON solicitud
FOR EACH ROW
BEGIN
    DECLARE estado_propietario BOOLEAN;
    SET estado_propietario = (SELECT estado FROM mascota WHERE id_mascota = NEW.id_mascota);
    
    IF NEW.fecha_final < CURRENT_DATE AND NEW.estado = 1 THEN
        UPDATE mascota SET estado = 0 WHERE id_mascota = NEW.id_mascota;
    ELSEIF NEW.fecha_final >= CURRENT_DATE AND NEW.estado = 0 AND estado_propietario = 1 THEN
        UPDATE mascota SET estado = 1 WHERE id_mascota = NEW.id_mascota;
    END IF;
END;