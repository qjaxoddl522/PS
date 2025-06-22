#nullable disable
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

partial class Program {
    public static void Main() {
        StreamReader reader = new StreamReader(Console.OpenStandardInput());
        StreamWriter writer = new StreamWriter(Console.OpenStandardOutput());
        
        int N = int.Parse(reader.ReadLine());
        int[,] grid = new int[N, N];
        for (int i=0; i<N; i++) {
            int[] input = Array.ConvertAll(reader.ReadLine().Split(' '), int.Parse);
            for (int j=0; j<N; j++) {
                grid[i, j] = input[j];
            }
        }

        // [r, c, 이전 방향(세로, 대각선, 가로)]
        int[,,] dp = new int[N, N, 3];
        dp[0, 1, 2] = 1;
        
        for (int r=0; r<N; r++) {
            for (int c=0; c<N; c++) {
                // 세로
                if (r+1 < N && grid[r+1, c] == 0)
                    dp[r+1, c, 0] += dp[r, c, 0] + dp[r, c, 1];
                // 대각선
                if ((r+1 < N && grid[r+1, c] == 0) && (c+1 < N && grid[r, c+1] == 0) && grid[r+1, c+1] == 0)
                    dp[r+1, c+1, 1] += dp[r, c, 0] + dp[r, c, 1] + dp[r, c, 2];
                // 가로
                if (c+1 < N && grid[r, c+1] == 0)
                    dp[r, c+1, 2] += dp[r, c, 1] + dp[r, c, 2];
            }
        }
        writer.WriteLine(dp[N-1, N-1, 0] + dp[N-1, N-1, 1] + dp[N-1, N-1, 2]);
        writer.Flush();
    }
}