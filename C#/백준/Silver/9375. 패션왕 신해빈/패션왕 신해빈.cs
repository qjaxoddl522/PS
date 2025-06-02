using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

class Solution {
    static void Main(String[] args) {
        StreamReader reader = new StreamReader(Console.OpenStandardInput());
        StreamWriter writer = new StreamWriter(Console.OpenStandardOutput());
        
        int T = int.Parse(reader.ReadLine());
        for (int i=0; i<T; i++) {
            int n = int.Parse(reader.ReadLine());
            Dictionary<string, int> cloth = new Dictionary<string, int>();
            
            for (int j=0; j<n; j++) {
                string[] name = reader.ReadLine().Split(' ');
                if (cloth.ContainsKey(name[1])) {
                    cloth[name[1]]++;
                }
                else {
                    cloth.Add(name[1], 1);
                }
            }
            
            int answer = 1;
            foreach (var item in cloth) {
                answer *= item.Value + 1;
            }
            writer.WriteLine(answer - 1);
        }
        
        reader.Close();
        writer.Flush();
        writer.Close();
    }
}