class Trainee:
    """Representa a un estudiante en prácticas.

    Attributes:
        nombre (str): Nombre completo del trainee.
        area_interes (str): Especialidad o área de interés.
        horas_acumuladas (int): Total de horas registradas.
    """

    def __init__(self, nombre: str, area_interes: str, horas_acumuladas: int = 0):
        """Inicializa un nuevo trainee.

        Args:
            nombre (str): Nombre del trainee.
            area_interes (str): Área de interés del trainee (ej. Backend, Data, Ciberseguridad).
            horas_acumuladas (int, optional): Horas de formación acumuladas. Por defecto 0.
        """
        self.nombre = nombre
        self.area_interes = area_interes
        self.horas_acumuladas = horas_acumuladas

    def resumen(self) -> str:
        """Devuelve un resumen con la información del trainee.

        Returns:
            str: Resumen con nombre, área de interés y horas acumuladas.
        """
        return (
            f"Trainee: {self.nombre}\n"
            f"Área de interés: {self.area_interes}\n"
            f"Horas acumuladas: {self.horas_acumuladas}"
        )


if __name__ == "__main__":
    trainee = Trainee("Tu Nombre", "Backend con Python")
    print(trainee.resumen())