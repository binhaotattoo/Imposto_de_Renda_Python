#base calculo salarial em(R$) com desconto da Aliquota em (%)



salário = int(input("digite a faixa de salario para cálculo do Imposto de Renda:""R$"))
   

if (salário <= 1903.98):  #isento desconto aliquota para faixa salarial de R$0.0 a R$1903.98
    print("isento de imposto")
    print("salario liquido é de:" "R$" , salário)

else: #desconto 7.5% aliquota referente faixa salarial R$1903.99 a R$2826.65
    if salário >= 1903.99 and salário <= 2826.65:
        print("aliquota 7.5%" " seu imposto devido é de :") 
        resultado = (salário / 100 * 7.5)
        print("R$",resultado)
        print("salário liquido é de:" "R$",salário - ( salário / 100 )* 7.5 ) 
        
    else: #desconto 15% aliquota referente faixa salarial R$2826.66 a R$3751.05
        if salário >=2826.66 and salário <=3751.05:
            print("aliquota 15% " " seu imposto devido é de :")
            resultado = (salário / 100 * 15)
            print("R$",resultado)
            print("salário liquido é de:""R$",salário - ( salário / 100 )* 15 ) 

        else: #desconto 22.5% aliquota referente faixa salarial R$3751.06 a R$4664.68
             if salário >=3751.06 and salário <=4664.68:
                print("aliquota 22.5%" " seu imposto devido é de :")
                resultado = (salário / 100 * 22.5)
                print("R$",resultado)
                print("salário liquido é de:""R$",salário - ( salário / 100 )* 22.5 ) 

             else: #desconto 27.5 % aliquota referente faixa salarial acima R$5000.00
                    if salário > 4664.68:
                        print("aliquota 27.5% "" seu imposto devido é de :")
                        resultado = (salário / 100 * 27.5)
                        print("R$",resultado)
                        print("salário liquido é de:""R$",salário - ( salário / 100 )* 27.5 )
                    
        
