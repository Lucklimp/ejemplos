INSERT INTO empleados (ID_RUT, NOMBRE, FECHA_NAC, FECHA_CONTRATO, SUELDO, TELEFONO, DIRECCION, ID_ROL, ID_TIPO, NOM_USUARIO, PASSWORD) VALUES
(12345678, 'Carlos Perez', '1985-04-20', '2020-01-15', 800000, 987654321, 'Calle Falsa 123', 1, 1, 'cperez', 'pass123'),
(23456789, 'Lucia Gomez', '1990-10-10', '2019-03-10', 500000, 912345678, 'Av. Siempre Viva 742', 2, 2, 'lgomez', 'pass456'),
(34567890, 'Juan Ramirez', '1978-02-22', '2018-05-30', 450000, 976543210, 'Calle 12 #34-56', 3, 1, 'jramirez', 'pass789'),
(45678901, 'Ana Torres', '1983-12-25', '2021-08-01', 700000, 998877665, 'Carrera 7 #89-10', 4, 1, 'atorres', 'pass012'),
(56789012, 'Diego Martinez', '1995-06-13', '2022-02-20', 550000, 987654322, 'Calle 45 #67-89', 5, 2, 'dmartinez', 'pass345'),
(67890123, 'Mariana Soto', '1988-11-05', '2017-11-10', 600000, 911223344, 'Avenida 50 #123-45', 6, 2, 'msoto', 'pass678'),
(78901234, 'Ricardo Diaz', '1992-03-19', '2019-07-12', 750000, 934567890, 'Calle 60 #12-45', 7, 1, 'rdiaz', 'pass901'),
(89012345, 'Sofia Vega', '1994-09-30', '2020-05-21', 470000, 945678123, 'Carrera 15 #33-76', 8, 2, 'svega', 'pass234'),
(90123456, 'Fernando Lopez', '1987-01-12', '2016-04-08', 690000, 923456789, 'Calle 22 #14-56', 9, 1, 'flopez', 'pass567'),
(10234567, 'Isabel Reyes', '1993-07-18', '2023-09-15', 620000, 912345679, 'Avenida 34 #98-76', 10, 1, 'ireyes', 'pass890');

INSERT INTO tipo_empleado (ID_TIPO, TIPO) VALUES
(1, 'Administrativo'),
(2, 'Técnico'),
(3, 'Gerencial'),
(4, 'Operativo'),
(5, 'Ventas'),
(6, 'Recursos Humanos'),
(7, 'Desarrollo de Software'),
(8, 'Marketing'),
(9, 'Finanzas'),
(10, 'Investigación y Desarrollo');


INSERT INTO departamento (ID_DEPTO, NOMBRE) VALUES
(1, 'Recursos Humanos'),
(2, 'Finanzas'),
(3, 'Tecnología'),
(4, 'Marketing'),
(5, 'Ventas'),
(6, 'Investigación y Desarrollo'),
(7, 'Servicio al Cliente'),
(8, 'Operaciones'),
(9, 'Legal'),
(10, 'Administración');

INSERT INTO asignacion (ID_ASIG, ID_DEPTO, ID_RUT) VALUES
(1, 1, 12345678),
(2, 2, 23456789),
(3, 3, 34567890),
(4, 4, 45678901),
(5, 5, 56789012),
(6, 6, 67890123),
(7, 7, 78901234),
(8, 8, 89012345),
(9, 9, 90123456),
(10, 10, 10234567);

INSERT INTO proyecto (ID_PROYECTO, NOMBRE, DESCRIPCION, FECHA_INICIO, FECHA_PLAZO) VALUES
(1, 'Desarrollo de Aplicación Móvil', 'Creación de una app para gestión de tareas.', '2023-01-10', '2023-06-10'),
(2, 'Implementación de ERP', 'Integración de un sistema ERP en la empresa.', '2023-02-15', '2023-08-15'),
(3, 'Campaña de Marketing Digital', 'Lanzamiento de una campaña en redes sociales.', '2023-03-01', '2023-09-01'),
(4, 'Mejora de Página Web', 'Rediseño y mejora de la experiencia de usuario en la web.', '2023-04-05', '2023-10-05'),
(5, 'Investigación de Mercado', 'Estudio de mercado para nuevos productos.', '2023-05-01', '2023-11-01'),
(6, 'Actualización de Infraestructura', 'Mejoras en la infraestructura tecnológica.', '2023-06-20', '2023-12-20'),
(7, 'Entrenamiento de Personal', 'Capacitación en habilidades técnicas y blandas.', '2023-07-10', '2023-12-10'),
(8, 'Proyecto de Expansión Internacional', 'Estrategia para entrar en mercados internacionales.', '2023-08-01', '2024-02-01'),
(9, 'Desarrollo de Software Personalizado', 'Creación de un software a medida para un cliente.', '2023-09-15', '2024-03-15'),
(10, 'Auditoría Interna', 'Revisión de procesos y cumplimiento normativo.', '2023-10-01', '2024-04-01');

