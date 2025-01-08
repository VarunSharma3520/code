import java.util.Scanner;

public class Main {
  // Method
  public static String myMethod(String[] args) {
    System.out.println("I just got executed from myMethod!");
    // System.out.println(args[0]);
    return "myMethod return String";
  }

  // user input
  public static void userInput() {
    Scanner myObj = new Scanner(System.in); // Create a Scanner object
    System.out.println("Enter username");
    String userName = myObj.nextLine(); // Read user input
    System.out.println("Username is: " + userName); // Output user input
    myObj.close();
  }

  // Method overloading
  static int plusMethod(int x, int y) {
    return x + y;
  }

  static double plusMethod(double x, double y) {
    return x + y;
  }

  public static void main(String[] args) {
    // userInput();
    userInput();

    // Student data
    String studentName = "John Doe";
    int studentID = 15;
    int studentAge = 23;
    float studentFee = 75.25f;
    char studentGrade = 'B';
    boolean isStudent = true;

    // Print variables
    System.out.println(isStudent);
    System.out.println("Student name: " + studentName);
    System.out.println("Student id: " + studentID);
    System.out.println("Student age: " + studentAge);
    System.out.println("Student fee: " + studentFee);
    System.out.println("Student grade: " + studentGrade);
    System.out.println(Math.random());
    int randomNum = (int) (Math.random() * 101); // 0 to 100 // Type casting double to int
    System.out.println(randomNum);

    // if-else example
    System.out.println("If-else example");
    if (studentAge >= 18) {
      System.out.println("Student is an adult");
    } else if (studentAge >= 13) {
      System.out.println("Student is a teenager");
    } else {
      System.out.println("Student is a minor");
    }
    int time = 20;
    String result = (time < 18) ? "Good day." : "Good evening.";
    System.out.println(result);

    // switch-case example
    System.out.println("Switch-case example");
    int day = 4;
    switch (day) {
      case 1:
        System.out.println("Monday");
        break;
      case 2:
        System.out.println("Tuesday");
        break;
      case 3:
        System.out.println("Wednesday");
        break;
      case 4:
        System.out.println("Thursday");
        break;
      case 5:
        System.out.println("Friday");
        break;
      case 6:
        System.out.println("Saturday");
        break;
      case 7:
        System.out.println("Sunday");
        break;
      default:
        System.out.println("Invalid day");
    }

    // while loop example
    System.out.println("While loop example");
    int i = 0;
    while (i < 5) {
      System.out.println(i);
      i++;
    }

    // do-while loop example
    System.out.println("Do-while loop example");
    int j = 0;
    do {
      System.out.println(j);
      j++;
    } while (j < 5);

    // for loop example
    System.out.println("For loop example");
    for (int k = 0; k < 5; k++) {
      System.out.println(k);
    }

    // for-each loop example
    System.out.println("For-each loop example");
    String[] cars = { "Volvo", "BMW", "Ford", "Mazda" };
    for (String car : cars) {
      System.out.println(car);
    }

    // break and continue example
    System.out.println("Break and continue example");
    for (int l = 0; l < 10; l++) {
      if (l == 4) {
        break;
      }
      System.out.println(l);
    }
    for (int m = 0; m < 10; m++) {
      if (m == 4) {
        continue;
      }
      System.out.println(m);
    }

    // arrays example
    System.out.println("Arrays example");
    String[] cars1 = { "Volvo", "BMW", "Ford", "Mazda" };
    System.out.println(cars1[0]);
    int[] myNum = { 10, 20, 30, 40 };
    System.out.println(myNum[0]);

    // looping multidimensional arrays
    System.out.println("Looping through a multidimensional array");
    int[][] myNumbers = { { 1, 2, 3, 4 }, { 5, 6, 7 } };
    for (int x = 0; x < myNumbers.length; x++) {
      for (int y = 0; y < myNumbers[x].length; y++) {
        System.out.println(myNumbers[x][y]);
      }
    }

    // methods example
    System.out.println("Methods example");
    String resultofMyMethod = myMethod(args);
    System.out.println(resultofMyMethod);

    // method overloading
    System.out.println("Method overloading example");
    int myNum1 = plusMethod(8, 5);
    double myNum2 = plusMethod(4.3, 6.26);
    System.out.println("int: " + myNum1);
    System.out.println("double: " + myNum2);
  }
}
