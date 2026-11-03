# Descobrir uma forma de contar a quantidade de bits a nivel decimal, exemplo

def cont_bits_dec(n):
    bit_comp = 15 #meu decimal de comparação
    
    qtd_bit = n & bit_comp
    
    return qtd_bit
    
dec = int(input("Escolha um decimal para contar os bits: "))

fun_bit = cont_bits_dec(dec)

print(f"O decimal {dec} tem ao total {fun_bit} bits '1'")
