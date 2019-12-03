using System;

class December2
{
  static bool IsValidNum(long cardNum)
  {
    string numString = "" + cardNum;
    int s1 = 0;
    int s2 = 0;
    int[] evens = new int[numString.Length];

    for (int i = 0; i < numString.Length; i++)
    {
      if (i % 2 == 0)
      {
        s1 += Convert.ToInt32(numString[i].ToString());
      }
      else
      {
        evens[i] = 2 * Convert.ToInt32(numString[i].ToString());
      }
    }

    foreach (int even in evens) {
      if(even >= 10)
      {
        s2 += even % 10;
        s2 += (int) even / 10;
      }
      else
      {
        s2 += even;
      }
    }

    int sum = s1 + s2;

    if(sum % 10 == 0) { return true; }
    else { return false; }
  }

  public static void Main(string[] args)
  {
    Console.Write("Input: ");
    long input = Convert.ToInt64(Console.ReadLine());
    string msg = (IsValidNum(input)) ? input + " passes the test" : input + " does not pass the test";
    Console.WriteLine("Output: " + msg);
  }
}
