def get_yes_no(question):
    while True:
        answer=input(question + "yes/no: ").strip().lower()
        if answer in ['yes','no']:
            return answer=='yes'
        print("Please answer with yes or no.")
        
        
        
def diagnose():
    print("Medical Expert System ")
    print("-------------------------")
    
    fever = get_yes_no("Do you have a fever?")
    cough = get_yes_no("Do you have a cough?")
    sore_throat = get_yes_no("Do you have a sore throat?")
    runny_nose = get_yes_no("Do you have a runny nose?")
    body_ache = get_yes_no("Do you have body aches?")
    fatigue = get_yes_no("Are you feeling fatigued?")
    short_breath = get_yes_no("Are you experiencing shortness of breath?")
    loss_smell = get_yes_no("Have you lost your sense of taste or smell?")
    sneezing = get_yes_no("Are you sneezing frequently?")
    itchy_eyes = get_yes_no("Do you have itchy or watery eyes?")
    
    if fever and cough and sore_throat and body_ache and fatigue:
        if short_breath or loss_smell:
            print("\n Diagnosis: You may have COVID-19.")
        else:
            print("\n Diagnosis: You may have the Flu.")
    elif  cough and sore_throat and runny_nose:
        print("\n Diagnosis: You may have the Common Cold.")
    elif  sneezing and itchy_eyes and runny_nose and not fever:
        print("\n Diagnosis: You may have Allergy.")
        
    else:
        print("\n Diagnosis: Symptoms do not match a known condition.")
        print("Please consult a healthcare professional.")

# Run the system
diagnose()

    

