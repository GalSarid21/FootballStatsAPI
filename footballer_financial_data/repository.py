from .models import FootballerFinancialData

class DbAccessFunctions():

    def get_all_footballers():
        footballer = FootballerFinancialData.objects.all()       
        return footballer

    def get_footballer_by_id(id):
        footballer = FootballerFinancialData.objects.get(id=id)       
        return footballer

    def get_footballer_by_full_name(full_name):
        footballer = FootballerFinancialData.objects.filter(full_name=full_name).first()       
        return footballer

    def add_footballer(footballer):
        footballer = FootballerFinancialData.objects.create(
            full_name = footballer['full_name'],
            net_woth = footballer['net_woth'],
            currency = footballer['currency'],
            nationality = footballer['nationality'],
            other_professions = footballer['other_professions'])
        return footballer
    