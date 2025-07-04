const comunasPorRegion = {
  "Arica y Parinacota": ["Arica", "Camarones", "Putre", "General Lagos"],
  "Tarapacá": ["Iquique", "Alto Hospicio", "Pozo Almonte"],
  "Antofagasta": ["Antofagasta", "Calama", "Tocopilla"],
  "Atacama": ["Copiapó", "Caldera", "Vallenar"],
  "Coquimbo": ["La Serena", "Coquimbo", "Ovalle"],
  "Valparaíso": ["Valparaíso", "Viña del Mar", "Quilpué", "San Antonio"],
  "Metropolitana": ["Santiago", "Puente Alto", "Maipú", "La Florida"],
  "O'Higgins": ["Rancagua", "San Fernando", "Santa Cruz"],
  "Maule": ["Talca", "Curicó", "Linares"],
  "Ñuble": ["Chillán", "San Carlos", "Bulnes"],
  "Biobío": ["Concepción", "Los Ángeles", "Coronel"],
  "La Araucanía": ["Temuco", "Angol", "Villarrica"],
  "Los Ríos": ["Valdivia", "La Unión", "Panguipulli"],
  "Los Lagos": ["Puerto Montt", "Osorno", "Castro"],
  "Aysén": ["Coyhaique", "Puerto Aysén"],
  "Magallanes": ["Punta Arenas", "Puerto Natales"]
};

$(document).ready(function () {
  $('#region').change(function () {
    const regionSeleccionada = $(this).val();
    const comunas = comunasPorRegion[regionSeleccionada] || [];

    const $comunaSelect = $('#comuna');
    $comunaSelect.empty();
    $comunaSelect.append('<option value="">Seleccione una comuna</option>');

    comunas.forEach(function (comuna) {
      $comunaSelect.append(`<option value="${comuna}">${comuna}</option>`);
    });
  });
});

