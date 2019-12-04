using System;
using System.Linq;

class December4
{
  static int h_index(int n, int[] arr)
  {
    int h = 0;
    for (int i = 0; i < arr.Length; i++)
    {
      var ct = arr.Where(num => num >= arr[i]).ToList().Count;

      if (ct >= arr[i] && arr[i] > h)
      {
         h = arr[i];
      }
    }
    return h;
  }

  public static void Main(string[] args)
  {
    Console.WriteLine(h_index(6, new int[6] {5, 5, 2, 10, 6, 5}));
  }
}
