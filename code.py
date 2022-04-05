#task 1:
def menu():
    print("which category would you like to choose?")
    print("1:set the generation 0 values")
    print("2:display the generation 0 values")
    print("3:run the model")
    print("4:export data")
    print("5:quit")
    choice=int(input("enter the number of choice here"))
    if choice==1:
     set_generation_0_values()
    elif choice==2:
     display_the_generation_0_values()
    elif choice==3:
     run_the_model()
    elif choice==4:
     export_data()
    elif choice==5:
     quit()
    else: 
        print("the number you have entered is invalid please enter an options number from below")
    menu()
   
#task 2:
def set_generation_0_values():
      global J
      J=float(input("enter the number of jeveniles"))
      global Jsr
      Jsr=float(input("enter the number of jeveniles servival rate"))
      global A
      A=float(input("enter the number of adults"))
      global Asr
      Asr=float(input("enter the number of adults servival rate"))
      global S
      S=float(input("enter the number of seniles"))
      global Ssr
      Ssr=float(input("enter the number of seniles servival rate"))
      global Sbr
      Sbr=float(input("enter the number of seniles birth rate"))
      global G1
      
      G1=float(input("enter the number of new generations"))

      menu()

#task 3:
def display_the_generation_0_values():
   print("poplulation numbers:")
   print("juveniles",J)
   print("adults",A)
   print("seniles",S)
   print("servival rates")
   print("juveniles",Jsr)
   print("adults",Asr)
   print("seniles",Ssr)
   print("birth rates")
   print("seniles",Sbr)
   print("new generation number",G1)
   menu()

#task 4:
def run_the_model():
    global J
    global A
    global S
    global J
    global Jsr
    global A
    global Asr
    global S
    global Ssr
    global Sbr
    global G
    global G1
    print("RESULTS")
    G=0
    print(G,"generations",J,"juveniles",A,"adults",S,"seniles",J+A+S,"total")
    
      
       
    while G<G1:

           next_J=A*Sbr
           next_A=J*Jsr
           next_S=(A*Asr)+(S+Ssr)
           J=next_J
           A=next_A
           S=next_S
           G=G+1
           print(G,"generations",J,"juveniles",A,"adults",S,"seniles",J+A+S,"total")
    menu()
#task 5
def save_data():
    global J
    global Jsr
    global A
    global Asr
    global S
    global Ssr
    global Sbr
    global G
    global file_name
    global choose 
    global G1
    file_name1= open(file_name,"a")
    G=0
    total=J+A+S

    show="""generations, juveniles, adults, seniles,total \n
{generation}, {juveniles}, {adults}, {seniles}, {total} \n"""

    content = {
        "generation":G,
        "juveniles":J,
        "adults":A,
        "seniles":S,
        "total":total
        }
    with open(file_name,"a")as fileA:
        fileA.write(show.format(**content))


    while G<G1:

           next_J=A*Sbr
           next_A=J*Jsr
           next_S=(A*Asr)+(S*Ssr)
           J=next_J
           A=next_A
           S=next_S
           G=G+1 

    show="""{generation}, {juveniles}, {adults}, {seniles}, {total} \n"""

    content = {
        "generation":G,
        "juveniles":J,
        "adults":A,
        "seniles":S,
        "total":total
        }
    with open(file_name,"a")as fileA:
        fileA.write(show.format(**content))
        file_name1.close()
    print("saved")
    menu()
        
def export_data():
    global file_name
    import os
    import os.path
    file_name= input("enter a suitble file name")
    if os.path.exists("./"+file_name):
        choose= input("this file already exists, whold you like to replace this file?")
        if choose=="y":
           save_data()

        elif choose=="n":
           export_data ()

    else: save_data()      
menu()