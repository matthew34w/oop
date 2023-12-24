class RentalProperty:
    def __init__(self, purchase_price, monthly_rent, operating_expenses, property_value_increase, holding_period):
        self.purchase_price = purchase_price
        self.monthly_rent = monthly_rent
        self.operating_expenses = operating_expenses
        self.property_value_increase = property_value_increase
        self.holding_period = holding_period

    def calculate_roi(self):
        total_rental_income = self.monthly_rent * 12 * self.holding_period
        total_operating_expenses = self.operating_expenses * self.holding_period
        total_property_value_increase = self.purchase_price * (1 + self.property_value_increase) ** self.holding_period
        total_cash_flow = total_rental_income - total_operating_expenses

        initial_investment = self.purchase_price
        total_return = total_cash_flow + (total_property_value_increase - initial_investment)

        roi = (total_return / initial_investment) * 100

        return roi



    
property1 = RentalProperty(
    purchase_price=200000,
    monthly_rent=1500,
    operating_expenses=6000,
    property_value_increase=0.03,  
    holding_period=5
)

   
roi_result = property1.calculate_roi()

  
print(f"Your ROI is : {roi_result:.2f}%")