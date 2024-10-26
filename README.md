# FeelAI - Detección de Emociones con NLP

**FeelAI** es una aplicación que utiliza inteligencia artificial y procesamiento de lenguaje natural (NLP) para detectar las emociones presentes en un texto ingresado. Esta herramienta identifica sentimientos como alegría, tristeza, enojo, miedo y disgusto, proporcionando un desglose emocional útil para aplicaciones en atención al cliente, análisis de redes sociales y más.

## Tecnologías Utilizadas

### Backend
- **Python**: Lenguaje principal para la lógica del servidor.
- **Flask**: Framework ligero para construir la API y servir la aplicación web.
- **Hugging Face API**: Para la detección precisa de emociones utilizando modelos avanzados de NLP.

### Frontend
- **HTML5**: Estructura del contenido de la aplicación web.
- **CSS3** (Neumorphism): Estilo visual moderno con diseño minimalista y sombreado suave.
- **Bootstrap 4**: Para garantizar responsividad y estilo básico.
- **JavaScript**: Manejo de eventos y solicitudes asíncronas.

### Comunicación Cliente-Servidor
- **AJAX (XMLHttpRequest)**: Envío y recepción de datos entre frontend y backend sin recargar la página.

### Entorno y Librerías
- **Requests**: Realiza solicitudes HTTP hacia la API de Hugging Face.
- **Jinja2**: Motor de plantillas de Flask para renderizar las páginas HTML dinámicamente.
