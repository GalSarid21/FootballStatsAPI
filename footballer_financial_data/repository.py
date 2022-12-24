from .models import FootballerFinancialData
from datetime import datetime

class DbAccessFunctions():

    def get_all_footballers():
        footballer = FootballerFinancialData.objects.all()       
        return footballer

    def get_footballers_by_net_worth(net_worth, include_greaters):
        if include_greaters:
            footballers = FootballerFinancialData.objects.filter(net_worth__gte=net_worth)       
        else:
            footballers = FootballerFinancialData.objects.filter(net_worth=net_worth)
        return footballers

    def get_footballer_by_id(id):
        footballer = FootballerFinancialData.objects.get(id=id)       
        return footballer

    def get_footballer_by_full_name(full_name):
        footballer = FootballerFinancialData.objects.filter(full_name=full_name).first()       
        return footballer

    def add_footballers(footballers):
        footballers_to_add = [FootballerFinancialData(
                                    full_name = footballer['full_name'], 
                                    net_worth = footballer['net_worth'],
                                    currency = footballer['currency'],
                                    nationality = footballer['nationality'],
                                    other_professions = footballer['other_professions']
                                ) for footballer in footballers]
        new_footballers = FootballerFinancialData.objects.bulk_create(footballers_to_add)
        return new_footballers

    def update_footballer(new_footballer, id, is_input_patial):
        footballer = FootballerFinancialData.objects.get(id=id)
        footballer.net_worth = new_footballer['net_worth']
        footballer.currency = new_footballer['currency']
        footballer.other_professions = new_footballer['other_professions']
        footballer.last_update = datetime.utcnow()
        if is_input_patial:
            footballer.save()
        else:
            footballer.full_name = new_footballer['full_name']
            footballer.nationality = new_footballer['nationality']
            footballer.save()
        return footballer

    def delete_footballer(id):
        footabller = FootballerFinancialData.objects.get(id=id)
        footabller.delete()

        
    