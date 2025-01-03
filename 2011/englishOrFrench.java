import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    
    System.out.println("Enter: ");
    int N = sc.nextInt();

    int countT = 0;
    int countS = 0;

    for (int i = 0; i < N; i++)
    {
      System.out.println();
      String line = sc.nextLine();

      for (int j = 0; j < line.length(); j++)
      {
        if (line.charAt(j) == 's' || line.charAt(j) == 'S')
          countS++;

        if (line.charAt(j) == 't' || line.charAt(j) == 'T')
          countT++;
      }
    }

    if (countT > countS)
      System.out.println("English");
    else
      System.out.println("French");
  }
}
