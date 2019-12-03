using System;

class December3
{
  static int[] DecimationSort(int[] numArray)
  {
    bool sorted = true;
    for (int i = 1; i < numArray.Length; i++)
    {
      if (numArray[i - 1] > numArray[i]) { sorted = false; }
    }
    if (sorted) { return numArray; }
    else
    {
      int[] halfArray = new int[numArray.Length / 2];
      for (int i = 0; i < halfArray.Length; i++)
      {
        halfArray[i] = numArray[i*2];
      }
      return DecimationSort(halfArray);
    }
  }

  public static void Main(string[] args)
  {
    foreach (int i in DecimationSort(new int[6] {3, 4, 5, 1, 2, 10})) {
      Console.WriteLine(i);
    }
  }
}
