import csv

ARCHIVO_CSV = 'instituciones_registradas.csv'

def guardar_datos_csv(datos, archivo=ARCHIVO_CSV):
    """Guarda los datos en un archivo CSV."""
    campos = [
        "institucion", "region", "comuna", "administracion", "curso",
        "direccion", "telefono_establecimiento", "correo_establecimiento",
        "nombre_encargado", "telefono_encargado", "correo_encargado",
        "cantidad_personas"
    ]
    try:
        with open(archivo, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=campos)
            if file.tell() == 0:  # Escribir encabezados si el archivo está vacío
                writer.writeheader()
            writer.writerow(datos)
        print(f"✅ Datos guardados en {archivo}")
    except Exception as e:
        print(f"❌ Error al guardar los datos: {e}")


class FormularioInstitucion:
    def __init__(self):
        self.regiones = [
            "Arica y Parinacota", "Tarapacá", "Antofagasta", "Atacama",
            "Coquimbo", "Valparaíso", "Metropolitana", "LGBO", "Maule",
            "Ñuble", "Biobío", "Araucanía", "Los Ríos", "Los Lagos",
            "Aysén", "Magallanes"
        ]
        self.comunas = {
            "Arica y Parinacota": ["Arica", "Putre", "Camina"],
            "Tarapacá": ["Iquique", "Alto Hospicio", "Pozo Almonte"],
            "Antofagasta": ["Antofagasta", "Calama", "Tocopilla"],
            "Atacama": ["Copiapó", "Vallenar", "Caldera"],
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
        self.administraciones = [
            "Municipal", "Particular Subvencionado", "Particular",
            "SLEP", "Estatal", "Educación superior", "Institución no educativa"
        ]
        self.datos = {}  # Aquí guardaremos los datos del formulario

    def seleccionar_opcion(self, mensaje, opciones):
        """Muestra opciones y devuelve la selección del usuario."""
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

    def rellenar_formulario(self):
        """Solicita y guarda los datos de la institución"""
        print("\n=== Formulario de Registro de Institución ===")

        self.datos["institucion"] = input("Nombre de la institución: ")
        self.datos["region"] = self.seleccionar_opcion("Selecciona una región:", self.regiones)
        self.datos["comuna"] = self.seleccionar_opcion("Selecciona una comuna:", self.comunas[self.datos["region"]])
        self.datos["administracion"] = self.seleccionar_opcion("Tipo de administración:", self.administraciones)
        self.datos["curso"] = input("Curso participante: ")
        self.datos["direccion"] = input("Dirección del establecimiento: ")
        self.datos["telefono_establecimiento"] = input("Número telefónico del establecimiento: ")
        self.datos["correo_establecimiento"] = input("Correo del establecimiento: ")
        self.datos["nombre_encargado"] = input("Nombre de la persona a cargo: ")
        self.datos["telefono_encargado"] = input("Número de la persona a cargo: ")
        self.datos["correo_encargado"] = input("Correo de la persona a cargo: ")
        self.datos["cantidad_personas"] = input("Cantidad de personas que participarán: ")

    def mostrar_resumen(self):
        """Muestra los datos ingresados y pide confirmación."""
        print("\n--- Datos registrados ---")
        for clave, valor in self.datos.items():
            print(f"{clave.replace('_', ' ').capitalize()}: {valor}")

        confirmar = input("\n¿Confirmar envío? (sí/no): ").strip().lower()
        if confirmar == "sí":
            guardar_datos_csv(self.datos)  # 👈 aquí se guarda en el CSV
            print("✅ Formulario enviado con éxito.")
        else:
            print("❌ Envío cancelado.")


# --- Uso del programa ---
if __name__ == "__main__":
    formulario = FormularioInstitucion()
    formulario.rellenar_formulario()
    formulario.mostrar_resumen()
