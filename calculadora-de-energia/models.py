class Aparelho:

    def __init__(self, nome: str, potencia_watts: float, horas_diarias: float, dias_no_mes: int):
        self.nome = nome
        self.potencia_watts = potencia_watts
        self.horas_diarias = horas_diarias
        self.dias_no_mes = dias_no_mes

    def calcular_consumo_mensal (self) -> float:
        return (self.potencia_watts * self.horas_diarias * self.dias_no_mes) / 1000

    def calcular_custo_mensal (self, tarifa: float = 0.85) -> float:
        return self.calcular_consumo_mensal() * tarifa

    def obter_classificacao(self) -> str:
        consumo_kWh = self.calcular_consumo_mensal ()
        if consumo_kWh < 30:
            return "Baixo Consumo."
        if consumo_kWh <= 100:
            return "Médio Consumo."
        return "Alto Consumo - Atenção"