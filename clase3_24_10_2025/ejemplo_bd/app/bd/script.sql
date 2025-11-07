CREATE TABLE vehiculo (
  patente varchar(6) PRIMARY KEY,
  marca varchar(30) NOT NULL,
  modelo varchar(30) NOT NULL,
  tiene_patita tinyint(1) NOT NULL,
  cant_puertas int(11) NOT NULL,
  tipo_vehiculo varchar(20) NOT NULL
);
