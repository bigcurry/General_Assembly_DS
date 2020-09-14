class HealthPlan:
    def __init__(
        self, name, deductible, coinsurance_rate, out_of_pocket_max, monthly_premium
    ):
        self.name = name
        self.deductible = deductible
        self.coinsurance_rate = coinsurance_rate
        self.out_of_pocket_max = out_of_pocket_max
        self.monthly_premium = monthly_premium

    def calculate_costs(self, expenses):
        return (
            self.calculate_total_premium()
            + self.calculate_deductible_paid(expenses)
            + self.calculate_coinsurance_paid(expenses)
        )

    def calculate_total_premium(self):
        return self.monthly_premium * 12

    def calculate_deductible_paid(self, expenses):
        return min(self.deductible, expenses)

    def calculate_coinsurance_paid(self, expenses):
        if expenses < self.deductible:
            return 0
        else:
            return min(
                (expenses - self.deductible) * self.coinsurance_rate,
                self.out_of_pocket_max - self.deductible,
            )
