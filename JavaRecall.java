/* Reid Sanders 
 * Java Recall
 * A simple Java program to recall some basic concepts in Java.
 * Date: 09/09/2025
 */

import java.util.*;

public class JavaRecall {
    private final String name;
    private final int age;

    private JavaRecall(String name, int age) {
        this.name = name;
        this.age = age;
    }

    // Getters
    public String getName() { return name; }
    public int getAge() { return age; }

    // Make Builder static so it can be used without an outer instance
    public static class Builder {
        private String name;
        private int age;

        public Builder setName(String name) {
            this.name = name;
            return this;
        }

        public Builder setAge(int age) {
            this.age = age;
            return this;
        }

        public JavaRecall build() {
            return new JavaRecall(name, age);
        }
    }

    public static void main(String[] args) {
        System.out.println("Haven't coded in Java for a while, so let's see what I remember!");

        // ArrayList reminder
        List<String> list = new ArrayList<>();
        list.add("This");
        list.add("is");
        list.add("a");
        list.add("test");

        // For-each loop reminder
        for (String s : list) {
            System.out.println(s);
        }
        // Remove element at index 2 ("a")
        String removed = list.remove(2);
        System.out.println("Removed: " + removed);

        System.out.println("------------------");

        // HashMap reminder
        Map<String, Integer> map = new HashMap<>();
        // HashMap is key-value pairs: first is key, second is value
        map.put("One", 1);
        map.put("Two", 2);
        map.put("Three", 3);

        // For-each loop to iterate through the map
        for (Map.Entry<String, Integer> entry : map.entrySet()) {
            System.out.println("Key: " + entry.getKey() + ", Value: " + entry.getValue());
        }
        map.put("Bank Account number", 123456789); // fake example
        System.out.println("Bank Account number: " + map.get("Bank Account number"));

        System.out.println("------------------");

        // 2D Array reminder
        int[][] array2D = {
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9}
        };
        // Nested for loop to iterate through the 2D array
        for (int i = 0; i < array2D.length; i++) {
            for (int j = 0; j < array2D[i].length; j++) {
                System.out.print(array2D[i][j] + " ");
            }
            System.out.println(); // New line after each row
        }

        System.out.println("------------------");

        // Scanner reminder
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter your name: ");
        String inputName = scanner.nextLine();
        System.out.println("Hello, " + inputName + "!");
        scanner.close();

        System.out.println("------------------");

        // Class and Object reminder using Builder
        JavaRecall person = new JavaRecall.Builder()
                                .setName("John")
                                .setAge(30)
                                .build();
        System.out.println("Person Name: " + person.getName() + ", Age: " + person.getAge());
    }
}
