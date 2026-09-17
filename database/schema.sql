CREATE TABLE clientes (
    id BIGSERIAL PRIMARY KEY,

    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    telefono VARCHAR(30) NOT NULL,
    email VARCHAR(255),

    fecha_creacion TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    fecha_actualizacion TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE equipos (
    id BIGSERIAL PRIMARY KEY,

    cliente_id BIGINT NOT NULL,

    tipo VARCHAR(50) NOT NULL,
    marca VARCHAR(100) NOT NULL,
    modelo VARCHAR(100) NOT NULL,
    numero_serie VARCHAR(100),

    fecha_creacion TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    fecha_actualizacion TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_equipo_cliente
        FOREIGN KEY (cliente_id)
        REFERENCES clientes(id)
        ON DELETE RESTRICT
);


CREATE TABLE ordenes_reparacion (
    id BIGSERIAL PRIMARY KEY,

    equipo_id BIGINT NOT NULL,

    problema_reportado TEXT NOT NULL,
    diagnostico TEXT,

    estado VARCHAR(30) NOT NULL DEFAULT 'PENDIENTE',

    fecha_ingreso TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    fecha_finalizacion TIMESTAMP,

    observaciones TEXT,

    fecha_creacion TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    fecha_actualizacion TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_orden_equipo
        FOREIGN KEY (equipo_id)
        REFERENCES equipos(id)
        ON DELETE RESTRICT,

    CONSTRAINT chk_orden_estado
        CHECK (
            estado IN (
                'PENDIENTE',
                'DIAGNOSTICO',
                'EN_REPARACION',
                'REPARADA',
                'ENTREGADA',
                'CANCELADA'
            )
        ),

    CONSTRAINT chk_fecha_finalizacion
        CHECK (
            fecha_finalizacion IS NULL
            OR fecha_finalizacion >= fecha_ingreso
        )
);


CREATE TABLE actividades (
    id BIGSERIAL PRIMARY KEY,

    orden_id BIGINT NOT NULL,

    descripcion TEXT NOT NULL,
    fecha TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_actividad_orden
        FOREIGN KEY (orden_id)
        REFERENCES ordenes_reparacion(id)
        ON DELETE RESTRICT
);


CREATE INDEX idx_equipos_cliente_id
    ON equipos(cliente_id);

CREATE INDEX idx_equipos_numero_serie
    ON equipos(numero_serie);

CREATE INDEX idx_ordenes_equipo_id
    ON ordenes_reparacion(equipo_id);

CREATE INDEX idx_ordenes_estado
    ON ordenes_reparacion(estado);

CREATE INDEX idx_ordenes_fecha_ingreso
    ON ordenes_reparacion(fecha_ingreso);

CREATE INDEX idx_actividades_orden_id
    ON actividades(orden_id);

CREATE INDEX idx_actividades_fecha
    ON actividades(fecha);