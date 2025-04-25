#nullable disable
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

partial class Program {
    public static void Main() {
        StreamReader reader = new StreamReader(Console.OpenStandardInput());
        StreamWriter writer = new StreamWriter(Console.OpenStandardOutput());
        
        int[] input = Array.ConvertAll(reader.ReadLine().Split(' '), int.Parse);
        int N = input[0]; int M = input[1];

        int[] knows = Array.ConvertAll(reader.ReadLine().Split(' '), int.Parse).Skip(1).ToArray();
        List<int>[] partys = new List<int>[M];
        bool[] isKnow = new bool[N+1];

        UnionFind uf = new UnionFind(N+1);
        for (int i=0; i<M; i++) {
            List<int> p = Array.ConvertAll(reader.ReadLine().Split(' '), int.Parse).Skip(1).ToList();
            partys[i] = p;
            for (int j=1; j<p.Count; j++) {
                uf.Union(p[j], p[j-1]);
            }
        }

        foreach (int num in knows) {
            isKnow[uf.Find(num)] = true;
        }

        int ans = 0;
        foreach (List<int> party in partys) {
            if (!isKnow[uf.Find(party[0])]) {
                ans++;
            }
        }

        writer.WriteLine(ans);
        writer.Flush();
    }
}

public class UnionFind {
    private int[] parent;
    private int[] rank;

    public UnionFind(int n) {
        parent = new int[n];
        rank = new int[n];
        for (int i = 0; i < n; i++) {
            parent[i] = i;
            rank[i] = 1;
        }
    }

    public int Find(int x) {
        if (parent[x] != x)
            parent[x] = Find(parent[x]);
        return parent[x];
    }

    public void Union(int x, int y) {
        int rootX = Find(x);
        int rootY = Find(y);

        if (rootX != rootY) {
            if (rank[rootX] > rank[rootY])
                parent[rootY] = rootX;
            else if (rank[rootX] < rank[rootY])
                parent[rootX] = rootY;
            else {
                parent[rootY] = rootX;
                rank[rootX]++;
            }
        }
    }
}