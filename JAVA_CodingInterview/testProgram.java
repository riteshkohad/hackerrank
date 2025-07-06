
public class testProgram {

    public static void main(String[] args) {
        System.out.println("Hello");

        // 1. reverse string in JAVA
        // System.out.println(reverse("HELLO").toCharArray());
        // 2. Swap TWO NUMBERS without using 3rd Variable 
        // swap_numbers(10, 20);
        // 3. Check if string has vowels 
        // System.out.println(check_vowels("input").toString());
        // 4. Check if number is a prime
        System.out.println(check_prime_number(15).toString());
    }

    // Reverse string in JAVA
    public static String reverse(String inpt) {
        if (inpt == null) {
            throw new IllegalArgumentException("Invalid String");
        }

        StringBuilder output = new StringBuilder();
        char[] chars = inpt.toCharArray();

        for (int i = inpt.length() - 1; i >= 0; i--) {
            output.append(chars[i]);
        }

        return output.toString();
    }

    // Function to swap two Integer Numbers
    public static void swap_numbers(Integer a, Integer b) {
        System.out.println("Original A: " + a.toString() + " B:" + b.toString());
        b = b + a;
        a = b - a;
        b = b - a;

        System.out.println("Swapped: A: " + a.toString() + " B:" + b.toString());
    }

    // Function to check if string has vowels present
    public static Boolean check_vowels(String input) {
        System.out.println("Original string: " + input);
        return input.toLowerCase().matches(".*[aeiou].*");
    }

    public static Boolean check_prime_number(Integer num) {
        if (num == 0 || num == 1) {
            System.out.println("Number: " + num.toString() + " is NOT a prime number!");
            return false;
        }

        if (num == 2) {
            System.out.println("Number: " + num.toString() + " is a prime number!");
            return true;
        }

        for (int i = 2; i <= num / 2; i++) {
            if (num % i == 0) {
                System.out.println("Number: " + num.toString() + " is a NOT prime number!");
                return false;
            }
        }

        System.out.println("Number: " + num.toString() + " is a prime number!");
        return true;
    }

}

// hello Aarya
