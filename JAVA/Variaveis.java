package JAVA;

import java.util.Scanner;

public class Variaveis {

    public static void main(String[] args){

        Scanner leitor = new Scanner(System.in);

        String nome = leitor.nextLine();
        int idade = leitor.nextInt();
        float altura = leitor.nextFloat();
        double peso = leitor.nextDouble();
        String tipoSanguineo = leitor.next();
        char fatorRh = leitor.next().charAt(0);

        System.out.printf("%s\n", nome);        
        System.out.printf("Idade: %d\n", idade);
        System.out.printf("Altura: %.2f\n", altura);
        System.out.printf("Peso: %.2f\n", peso);
        System.out.printf("Tipo Sanguíneo: %s%c\n", tipoSanguineo, fatorRh);

        leitor.close(); // Fecha o Scanner para evitar vazamento de recursos
    }
}
 
