def seleccionar_opcion(mensaje, opciones):
    print(mensaje)
    for i, opcion in enumerate(opciones, 1):
        print(f"{i}. {opcion}")
    while True:
        try:
            seleccion = int(input("Selecciona una opción (número): "))
            if 1 <= seleccion <= len(opciones):
                return opciones[seleccion - 1]
            else:
                print("Opción fuera de rango. Intenta nuevamente.")
        except ValueError:
            print("Entrada inválida. Por favor ingresa un número.")

def formulario_institucion():
    print("=== Formulario de Registro de Institución ===")

    regiones = ["Arica y Parinacota", "Tarapacá", "Antofagasta", "Atacama" "Coquimbo", "Valparaíso", "Metropolitana", "LGBO", "Maule", "Ñuble", "Biobío", "Araucanía", "Los Ríos", "Los Lagos", "Aysén", "Magallanes"]
    comunas = {
        "Arica y Parinacota": ["Arica", "Putre", "Camina"],
        "Tarapacá": ["Iquique", "Alto Hospicio", "Pozo Almonte"],
        "Antofagasta": ["Antofagasta", "Calama", "Tocopilla"],
        "Atacama": ["Copiapó", "Vallenar", "Caldera "],
        "Coquimbo": ["La Serena", "Coquimbo", "Ovalle"],        
        "Metropolitana": ["Santiago", "Puente Alto", "Maipú"],
        "Valparaíso": ["Valparaíso", "Viña del Mar", "Quilpué"],
        "LGBO": ["Rancagua", "San Fernando", "Pichilemu"],
        "Maule": ["Talca", "Curicó", "Linares"],        
        "Ñuble": ["Chillán", "San Carlos", "Quirihue"],
        "Araucanía": ["Temuco", "Padre Las Casas", "Villarrica"],
        "Los Ríos": ["Valdivia", "La Unión", "Lanco"],     
        "Los Lagos": ["Puerto Montt", "Osorno", "Castro"],
        "Aysén": ["Coyhaique", "Puerto Aysén", "Chile Chico"],
        "Magallanes": ["Punta Arenas", "Puerto Natales", "Porvenir"],
        "Biobío": ["Concepción", "Talcahuano", "Chiguayante"]
    }
    administraciones = ["Municipal", "Particular Subvencionado", "Particular", "SLEP", "Estatal", "Educación superior", "Institución no educativa"]

    institucion = input("Nombre de la institución: ")
    region = seleccionar_opcion("Selecciona una región:", regiones)
    comuna = seleccionar_opcion("Selecciona una comuna:", comunas[region])
    administracion = seleccionar_opcion("Tipo de administración:", administraciones)
    curso = input("Curso participante: ")
    direccion = input("Dirección del establecimiento: ")
    telefono = input("Número telefónico del establecimiento: ")
    correo = input("Correo del establecimiento: ")
    nombre_encargado = input("Nombre de la persona a cargo: ")
    telefono_encargado = input("Número de la persona a cargo: ")
    correo_encargado = input("Correo de la persona a cargo: ")
    cantidad_personas = input("Cantidad de personas que participarán: ")

    datos = {
        "institucion": institucion,
        "region": region,
        "comuna": comuna,
        "administracion": administracion,
        "curso": curso,
        "direccion": direccion,
        "telefono_establecimiento": telefono,
        "correo_establecimiento": correo,
        "nombre_encargado": nombre_encargado,
        "telefono_encargado": telefono_encargado,
        "correo_encargado": correo_encargado,
        "cantidad_personas": cantidad_personas
    }

    print("\n--- Datos registrados ---")
    for clave, valor in datos.items():
        print(f"{clave.replace('_', ' ').capitalize()}: {valor}")

    confirmar = input("\n¿Confirmar envío? (sí/no): ").strip().lower()
    if confirmar == "sí":
        print("Formulario enviado con éxito.")
    else:
        print("Envío cancelado.")

formulario_institucion()