INSERT INTO proyecto_emp (ID_PROYEMP, ID_PROYECTO, ID_TIPO) VALUES
(1, 1, 1),
(2, 1, 2),
(3, 2, 1),
(4, 2, 3),
(5, 3, 2),
(6, 4, 1),
(7, 5, 2),
(8, 6, 3),
(9, 7, 1),
(10, 8, 2);

INSERT INTO informe (ID_INFORME, ID_RUT, FECHA_HORA, REPORTE) VALUES
(1, 12345678, '2023-01-15', 'Informe mensual de desempeño del empleado.'),
(2, 23456789, '2023-01-20', 'Revisión de cumplimiento de objetivos.'),
(3, 34567890, '2023-01-25', 'Informe de actividades realizadas en el proyecto.'),
(4, 45678901, '2023-02-05', 'Análisis de los resultados de la campaña de marketing.'),
(5, 56789012, '2023-02-15', 'Informe sobre el progreso de ventas del trimestre.'),
(6, 67890123, '2023-02-25', 'Informe de auditoría interna de procesos.'),
(7, 78901234, '2023-03-10', 'Resultados de la investigación de mercado.'),
(8, 89012345, '2023-03-15', 'Informe sobre la actualización de infraestructura.'),
(9, 90123456, '2023-03-20', 'Revisión de la capacitación del personal.'),
(10, 10234567, '2023-04-01', 'Informe de finalización de proyecto y resultados.');

INSERT INTO registro_tiempo (ID_REG_TIEMPO, FECHA, CANT_HORAS, DESCRIPCION, HORA_EXTRA, OBSERVACION, ID_PROYEMP) VALUES
(1, '2023-01-12', 8, 'Trabajo en el desarrollo de la aplicación móvil.', 2, 'Se trabajó en horas extra.', 1),
(2, '2023-01-15', 7, 'Reunión de coordinación del proyecto ERP.', 0, 'No se trabajó horas extra.', 2),
(3, '2023-01-20', 6, 'Desarrollo de la campaña de marketing.', 1, 'Se trabajó una hora extra para finalizar.', 3),
(4, '2023-01-22', 8, 'Análisis de resultados de la investigación de mercado.', 0, 'Sin horas extra.', 4),
(5, '2023-02-10', 5, 'Revisión de la infraestructura tecnológica.', 3, 'Horas extra necesarias para completar la tarea.', 5),
(6, '2023-02-15', 8, 'Capacitación del personal en nuevas herramientas.', 0, 'Capacitación regular.', 6),
(7, '2023-03-01', 7, 'Desarrollo de software a medida.', 2, 'Se trabajó en horas extra para cumplir con el plazo.', 7),
(8, '2023-03-15', 8, 'Revisión de procesos y auditoría interna.', 1, 'Una hora extra para completar la auditoría.', 8),
(9, '2023-03-25', 6, 'Entrenamiento del personal en habilidades blandas.', 0, 'Sin horas extra.', 9),
(10, '2023-04-01', 8, 'Finalización de proyecto y entrega de informes.', 4, 'Horas extra para cumplir con la entrega.', 10);

INSERT INTO modulos (ID_MODULO, NOM_MODULO, ID_ROL) VALUES
(1, 'Gestión de Empleados', 1),
(2, 'Reportes de Proyectos', 2),
(3, 'Administración de Roles', 1),
(4, 'Gestión de Asignaciones', 2),
(5, 'Control de Tiempos', 3),
(6, 'Gestión de Informes', 1),
(7, 'Configuración del Sistema', 2),
(8, 'Monitoreo de Proyectos', 3),
(9, 'Capacitación de Personal', 1),
(10, 'Análisis de Datos', 3);

INSERT INTO roles (ID_ROL, ROL, PERMISOS) VALUES
(1, 'Administrador', 'Crear, Leer, Actualizar, Eliminar'),
(2, 'Gerente de Proyecto', 'Leer, Actualizar, Asignar Recursos'),
(3, 'Desarrollador', 'Leer, Crear, Actualizar'),
(4, 'Analista', 'Leer, Crear, Reportar'),
(5, 'Recursos Humanos', 'Leer, Crear, Actualizar, Eliminar Empleados'),
(6, 'Soporte Técnico', 'Leer, Actualizar, Resolver Incidencias'),
(7, 'Auditor', 'Leer, Revisar, Reportar'),
(8, 'Diseñador', 'Leer, Crear, Actualizar Diseño'),
(9, 'Tester', 'Leer, Probar, Reportar Errores'),
(10, 'Cliente', 'Leer Reportes, Dar Retroalimentación');

