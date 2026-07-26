# Sistema de Administración de Empleados (SAE)

> **Versión:** 1.0  
> **Estado:** En planificación

---

# Documento de Inicio del Proyecto (Project Charter)

## 1. Introducción

El **Sistema de Administración de Empleados (SAE)** es un proyecto educativo diseñado para aprender el desarrollo de software utilizando **Python** como lenguaje principal. Su objetivo es recorrer todo el ciclo de vida de una aplicación, desde una aplicación de consola hasta una plataforma web desplegada en un servidor.

Durante el desarrollo se abordarán conceptos de programación básica, programación orientada a objetos, bases de datos, APIs REST, automatización, pruebas, desarrollo web, seguridad y despliegue.

Este proyecto simulará un entorno de desarrollo profesional, aplicando buenas prácticas, metodologías de trabajo y control de versiones.

---

# 2. Objetivos

## Objetivo General

Desarrollar un sistema integral para la administración de empleados de una empresa mientras se adquieren conocimientos progresivos sobre el ecosistema de desarrollo con Python.

## Objetivos Específicos

- Aprender los fundamentos de Python.
- Aplicar Programación Orientada a Objetos.
- Comprender el funcionamiento de las bases de datos.
- Diseñar una API REST.
- Desarrollar una interfaz web.
- Implementar autenticación y autorización.
- Automatizar procesos empresariales.
- Aplicar pruebas unitarias e integración.
- Desplegar la aplicación utilizando Docker.

---

# 3. Alcance

El sistema permitirá administrar la información de los empleados de una empresa mediante diferentes módulos.

### Funcionalidades principales

- Gestión de empleados.
- Gestión de departamentos.
- Gestión de cargos.
- Control de asistencia.
- Gestión de vacaciones.
- Gestión de permisos.
- Gestión de nómina (versión simplificada).
- Reportes.
- Panel administrativo.
- Autenticación de usuarios.
- Automatización de tareas.

---

# 4. Objetivos de Aprendizaje

## Programación

- Variables
- Tipos de datos
- Operadores
- Condicionales
- Ciclos
- Funciones
- Módulos
- Manejo de excepciones
- Lectura y escritura de archivos
- Decoradores
- Tipado
- Programación Orientada a Objetos

---

## Bases de Datos

- SQLite
- PostgreSQL
- SQL
- Relaciones
- Normalización
- Índices
- Transacciones
- ORM

---

## Backend

- FastAPI
- APIs REST
- JSON
- HTTP
- Swagger/OpenAPI
- JWT
- OAuth2
- Validaciones
- Middlewares

---

## Frontend

- HTML
- CSS
- JavaScript
- React (fase avanzada)
- Consumo de APIs

---

## Automatización

- Generación de reportes
- Exportación a Excel
- Exportación a PDF
- Envío automático de correos
- Programación de tareas

---

## DevOps

- Git
- GitHub
- Docker
- Docker Compose
- CI/CD
- Linux
- VPS
- Nginx

---

# 5. Tecnologías Previstas

| Área                  | Tecnología                  |
| --------------------- | --------------------------- |
| Lenguaje              | Python                      |
| Base de datos inicial | SQLite                      |
| Base de datos final   | PostgreSQL                  |
| ORM                   | SQLAlchemy                  |
| API                   | FastAPI                     |
| Frontend              | HTML, CSS y JavaScript      |
| Framework Frontend    | React (fase avanzada)       |
| Autenticación         | JWT                         |
| Testing               | Pytest                      |
| Automatización        | APScheduler                 |
| Reportes              | Pandas, OpenPyXL, ReportLab |
| Contenedores          | Docker                      |
| Control de versiones  | Git                         |
| Despliegue            | VPS Linux                   |

---

# 6. Roles del Sistema

## Administrador

Tiene acceso completo al sistema.

### Permisos

- Crear empleados.
- Eliminar empleados.
- Modificar información.
- Administrar usuarios.
- Generar reportes.
- Configurar el sistema.

---

