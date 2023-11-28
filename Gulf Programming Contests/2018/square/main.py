def get_combinations(sequance,requests):
    combinations=[]
    for request in requests:
            


def calculate(sequance,requests):
    if len(sequance)==0:
        return True

    
    combinations = get_combinations(sequance,requests)


sequance = ['1', '0', '9', '1', '2', '1', '1', '0', '3', '7', '4']
requests=["01","109","91","13","201"]
print(calculate(sequance))