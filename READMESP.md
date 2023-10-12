# Chatbot Ziomara para ZIONE Shop

## Descripción General

¡Bienvenido al repositorio del chatbot Ziomara para ZIONE Shop! Esta aplicación web basada en Streamlit sirve como interfaz de chatbot diseñada para asistir a los usuarios con diversas consultas relacionadas con la plataforma de venta en línea de ZIONE Shop. Alimentado por un modelo de lenguaje LLaMa 2 70B afinado y aprovechando la API de Replicate para la inferencia del modelo, Ziomara ofrece respuestas personalizadas basadas en diferentes tonos o personalidades que los usuarios pueden seleccionar desde la barra lateral.

## Tabla de Contenidos

- [Importaciones](#importaciones)
- [Configuración de Streamlit](#configuración-de-streamlit)
- [Barra Lateral](#barra-lateral)
- [Estado de la Sesión](#estado-de-la-sesión)
- [Manejo de Mensajes](#manejo-de-mensajes)
- [Indicaciones del Sistema Predefinidas](#indicaciones-del-sistema-predefinidas)
- [Lógica del Chatbot](#lógica-del-chatbot)

## Importaciones

- `streamlit` para la interfaz de la aplicación web
- `replicate` para la inferencia del modelo
- `os` para el manejo de variables de entorno

## Configuración de Streamlit

- El título de la página y los estilos CSS personalizados se configuran para proporcionar una interfaz fácil de usar.

## Barra Lateral

- La barra lateral contiene una imagen, un título y un menú desplegable para seleccionar la personalidad del chatbot.
- También obtiene el token de la API de Replicate de `st.secrets` y lo establece como una variable de entorno.

## Estado de la Sesión

- La aplicación utiliza el estado de la sesión de Streamlit para mantener un historial de conversación.

## Manejo de Mensajes

- Los mensajes se muestran en una interfaz de chat donde el usuario puede interactuar con el chatbot. También se puede borrar el historial del chat.

## Indicaciones del Sistema Predefinidas

- El código incluye indicaciones del sistema predefinidas diseñadas para generar respuestas en diferentes tonos (profesional, entusiasta, comercial).

## Lógica del Chatbot

- La función `generate_ziomara_response()` interactúa con el modelo de lenguaje LLaMa 2 70B a través de la API de Replicate. Toma la entrada del usuario y genera una respuesta basada en la personalidad seleccionada.

## Conclusión

En general, la aplicación está bien estructurada y sirve como una solución integral de servicio al cliente. Se han aplicado técnicas avanzadas de afinado y diseño de indicaciones para hacer que Ziomara sea más precisa y receptiva.

---

## Información del Autor

Desarrollado por Juan Jaramillo | Prompt Engineer y Experto en IA y Machine Learning especializado en IA generativa y Fine-Tuning PEFT y RLHF.

- 🌐 Sitio web: [juanjaramillo.tech](https://juanjaramillo.tech/)
- 📧 Correo electrónico: [info@juanjaramillo.tech](mailto:info@juanjaramillo.tech)
- 💼 LinkedIn: [Juan Jaramillo](https://www.linkedin.com/in/juan-jaramillo/)
