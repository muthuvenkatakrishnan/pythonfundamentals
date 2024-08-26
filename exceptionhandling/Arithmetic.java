package exceptionhandling;

class Arithmetic {

    public static void main(String[] args) {
        for (int i = 0; i < 5; i++) {
            try {
                int a = 10;
                int b = i;
                System.out.println(a/b);
            } catch (ArithmeticException e) {
                System.out.println("Exception: " + e);
            }
        }
    }
    
}