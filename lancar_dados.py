# Arquivo: lancar_dados.py
import random

def lancar_dados():
    try:
        num_dados = int(input("Quantos dados você quer lançar? "))
        num_lados = int(input("Quantos lados cada dado tem? (ex.: 6 para um dado comum) "))
        
        if num_dados <= 0 or num_lados <= 0:
            print("Por favor, insira números positivos maiores que zero.")
            return
        
        print("\nResultados do lançamento:")
        for i in range(num_dados):
            resultado = random.randint(1, num_lados)
            print(f"Dado {i + 1}: {resultado}")
    
    except ValueError:
        print("Por favor, insira apenas números inteiros válidos.")

if __name__ == "__main__":
    print("Simulador de Lançamento de Dados")
    lancar_dados()