## Recursos Humanos

Gestiona la información laboral.

### Permisos

- Registrar empleados.
- Gestionar vacaciones.
- Gestionar permisos.
- Registrar asistencia.
- Consultar reportes.

---

## Jefe de Departamento

Puede administrar únicamente los empleados pertenecientes a su departamento.

---

## Empleado

Tiene acceso únicamente a su información.

### Puede

- Consultar su perfil.
- Ver vacaciones.
- Ver permisos.
- Consultar asistencia.
- Descargar certificados.

---

# 7. Módulos del Sistema

## Autenticación

- Inicio de sesión.
- Cierre de sesión.
- Recuperación de contraseña.
- Gestión de roles.

---

## Gestión de Empleados

- Crear empleado.
- Editar empleado.
- Eliminar empleado.
- Buscar empleado.
- Listar empleados.

---

## Departamentos

- Crear departamento.
- Editar departamento.
- Eliminar departamento.

---

## Cargos

- Crear cargo.
- Asignar cargo.
- Historial laboral.

---

## Asistencia

- Registrar entrada.
- Registrar salida.
- Consultar historial.
- Generar reportes.

---

## Vacaciones

- Solicitar vacaciones.
- Aprobar solicitudes.
- Rechazar solicitudes.
- Consultar historial.

---

## Permisos

- Crear solicitud.
- Aprobar.
- Rechazar.
- Historial.

---

## Reportes

- Reportes PDF.
- Reportes Excel.
- Estadísticas.

---

## Administración

- Gestión de usuarios.
- Configuración.
- Auditoría (logs).

---

# 8. Metodología

El proyecto será desarrollado de forma incremental.

Cada fase agregará nuevos conocimientos sin reemplazar completamente la arquitectura existente.

Cada etapa incluirá:

- Objetivos de aprendizaje.
- Nuevos conceptos.
- Refactorización.
- Pruebas.
- Documentación.

---

# 9. Principios del Proyecto

- Código limpio.
- Simplicidad.
- Documentación constante.
- Commits pequeños y descriptivos.
- Refactorización continua.
- Separación de responsabilidades.
- Aprendizaje práctico.
- Buenas prácticas de ingeniería de software.

---

# 10. Arquitectura Evolutiva

```text
Aplicación por consola
        │
        ▼
Programación Orientada a Objetos
        │
        ▼
Persistencia con archivos
        │
        ▼
SQLite
        │
        ▼
PostgreSQL
        │
        ▼
FastAPI
        │
        ▼
Frontend Web
        │
        ▼
Docker
        │
        ▼
Despliegue en VPS
        │
        ▼
Automatización
        │
        ▼
CI/CD
```

---

# 11. Reglas del Proyecto

- No utilizar librerías que oculten el funcionamiento interno de los conceptos antes de comprenderlos.
- Cada nueva característica deberá documentarse.
- Todo cambio importante deberá registrarse mediante Git.
- Se priorizará la comprensión del código sobre la velocidad de desarrollo.
- Cada módulo deberá incluir pruebas antes de considerarse finalizado.

---

# 12. Resultado Esperado

Al finalizar el proyecto se dispondrá de un sistema funcional de administración de empleados que simule un producto real y sirva como base para futuros desarrollos empresariales.

El proyecto permitirá adquirir experiencia práctica en:

- Desarrollo Backend.
- Desarrollo Frontend.
- Bases de datos.
- Automatización.
- Testing.
- DevOps.
- Control de versiones.
- Despliegue de aplicaciones.

---

# Próximos Documentos

Después de este documento se desarrollarán los siguientes:

1. Roadmap del proyecto.
2. Arquitectura del sistema.
3. Modelo Entidad-Relación (ERD).
4. Historias de Usuario.
5. Casos de Uso.
6. Estructura de carpetas.
7. Guía de Git y flujo de trabajo.
8. Estándares de código (PEP 8).
9. Convenciones de nombres.
10. Plan de pruebas.
11. Manual de despliegue.
12. Documentación de la API.
