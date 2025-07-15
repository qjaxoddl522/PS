using System;
using System.Collections.Generic;
using System.IO;

class Solution {
    static void Main(String[] args) {
        StreamReader reader = new StreamReader(Console.OpenStandardInput());
        StreamWriter writer = new StreamWriter(Console.OpenStandardOutput());
        
        int n = int.Parse(reader.ReadLine());
        string str = reader.ReadLine();
        
        ulong MOD = 1234567891;
        ulong result = 0;
        ulong pow = 1;
        
        for (int i=0; i<n; i++) {
            ulong order = (ulong)(str[i] - 96);
            result = (result + (order * pow)) % MOD;
            
            pow = (pow * 31) % MOD;
        }
        writer.WriteLine(result);
        
        reader.Close();
        writer.Close();
    }
}