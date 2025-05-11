#nullable disable

partial class Program {
    public static void Main() {
        StreamReader reader = new StreamReader(Console.OpenStandardInput());
        StreamWriter writer = new StreamWriter(Console.OpenStandardOutput());
        
        int N = int.Parse(reader.ReadLine());
        int[] M = Array.ConvertAll(reader.ReadLine().Split(), int.Parse);

        int[][] food = new int[N][];
        for (int i = 0; i < N; i++) {
            food[i] = Array.ConvertAll(reader.ReadLine().Split(), int.Parse);
        }

        int minCost = int.MaxValue;
        int minUsed = 0;
        (int p, int f, int s, int v, int c) cur = (0, 0, 0, 0, 0);
        void backtrack(int start, int used) {
            if (minCost <= cur.c) {
                return;
            }

            if (cur.p >= M[0] && cur.f >= M[1] && cur.s >= M[2] && cur.v >= M[3]) {
                minCost = cur.c;
                minUsed = used;
                return;
            }

            for (int i = start; i < N; i++) {
                if (((1 << i) & used) == 0) {
                    cur.p += food[i][0];
                    cur.f += food[i][1];
                    cur.s += food[i][2];
                    cur.v += food[i][3];
                    cur.c += food[i][4];

                    backtrack(i+1, used | (1 << i));

                    cur.p -= food[i][0];
                    cur.f -= food[i][1];
                    cur.s -= food[i][2];
                    cur.v -= food[i][3];
                    cur.c -= food[i][4];
                }
            }
        }

        backtrack(0, 0);
        
        writer.WriteLine((minCost != int.MaxValue) ? minCost : -1);
        for (int i = 0; i < N; i++) {
            if (((1 << i) & minUsed) > 0) {
                writer.Write(i+1 + " ");
            }
        }

        writer.Flush();
    }
}