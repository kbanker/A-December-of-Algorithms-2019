import java.util.*;

public class java_kbanker
{
  public static Integer[] getFibonacciPrimes(int n)
  {
    ArrayList<Integer> arr = new ArrayList<Integer>();
    ArrayList<Integer> primes = new ArrayList<Integer>();

    int curr = 2;
    int last = 1;

    while(arr.size() < n)
    {
      boolean isPrime = true;

      for(int i: primes)
      {
        if(curr % i == 0) { isPrime = false; }
      }

      if (isPrime)
      {
        arr.add(curr);
        primes.add(curr);
      }

      int x = curr;
      curr += last;
      last = x;
    }

    return arr.toArray(new Integer[arr.size()]);
  }

  public static void main(String[] args)
  {
    for(int i: getFibonacciPrimes(5))
    {
      System.out.println(i);
    }
  }
}
