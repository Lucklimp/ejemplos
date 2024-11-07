CREATE DATABASE IF NOT EXISTS gestion_empleados_mg;
USE gestion_empleados_mg;

CREATE TABLE IF NOT EXISTS empleados (
    ID_RUT INT NOT NULL AUTO_INCREMENT,
    NOMBRE VARCHAR(255) NOT NULL,
    FECHA_NAC DATE NOT NULL,
    FECHA_CONTRATO DATE NOT NULL,
    SUELDO INT NOT NULL,
    TELEFONO INT NOT NULL,
    DIRECCION VARCHAR(150) NOT NULL,
    ID_ROL INT NOT NULL,
    ID_TIPO INT NOT NULL, 
    NOM_USUARIO VARCHAR(255) NOT NULL,
    PASSWORD VARCHAR (255) NOT NULL,
    PRIMARY KEY (ID_RUT),
    FOREIGN KEY (ID_ROL) REFERENCES roles(ID_ROL),
    FOREIGN KEY (ID_TIPO) REFERENCES tipo_empleado(ID_TIPO));

CREATE TABLE IF NOT EXISTS tipo_empleado (
    ID_TIPO INT NOT NULL,
    TIPO VARCHAR (100) NOT NULL,
    PRIMARY KEY (ID_TIPO));

CREATE TABLE IF NOT EXISTS departamento (
    ID_DEPTO INT NOT NULL,
    NOMBRE VARCHAR(150) NOT NULL,
    ID_RUT INT NOT NULL,
    PRIMARY KEY (ID_DEPTO),
    FOREIGN KEY (ID_RUT) REFERENCES empleados(ID_RUT));

CREATE TABLE IF NOT EXISTS asignacion (
    ID_ASIG INT NOT NULL,
    ID_DEPTO INT NOT NULL,
    ID_RUT INT NOT NULL,
    PRIMARY KEY (ID_ASIG),
    FOREIGN KEY (ID_DEPTO) REFERENCES departamento(ID_DEPTO),
    FOREIGN KEY (ID_RUT) REFERENCES empleados(ID_RUT));

CREATE TABLE IF NOT EXISTS proyecto (
    ID_PROYECTO INT NOT NULL,
    NOMBRE VARCHAR(255) NOT NULL,
    DESCRIPCION VARCHAR(255) NOT NULL,
    FECHA_INICIO DATE NOT NULL,
    FECHA_PLAZO DATE NOT NULL,
    PRIMARY KEY (ID_PROYECTO));

CREATE TABLE IF NOT EXISTS proyecto_emp (
    ID_PROYEMP INT NOT NULL,
    ID_PROYECTO INT NOT NULL,
    ID_TIPO INT NOT NULL,
    PRIMARY KEY (ID_PROYEMP),
    FOREIGN KEY ID_PROYECTO REFERENCES proyecto(ID_PROYECTO),
    FOREIGN KEY ID_TIPO REFERENCES tipo_empleado(ID_TIPO));

CREATE TABLE IF NOT EXISTS informe (
    ID_INFORME INT NOT NULL,
    ID_RUT INT NOT NULL,
    FECHA_HORA DATE NOT NULL,
    REPORTE TEXT NOT NULL,
    PRIMARY KEY (ID_INFORME),
    FOREIGN KEY ID_RUT REFERENCES empleados(ID_RUT));

CREATE TABLE IF NOT EXISTS registro_tiempo (
    ID_REG_TIEMPO INT NOT NULL,
    FECHA DATE NOT NULL,
    CANT_HORAS INT NOT NULL,
    DESCRIPCION VARCHAR(255) NOT NULL,
    HORA_EXTRA INT NOT NULL,
    OBSERVACION VARCHAR(255) NOT NULL,
    ID_PROYEMP INT NOT NULL,
    PRIMARY KEY (ID_REG_TIEMPO),
    FOREIGN KEY ID_PROYEMP REFERENCES proyecto_emp(ID_PROYEMP));

CREATE TABLE IF NOT EXISTS modulos (
    ID_MODULO INT NOT NULL,
    NOM_MODULO VARCHAR (100) NOT NULL,
    ID_ROL INT NOT NULL,
    PRIMARY KEY (ID_MODULO),
    FOREIGN KEY ID_ROL REFERENCES (ID_ROL));

CREATE TABLE IF NOT EXISTS roles (
    ID_ROL INT NOT NULL,
    ROL VARCHAR (150) NOT NULL,
    PERMISOS VARCHAR (150) NOT NULL,
    PRIMARY KEY (ID_ROL));