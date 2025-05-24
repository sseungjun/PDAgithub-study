import java.util.Scanner;

public class hello{

    public void sqrt(int input){

        int total = 1;

        for(int i=0 ; i<input ; i++ ){

            total *= input;

            
        }
    }



    public static void main(String[] args) {
        

        Scanner scanner = new Scanner(System.in);

        System.out.println("숫자를 입력하세요 : ");

        int input = scanner.nextInt();


    }
}