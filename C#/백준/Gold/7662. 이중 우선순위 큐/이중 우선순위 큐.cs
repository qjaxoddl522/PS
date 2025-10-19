#nullable disable
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

partial class Program {
    public static void Main() {
        StreamReader reader = new StreamReader(Console.OpenStandardInput());
        StreamWriter writer = new StreamWriter(Console.OpenStandardOutput());
        
        int T = int.Parse(reader.ReadLine());
        for (int t=0; t<T; t++) {
            SortedSet<int> set = new SortedSet<int>();
            Dictionary<int, int> numbers = new Dictionary<int, int>();
            int N = int.Parse(reader.ReadLine());
            for (int i=0; i<N; i++) {
                string[] input = reader.ReadLine().Split(' ');
                if (input[0] == "I") {
                    int n = int.Parse(input[1]);
                    set.Add(n);
                    if (numbers.ContainsKey(n))
                        numbers[n]++;
                    else
                        numbers.Add(n, 1);
                }
                else if (input[0] == "D" && set.Count > 0) {
                    if (input[1] == "1") {
                        int max = set.Max;
                        numbers[max]--;
                        if (numbers[max] < 1) {
                            set.Remove(max);
                            numbers.Remove(max);
                        }
                    }
                    else if (input[1] == "-1") {
                        int min = set.Min;
                        numbers[min]--;
                        if (numbers[min] < 1) {
                            set.Remove(min);
                            numbers.Remove(min);
                        }
                    }
                }
            }
            if (set.Count > 0)
                writer.WriteLine($"{set.Max} {set.Min}");
            else
                writer.WriteLine("EMPTY");
        }
        writer.Flush();
    }
}