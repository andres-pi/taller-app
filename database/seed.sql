INSERT INTO clientes (
    nombre,
    apellido,
    telefono,
    email
)
VALUES
    (
        'Juan',
        'Pérez',
        '3885123456',
        'juan.perez@email.com'
    ),
    (
        'María',
        'Gómez',
        '3884987654',
        'maria.gomez@email.com'
    ),
    (
        'Carlos',
        'López',
        '3884765432',
        'carlos.lopez@email.com'
    ),
    (
        'Lucía',
        'Martínez',
        '3884556789',
        'lucia.martinez@email.com'
    );


INSERT INTO equipos (
    cliente_id,
    tipo,
    marca,
    modelo,
    numero_serie
)
VALUES
    (
        1,
        'Notebook',
        'Lenovo',
        'IdeaPad 3',
        'LEN-IDEA-001'
    ),
    (
        1,
        'Celular',
        'Samsung',
        'Galaxy A54',
        'SAM-A54-001'
    ),
    (
        2,
        'Notebook',
        'HP',
        'Pavilion 15',
        'HP-PAV-002'
    ),
    (
        3,
        'PC',
        'GigaByte',
        'PC Gamer',
        'GB-PC-003'
    ),
    (
        4,
        'Celular',
        'Motorola',
        'Moto G84',
        'MOT-G84-004'
    );


INSERT INTO ordenes_reparacion (
    equipo_id,
    problema_reportado,
    diagnostico,
    estado,
    fecha_ingreso,
    fecha_finalizacion,
    observaciones
)
VALUES
    (
        1,
        'La notebook no enciende.',
        'Problema en la fuente de alimentación.',
        'EN_REPARACION',
        CURRENT_TIMESTAMP - INTERVAL '3 days',
        NULL,
        'Se solicitó repuesto.'
    ),
    (
        2,
        'El celular se reinicia constantemente.',
        'Se detectó problema de software.',
        'REPARADA',
        CURRENT_TIMESTAMP - INTERVAL '5 days',
        CURRENT_TIMESTAMP - INTERVAL '2 days',
        'Sistema reinstalado y actualizado.'
    ),
    (
        3,
        'La notebook presenta lentitud.',
        NULL,
        'PENDIENTE',
        CURRENT_TIMESTAMP - INTERVAL '1 day',
        NULL,
        NULL
    ),
    (
        4,
        'La PC se apaga durante el uso.',
        'Temperatura elevada del procesador.',
        'DIAGNOSTICO',
        CURRENT_TIMESTAMP - INTERVAL '2 days',
        NULL,
        'Se está realizando prueba de temperatura.'
    ),
    (
        5,
        'La pantalla presenta líneas.',
        'Panel LCD defectuoso.',
        'ENTREGADA',
        CURRENT_TIMESTAMP - INTERVAL '10 days',
        CURRENT_TIMESTAMP - INTERVAL '5 days',
        'Se reemplazó el módulo de pantalla.'
    );


INSERT INTO actividades (
    orden_id,
    descripcion,
    fecha
)
VALUES
    (
        1,
        'Se realizó inspección inicial del equipo.',
        CURRENT_TIMESTAMP - INTERVAL '3 days'
    ),
    (
        1,
        'Se verificó la fuente de alimentación.',
        CURRENT_TIMESTAMP - INTERVAL '2 days'
    ),
    (
        1,
        'Se solicitó repuesto de fuente.',
        CURRENT_TIMESTAMP - INTERVAL '1 day'
    ),
    (
        2,
        'Se realizó diagnóstico de software.',
        CURRENT_TIMESTAMP - INTERVAL '5 days'
    ),
    (
        2,
        'Se reinstaló el sistema operativo.',
        CURRENT_TIMESTAMP - INTERVAL '4 days'
    ),
    (
        2,
        'Se realizaron pruebas de funcionamiento.',
        CURRENT_TIMESTAMP - INTERVAL '3 days'
    ),
    (
        4,
        'Se realizó prueba de temperatura.',
        CURRENT_TIMESTAMP - INTERVAL '2 days'
    ),
    (
        4,
        'Se verificó el sistema de refrigeración.',
        CURRENT_TIMESTAMP - INTERVAL '1 day'
    ),
    (
        5,
        'Se confirmó falla del panel LCD.',
        CURRENT_TIMESTAMP - INTERVAL '9 days'
    ),
    (
        5,
        'Se reemplazó el módulo de pantalla.',
        CURRENT_TIMESTAMP - INTERVAL '7 days'
    ),
    (
        5,
        'Se realizaron pruebas finales.',
        CURRENT_TIMESTAMP - INTERVAL '6 days'
    );