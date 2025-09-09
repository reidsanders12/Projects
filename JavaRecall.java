/*Reid Sanders 
**Java Recall
**A simple Java program to recall some basic concepts in Java programming language.
**Date: 09/09/2025
*/

import java.util.*;

public class JavaRecall{

    public class Builder {
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

    public static void main(Stringp[] args){
        System.out.prinln("Haven't coded in Java for a while, so let's see what I remember!");

        //ArrayList reminder
        List<String> list = new ArrayList<>();
        list.add("This");
        list.add("is");
        list.add("a");
        list.add("test");

        //For-each loop reminder
        for(String s: list){
            System.out.println(s);
        }
        System.out.println(list.pop(2)); //Should remove the index at 2, which should be "a"
        
        System.out.println("------------------");

        //HashMap reminder
        Map<String, Integer> map = new HashMap<>();
        //Remind myself that a hashmap is a key-value pair, first is the key, second is the value
        map.put("One", 1);
        map.put("Two", 2);
        map.put("Three", 3);
        //For-each loop to iterate through the map
        for(String key: map.keySet()){
            System.out.println("Key: " + key + ", Value: " + map.get(key));
        }
        map.put("Bank Account number", 123456789); //Adding a fake bank account number to the map, to show it can be used for cybersecurity purposes
        System.out.println("Bank Account number: " + map.get("Bank Account number"));

        System.out.println("------------------");

        //2D Array reminder
        int[][] array2D = {
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9}
        };
        //Nested for loop to iterate through the 2D array
        for(int i = 0; i < array2D.length; i++){
            for(int j = 0; j < array2D[i].length; j++){ //Note the use of array2D[i].length to get the length of the specific row
                System.out.print(array2D[i][j] + " ");
            }
            System.out.println(); //New line after each row
        }


        System.out.println("------------------");
        //Scanner reminder
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter your name: ");
        String name = scanner.nextLine();
        System.out.println("Hello, " + name + "!");

        System.out.println("------------------");
        //Class and Object reminder
        Building person = new Builder().setName("John").setAge(30).build();
        System.out.println("Person Name: " + person.getName() + ", Age: " + person.getAge());
    }
}


