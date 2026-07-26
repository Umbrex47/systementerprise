"""
Modelos base del Sistema de Administración de Empleados (SAE).

¿Qué es una clase?
------------------
Una clase es un molde o plantilla que describe cómo se crea un objeto.
Define qué datos (atributos) guarda y qué acciones (métodos) puede hacer.

¿Para qué sirven en este proyecto?
----------------------------------
Representan las entidades reales del negocio: personas que usan el sistema
(usuarios), quienes lo administran y quienes trabajan en la empresa.

¿Cómo aportan?
--------------
- Separan responsabilidades: cada clase modela un rol distinto.
- Permiten reutilizar código con herencia (Administrador y Empleado parten de Usuario).
- Facilitan crecer el sistema sin reescribir la lógica común (login, datos básicos).
- Preparan el camino hacia persistencia, APIs y permisos más adelante.
"""


class User:
    """
    Usuario del sistema.

    Es la clase base: cualquier persona que inicia sesión en el SAE.
    Guarda la identidad de acceso (correo, nombre, contraseña) y sirve
    como punto común para roles más específicos.
    """

    def __init__(self, email: str, name: str, password: str, age: int | None = None) -> None:
        self.email = email
        self.name = name
        self.password = password
        self.age = age

    def authenticate(self, password: str) -> bool:
        """Comprueba si la contraseña ingresada coincide con la del usuario."""
        return self.password == password

    def __str__(self) -> str:
        return f"User(name={self.name!r}, email={self.email!r})"


class Administrator(User):
    """
    Administrador del sistema.

    Hereda de User: ya es un usuario con acceso, pero con permisos totales
    (crear/eliminar empleados, gestionar usuarios, reportes, configuración).

    Aporta la capa de control: diferencia a quien opera el sistema de quien
    solo consulta su propia información.
    """

    def __init__(
        self,
        email: str,
        name: str,
        password: str,
        age: int | None = None,
        admin_level: str = "full",
    ) -> None:
        super().__init__(email, name, password, age)
        self.admin_level = admin_level

    def can_manage_users(self) -> bool:
        """Indica si este administrador puede gestionar otros usuarios."""
        return True

    def can_generate_reports(self) -> bool:
        """Indica si este administrador puede generar reportes."""
        return True

    def __str__(self) -> str:
        return f"Administrator(name={self.name!r}, level={self.admin_level!r})"


class Employee(User):
    """
    Empleado de la empresa.

    Hereda de User porque también puede iniciar sesión, pero además guarda
    datos laborales (cargo, departamento, código de empleado).

    Aporta el núcleo del negocio del SAE: es la entidad que se administra
    (perfil, asistencia, vacaciones, permisos). Su acceso queda limitado
    a su propia información.
    """

    def __init__(
        self,
        email: str,
        name: str,
        password: str,
        employee_id: str,
        department: str,
        position: str,
        age: int | None = None,
    ) -> None:
        super().__init__(email, name, password, age)
        self.employee_id = employee_id
        self.department = department
        self.position = position

    def get_profile_summary(self) -> str:
        """Devuelve un resumen legible del perfil laboral del empleado."""
        return (
            f"{self.name} ({self.employee_id}) - "
            f"{self.position} en {self.department}"
        )

    def __str__(self) -> str:
        return (
            f"Employee(id={self.employee_id!r}, name={self.name!r}, "
            f"department={self.department!r})"
        )
