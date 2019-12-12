import java.util.regex.*;
import java.util.Scanner;

class EmailChecker
{
  public static boolean checkEmail(String email) { return Pattern.matches("^[.\\w\\d-]+@[\\w]+\\.com$", email);}

  public static void main(String[] args)
  {
    Scanner scan = new Scanner(System.in);
    System.out.println(checkEmail(scan.nextLine()));
  }
}
