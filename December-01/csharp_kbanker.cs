using System;

class December1
{
  static int sevenish_number(int pos)
  {

    int[] numbers = new int[2 * pos + 1];
    int currentPower = 1;

    numbers[0] = 1;
    numbers[1] = 7;
    numbers[2] = 8;

    for(int i = 3; i < pos; i++)
    {
      if(numbers[i] != 0)
      {
        continue;
      }

      currentPower++;
      numbers[i] = (int) Math.Pow(7, currentPower);

      for(int k = 0; k < i; k++)
      {
        numbers[i + 1 + k] = numbers[i] + numbers[k];
      }
    }

    return numbers[pos - 1];
  }

  public static void Main(string[] args)
  {
    Console.WriteLine(sevenish_number(15));
  }
}
